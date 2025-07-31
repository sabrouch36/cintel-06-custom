# 🎬 Sabri’s Box Office Dashboard

This is a custom interactive data app built with [PyShiny](https://shiny.posit.co/py/) as part of Module 6 - Custom Interactive App & Engage.

It allows users to explore box office movie revenues by year and month using dynamic filters, data tables, and visualizations.

---

## 🚀 Features

- 🎛️ Interactive filters: select year and months.
- 📊 Bar chart showing total revenue by month.
- 🥧 Pie chart showing revenue share by month.
- 🧾 Data table sorted by revenue.
- 📦 Summary panel: top movie, lowest month, total movies.

---

## 📂 Folder Structure

cintel-06-custom/
│
├── dashboard/
│ └── app_fixed.py ← main app file
│
├── requirements.txt
├── .gitignore
├── README.md


---



---

## 🔗 Useful Links

- 📁 GitHub Repo: [Sabri - cintel-06-custom](https://github.com/sabrouch36/cintel-06-custom)
- 🌐 Live Demo on Shinylive: [View App](https://shinylive.io/py/app/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMAMwCdiYACAZwAsBLCbJjmVYnTJMAgujxMArhwl1KAEzh1ZcKITIcAbnBUBHADoQ+AoU1RQI8qCybWz8w8cHCYUMqgA2xMh44AjLGxPb1sbTzJDQwBiJgBlWE84JhhiTQ4kqzIoJjJiVj5JDzckgGFYgDUmEnJKCMs3bIBeJhBDJnamfTAUtLguxCZgNo6RroAxa2EADS6JLoAhKDo-dNnOsAB5dEo2OD4lNa6RTQa6JgAmQ7AAFV2mRbJXCCv5osIAayYABQsyXborrckmMiuxZsMRu0utdiKgmABxSTPfDrAAiSL6KOhdwAskttB4WFccRwWCwOKQmABJfjEMn+DyYiFMAC6eGZXWwqgBSEG5wADOcAMwsgBUAEZxeyIKNuqQ-v1Bl0AFIWSRLbBXMZwPx0dV0TVYsB4uiENhXMR0DgeYlQQ1zMDKjFXJ0ee3rESSADmkhYESNsTgqAoMD8ByNG3UxDDPIdADlUnBQ+G2RywHJtBBJJiBsBxQBWflF4v8iQCkvFiTigAcFaLZfLFarAE466WLuK22WACxdpjigDshab-YAbH3xc3hyWq9Xp8WWYYAL6RSw0AD6PXSNmaqHkGFRDTGdFgcAAFJkoABKVcxACqVKYRWwxEkdTQqHX0iYzWkWCgXpwOu5KKH4Sxnsyf4gTq4HMiMf5cKgb7AXAjLqBBYBcksVyBmhwgAJrcmsZrEBwhBwCwjRDGAArCl0bKsKhcDqHA8iNF0tFCl0V7SpCHQIRASFkOuZrMe8fjEAAHuuXoMJIqAYSk5BsESAZMeoTA4vKKnEWwpHkZR8gbluFHUUpCpgCyGC5L4fpnjxjF4axjRGZuqTbmZ2n0dZxC2WQ9k8XB-EcBgbB0PZvF8VIIWuHQ7zyMQADuEAYSUcjFPITB+DwoqivEuocLlTCADwbgD++9xkXtIFMrBRgz6vsJJAeJIMAQCwEE1Xxf7mBAqHrolqEeB1UWQn+bDnBhxWADX7cRQAVgCYBDY8xSUwGw0DQZFJIe7ASUsDhgNVI3wSFDVCeuFCSf5XQsC1sXYOdcCXRVQVdSdb5ncEV1gGBdDrp9z2dUdf6nchn0Yag6R-V4-qHVFsOvf+vUeP1g3DUd7TA+9yGXuu9Cnop7lAVkfiMgDI3w5CTX9Rw8h-JRZ6jhIo43oDLMs9EcRKNoZxeF6ZGGIoNCMXQ3Nnohb4SCDZASCwFHkqQV6IKuIwAALpeoWhwBgJRQB4hDMoLTAbR4FByPI65GfZSuAyMci6GLglvhgWHhVeLMjXbDtCRg5kqQFL1MHIZCSHQMquSZLDAOHhOR10vveaSXBe07vvtW7i7PIDKtS8yasKEo1mPXUIyGzdMB3Q9l1WwHRk-kb1qm6xFs0PZAdByHMo0F0xWAKX7cR6YlXBei0jIpUZV5LskMe8DKqcDCAADkEgLxgABWpEpeLZA+9pacT10ysdNnWPF0fciWAX-2A4bP1Q941c2x0tfNMbjfm5b7tRbJr6oKxddGRgb+8lsoE2UtxaiGZKDZm8mXVumcRobS9BIKAkk67hAwDdPwn004ByAb-fcYN3hcDYl0H6awUGNBQRIJqgh2JgCiGMMYo55jMLWKxQCNC6B0JJmod43EA4oIwXAYSGgfDni6IAXg3ABTO0wAASnATM2Yso8C0mAg6AjJJCOEtgIoYYhpdHkYopIZ4AAkN51GP3aOgy6ZF3jtQYFkDQpBGjdnzJ-Pi6CNBejYMJeqb44Ee2ER3euXpD7tGPu4N8udz6KDoFgaGBs4BCwhkBMGisa5Cxfg3JQTcP64Lkvg-+NBAEFJAXHLyB0IEKKgZiKysD3GQg4ELPBrEMBJmDNga26N2iIOQag3cJsMGSCwdDHBljISCIuv5fkGB8wSBmXM9YCYmCHiyGsNgUA6HkRqLGJgJwtm1HDA0wJwdQ4hLCZCXpth+lmEGZg7BASoqCJSWeFp+4TjNQohIXRqFKJvIwMQx6yC3ywnUHQgApOKDA4oaDgvBWsP0SwsgQC9IyRorZqG+UEJRdBhAYAYB+H6VCULOEsGOR0QRssREcDERhCRgAJnbkdUrMSRYgbLkMozSFTyXtEESg0kZ4F5wF0OqDwC8eWByCWcxBFyIlCWifnOJOM8bwESULEy505qMgfic4Jr8cnvxbleDBzh1wfOzO1bKdDIEsvISwbZ8gh6NAmISOA7NoDoDrmIBSH4vwyGFtzFmYAlwsiAA)

---

## 💻 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/sabrouch36/cintel-06-custom

# Create virtual environment
python -m venv .venv

# Activate it
.venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
shiny run --reload dashboard/app_fixed.py

🛠️ Technologies Used
Python 3.10+

PyShiny (Shiny for Python)

Pandas

Matplotlib

Author
Created by Sabri Hamdaoui
MS in Data Analytics
Northwest Missouri State University