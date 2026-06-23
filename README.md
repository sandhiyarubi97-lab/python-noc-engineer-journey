# python-noc-engineer-journey
30 Days python for engineers - Day 1 to 5 complete

Automating network operations with Python. Zero to NOC-ready in 30 days.

## 📅 Progress Tracker

| Day | Topic | Status | Key Skills |
| --- | --- | --- | --- |
| **Day 1-5** | Python Fundamentals | ✅ Complete | Variables, Strings, Loops, Lists/Dicts, File I/O |
| **Day 6** | Netmiko SSH Automation | ✅ Complete | `ConnectHandler`, device login, error handling |
| **Day 7** | Parse `show interface brief` | ✅ Complete | Mock output, CSV export, TextFSM intro |
| **Day 8** | NOC Alert System | ✅ Complete | Read CSV, filter DOWN interfaces, error handling |
| **Day 9** | Config Backup + TextFSM | ⏳ Next | `show run`, structured data parsing |
| **Day 10-30** | Coming Soon | 🔜 | SNMP, APIs, Multi-threading, Web Dashboard |

## 🛠️ Skills Covered So Far
1. **Device Automation:** Netmiko SSH, handling `TimeoutException`, `AuthenticationException`
2. **Data Parsing:** CSV read/write, filtering network data
3. **Error Handling:** `FileNotFoundError`, `ValueError`, DNS issues, Git troubleshooting
4. **NOC Workflows:** Interface monitoring, alert generation, mock-driven development

## 💡 Key Learnings
- we can develop using mock data without live device access
- Every error = Real NOC scenario: DNS fail, Firewall block, File path issues
- Git repo = Your automation portfolio

## 🔥 Run Day 8 Alert Script
```bash
cd Day08_Alert_down
python day_8_alert_down_interfaces.py
