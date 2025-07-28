from shiny import App, ui, render, reactive, req
import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH = "box_office_movies.csv"

@reactive.Calc
def read_movies():
    return pd.read_csv(CSV_PATH)

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.h3("🎛️ Filters"),
        ui.input_select("year", "🎞️ Select Year", choices=[], selected=None),
        ui.input_checkbox_group("months", "📅 Select Months", choices=[], selected=[]),
        ui.hr(),
        ui.markdown("Created by **Sabri** 🍿"),
    ),
    ui.layout_columns(
        # Left Column
        ui.panel_well(
            ui.h1("🎬 Sabri’s Box Office Dashboard"),
            ui.h4("💸 Movie Revenue Explorer"),
            ui.output_text("selection_text"),
            ui.output_ui("revenue_box"),
            ui.output_plot("revenue_plot", height="400px"),
        ),
        # Right Column
        ui.panel_well(
            ui.h4("🎞️ Movie Data"),
            ui.output_data_frame("filtered_table"),
        ),
        col_widths=(6, 6)  # 50/50 layout
    )
)

def server(input, output, session):

    @reactive.Effect
    def update_inputs():
        df = read_movies()
        years = sorted([str(int(y)) for y in df["year"].unique()])

        month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December']
        months_available = df["month"].unique().tolist()
        months = [m for m in month_order if m in months_available]

        ui.update_select("year", choices=years, selected=years[0])
        ui.update_checkbox_group("months", choices=months, selected=months)

    @reactive.Calc
    def filtered_data():
        df = read_movies()
        req(input.year())
        req(input.months())
        return df[
            (df["year"] == int(input.year())) &
            (df["month"].isin(input.months()))
        ]

    @output
    @render.text
    def selection_text():
        df = filtered_data()
        return f"🎥 Showing {len(df)} movies from {input.year()} in months: {', '.join(input.months())}."

    @output
    @render.ui
    def revenue_box():
        total = filtered_data()["revenue"].sum()
        return ui.value_box(f"${total:,}", "🎯 Total Revenue", showcase="💰")

    @output
    @render.data_frame
    def filtered_table():
        return filtered_data()[["movie", "month", "year", "revenue"]].sort_values(by="revenue", ascending=False)

    @output
    @render.plot
    def revenue_plot():
        df = filtered_data()
        month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December']
        df_grouped = df.groupby("month")["revenue"].sum().reindex(month_order).dropna()

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(df_grouped.index, df_grouped.values, color="#FF6B6B", edgecolor="black")
        ax.set_title(f" Total Revenue by Month in {str(input.year())}")
        ax.set_xlabel("Month")
        ax.set_ylabel("Revenue ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        return fig

app = App(app_ui, server)
