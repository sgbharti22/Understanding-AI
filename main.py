import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("OPENAI_API_KEY")
if not API_KEY:
    raise RuntimeError("OPENAI_API_KEY not found in environment. Set it in a .env file or export it.")

client = OpenAI(api_key=API_KEY)


def ask_gpt(prompt: str) -> str:
    response = client.responses.create(
        model="gpt-5-nano",      # or "gpt-5" if you want that specifically
        input=[
            {"role": "system", "content": "You should not explain when people ask about the ai agents topic."},
            {"role": "user", "content": prompt}
        ],
        reasoning={"effort": "low"},  # optional: control reasoning effort for gpt-5 / 5.1
        store=True
    )

    return response.output_text


if __name__ == "__main__":
    question = "Explain agent-to-agent communication in simple terms."
    answer = ask_gpt(question)
    print("GPT answer: ------------------------------------------------------------>\n", answer)
