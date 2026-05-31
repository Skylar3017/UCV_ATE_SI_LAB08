from google.adk.agents.llm_agent import Agent

def explicar_concepto(concepto: str) -> dict:
    conceptos = {
        "api": "Una API permite comunicación entre sistemas.",
        "algoritmo": "Un algoritmo es una secuencia de pasos.",
        "base de datos": "Una base de datos almacena información.",
        "IA": "La IA permite que los sistemas aprendan y tomen decisiones.",
        "machine learning": "Es una rama de la IA basada en el aprendizaje mediante datos.",
        "red neuronal": "Modelo computacional inspirado en el funcionamiento del cerebro humano.",
        "cloud computing": "Permite acceder a recursos informáticos a través de internet.",
        "ciberseguridad": "Conjunto de prácticas para proteger sistemas y datos.",
        }
    
    concepto = concepto.lower().strip()

    if concepto in conceptos:
        return {
            "status": "success",
            "explicacion": conceptos[concepto]
        }
    return {
        "status": "not_found",
        "explicacion": "Concepto no registrado."
    }

def calcular_promedio(nota1: float, nota2: float, nota3: float) -> dict:
    promedio = (nota1 + nota2 + nota3) / 3

    return {
        "status": "success",
        "promedio": round(promedio, 2)
    }
    
root_agent = Agent(
    model="gemini-flash-latest",
    name="agente_ucv",
    description="Agente académico UCV",
    instruction="""Eres un asistente académico. Responde en español. Usa lenguaje simple.""",
    tools=[explicar_concepto, calcular_promedio]
)