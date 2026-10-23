from fastapi import APIRouter
from fastapi.responses import JSONResponse
from repositorio import RepositorioMySql
from schema.usuarios.usuario import Usuario
from schema.usuarios.usuarioDto import UsuarioDto

repo = RepositorioMySql()
router = APIRouter()


@router.get("/")
async def primerEndpoint():
    return {
        "hola":"mundo"
    }

@router.post("/usuarios",response_model=UsuarioDto)
async def crearUsuario(usuario:Usuario):
     res,id = repo.crearUsuario(usuario)
     usuarioResponse = UsuarioDto(
          id=id,
          nombre=res.nombre,
          email=res.email,
          edad=res.edad)
     return JSONResponse(
          status_code=201,
          content={
               "message":"Usuario creado correctamente",
               "status":True,
               "data":usuarioResponse.model_dump()
          }
          
          )



@router.get("/usuarios")
async def obtenerUsuarios():
    usuarios = repo.obtenerUsuarios()
    usuariosMapeados:list[UsuarioDto] = []
    for user in usuarios:
        usuario = UsuarioDto(
             id=user["id"],
             nombre=user["nombres"],
             email=user["correo"],
             edad=user["edad"]

             )
        usuariosMapeados.append(usuario)

    return JSONResponse(
         status_code=200,
         content={"message":f"Usuarios encontrados : {len(usuarios)}",
                  "status":True,
                  "data":[usuario.model_dump()  for usuario in usuariosMapeados]})


@router.get("/usuarios/{id}")
async def obtenerUsuario(id:int):
     user = repo.obtenerUsuarioId(id)
     if (user == None):
          return JSONResponse(status_code=404,content={
               "messaeg":f"No se encontro el usuario con el id {id}",
               "status":False,
               "data":[]
          })
     usuario = UsuarioDto(
                id=user["id"],
                nombre=user["nombres"],
                email=user["correo"],
                edad=user["edad"]
                )
     return JSONResponse(status_code=200,content={
                    "messaeg":f"Se encontro el usuario con el id {id}",
                    "status":True,
                    "data":usuario.model_dump()
               })

@router.delete("/usuarios/{id}")
async def eliminarUsuario(id:int):
    res = repo.eliminarUsuario(id)
    if(not res):
        return JSONResponse(
                status_code=404,
                content={
                    "mensaje":f"No se encontro el usuario con el id {id}"
        }    )
    return JSONResponse(
                status_code=204,content={}    )



@router.put("/usuarios/{id}")
async def actualizarUsuario(id:int,usuario:Usuario):
    seActualizo,user =  repo.actualizarUsuario(usuario,id)

    if(not seActualizo):
          return JSONResponse(
                      status_code=404,
                      content={
                          "mensaje":f"Hubo un error al actualizar al usuario",
                    "status":False,

        }    )
    return JSONResponse(
                status_code=200,
                content={
                    "mensaje":f"Se actualizo correctamente el usuario",
                    "status":True,
                    "data":user.model_dump()
        }    )