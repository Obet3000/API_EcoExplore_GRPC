import config as cf
import documentdb.schemas as schemas
import bson

from documentdb.document import Collections
from typing import List, Optional
from bson import ObjectId

def serialize_id(uid: str):
    return bson.ObjectId(uid)

def getComentario(reseniaId: str):
    cls = Collections().get_collection(cf.COMENTARY_COLLECTION)
    reseniaId = serialize_id(reseniaId)
    resenia_search = {"_id": reseniaId}
    comentario = cls.find_one(resenia_search)

    try:
        if comentario:
            print(f"Comentario obtenido de la base de datos: {comentario}")

            comentario = schemas.Reseña(**comentario)
            return comentario
        else:
            return None
    except Exception as e:
        print(f"Error al procesar el comentario: {e}")
        return None
