# Velaris Tools

```
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