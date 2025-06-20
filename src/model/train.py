# src/model/train.py

import pandas as pd
from joblib import dump
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.processing.preprocessing import add_age_group, add_household_features


def load_data(path="data/processed/train_processed.csv"):
    """Carrega dados pré-processados."""
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print(f"Arquivo não encontrado em {path}.")
        print("Por favor, execute o passo de pré-processamento primeiro.")
        return None
    return df


def build_pipeline():
    numeric_feats = ["Age", "Fare", "HouseholdSize", "Pclass", "SibSp", "Parch"]
    categorical_feats = ["Sex", "Embarked", "AgeGroup", "AloneXAgeGroup"]

    from sklearn.impute import SimpleImputer

    numeric_transformer = make_pipeline(
        SimpleImputer(strategy="median"), StandardScaler()
    )
    categorical_transformer = make_pipeline(
        SimpleImputer(strategy="most_frequent"),
        OneHotEncoder(drop="first", handle_unknown="ignore", sparse_output=False),
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_feats),
            ("cat", categorical_transformer, categorical_feats),
        ],
        remainder="drop",  # ignora colunas não especificadas
    )

    pipeline = make_pipeline(
        preprocessor, LogisticRegression(max_iter=1000, solver="liblinear")
    )
    return pipeline


def evaluate_model(scores, y_test, y_pred_proba, model, X_test):
    """Gera um descritivo avaliativo dos valores das validações cross, hold-out e outras."""
    print(f"ROC-AUC CV scores: {scores}")
    print(f"Média ROC-AUC: {scores.mean():.3f}")
    print(f"Desvio padrão ROC-AUC: {scores.std():.3f}")
    print(f"Mínimo ROC-AUC: {scores.min():.3f}")
    print(f"Máximo ROC-AUC: {scores.max():.3f}")

    from sklearn.metrics import roc_auc_score

    test_roc_auc = roc_auc_score(y_test, y_pred_proba)
    print(f"Acurácia no conjunto de teste: {model.score(X_test, y_test):.3f}")
    print(f"ROC-AUC no conjunto de teste: {test_roc_auc:.3f}")

    if scores.mean() > 0.8:
        print(
            "O modelo apresenta um bom desempenho, com uma média ROC-AUC superior a 0.8."
        )
    elif scores.mean() > 0.7:
        print(
            "O modelo apresenta um desempenho mediano, com uma média ROC-AUC entre 0.7 e 0.8."
        )
    else:
        print(
            "O modelo apresenta um desempenho ruim, com uma média ROC-AUC inferior a 0.7."
        )


def train_and_evaluate():
    df = load_data()
    if df is None:
        return

    if "Survived" not in df.columns:
        print("Coluna 'Survived' não encontrada. Verifique o arquivo de dados.")
        return

    X = df.drop(
        columns=["Survived", "PassengerId", "Name", "Ticket", "Cabin"], errors="ignore"
    )
    y = df["Survived"]

    # split treino/teste. # TODO: Como tenho 2 datasets separados, o que seria o ideial para esse passo?
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = build_pipeline()

    # avaliação por cross-val
    print("Avaliando modelo com cross-validation...")
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring="roc_auc")

    # treino final e avaliação no hold-out
    print("Treinando modelo final...")
    model.fit(X_train, y_train)

    y_pred_proba = model.predict_proba(X_test)[:, 1]

    evaluate_model(scores, y_test, y_pred_proba, model, X_test)

    # salvar o pipeline completo
    dump(model, "models/logreg_titanic.joblib")
    print("Modelo salvo em models/logreg_titanic.joblib")


if __name__ == "__main__":
    train_and_evaluate()
