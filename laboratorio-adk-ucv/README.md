# laboratorio-adk-ucv

Proyecto de ejemplo para un agente académico UCV usando Google ADK.

## Estructura del proyecto

```
laboratorio-adk-ucv/
│
├── agente_ucv/
│   ├── __init__.py
│   └── agent.py
│
├── tests/
│   └── test_agent.py
│
├── .env
├── pyproject.toml
├── README.md
├── .gitignore
└── sonar-project.properties
```

## Preparación

1. Instalar Poetry si no está instalado:
   ```bash
   pip install poetry
   ```
2. Instalar dependencias:
   ```bash
   poetry install
   ```
3. Configurar la clave en `.env`:
   ```env
   GOOGLE_API_KEY="TU_API_KEY"
   ```

## Ejecución

- Ejecutar el agente:
  ```bash
  poetry run adk run agente_ucv
  ```
- Ejecutar la interfaz web:
  ```bash
  poetry run adk web --port 8000
  ```
- Abrir en el navegador:
  ```text
  http://localhost:8000
  ```

## Pruebas

```bash
poetry run pytest
```

## SonarQube

Este proyecto incluye configuración para SonarQube en `sonar-project.properties` y GitHub Actions en `.github/workflows/sonarqube.yml`.
