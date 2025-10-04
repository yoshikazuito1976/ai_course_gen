from pydantic import BaseModel, Field

class OutlineIn(BaseModel):
    topic: str = Field(..., examples=["クラウドの責任共有モデル"])
    grade: str = Field(..., examples=["専門学校1年"])

class OutlineOut(BaseModel):
    ok: bool
    data: dict
