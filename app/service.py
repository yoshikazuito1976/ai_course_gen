import json
from pathlib import Path
from jinja2 import Template
from openai import OpenAI
from .config import settings

client = OpenAI(api_key=settings.openai_api_key)

def render_prompt(name: str, **vars) -> str:
    tpl = Template(Path(f"app/prompts/{name}").read_text(encoding="utf-8"))
    return tpl.render(**vars)

def generate_outline(topic: str, grade: str) -> dict:
    prompt = render_prompt("lesson_outline.jinja", topic=topic, grade=grade)
    resp = client.chat.completions.create(
        model=settings.model_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=settings.temperature,
        response_format={"type": "json_object"},
    )
    return json.loads(resp.choices[0].message.content)
