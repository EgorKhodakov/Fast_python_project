from pydantic import BaseModel

class ColorShema(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str
