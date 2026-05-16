# 🔍 Network Monitor — Pacôme SINWILLY

Outil Python de surveillance réseau local.

## ✨ Fonctionnalités
- Scan automatique des IPs 192.168.1.1 → 192.168.1.20
- Détection des hôtes actifs et inactifs
- Log horodaté dans `log.txt`
- Rapport terminal propre

## 🛠️ Technologies
- Python 3
- subprocess · datetime · platform

## 🚀 Utilisation

```bash
git clone https://github.com/Pacomesinwilly/network-monitor.git
cd network-monitor
python network_monitor.py
```

## 📄 Exemple de log

```
[2025-05-16 10:00:01] [INFO] === Début du scan réseau ===
[2025-05-16 10:00:02] [INFO] ✅ 192.168.1.1 — ACTIF
[2025-05-16 10:00:03] [INFO] ❌ 192.168.1.2 — INACTIF
```

## 👤 Auteur
**Pacôme SINWILLY** — [GitHub](https://github.com/Pacomesinwilly)