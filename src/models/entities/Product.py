from utils.DateFormat import DateFormat

class Product():
    def __init__(self, idProducto, idClase=None, codigo=None, correlativo=None, nombre=None, activo=None, eliminado=None, fechaRegistro=None, usuarioRegistro=None, fechaEdicion=None, usuarioEdicion=None) -> None:
        self.idProducto = idProducto
        self.idClase = idClase
        self.codigo = codigo
        self.correlativo = correlativo
        self.nombre = nombre
        self.activo = activo
        self.eliminado = eliminado
        self.fechaRegistro = fechaRegistro
        self.usuarioRegistro = usuarioRegistro
        self.fechaEdicion = fechaEdicion
        self.usuarioEdicion = usuarioEdicion

    def to_JSON(self):
        if self.fechaRegistro != None:
            self.fechaRegistro = DateFormat.convert_date(self.fechaRegistro)
        
        if self.fechaEdicion != None:
            self.fechaEdicion = DateFormat.convert_date(self.fechaEdicion)
        
        return {
            'idProducto': self.idProducto,
            'idClase': self.idClase,
            'codigo': self.codigo,
            'correlativo': self.correlativo,
            'nombre': self.nombre,
            'activo': self.activo,
            'eliminado': self.eliminado,
            'fechaRegistro': self.fechaRegistro,
            'usuarioRegistro': self.usuarioRegistro,
            'fechaEdicion': self.fechaEdicion,
            'usuarioEdicion': self.usuarioEdicion
        }
