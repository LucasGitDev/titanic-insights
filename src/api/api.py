from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.processing.preprocessing import preprocess

tags_metadata = [
    {
        "name": "Predição",
        "description": "Endpoints para realizar predições de sobrevivência.",
    },
    {
        "name": "Geral",
        "description": "Endpoints gerais da API.",
    },
]

app = FastAPI(
    title="Titanic Insights API",
    description="""
API para prever a probabilidade de sobrevivência de um passageiro no Titanic. 🚢

**Funcionalidades:**
- Predição de sobrevivência baseada em dados do passageiro.
- Documentação interativa via Swagger UI (`/docs`).
    """,
    version="0.1.0",
    openapi_tags=tags_metadata,
    contact={
        "name": "Lucas",
        "url": "https://github.com/lucasgitdev",
    },
)

model_path = Path("models/logreg_titanic.joblib")
model = None


# --- Modelos Pydantic ---
class Passenger(BaseModel):
    Pclass: int = Field(
        ..., example=3, description="Classe do ticket (1 = 1ª, 2 = 2ª, 3 = 3ª)"
    )
    Sex: str = Field(..., example="male", description="Sexo do passageiro")
    Age: float | None = Field(None, example=22.0, description="Idade em anos")
    SibSp: int = Field(..., example=1, description="Número de irmãos/cônjuges a bordo")
    Parch: int = Field(..., example=0, description="Número de pais/filhos a bordo")
    Fare: float | None = Field(None, example=7.25, description="Tarifa do passageiro")
    Embarked: str | None = Field(
        None,
        example="S",
        description="Porto de embarque (C = Cherbourg, Q = Queenstown, S = Southampton)",
    )

    class Config:
        schema_extra = {
            "example": {
                "Pclass": 3,
                "Sex": "male",
                "Age": 22,
                "SibSp": 1,
                "Parch": 0,
                "Fare": 7.25,
                "Embarked": "S",
            }
        }


class PredictionResponse(BaseModel):
    survival_probability: float = Field(
        ..., example=0.87, description="Probabilidade de sobrevivência (0.0 a 1.0)"
    )


# --- Eventos da API ---
@app.on_event("startup")
async def startup_event():
    """Carrega o modelo durante a inicialização da API."""
    global model
    if model_path.exists():
        model = joblib.load(model_path)
    else:
        # A API pode rodar, mas o endpoint de predição retornará erro.
        print(
            f"AVISO: Modelo não encontrado em '{model_path}'. O endpoint /predict não funcionará."
        )


# --- Endpoints da API ---
@app.get("/", tags=["Geral"], summary="Endpoint de Boas-Vindas")
def read_root():
    """
    Retorna uma mensagem de boas-vindas. Útil para verificar se a API está online.
    """
    return {"message": "Bem-vindo à API de Predição de Sobrevivência do Titanic"}


@app.post(
    "/predict",
    response_model=PredictionResponse,
    tags=["Predição"],
    summary="Prevê a probabilidade de sobrevivência",
    description="Recebe os dados de um passageiro e retorna a probabilidade de sobrevivência estimada pelo modelo.",
    responses={
        200: {
            "description": "Predição bem-sucedida",
            "content": {
                "application/json": {"example": {"survival_probability": 0.87}}
            },
        },
        503: {"description": "Modelo não disponível"},
    },
)
def predict(passenger: Passenger) -> PredictionResponse:
    """
    Realiza a predição de sobrevivência para um único passageiro.

    - **passenger**: um objeto com os dados do passageiro.
    """
    if model is None:
        raise HTTPException(
            status_code=503,
            detail=f"Modelo não disponível. Verifique se o arquivo '{model_path}' existe.",
        )

    df = pd.DataFrame([passenger.dict()])
    df_processed = preprocess(df)

    # [:, 1] para obter a probabilidade da classe positiva (sobreviveu)
    prob = model.predict_proba(df_processed)[0, 1]
    return PredictionResponse(survival_probability=prob)
