import click
from dotenv import load_dotenv

from text_correction import run_text_correction

load_dotenv()

@click.command()
@click.option("--file_path", default="./textfile.txt", help="Text file that should be analyzed")
@click.option("--revisions", default=3, help="How often each section should be visited at the maximum before"
                                             "moving to the next section")
def analysis(file_path, revisions):

    with open(file_path, "r") as f:
        num_lines = sum(1 for _ in f)

    with open(file_path, "r") as f:
        line_count = 1
        for line in f:
            click.echo(f"Typo Search starting: Section {line_count} / {num_lines}")
            line_errors = run_text_correction(line, revisions)

            click.echo("Typo Search Done, writing to output file...")

            # write typos of line to output file
            with open("./typolog.txt", "w") if line_count == 1 else open("./typolog.txt", "a") as o:
                for line_error in line_errors:
                    o.write(f"Section {line_count} Typo Found -->\n")
                    for key, value in line_error.items():
                        o.write(f"{key}: {value}\n")
                    o.write("\n")


            click.echo(f"Section Done {line_count} / {num_lines}")

            line_count += 1

if __name__ == '__main__':
    analysis()