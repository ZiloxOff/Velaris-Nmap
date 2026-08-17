MIT license
Velaris-Banner

```
██╗   ██╗███████╗██╗      █████╗ ██████╗ ██╗███████╗
██║   ██║██╔════╝██║     ██╔══██╗██╔══██╗██║██╔════╝
██║   ██║█████╗  ██║     ███████║██████╔╝██║███████╗
╚██╗ ██╔╝██╔══╝  ██║     ██╔══██║██╔══██╗██║╚════██║
 ╚████╔╝ ███████╗███████╗██║  ██║██║  ██║██║███████║
  ╚═══╝  ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
████████╗ ██████╗  ██████╗ ██╗
╚══██╔══╝██╔═══██╗██╔═══██╗██║
   ██║   ██║   ██║██║   ██║██║
   ██║   ██║   ██║██║   ██║██║
   ██║   ╚██████╔╝╚██████╔╝███████╗
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
```

Velaris-Logo **Velaris-Tools** (v1.1.0)

Velaris-Tools is a multifunction network scanning tool dedicated to pentesting, built on top of **Nmap**. The project is open source and designed to be fully configurable according to user needs. All scans are managed through a clean interactive menu, centralizing multiple Nmap features into a single unified platform. No advanced knowledge required to run powerful scans.

⚠️ **Disclaimer:**
This tool is intended exclusively for **educational and lawful use**. Any malicious use is strictly prohibited and disclaimed. As an educational tool, it is your responsibility to only scan systems that you own or that you have explicit permission to test. Unauthorized scanning may be illegal in your country.

📝 **Description:**
⚙️ Compatible with Windows (and Linux with minor adjustments).
🧠 Legal, advanced and optimized version.
🔎 Tool oriented toward pentesting and host/network discovery.
🖥️ Interactive CLI menu wrapping Nmap scans.
📁 Simple one-click setup via `setup.bat`.
🔒 Detects Administrator privileges before sensitive scans.
📊 Clean colored output with service and version detection.

📸 **Preview:**
```
[8] Exit selected.

        __     __  ________  __         ______   _______   ______   ______
       /  |   /  |/        |/  |       /      \ /       \ /      | /      \
       $$ |   $$ |$$$$$$$$/ $$ |      /$$$$$$  |$$$$$$$  |$$$$$$/ /$$$$$$  |
       $$ |   $$ |$$ |__    $$ |      $$ |__$$ |$$ |__$$ |  $$ |  $$ \__$$/
       $$  \ /$$/ $$    |   $$ |      $$    $$ |$$    $$<   $$ |  $$      \
        $$  /$$/  $$$$$/    $$ |      $$$$$$$$ |$$$$$$$  |  $$ |   $$$$$$  |
         $$ $$/   $$ |_____ $$ |_____ $$ |  $$ |$$ |  $$ | _$$ |_ /  \__$$ |
          $$$/    $$       |$$       |$$ |  $$ |$$ |  $$ |/ $$   |$$    $$/
           $/     $$$$$$$$/ $$$$$$$$/ $$/   $$/ $$/   $$/ $$$$$$/  $$$$$$/
```

⚙️ **Installation:**

Install the latest version of **Python (3.13)**:
- **Windows:** [Download Here](https://python.org/downloads) (the "PATH" option must be enabled during installation)
- **Linux:** `sudo apt install python3 -y`

Install **Nmap**:
- **Windows:** [Download Here](https://nmap.org/download.html)
- **Linux:** `sudo apt install nmap -y`

Clone the repository:
```
git clone https://github.com/ZiloxOff/Velaris-Nmap.git
```

Enter the project folder:
```
cd Velaris-Nmap
```

Run the setup:
- **Windows:** double-click `setup.bat`
- **Linux:** `pip install -r requirements.txt`

Launch the tool:
- **Windows:** `.venv\Scripts\python main.py`
- **Linux:** `python3 main.py`

🔄 **Update:**
Enter the project folder:
```
cd Velaris-Tools
```
Update launch:
```
git pull
```

🚀 **Features:**

Pentesting:
- **Scan IP / PORT** : TCP scan of a host, then detailed state/service/version report on a chosen port.
- **Service Detection** : Identifies the service, product and version running on your ports.
- **OS Detection** : Fingerprints the target operating system (`-O`). Administrator privileges required.
- **Ping Scan** : Checks if a host is UP or DOWN (`-sn`).
- **Quick Scan** : Fast scan of the 100 most common ports (`-F`).
- **Full Scan** : Full TCP sweep of ports 1-65535 (`-p- -sT`).
- **Custom Scan** : Run any Nmap arguments of your choice and get the CSV output.

Notations:
- `/` : Or
- `<>` : Value (you type it)

👨‍💻 **Credits:**
Developed by: **Izuki**
GitHub: github.com/<your-username>
Legend: MIT License
Version: v1.1.0

------------------------------------------------------------------------------------------------
V2 README.md

> **Made by Izuki** · for educational purposes only

A terminal-based network scanning tool built in Python on top of **Nmap**.

---

## Features

| # | Option            | Description                                    |
|---|-------------------|------------------------------------------------|
| 1 | Scan IP / PORT    | TCP scan + detailed port/service inspection    |
| 2 | Service Detection | Service name, product and version detection    |
| 3 | OS Detection      | Tries to fingerprint the target OS (`-O`)      |
| 4 | Ping Scan         | Checks if a host is up or down (`-sn`)         |
| 5 | Quick Scan        | Fast scan of the 100 most common ports (`-F`)  |
| 6 | Full Scan         | Full TCP sweep of ports 1–65535 (`-p- -sT`)    |
| 7 | Custom Scan       | Run any Nmap arguments of your choice          |
| 8 | Exit              | Leave the tool                                 |

---

## Requirements

- **Python 3.7+**
- **Nmap** (binary) — https://nmap.org/download.html
- Python packages (auto-installed by `setup.bat`):
  - `python-nmap`
  - `colorama`

---

## Installation

### Windows — one click

Double-click **`setup.bat`**. It will:

1. Check Python and pip
2. Create a virtual environment (`.venv`)
3. Upgrade pip
4. Install all requirements
5. Verify that Nmap is available

Then run the tool:

```
.venv\Scripts\python main.py
```

### Manual setup

```
pip install -r requirements.txt
python main.py
```

> Make sure `nmap` is installed and reachable from your `PATH`.

---

## Usage

Choose an option from the menu and follow the prompts. All scans ask for a
target IP first (IPv4 address, hostname, or CIDR range).

Example — option **1 / Scan IP / PORT**:

```
Input IP: 192.168.1.1
[LOG] Starting scan on 192.168.1.1...
...
Which port do you want to use? 80

========== RESULT ==========
IP      : 192.168.1.1
PORT    : 80/tcp
STATE   : open
SERVICE : http
============================
```

---

## Notes

- OS Detection (`-O`) may require **Administrator** privileges on Windows.
- Full Scan scans all 65535 ports and can take a long time.
- Use Custom Scan if you need special flags (e.g. `-sS -T4`).

## Disclaimer

This tool is for **education and authorized testing only**. You are
responsible for everything you scan. Never scan systems that you do not own or
do not have explicit permission to test.

---

© Izuki — Velaris Tools
