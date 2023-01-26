from flask import Blueprint, jsonify, request

# Entities
from models.entities.Product import Product

# Models 
from models.ProductModel import ProductModel

main = Blueprint('product_blueprint', __name__)

@main.route('/')
def get_products():
    try:
        products = ProductModel.get_products()
        return jsonify(products)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<idProducto>')
def get_product(idProducto):
    try:
        product = ProductModel.get_product(idProducto)
        if product != None:
            return jsonify(product)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_product():
    try:
        idclase = int(request.json['idclase'])
        codigo = request.json['codigo']
        correlativo = int(request.json['correlativo'])
        nombre = request.json['nombre']
        activo = int(request.json['activo'])
        eliminado = int(request.json['eliminado'])
        fechaRegistro = request.json['fechaRegistro']
        usuarioRegistro = request.json['usuarioRegistro']

        if idclase==None or idclase==0 or idclase=="":
            return jsonify({'message': 'Variable sin argumento'}), 500
            
        if codigo==None or codigo==0 or codigo=="":
            return jsonify({'message': 'Variable sin argumento'}), 500
        
        if correlativo==None or correlativo==0 or correlativo=="":
            return jsonify({'message': 'Variable sin argumento'}), 500
        
        if nombre==None or nombre==0 or nombre=="":
            return jsonify({'message': 'Variable sin argumento'}), 500
        
        if activo==None or activo==0 or activo=="":
            return jsonify({'message': 'Variable sin argumento'}), 500
        
        if eliminado==None or eliminado=="":
            return jsonify({'message': 'Variable sin argumento'}), 500

        if fechaRegistro==None or fechaRegistro==0 or fechaRegistro=="":
            return jsonify({'message': 'Variable sin argumento'}), 500

        if usuarioRegistro==None or usuarioRegistro==0 or usuarioRegistro=="":
            return jsonify({'message': 'Variable sin argumento'}), 500

        product = Product("", idclase, codigo, correlativo, nombre, activo, eliminado, fechaRegistro, usuarioRegistro, None, None)

        affected_row = ProductModel.add_product(product)

        if affected_row == 1:
            return jsonify(product.idProducto)
        else:
            return jsonify({'message': 'Error on insert'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update/<idProducto>', methods=['PUT'])
def update_product(idProducto):
    try:
        idclase = int(request.json['idclase'])
        codigo = request.json['codigo']
        correlativo = int(request.json['correlativo'])
        nombre = request.json['nombre']
        activo = int(request.json['activo'])
        eliminado = int(request.json['eliminado'])
        fechaRegistro = request.json['fechaRegistro']
        usuarioRegistro = request.json['usuarioRegistro']
        fechaEdicion = request.json['fechaEdicion']
        usuarioEdicion = request.json['usuarioEdicion']

        if idclase==None or idclase==0 or idclase=="":
            return jsonify({'message': 'Variable sin argumento'}), 500
            
        if codigo==None or codigo==0 or codigo=="":
            return jsonify({'message': 'Variable sin argumento'}), 500
        
        if correlativo==None or correlativo==0 or correlativo=="":
            return jsonify({'message': 'Variable sin argumento'}), 500
        
        if nombre==None or nombre==0 or nombre=="":
            return jsonify({'message': 'Variable sin argumento'}), 500
        
        if activo==None or activo=="":
            return jsonify({'message': 'Variable sin argumento'}), 500
        
        if eliminado==None or eliminado=="":
            return jsonify({'message': 'Variable sin argumento'}), 500

        if fechaRegistro==None or fechaRegistro==0 or fechaRegistro=="":
            return jsonify({'message': 'Variable sin argumento'}), 500

        if usuarioRegistro==None or usuarioRegistro==0 or usuarioRegistro=="":
            return jsonify({'message': 'Variable sin argumento'}), 500

        if fechaEdicion==None or fechaEdicion==0 or fechaEdicion=="":
            return jsonify({'message': 'Variable sin argumento'}), 500

        if usuarioEdicion==None or usuarioEdicion==0 or usuarioEdicion=="":
            return jsonify({'message': 'Variable sin argumento'}), 500

        product = Product(idProducto, idclase, codigo, correlativo, nombre, activo, eliminado, fechaRegistro, usuarioRegistro, fechaEdicion, usuarioEdicion)

        affected_row = ProductModel.update_product(product)

        if affected_row == 1:
            return jsonify(product.idProducto)
        else:
            return jsonify({'message': 'No product update'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<idProducto>', methods=['DELETE'])
def delete_product(idProducto):
    try:
        product = Product(idProducto)
        
        affected_row = ProductModel.delete_product(product)

        if affected_row == 1:
            return jsonify(product.idProducto)
        else:
            return jsonify({'message': 'Not product delete'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500