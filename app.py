from flask import Flask, request, jsonify
from pathlib import Path
import PyPDF2
import google.generativeai as genai
import time

# Configurar Google Generative AI
genai.configure(api_key="AIzaSyBHM7xAhjqdrp_abnbKLfzcF7NrDbWK6L4")
model = genai.GenerativeModel("gemini-2.0-flash")

app = Flask(__name__)

def extract_text_from_pdf(pdf_path):
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        return None
    try:
        with pdf_path.open("rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            return text if text.strip() else None
    except Exception:
        return None

@app.route("/upload_pdf", methods=["POST"])
def upload_pdf():
    if "file" not in request.files:
        return jsonify({"error": "No se recibió ningún archivo"}), 400
    
    pdf_file = request.files["file"]
    temp_path = "temp.pdf"
    pdf_file.save(temp_path)
    
    pdf_text = extract_text_from_pdf(temp_path)
    Path(temp_path).unlink()

    if not pdf_text:
        return jsonify({"error": "No se pudo leer el PDF"}), 500

    start_time = time.time()
    chat = model.start_chat()

    prompt = f"""
Eres un analista experto. Tienes un historial de ventas de los últimos 3 meses:

{pdf_text}

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

    return jsonify(
        response.text)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
