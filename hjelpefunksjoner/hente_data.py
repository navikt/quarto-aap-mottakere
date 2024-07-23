# todo: legge i dvh-tools
import pandas as pd
from google.cloud.bigquery import Client

def hente_bq_df(
    table_bq: str,
    where_clause: str = None,
    project_id: str = "spenn-prod-23e0",
    schema_bq: str = "spenn_offentlig",
) -> pd.DataFrame:
    """Lager en dataframe fra en BigQuery-tabell. Oppretter client og kjører query,
    med én eventuell where-clause. 

    Args:
        table_bq (str): tabellnavn i BQ
        where_clause (str, optional): eventuell where-clause. Eks: "ytelse = Dagpenger" Defaults to None.
        project_id (str, optional): prosjekt i BQ. Defaults to "spenn-prod-23e0".
        schema_bq (str, optional): skjema i BQ. Defaults to "spenn_offentlig".

    Returns:
        pd.DataFrame: dataframe med data fra BQ
    """
    bq_client = Client(project=project_id)
    query = f"select * from {schema_bq}.{table_bq}"
    if where_clause:
        query += f" where {where_clause}"
    df = bq_client.query(query).to_dataframe()
    return df
