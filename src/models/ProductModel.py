from database.db import get_connection
from .entities.Product import Product

class ProductModel:
    @classmethod
    def get_products(self):
        try:
            connection = get_connection()
            products = []

            with connection.cursor() as cursor:
                cursor.execute('SELECT 	"idProducto", "idClase", "codigo", "correlativo", "nombre", "activo", "eliminado", "fechaRegistro", "usuarioRegistro", "fechaEdicion", "usuarioEdicion" FROM product ORDER BY "codigo" ASC')
                resultset = cursor.fetchall()

                for row in resultset:
                    product = Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                    products.append(product.to_JSON())
            
            connection.close()
            return products
        except Exception as ex:
            raise ex

    @classmethod
    def get_product(self, idProducto):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('SELECT 	"idProducto", "idClase", "codigo", "correlativo", "nombre", "activo", "eliminado", "fechaRegistro", "usuarioRegistro", "fechaEdicion", "usuarioEdicion" FROM product WHERE "idProducto" = %s',(idProducto,))
                row = cursor.fetchone()
                
                product = None
                if row != None:
                    product = Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                    product = product.to_JSON()
                               
            connection.close()
            return product
        except Exception as ex:
            raise ex

    @classmethod
    def add_product(self, product):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(""" INSERT INTO product ("idClase", codigo, correlativo, nombre, activo, eliminado, "fechaRegistro", "usuarioRegistro") VALUES
                                (%s, %s, %s, %s, %s, %s, %s, %s)""", (product.idClase, product.codigo, product.correlativo, product.nombre, product.activo, product.eliminado, product.fechaRegistro, product.usuarioRegistro))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise ex

    @classmethod
    def update_product(self, product):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(""" UPDATE product SET "idClase" = %s, codigo = %s, correlativo = %s, nombre = %s, activo = %s, eliminado = %s, "fechaRegistro" = %s, "usuarioRegistro" = %s, "fechaEdicion" = %s, "usuarioEdicion" = %s WHERE "idProducto" = %s """, (product.idClase, product.codigo, product.correlativo, product.nombre, product.activo, product.eliminado, product.fechaRegistro, product.usuarioRegistro, product.fechaEdicion, product.usuarioEdicion, product.idProducto))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise ex
        
    @classmethod
    def delete_product(self, product):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM product WHERE \"idProducto\" = %s", (product.idProducto,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise ex