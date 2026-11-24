from dotenv import load_dotenv
from openai import AuthenticationError, OpenAI  # type: ignore
from colorama import Fore
import os
import base64

from rich.console import Console  # type: ignore
from rich.pretty import pprint

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise RuntimeError("GROQ_API_KEY is missing. Add it to the .env file next to main.py.")

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=groq_api_key,
)
console = Console()
console.rule("[bold green]Generating Content with Responses[/bold green]")

try:
    response = client.responses.create(
        model="openai/gpt-oss-120b",
        input="Write a two-sentence horror story about a haunted house.",
        temperature=0.9,
    )
except AuthenticationError as exc:
    raise RuntimeError(
        "Groq rejected GROQ_API_KEY. Set it to a valid key from Groq Console "
        "in the .env file next to main.py; an OpenAI API key will not work."
    ) from exc

print(response.output_text)