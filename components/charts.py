import plotly.express as px


def expense_pie(expense_df):

    fig = px.pie(
        expense_df,
        names="category",
        values="amount",
        hole=.65
    )

    fig.update_layout(
        height=420,
        margin=dict(
            l=10,
            r=10,
            t=40,
            b=10
        ),
        legend_title=""
    )

    return fig


def expense_line(trend_df):

    fig = px.line(
        trend_df,
        x="date",
        y="amount",
        markers=True
    )

    fig.update_layout(
        height=420,
        margin=dict(
            l=10,
            r=10,
            t=40,
            b=10
        ),
        xaxis_title="",
        yaxis_title=""
    )

    return fig