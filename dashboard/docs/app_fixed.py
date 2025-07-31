from shiny import App, ui, render, reactive, req
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Path to CSV
CSV_PATH = Path(__file__).parent / "box_office_movies.csv"

# Reactive function to read the CSV
@reactive.Calc
def read_movies():
    return pd.read_csv(CSV_PATH)

# UI layout
app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.h3("🎛️ Filters"),
        ui.input_select("year", "🎞️ Select Year", choices=[], selected=None),
        ui.input_checkbox_group("months", "📅 Select Months", choices=[], selected=[]),
        ui.hr(),
        ui.markdown("Created by **Sabri** 🍿"),
    ),
    ui.layout_columns(
        # Left Panel
        ui.panel_well(
            ui.h1("🎬 Sabri’s Box Office Dashboard"),
            ui.h4("💸 Movie Revenue Explorer"),
            ui.output_text("selection_text"),
            ui.output_ui("revenue_box"),
            ui.output_plot("revenue_plot", height="400px"),
            ui.output_plot("revenue_pie", height="400px"),
        ),
        # Right Panel
        ui.panel_well(
            ui.h4("🎞️ Movie Data"),
            ui.output_data_frame("filtered_table"),
            ui.output_ui("summary_box")  # 👈 Summary section
        ),
        col_widths=(6, 6)
    )
)

# Server logic
def server(input, output, session):

    # Dynamically update inputs
    @reactive.Effect
    def update_inputs():
        df = read_movies()
        years = sorted(df["year"].dropna().astype(str).unique())

        month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December']
        months_available = df["month"].dropna().unique().tolist()
        months = [m for m in month_order if m in months_available]

        ui.update_select("year", choices=years, selected=years[0])
        ui.update_checkbox_group("months", choices=months, selected=months)

    # Filtered dataset
    @reactive.Calc
    def filtered_data():
        df = read_movies()
        req(input.year())
        req(input.months())
        return df[
            (df["year"].astype(str) == input.year()) &
            (df["month"].isin(input.months()))
        ]

    # Selection text
    @output
    @render.text
    def selection_text():
        df = filtered_data()
        return f"🎥 Showing {len(df)} movies from {input.year()} in months: {', '.join(input.months())}."

    # Revenue value box
    @output
    @render.ui
    def revenue_box():
        total = filtered_data()["revenue"].sum()
        return ui.value_box(f"${total:,.2f}", "🎯 Total Revenue", showcase="💰")

    # Data table
    @output
    @render.data_frame
    def filtered_table():
        return filtered_data()[["movie", "month", "year", "revenue"]].sort_values(by="revenue", ascending=False)

    # Revenue bar plot
    @output
    @render.plot
    def revenue_plot():
        df = filtered_data()
        month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December']
        df_grouped = df.groupby("month")["revenue"].sum().reindex(month_order).dropna()

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(df_grouped.index, df_grouped.values, color="#FF6B6B", edgecolor="black")
        ax.set_title(f"📊 Total Revenue by Month in {input.year()}")
        ax.set_xlabel("Month")
        ax.set_ylabel("Revenue ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        return fig

    # Revenue pie chart
    @output
    @render.plot
    def revenue_pie():
        df = filtered_data()
        df_grouped = df.groupby("month")["revenue"].sum()
        if df_grouped.empty:
            fig, ax = plt.subplots()
            ax.text(0.5, 0.5, "No Data", ha='center', va='center')
            return fig

        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(df_grouped.values,
               labels=df_grouped.index,
               autopct='%1.1f%%',
               startangle=90,
               colors=plt.cm.Pastel1.colors)
        ax.set_title("📈 Revenue Share by Month")
        ax.axis('equal')
        return fig

    # Summary box under the table
    @output
    @render.ui
    def summary_box():
        df = filtered_data()
        if df.empty:
            return ui.markdown("⚠️ No data to summarize.")

        top_movie = df.loc[df["revenue"].idxmax()]
        lowest_month = df.groupby("month")["revenue"].sum().idxmin()
        total_movies = len(df)

        return ui.panel_well(
            ui.h4("📊 Quick Insights"),
            ui.tags.ul(
                ui.tags.li(f"🎖️ Top Movie: **{top_movie['movie']}** (${top_movie['revenue']:,})"),
                ui.tags.li(f"🧊 Lowest Revenue Month: **{lowest_month}**"),
                ui.tags.li(f"🎬 Movies Displayed: **{total_movies}**"),
            )
        )

# Run the app
app = App(app_ui, server)
