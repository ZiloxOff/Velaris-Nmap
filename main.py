import os
import sys
import nmap
from colorama import Fore, init

init(autoreset=True)

VERSION = "1.1.0"
AUTHOR = "Izuki"
TOOL_NAME = "Velaris Tools"


# ============================================================
# UTILS
# ============================================================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input(Fore.YELLOW + "\nPress ENTER to return to menu...")


def log(message):
    print(Fore.RED + f"[LOG] {message}")


def error(message):
    print(Fore.RED + f"[ERROR] {message}")


def warning(message):
    print(Fore.YELLOW + f"[WARNING] {message}")


# ============================================================
# ENVIRONMENT CHECK
# ============================================================

def check_environment():
    print(Fore.RED + "\n[SYSTEM] Checking Nmap...")

    try:
        scanner = nmap.PortScanner()
        major, minor = scanner.nmap_version()

    except nmap.PortScannerError:
        error("Nmap is not installed or not found in PATH.")
        error("Download it from: https://nmap.org/download.html")
        return False

    except Exception as exc:
        error(str(exc))
        return False

    print(Fore.RED + f"[SYSTEM] Nmap {major}.{minor} detected.")
    print(Fore.RED + f"[SYSTEM] {TOOL_NAME} v{VERSION} ready.")
    return True


def confirm_exit():
    choice = input(
        Fore.YELLOW
        + "\nExit {0}? [y/N]: ".format(TOOL_NAME)
    )

    if choice.strip().lower() in ("y", "yes"):
        clear()
        print(Fore.RED + "\nGoodbye!\n")
        sys.exit(0)


def is_admin():
    try:
        if os.name == "nt":
            import ctypes
            return bool(ctypes.windll.shell32.IsUserAnAdmin())
        return os.geteuid() == 0
    except Exception:
        return False


# ============================================================
# MAIN ASCII
# ============================================================

def ascii():
    print(Fore.RED + r"""
        __     __  ________  __         ______   _______   ______   ______
       /  |   /  |/        |/  |       /      \ /       \ /      | /      \
       $$ |   $$ |$$$$$$$$/ $$ |      /$$$$$$  |$$$$$$$  |$$$$$$/ /$$$$$$  |
       $$ |   $$ |$$ |__    $$ |      $$ |__$$ |$$ |__$$ |  $$ |  $$ \__$$/
       $$  \ /$$/ $$    |   $$ |      $$    $$ |$$    $$<   $$ |  $$      \
        $$  /$$/  $$$$$/    $$ |      $$$$$$$$ |$$$$$$$  |  $$ |   $$$$$$  |
         $$ $$/   $$ |_____ $$ |_____ $$ |  $$ |$$ |  $$ | _$$ |_ /  \__$$ |
          $$$/    $$       |$$       |$$ |  $$ |$$ |  $$ |/ $$   |$$    $$/
           $/     $$$$$$$$/ $$$$$$$$/ $$/   $$/ $$/   $$/ $$$$$$/  $$$$$$/

                    Made by Izuki
              (for educational purpose only)
               Velaris Tools v%s

                [1] Scan IP / PORT
                [2] Service Detection
                [3] OS Detection
                [4] Ping Scan
                [5] Quick Scan
                [6] Full Scan
                [7] Custom Scan
                [8] Exit
    """ % VERSION)


# ============================================================
# SCAN IP ASCII
# ============================================================

def ascii_scan_ip():
    print(Fore.RED + r"""
      ______    ______    ______   __    __        ______  _______
     /      \  /      \  /      \ /  \  /  |      /      |/       \
    /$$$$$$  |/$$$$$$  |/$$$$$$  |$$  \ $$ |      $$$$$$/ $$$$$$$  |
    $$ \__$$/ $$ |  $$/ $$ |__$$ |$$$  \$$ |        $$ |  $$ |__$$ |
    $$      \ $$ |      $$    $$ |$$$$  $$ |        $$ |  $$    $$/
     $$$$$$  |$$ |   __ $$$$$$$$ |$$ $$ $$ |        $$ |  $$$$$$$/
    /  \__$$ |$$ \__/  |$$ |  $$ |$$ |$$$$ |       _$$ |_ $$ |
    $$    $$/ $$    $$/ $$ |  $$ |$$ | $$$ |      / $$   |$$ |
     $$$$$$/   $$$$$$/  $$/   $$/ $$/   $$/       $$$$$$/ $$/
    """)


# ============================================================
# SERVICE ASCII
# ============================================================

def ascii_service():
    print(Fore.RED + r"""
       _____                  _
      / ____|                (_)
     | (___   ___ _ ____   _____  ___ ___
      \___ \ / _ \ '__\ \ / / |/ __/ _ \
      ____) |  __/ |   \ V /| | (_|  __/
     |_____/ \___|_|    \_/ |_|\___\___|

            SERVICE DETECTION
    """)


# ============================================================
# OS ASCII
# ============================================================

def ascii_os():
    print(Fore.RED + r"""
       ____   _____
      / __ \ / ____|
     | |  | | (___
     | |  | |\___ \
     | |__| |____) |
      \____/|_____/

          OS DETECTION
    """)


# ============================================================
# PING ASCII
# ============================================================

def ascii_ping():
    print(Fore.RED + r"""
       _____  _____ _   _  _____
      |  __ \|_   _| \ | |/ ____|
      | |__) | | | |  \| | |  __
      |  ___/  | | | . ` | | |_ |
      | |     _| |_| |\  | |__| |
      |_|    |_____|_| \_|\_____|

             PING SCAN
    """)


# ============================================================
# QUICK ASCII
# ============================================================

def ascii_quick():
    print(Fore.RED + r"""
        ____  _   _ ___ ____ _  __
       / __ \| | | |_ _/ ___| |/ /
      | |  | | | | || | |   | ' /
      | |__| | |_| || | |___| . \
       \___\_\\___/|___\____|_|\_\

             QUICK SCAN
    """)


# ============================================================
# FULL ASCII
# ============================================================

def ascii_full():
    print(Fore.RED + r"""
       _____ _    _ _      _
      |  ___| |  | | |    | |
      | |_  | |  | | |    | |
      |  _| | |  | | |    | |
      | |   | |__| | |____| |____
      |_|    \____/|______|______|

              FULL SCAN
    """)


# ============================================================
# CUSTOM ASCII
# ============================================================

def ascii_custom():
    print(Fore.RED + r"""
        _____          _
       / ____|        | |
      | |    _   _ ___| |_ ___  _ __ ___
      | |   | | | / __| __/ _ \| '_ ` _ \
      | |___| |_| \__ \ || (_) | | | | | |
       \_____\__,_|___/\__\___/|_| |_| |_|

             CUSTOM SCAN
    """)


# ============================================================
# SHOW TCP PORTS
# ============================================================

def show_tcp_ports(scanner, ip, detailed=False):
    if "tcp" not in scanner[ip]:
        print(Fore.RED + "No TCP ports found.")
        return []

    ports = []

    if detailed:
        print(Fore.RED + "\nPORT        STATE       SERVICE        VERSION")
        print(Fore.RED + "-" * 65)
    else:
        print(Fore.RED + "\nPORT        STATE       SERVICE")
        print(Fore.RED + "-" * 45)

    for port in sorted(scanner[ip]["tcp"]):

        state = scanner[ip]["tcp"][port].get(
            "state",
            "unknown"
        )

        service = scanner[ip]["tcp"][port].get(
            "name",
            "unknown"
        )

        if detailed:
            product = scanner[ip]["tcp"][port].get(
                "product",
                ""
            )
            version = scanner[ip]["tcp"][port].get(
                "version",
                ""
            )
            extra = " ".join(
                x for x in (product, version) if x
            )

            print(
                Fore.RED
                + f"{port}/tcp     {state:<10}  {service:<12}  {extra}"
            )
        else:
            print(
                Fore.RED
                + f"{port}/tcp     {state:<10}  {service}"
            )

        ports.append(port)

    return ports


# ============================================================
# 1 - SCAN IP / PORT
# ============================================================

def port_scan():

    clear()
    ascii_scan_ip()

    print(Fore.RED + "\n========== SCAN IP / PORT ==========\n")

    ip = input(Fore.RED + "Input IP: ")

    if not ip.strip():
        error("No IP provided.")
        pause()
        return

    try:

        scanner = nmap.PortScanner()

        log(f"Starting scan on {ip}...")
        log("Scanning TCP ports...")

        scanner.scan(
            hosts=ip,
            arguments="-sT"
        )

        if ip not in scanner.all_hosts():

            error("Host not found or unreachable.")
            pause()
            return

        print(
            Fore.RED
            + f"\nHost {ip}: "
            + scanner[ip].state()
        )

        ports = show_tcp_ports(
            scanner,
            ip
        )

        if not ports:

            pause()
            return

        print()
        log("Scan completed.")

        selected = input(
            Fore.RED
            + "\nWhich port do you want to use? "
        )

        try:
            selected_port = int(selected)

        except ValueError:

            error("Invalid port.")
            pause()
            return

        if selected_port not in ports:

            error(
                f"Port {selected_port} "
                "was not found."
            )

            pause()
            return

        log(
            f"Scanning {ip}:{selected_port}..."
        )

        scanner.scan(
            hosts=ip,
            ports=str(selected_port),
            arguments="-sT -sV"
        )

        state = scanner[ip]["tcp"][selected_port].get(
            "state",
            "unknown"
        )

        service = scanner[ip]["tcp"][selected_port].get(
            "name",
            "unknown"
        )

        product = scanner[ip]["tcp"][selected_port].get(
            "product",
            ""
        )

        version = scanner[ip]["tcp"][selected_port].get(
            "version",
            ""
        )

        extra = " ".join(
            x for x in (product, version) if x
        )

        print(Fore.RED + "\n========== RESULT ==========")
        print(Fore.RED + f"IP      : {ip}")
        print(Fore.RED + f"PORT    : {selected_port}/tcp")
        print(Fore.RED + f"STATE   : {state}")
        print(Fore.RED + f"SERVICE : {service}")
        if extra:
            print(Fore.RED + f"VERSION : {extra}")
        print(Fore.RED + "============================")

    except nmap.PortScannerError as exc:

        error(f"Nmap error: {exc}")

    except (KeyboardInterrupt, EOFError):

        confirm_exit()
        return

    except Exception as exc:

        error(str(exc))

    pause()


# ============================================================
# 2 - SERVICE DETECTION
# ============================================================

def service_detection():

    clear()
    ascii_service()

    print(Fore.RED + "\n========== SERVICE DETECTION ==========\n")

    ip = input(Fore.RED + "Input IP: ")

    ports = input(
        Fore.RED
        + "Input ports (empty = common ports, "
        "e.g. 80,443 or 1-1000): "
    ).strip()

    try:

        scanner = nmap.PortScanner()

        if ip.strip():

            log(f"Target: {ip}")

        else:

            error("No IP provided.")
            pause()
            return

        if not ports:
            ports = "1-1000"
            log("Ports: 1-1000 (common)")
        else:
            log(f"Ports: {ports}")

        log("Detecting services...")

        scanner.scan(
            hosts=ip,
            ports=ports,
            arguments="-sV"
        )

        if ip in scanner.all_hosts():

            show_tcp_ports(
                scanner,
                ip,
                detailed=True
            )

        else:

            error("Host not found.")

    except nmap.PortScannerError as exc:

        error(str(exc))

    except (KeyboardInterrupt, EOFError):

        confirm_exit()
        return

    except Exception as exc:

        error(str(exc))

    pause()


# ============================================================
# 3 - OS DETECTION
# ============================================================

def os_detection():

    clear()
    ascii_os()

    print(Fore.RED + "\n========== OS DETECTION ==========\n")

    ip = input(Fore.RED + "Input IP: ")

    if not ip.strip():
        error("No IP provided.")
        pause()
        return

    if not is_admin():

        warning("Administrator privileges required for OS detection.")

        if os.name == "nt":
            error("Please run this tool as Administrator.")
        else:
            error("Please run this tool as root (sudo).")

        pause()
        return

    log("Administrator privileges detected.")

    try:

        scanner = nmap.PortScanner()

        log("Starting OS detection...")

        scanner.scan(
            hosts=ip,
            arguments="-O"
        )

        if ip not in scanner.all_hosts():

            error("Host not found.")
            pause()
            return

        if "osmatch" in scanner[ip]:

            matches = scanner[ip]["osmatch"]

            if matches:

                print(Fore.RED + "\nPossible OS:")

                for match in matches:

                    print(
                        Fore.RED
                        + "- "
                        + match.get(
                            "name",
                            "Unknown"
                        )
                    )

            else:

                print(
                    Fore.RED
                    + "No OS detected."
                )

        else:

            print(
                Fore.RED
                + "No OS information."
            )

    except nmap.PortScannerError as exc:

        error(str(exc))

    except (KeyboardInterrupt, EOFError):

        confirm_exit()
        return

    except Exception as exc:

        error(str(exc))

    pause()


# ============================================================
# 4 - PING SCAN
# ============================================================

def ping_scan():

    clear()
    ascii_ping()

    print(Fore.RED + "\n========== PING SCAN ==========\n")

    ip = input(Fore.RED + "Input IP: ")

    if not ip.strip():
        error("No IP provided.")
        pause()
        return

    try:

        scanner = nmap.PortScanner()

        log(f"Checking {ip}...")

        scanner.scan(
            hosts=ip,
            arguments="-sn"
        )

        if ip in scanner.all_hosts():

            print(
                Fore.RED
                + f"\n{ip} is UP"
            )

        else:

            print(
                Fore.RED
                + f"\n{ip} is DOWN or unreachable"
            )

    except nmap.PortScannerError as exc:

        error(str(exc))

    except (KeyboardInterrupt, EOFError):

        confirm_exit()
        return

    except Exception as exc:

        error(str(exc))

    pause()


# ============================================================
# 5 - QUICK SCAN
# ============================================================

def quick_scan():

    clear()
    ascii_quick()

    print(Fore.RED + "\n========== QUICK SCAN ==========\n")

    ip = input(Fore.RED + "Input IP: ")

    if not ip.strip():
        error("No IP provided.")
        pause()
        return

    try:

        scanner = nmap.PortScanner()

        log("Starting quick scan...")

        scanner.scan(
            hosts=ip,
            arguments="-F"
        )

        if ip in scanner.all_hosts():

            show_tcp_ports(
                scanner,
                ip
            )

        else:

            error("Host not found.")

    except nmap.PortScannerError as exc:

        error(str(exc))

    except (KeyboardInterrupt, EOFError):

        confirm_exit()
        return

    except Exception as exc:

        error(str(exc))

    pause()


# ============================================================
# 6 - FULL SCAN
# ============================================================

def full_scan():

    clear()
    ascii_full()

    print(Fore.RED + "\n========== FULL SCAN ==========\n")

    ip = input(Fore.RED + "Input IP: ")

    if not ip.strip():
        error("No IP provided.")
        pause()
        return

    try:

        scanner = nmap.PortScanner()

        log("Starting full TCP scan...")
        log("Scanning ports 1-65535...")
        log("This can take some time.")

        scanner.scan(
            hosts=ip,
            arguments="-p- -sT"
        )

        if ip in scanner.all_hosts():

            show_tcp_ports(
                scanner,
                ip
            )

        else:

            error("Host not found.")

    except nmap.PortScannerError as exc:

        error(str(exc))

    except (KeyboardInterrupt, EOFError):

        confirm_exit()
        return

    except Exception as exc:

        error(str(exc))

    pause()


# ============================================================
# 7 - CUSTOM SCAN
# ============================================================

def custom_scan():

    clear()
    ascii_custom()

    print(Fore.RED + "\n========== CUSTOM SCAN ==========\n")

    ip = input(Fore.RED + "Input IP: ")

    if not ip.strip():
        error("No IP provided.")
        pause()
        return

    arguments = input(
        Fore.RED
        + "Input Nmap arguments (empty = -sV): "
    ).strip()

    if not arguments:
        arguments = "-sV"

    try:

        scanner = nmap.PortScanner()

        log(f"Target: {ip}")
        log(f"Arguments: {arguments}")

        scanner.scan(
            hosts=ip,
            arguments=arguments
        )

        if ip in scanner.all_hosts():

            if "tcp" in scanner[ip]:

                show_tcp_ports(
                    scanner,
                    ip
                )

            print()

            print(
                Fore.RED
                + scanner.csv()
            )

        else:

            error("Host not found.")

    except nmap.PortScannerError as exc:

        error(str(exc))

    except (KeyboardInterrupt, EOFError):

        confirm_exit()
        return

    except Exception as exc:

        error(str(exc))

    pause()


# ============================================================
# MAIN
# ============================================================

def main():

    if not check_environment():
        pause()
        return

    running = True

    while running:

        try:

            clear()

            ascii()

            user_choice = input(
                Fore.RED
                + "Select an option: "
            )

            if user_choice == "1":

                port_scan()

            elif user_choice == "2":

                service_detection()

            elif user_choice == "3":

                os_detection()

            elif user_choice == "4":

                ping_scan()

            elif user_choice == "5":

                quick_scan()

            elif user_choice == "6":

                full_scan()

            elif user_choice == "7":

                custom_scan()

            elif user_choice == "8":

                confirm_exit()
                running = False

            else:

                error("Invalid option.")
                pause()

        except (KeyboardInterrupt, EOFError):

            confirm_exit()
            running = False

        except Exception as exc:

            error(str(exc))
            pause()


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    main()