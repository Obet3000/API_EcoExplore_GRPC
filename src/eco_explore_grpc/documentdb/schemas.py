from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr
from pydantic_mongo import ObjectIdField
from pydantic_extra_types.phone_numbers import PhoneNumber


class Reseña(BaseModel):
    Evaluacion: int
    Comentario: str

