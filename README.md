# Understanding-AI

This repo contains simple examples for practicing with the OpenAI SDK.

Setup
-----

- Install dependencies:

```bash
pip install -r requirements.txt
```

- Create a `.env` file from the example and add your key:

```bash
cp .env.example .env
# then edit .env and set OPENAI_API_KEY
```

- Run the example:

```bash
python main.py
```

Notes
-----
- Do NOT commit your `.env` file. It's already listed in `.gitignore`.
- `main.py` reads `OPENAI_API_KEY` from the environment using `python-dotenv`.