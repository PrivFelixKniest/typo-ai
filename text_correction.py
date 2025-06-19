import json
import os
from typing import Optional

import click
from google import genai
from google.genai import types
from pydantic import BaseModel


class RechtschreibFehler(BaseModel):
    fehlerImText: str
    umliegendeWorte: str
    umliegenderSatz: str
    verbesserung: str


def run_text_correction(line: str, revisions: int) -> list[dict[str, str]]:
    all_errors: list[dict[str, str]] = []

    prompt = (
        f"Gegeben ist der folgende Abschnitt eines Fließtextes, welcher mit START und ENDE markiert ist. Du sollst den "
        f"Text auf Rechtschreibfehler Korrekturlesen um dem Autor zu helfen. Finde alle Rechtschreibfehler und gib sie "
        f"von oben nach unten an den Autor zurück. \n \n"
        f"START \n"
        f"{line}"
        f"ENDE \n \n"
        f"Für jeden Rechtschreibfehler, gib den Fehler zurück, die umliegenden Worte sowie der Satz in welchem der Rechtschreibfehler vorkommt und einen "
        f"Verbesserungsvorschlag."
    )

    follow_up_prompt = (
        f"Finde weitere Rechtschreibfehler"
    )

    client = genai.Client(api_key=os.environ.get("GENAI_API_KEY"))

    chat = client.chats.create(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            temperature=.9,
            response_mime_type="application/json",
            response_schema=list[RechtschreibFehler]
        )
    )


    for i in range(revisions):

        click.echo(f"Analyzing Typos {str(i+1)}/{str(revisions)}")

        p = prompt if i == 0 else follow_up_prompt

        chat_response = chat.send_message(p)
        response = chat_response.text

        if response == "[]":
            break

        errors: list[dict[str, str]] = json.loads(response)

        all_errors += errors

    return all_errors
