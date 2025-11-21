from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/analyze_sales", methods=["POST"])
def analyze_sales():
    if not request.is_json:
        return jsonify({"error": "Se esperaba JSON"}), 400
    
    data = request.get_json()
    producto = data.get("producto_sugerir")
    ventas = data.get("ventas_3_meses", [])

    # Contar compras por cliente para calcular afinidad simple
    clientes = {}
    for venta in ventas:
        cliente = venta.get("cliente")
        if cliente not in clientes:
            clientes[cliente] = 0
        clientes[cliente] += sum([p.get("qty", 0) for p in venta.get("productos_comprados", [])])

    # Normalizar a porcentaje de afinidad (máximo 100%)
    max_compras = max(clientes.values(), default=1)
    clientes_sugeridos = [
        {
            "ClienteId": idx+1,
            "Nombre": nombre,
            "Afinidad": f"{int(cantidad / max_compras * 100)}%"
        } for idx, (nombre, cantidad) in enumerate(clientes.items())
    ]

    result = [{
        "Producto": producto.get("name"),
        "Categoria": producto.get("categ_id"),
        "ClienteVendedorId": producto.get("id"),
        "ClientesSugeridos": clientes_sugeridos,
        "ProductosRelacionados": [p["product_name"] for v in ventas for p in v.get("productos_comprados", []) if p["product_name"] != producto.get("name")],
        # quitamos estrategia
    }]

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
