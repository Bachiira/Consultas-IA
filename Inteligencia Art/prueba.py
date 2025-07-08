import google.generativeai as genai
import os

# --- CONFIGURACIÓN DE TU CLAVE API ---
# REEMPLAZA 'TU_API_KEY_AQUI' CON TU CLAVE API REAL DE GOOGLE AI STUDIO.
# ¡NUNCA COMPARTAS ESTE CÓDIGO CON TU CLAVE REAL EN UN ENTORNO PÚBLICO!
# Idealmente, usa os.environ["GOOGLE_API_KEY"] después de configurar la variable de entorno.
API_KEY = 'AIzaSyAApmm1y5KT_GbvLHDnElUZslgnBlYOMZU' 

if API_KEY == 'TU_API_KEY_AQUI':
    print("ADVERTENCIA: Por favor, reemplaza 'TU_API_KEY_AQUI' con tu clave API real para poder listar los modelos.")
    print("El programa no podrá comunicarse con la API sin una clave válida.")
else:
    try:
        genai.configure(api_key=API_KEY)

        print("Listando modelos disponibles para tu clave API y región:")
        found_supported_model = False
        for m in genai.list_models():
            # Filtra para mostrar solo modelos que soportan la generación de contenido de texto
            if 'generateContent' in m.supported_generation_methods:
                print(f"  Nombre del Modelo: {m.name}")
                print(f"    Descripción: {m.description}")
                print(f"    Métodos Soportados: {m.supported_generation_methods}")
                print(f"    Entrada de Token Máxima: {m.input_token_limit}")
                print(f"    Salida de Token Máxima: {m.output_token_limit}")
                print("-" * 30) # Separador para mejor lectura
                found_supported_model = True
        
        if not found_supported_model:
            print("No se encontraron modelos que soporten 'generateContent' con tu clave API en tu región.")
            print("Por favor, verifica que tu clave API sea correcta y que la API de Gemini esté disponible en tu región.")
            print("Puedes consultar la documentación oficial de Google AI Studio para ver la disponibilidad regional de los modelos.")
        else:
            print("\n^ Por favor, utiliza uno de los 'Nombres de Modelo' listados arriba que soporte 'generateContent' en tu código Flask (app.py).")

    except Exception as e:
        print(f"Ocurrió un error al configurar la API o listar los modelos: {e}")
        print("Asegúrate de que tu clave API sea correcta y que haya conectividad a Internet.")