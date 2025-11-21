from flask import Flask, request, jsonify
import google.generativeai as genai
import time

# Configurar Google Generative AI
genai.configure(api_key="AIzaSyBHM7xAhjqdrp_abnbKLfzcF7NrDbWK6L4")
model = genai.GenerativeModel("gemini-2.0-flash")

app = Flask(__name__)

@app.route("/analyze_sales", methods=["POST"])
def analyze_sales():
    data = request.get_json()
    if not data or "sales_text" not in data:
        return jsonify({"error": "No se recibió el texto de ventas"}), 400

    sales_text = data["sales_text"]

    start_time = time.time()
    chat = model.start_chat()

    prompt = f"""
Eres un analista experto. Tienes un historial de ventas de los últimos 3 meses:

{sales_text}

Tareas:
1. Detecta productos sin ventas o con baja actividad.
2. Para cada producto genera:
   - Nombre del producto
   - Categoria
   - ID ficticio de cliente principal
   - Productos relacionados (3)
   - Estrategia de reactivación
   - Lista de clientes sugeridos con porcentaje de afinidad EN FORMATO:
     [
        {{
          "ClienteId": "123",
          "Nombre": "Cliente X",
          "Afinidad": "85%"
        }},
        ...
     ]

IMPORTANTE:
- La afinidad debe simular análisis real: porcentajes altos para clientes que compran productos similares.
- El JSON debe respetar este formato:

[
  {{
    "Producto": "NombreProducto",
    "Categoria": "CategoriaProducto",
    "ClienteVendedorId": "12345",
    "ClientesSugeridos": [
      {{ "ClienteId": "1", "Nombre": "Cliente A", "Afinidad": "90%" }},
      {{ "ClienteId": "2", "Nombre": "Cliente B", "Afinidad": "75%" }},
      {{ "ClienteId": "3", "Nombre": "Cliente C", "Afinidad": "60%" }}
    ],
    "ProductosRelacionados": ["Prod1", "Prod2", "Prod3"],
    "Estrategia": "Texto corto aquí"
  }}
]

No agregues explicaciones.
Solo JSON válido.
"""

    response = chat.send_message(prompt)
    end_time = time.time()

    return jsonify({"result": response.text, "time_taken": end_time - start_time})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
