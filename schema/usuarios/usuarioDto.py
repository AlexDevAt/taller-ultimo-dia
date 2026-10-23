from pydantic import BaseModel,Field


class UsuarioDto(BaseModel):
    id:int
    nombre:str
    email:str
    edad:int = Field(ge=0)