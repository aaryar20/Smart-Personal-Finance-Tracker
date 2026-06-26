![Python](https://img.shields.io/badge/Python-3.13-blue)

![Streamlit](https://img.shields.io/badge/Streamlit-1.58-red)

![SQLite](https://img.shields.io/badge/SQLite-Database-green)

![License](https://img.shields.io/badge/License-MIT-yellow)
# 💰 Smart Personal Finance Tracker

## 🚀 Live Demo

👉 **[Open Smart Personal Finance Tracker](https://smart-personal-finance-tracker-pgenetdzjl9ksnkwp6bp4w.streamlit.app/)**
A modern **Personal Finance Management System** built with **Python**, **Streamlit**, **SQLite**, and **Plotly**.

The application helps users manage income, expenses, monthly budgets, savings goals, and financial analytics through an intuitive dashboard.

---

## 📷 Project Preview

> Add screenshots here after deployment.

### Dashboard

![Dashboard](docs/screenshots/dashboard.png)

### Transaction History

![Transactions](docs/screenshots/transactions.png)

### Reports

![Reports](docs/screenshots/reports.png)

### Savings Goals

![Savings Goals](docs/screenshots/goals.png)

---

# ✨ Features

## 💰 Transaction Management

- Add Income & Expenses
- Edit Transactions
- Delete Transactions
- Transaction History
- Search Transactions
- Filter by Category
- Filter by Transaction Type
- Date Range Filter

---

## 📊 Dashboard

- Financial Overview
- Income Summary
- Expense Summary
- Current Balance
- Expense Trend
- Expense Distribution
- Monthly Analytics
- Recent Transactions
- Budget Progress
- Smart Insights

---

## 💵 Budget Manager

- Set Monthly Budget
- Budget Progress Bar
- Remaining Budget
- Budget Alerts
- Budget Analytics

---

## 🎯 Savings Goals

- Create Savings Goal
- Track Progress
- Remaining Amount
- Goal Completion Percentage

---

## 📈 Reports

- Expense Reports
- Monthly Reports
- Financial Summary
- CSV Export
- Excel Export
- PDF Export *(Coming Soon)*

---

## 🏷 Category Management

- Dynamic Categories
- Add Categories
- Delete Categories

---

# 🛠 Tech Stack

| Technology | Usage |
|------------|------|
| Python | Backend |
| Streamlit | Web Framework |
| SQLite | Database |
| Pandas | Data Processing |
| Plotly | Charts |
| OpenPyXL | Excel Export |
| ReportLab | PDF Export |

---

# 📁 Project Structure

```
FinanceTracker/
│
├── app.py
├── config.py
├── database.py
├── utils.py
├── requirements.txt
├── style.css
│
├── assets/
│
├── components/
│   ├── sidebar.py
│   ├── cards.py
│   ├── charts.py
│   └── exports.py
│
├── pages/
│   ├── Dashboard.py
│   ├── Add_Transaction.py
│   ├── Transaction_History.py
│   ├── Budget_Manager.py
│   ├── Reports.py
│   ├── Categories.py
│   └── Savings_Goals.py
│
└── docs/
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Personal-Finance-Tracker.git
```

---

## Move into Project

```bash
cd Smart-Personal-Finance-Tracker
```

---

## Create Virtual Environment

### macOS/Linux

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Initialize Database

```bash
python database.py
```

---

## Run Application

```bash
streamlit run app.py
```

---

# 📊 Future Improvements

- User Authentication
- Cloud Database
- Mobile Responsive UI
- AI Financial Advisor
- Expense Forecasting
- Recurring Transactions
- Bill Reminder System

---

# 👨‍💻 Author

**Aarya Rashinker**

Electronics & Telecommunication Engineering Student

Interested in:

- Software Development
- Full Stack Development
- AI Applications
- Data Analytics

---

# 📜 License

This project is licensed under the MIT License.