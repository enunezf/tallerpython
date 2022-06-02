from typing import Union

from pydantic import BaseModel


class RecetaBase(BaseModel):
    nombre: str
    descripcion: Union[str, None] = None


class RecetaCreate(RecetaBase):
    pass


class Receta(RecetaBase):
    id: int

    class Config:
        orm_mode = True