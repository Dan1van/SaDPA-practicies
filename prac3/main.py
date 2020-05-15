import requests
import pandas as pd
import plotly.graph_objects as go

link = "http://www.meteo-tv.ru/weather/archive/?month=%s&year=%s"


def main():
    fig = go.Figure()

    for year in range(2015, 2020+1):

        if year == 2020:
            start_month = 1
            end_month = 2
        else:
            start_month = 1
            end_month = 12

        for month in range(start_month, end_month+1):
            page = requests.get(link % (month, year))
            df = pd.read_html(page.text, header=0)[1]

            fig.add_trace(go.Scatter(x=df.iloc[:, 0], y=df.iloc[:, 1],
                                     mode='lines+markers',
                                     name=f'Погода на {month}.{year}'))

    fig.show()


if __name__ == '__main__':
    main()
