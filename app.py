from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/analyze_sales", methods=["POST"])
def analyze_sales():
    if not request.is_json:
        return jsonify({"error": "Se esperaba JSON"}), 400
    
    data = request.get_json()
    producto = data.get("producto_sugerir")

    # Aceptar ambos formatos
    ventas = data.get("ventas_3_meses") or data.get("ventas_filtradas") or []

    ventas_normalizadas = []

    # --- Normalizar ventas_filtradas a formato común ---
    for v in ventas:
        if "productos_comprados" in v:
            # Ya está en formato correcto
            ventas_normalizadas.append(v)
        else:
            # Convertir ventas_filtradas → ventas_3_meses
            ventas_normalizadas.append({
                "order_id": v.get("order_id"),
                "cliente": v.get("cliente"),
                "fecha": v.get("fecha"),
                "total_orden": v.get("total_orden"),
                "productos_comprados": [
                    {
                        "product_id": v.get("producto_id"),
                        "product_name": v.get("producto_name"),
                        "qty": v.get("qty"),
                        "price_unit": v.get("price_unit"),
                        "subtotal": v.get("subtotal")
                    }
                ]
            })

    # ------------------------------
    # Calcular afinidad por cliente
    # ------------------------------
    clientes = {}
    for venta in ventas_normalizadas:
        cliente = venta.get("cliente")
        if cliente not in clientes:
            clientes[cliente] = 0
        clientes[cliente] += sum([p.get("qty", 0) for p in venta.get("productos_comprados", [])])

    # Normalizar porcentajes
    max_compras = max(clientes.values(), default=1)
    clientes_sugeridos = [
        {
            "ClienteId": idx + 1,
            "Nombre": nombre,
            "Afinidad": f"{int(cantidad / max_compras * 100)}%"
        }
        for idx, (nombre, cantidad) in enumerate(clientes.items())
    ]

    # -----------------------------------
    # Productos relacionados sugeridos
    # -----------------------------------
    relacionados = []
    for venta in ventas_normalizadas:
        for p in venta.get("productos_comprados", []):
            if p["product_name"] != producto.get("name"):
                relacionados.append(p["product_name"])

    result = [{
        "Producto": producto.get("name"),
        "Categoria": producto.get("categ_id"),
        "ClienteVendedorId": producto.get("id"),
        "ClientesSugeridos": clientes_sugeridos,
        "ProductosRelacionados": relacionados
    }]

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
