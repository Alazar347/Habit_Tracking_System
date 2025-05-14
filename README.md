# 📊 Pixela CLI Tracker

This is a Python command-line application that interfaces with the [Pixela](https://pixe.la) API. It allows users to create an account, log in, create graphs, and manage daily data (pixels) on those graphs.

---

## 🔧 Features

- ✅ Create a Pixela user account
- 🔐 Login and validate existing accounts
- 📈 Create graphs to track habits or data
- 🟩 Add daily data to your graph
- 🔄 Update data on specific dates
- ❌ Delete pixel data by date

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or later
- Internet connection (for accessing the Pixela API)
- Optional: Create a Pixela account manually at https://pixe.la or through this script

### Installation

1. Clone the repository or download the script.

2. Install `requests` if you don’t have it:

```bash
pip install requests
```

3. Run the script:

```bash
python main.py
```

---

## 📘 Usage

### First Run

When you run the script, you will be prompted to either:

1. **Create a new account** (provide a username and token)
2. **Log in to an existing account** (enter the same credentials you used when creating the account)

> 🔒 Your **token** acts like a password. Keep it secure.

---

### Main Menu Options

After login:

1. **Create a new graph** – Define a graph for your data (e.g., exercise, study time).
2. **Add today's data** – Record the current day's entry for your graph.
3. **Update past data** – Modify the quantity of a previously logged pixel.
4. **Delete data** – Remove a pixel from a specific date.
5. **Exit** – End the program.

---

## 🧪 Example Graph Configuration

When creating a graph, you’ll be asked for:

- **Graph ID** – A unique identifier (e.g., `studygraph`)
- **Name** – Human-readable name for the graph
- **Unit** – What you're measuring (e.g., `minutes`, `km`)
- **Type** – Must be either `int` or `float`
- **Color** – One of: `shibafu`, `momiji`, `sora`, `ichou`, `ajisai`, `kuro`

---

## 🔗 API Reference

- [Pixela Official Documentation](https://docs.pixe.la)

---


