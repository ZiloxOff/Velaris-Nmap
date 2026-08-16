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
git clone https://github.com/<your-username>/Velaris-Tools.git
```

Enter the project folder:
```
cd Velaris-Tools
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
