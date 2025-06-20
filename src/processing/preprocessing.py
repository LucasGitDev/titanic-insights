import pandas as pd


def add_household_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adiciona as características do agregado familiar ao DataFrame fornecido.

    Esta função cria duas novas colunas no DataFrame:
    - 'HouseholdSize': Esta coluna é a soma das colunas 'SibSp' (número de irmãos/cônjuges a bordo) e 'Parch' (número de pais/filhos a bordo) mais um (o próprio passageiro).
    - 'IsAlone': Esta coluna é uma variável binária que indica se o passageiro está sozinho ou não. É 1 se 'HouseholdSize' é igual a 1, caso contrário, é 0.

    Parâmetros:
    df (pd.DataFrame): DataFrame original a ser processado.

    Retorna:
    df (pd.DataFrame): DataFrame após a adição das colunas 'HouseholdSize' e 'IsAlone'.
    """
    df["HouseholdSize"] = df["SibSp"] + df["Parch"] + 1
    df["IsAlone"] = (df["HouseholdSize"] == 1).astype(int)
    return df


def add_age_group(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adiciona a coluna 'AgeGroup' ao DataFrame fornecido.

    Esta função cria uma nova coluna chamada 'AgeGroup' que categoriza a idade do passageiro em um dos seguintes grupos: 'Child', 'Teen', 'Adult', 'Senior'.
    A categorização é feita de acordo com os seguintes intervalos de idade:
    - 'Child': 0-12 anos
    - 'Teen': 12-18 anos
    - 'Adult': 18-60 anos
    - 'Senior': 60-80 anos

    Parâmetros:
    df (pd.DataFrame): DataFrame original a ser processado.

    Retorna:
    df (pd.DataFrame): DataFrame após a adição da coluna 'AgeGroup'.
    """
    bins = [0, 12, 18, 60, 80]
    labels = ["Child", "Teen", "Adult", "Senior"]
    df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels)
    return df


def add_alone_x_age_group(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adiciona a coluna 'AloneXAgeGroup' ao DataFrame fornecido.

    Esta função cria uma nova coluna chamada 'AloneXAgeGroup' que é a combinação das colunas 'AgeGroup' e 'Alone'.
    A coluna 'Alone' é uma variável binária que indica se o passageiro está sozinho ou não (1 se estiver sozinho, 0 caso contrário).
    A coluna 'AgeGroup' é uma variável categórica que indica o grupo de idade do passageiro ('Child', 'Teen', 'Adult', 'Senior').
    A nova coluna 'AloneXAgeGroup' é a combinação dessas duas colunas, fornecendo uma característica de interação entre o grupo de idade e o status de estar sozinho.

    Parâmetros:
    df (pd.DataFrame): DataFrame original a ser processado.

    Retorna:
    df (pd.DataFrame): DataFrame após a adição da coluna 'AloneXAgeGroup'.
    """

    df["Alone"] = (df["HouseholdSize"] == 1).astype(int)
    df["AloneXAgeGroup"] = (
        df["AgeGroup"].astype(str) + "_Alone" + df["Alone"].astype(str)
    )
    return df


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza o pré-processamento do DataFrame fornecido.

    Esta função adiciona recursos de agregação familiar, agrupa a idade em categorias e cria uma interação entre o grupo de idade e o status de estar sozinho.
    Além disso, preenche os valores ausentes para as colunas 'Age', 'Embarked' e 'Fare' com a mediana (para 'Age' e 'Fare') e a moda (para 'Embarked').

    Parâmetros:
    df (pd.DataFrame): DataFrame original a ser pré-processado.

    Retorna:
    df (pd.DataFrame): DataFrame após o pré-processamento.
    """
    df = add_household_features(df)
    df = add_age_group(df)
    df = add_alone_x_age_group(df)

    if "Age" in df.columns:
        df["Age"] = df["Age"].fillna(df["Age"].median())
    if "Embarked" in df.columns:
        df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    if "Fare" in df.columns:
        df["Fare"] = df["Fare"].fillna(df["Fare"].median())
    return df


def main():
    from pathlib import Path

    Path("data/processed").mkdir(parents=True, exist_ok=True)

    df_train = pd.read_csv("data/raw/train.csv")
    df_train_processed = preprocess(df_train)
    df_train_processed.to_csv("data/processed/train_processed.csv", index=False)
    print(
        "Dados de treino pré-processados e salvos em data/processed/train_processed.csv"
    )

    df_test = pd.read_csv("data/raw/test.csv")
    df_test_processed = preprocess(df_test)
    df_test_processed.to_csv("data/processed/test_processed.csv", index=False)
    print(
        "Dados de teste pré-processados e salvos em data/processed/test_processed.csv"
    )


if __name__ == "__main__":
    main()
