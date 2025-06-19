# Typo Analysis AI

This project contains a Python script allowing you to find typos in your text!
The prompts are currently adjusted for german text files, feel free to adjust or translate
them as needed.

## Implementation

- Click (CLI)
- Google Genai with the Gemini Models

## Usage

1. Add a `.env` file with a GOOGLE_API_KEY variable
2. Run `pip install -r requirements.txt` in your python environment or create a venv first
3. Add a `textfile.txt` with the text you want to check to the base of this project
   - Make sure that each line of your file represents a full section of content, ideally with a couple sentences.
4. Run the script
   - use `python analyze.py` to run the script with default options
   - use `python analyze.py --help` to view all options
5. The Script will write to `typolog.txt` incrementally

## Common Issues

### Answer Quality

While the LLMs are quite good at finding errors, it usually takes a couple takes before they find everything.
Adjust the revision parameter as needed based on the length of your lines. The Script will break once the LLM returns
an empty list. But keep in mind that you might burn more tokens than necessary with a higher revision maximum.

Also, the model might pick up non-errors occasionally.

### Gemini Free Tier

The script might run into Rate Limiting Errors from Gemini, especially for the free tier. If needed, add some form of
throttling logic or check your text in smaller chunks.
