import subprocess
import platform
import datetime
import os

LOG_FILE = "log.txt"

def ping(ip):
    """Ping une IP et retourne True si accessible"""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", "-w", "1000", ip]
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=3
        )
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False

def write_log(message):
    """Écrit dans le fichier log avec timestamp"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)
    print(line.strip())

def scan_network(base_ip="192.168.1", start=1, end=20):
    """Scanne les IPs du réseau local"""
    write_log(f"=== Début du scan réseau {base_ip}.{start} → {base_ip}.{end} ===")
    
    actives = []
    inactives = []

    for i in range(start, end + 1):
        ip = f"{base_ip}.{i}"
        if ping(ip):
            write_log(f"✅ {ip} — ACTIF")
            actives.append(ip)
        else:
            write_log(f"❌ {ip} — INACTIF")
            inactives.append(ip)

    write_log(f"=== Scan terminé : {len(actives)} actifs / {len(inactives)} inactifs ===")
    return actives, inactives

def afficher_rapport(actives, inactives):
    """Affiche un rapport propre dans le terminal"""
    print("\n" + "="*50)
    print("       RAPPORT RÉSEAU — PACÔME SINWILLY")
    print("="*50)
    print(f"\n✅ Hôtes ACTIFS ({len(actives)}) :")
    for ip in actives:
        print(f"   → {ip}")
    print(f"\n❌ Hôtes INACTIFS ({len(inactives)}) :")
    for ip in inactives:
        print(f"   → {ip}")
    print("\n" + "="*50)
    print(f"📄 Log sauvegardé dans : {os.path.abspath(LOG_FILE)}")
    print("="*50 + "\n")

if __name__ == "__main__":
    print("\n🔍 Network Monitor — Pacôme SINWILLY")
    print("Scan du réseau 192.168.1.1 → 192.168.1.20\n")
    
    actives, inactives = scan_network(
        base_ip="192.168.1",
        start=1,
        end=20
    )
    afficher_rapport(actives, inactives)