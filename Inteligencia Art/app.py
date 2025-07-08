import google.generativeai as genai
from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)

# --- CONFIGURACIÓN DE TU CLAVE API ---
# ¡ADVERTENCIA DE SEGURIDAD! NO USES TU CLAVE API DIRECTAMENTE EN CÓDIGO EN PRODUCCIÓN.
# Usa variables de entorno (os.environ.get("GOOGLE_API_KEY")) o un sistema de gestión de secretos.
API_KEY = 'AIzaSyAApmm1y5KT_GbvLHDnElUZslgnBlYOMZU' 

if API_KEY == 'TU_API_KEY_AQUI':
    print("ADVERTENCIA: Por favor, reemplaza 'TU_API_KEY_AQUI' con tu clave API real en app.py.")
    print("El servidor podría no funcionar sin una clave válida.")
    # Considera salir o manejar este error de forma más robusta en producción.
    # Para desarrollo, quizás quieras usar una clave por defecto para probar la UI.
else:
    try:
        genai.configure(api_key=API_KEY)
        # Intenta usar un modelo que sabes que funciona, por ejemplo 'gemini-1.5-flash-001' o el que te haya listado el script anterior.
        # Si 'gemini-pro' funcionó, úsalo. Si no, usa el que identificaste.
        model = genai.GenerativeModel('gemma-3n-e2b-it') # O 'gemini-pro', o el que funcione para ti
        print(f"Modelo de IA cargado: {model.model_name}")
    except Exception as e:
        print(f"Error al configurar la API de Gemini: {e}")
        # En un entorno de producción, podrías querer registrar esto y no arrancar la app.
        model = None # Asegúrate de que el modelo sea None si la configuración falla

# --- Rutas de la Aplicación Flask ---

@app.route('/')
def index():
    # Renderiza la plantilla HTML principal
    return render_template('index.html')

@app.route('/ask_ai', methods=['POST'])
def ask_ai():
    user_question = request.json.get('question')
    if not user_question:
        return jsonify({"response": "Por favor, ingresa una pregunta."}), 400

    if not model:
        return jsonify({"response": "El servicio de IA no está disponible. Por favor, verifica la configuración de la API."}), 500

    try:
        # Aquí puedes aplicar tus técnicas de ingeniería de prompts
        # Por ejemplo, podrías añadir un prefijo o sufijo a la pregunta
        prompt = f"El usuario pregunta: {user_question}\nResponde de manera concisa y útil."
        
        response = model.generate_content(prompt)
        ai_response = response.text
        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"response": f"Ocurrió un error al procesar tu consulta: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True) # debug=True recarga el servidor automáticamente con cambios y muestra errores