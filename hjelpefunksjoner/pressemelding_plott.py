import plotly.graph_objects as go
from hjelpefunksjoner import hente_bq_df

def pressemelding_plott(max_aarmnd: int = None, xmin: str = None) -> go.Figure:
    """Plotter antall mottakere av arbeidsavklaringspenger per måned, som er brukt i 
    pressemeldingene om arbeidsavklaringspenger.

    Henter data fra BigQuery-tabellen agg_arbeidsmarkedsstonader_mnd, filtrert på ytelse

    Args:
        max_aarmnd (int, optional): Høyeste aarmnd, på formen YYYYMM. Defaults to None.
        xmin (str, optional): Laveste x-verdi for x-aksen. Defaults to None.

    Returns:
        go.Figure: Plotly-figur med antall mottakere av arbeidsavklaringspenger per måned
    """    

    table_bq = "agg_arbeidsmarkedsstonader_mnd"
    where_clause = f"ytelse = 'Arbeidsavklaringspenger'"
    if max_aarmnd:
        where_clause += f" and aarmnd <= {max_aarmnd}"
    df = hente_bq_df(table_bq=table_bq, where_clause=where_clause)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["aarmnd_dato"], y=df["mottaker_antall"], mode='lines', name='Antall mottakere av AAP'))
    fig.update_layout(xaxis_title="Måned", yaxis_title="Antall månedlige mottakere")
    if xmin:
        fig.update_layout(xaxis=dict(range=[xmin, df["aarmnd_dato"].max()]))
    fig.update_layout(showlegend=True, legend=dict(x=.98, y=.98, xanchor='right', yanchor='top'))
    fig.update_yaxes(range=[0, df["mottaker_antall"].max()*1.1])

    return fig