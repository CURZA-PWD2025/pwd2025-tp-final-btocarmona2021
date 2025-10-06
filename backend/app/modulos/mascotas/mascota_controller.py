from .mascota_model import MascotaModel

@staticmethod
def obtener_mascotas():
    mascotas = MascotaModel.obtener_mascotas()
    return mascotas

@staticmethod
def obtener_mascota(data: dict):
    mascota = MascotaModel.obtener_mascota(data["id"])
    return mascota

@staticmethod
def crear_mascota(data: dict):
    mascota = MascotaModel.crear_mascota(
        data["nombre"],
        data["especie"],
        data["raza"],
        data["edad"],
        data["fecha_nacimiento"],
        data["sexo"],
        data["color"],
        data["peso"],
        data["id_usuario"],
        data["fecha_registro"])
    return mascota

@staticmethod
def actualizar_mascota(data: dict):
    mascota = MascotaModel.actualizar_mascota(
        data["id"],
        data["nombre"],
        data["especie"],
        data["raza"],
        data["edad"],
        data["fecha_nacimiento"],
        data["sexo"],
        data["color"],
        data["peso"],
        data["id_usuario"],
        data["fecha_registro"])
    return mascota

@staticmethod
def eliminar_mascota(data:dict):
    resultado = MascotaModel.eliminar_mascota(data["id"])