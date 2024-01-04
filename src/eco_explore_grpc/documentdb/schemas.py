from pydantic import BaseModel

class Reseña(BaseModel):
    Evaluacion: int
    Comentario: str

