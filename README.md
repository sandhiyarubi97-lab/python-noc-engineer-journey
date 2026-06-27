# Python-NOC-Journey
30 Day Python for NOC Engineer
Learning Python for Network Operations and Automation from Chennai 🇮🇳

## 📈 Progress: 11/30 Days Complete

- [x] **Day 1:** Variables, input(), print()
- [x] **Day 2:** String methods - split(), strip(), replace()
- [x] **Day 3:** Loops - for/while + break/continue
- [x] **Day 4:** Lists and Dictionaries - NOC inventory basics
- [x] **Day 5:** File Handling - Log Analyzer
- [x] **Day 6:** Netmiko - SSH to Cisco devices
- [x] **Day 7:** TextFSM - Parse `show` command output
- [x] **Day 8:** CSV Alerting - Alert for DOWN interfaces
- [x] **Day 9:** Config Backup - Netmiko + TextFSM + Mock Fallback
- [x] **Day 10:** Logging - 24x7 monitoring + audit trail
<<<<<<< HEAD
- [ ] **Day 11:** CSV Reporting - Uptime extraction + daily reports +Email alerts
- [ ] **Day 12:** Multi-threading monitor 10 devices parallel
- [ ] **Day 13:** SNMP Basics - CPU/Memory Monitoring
>>>>>>> b72b5aeddaaf46f6182e4afe2f72329b58188db1
- [ ] **Day 14:** Flask Dashboard - Web UI
- [ ] **Day 15:** Flask Dashboard - Web UI for monitoring
...
- [ ] **Day 30:** Capstone - Full NOC Automation Suite

## 🔥 Key Projects

### **Day 5: Log Analyzer**
Built log analyzer that parses router logs and counts ERROR/WARNING lines.
**Tech:** Python, file I/O, loops, conditionals

### **Day 9: Config Backup Tool**
Automated config backup for Cisco devices using Netmiko. Added TextFSM parsing + mock fallback for when devices are unreachable.
**Tech:** Netmiko, TextFSM, Exception Handling, Production Patterns

### **Day 10: 24x7 Uptime Monitor**
Implemented production-grade logging for router monitoring. Captures all events with timestamps for audit trail. Graceful fallback when devices fail.
**Tech:** `logging` module, Netmiko, `try/except`, Mock-driven development

## 🚀 Run Projects

### **Day 5: Log Checker**
```bash
python Day05_File_Handling/day5_log_checker.py``
