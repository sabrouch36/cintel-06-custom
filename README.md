# 🎬 Sabri’s Box Office Dashboard

This is a custom interactive dashboard built using [Shiny for Python](https://shiny.posit.co/py/).
It allows users to explore movie box office revenue data across different years and months.

## 💡 Features

- Filter movies by **year** and **month**
- View **total revenue** dynamically
- Interactive **bar chart** of monthly revenue
- **Sortable data table** showing movie-level details
- Built with `shiny`, `pandas`, and `matplotlib`

## 📁 Files Included

- `app.py` – Main PyShiny application
- `box_office_movies.csv` – Movie dataset
- `requirements.txt` – Required Python packages
- `.gitignore` – Common exclusions
- `README.md` – Project overview

## 🚀 How to Run

1. Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
shiny run --reload app.py
```

4. Open in browser at:

```
http://localhost:8000
```

---

**Created by Sabri 🍿**