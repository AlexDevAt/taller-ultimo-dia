from pydantic import BaseModel,Field


class Usuario(BaseModel):
    nombre:str
    email:str
    contra:str
    edad:int = Field(ge=0)