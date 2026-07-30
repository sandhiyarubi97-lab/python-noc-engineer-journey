# Python-NOC-Journey
30 Day Python for NOC Engineer
Learning Python for Network Operations and Automation 

## 📈 Progress: 30/30 Days Complete

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
- [x] **Day 11:** CSV Reporting - Uptime extraction + daily reports + Email alerts
- [x] **Day 12:** Multi-threading - Monitor 12 devices parallel - 10x speed boost
- [x] **Day 13:** SNMP Basics - CPU/Memory Monitoring
- [x] **Day 14:** Flask Dashboard - Live Web UI with charts
- [x] **Day 15:** Email Alerts - SMTP + CSV attachments + HTML reports
- [x] **Day 16:** Task Scheduler - Automated daily email alerts at 9 AM + Windows Task Scheduler / cron
- [x] **Day 17:** API Monitoring - Check REST API status codes + response time
- [x] **Day 18:** Ping Sweep - Multi-threaded ping for /24
- [x] **Day 19:** Firewall Log Parser - Extract blocked IPs + GeoIP lookup
- [x] **Day 20:** Bandwidth Monitor - psutil + live bandwidth graphs
- [x] **Day 21:** Syslog Server - Receive and store logs from network devices
- [x] **Day 22:** Ticketing Integration - Auto create tickets in Jira/ServiceNow on DOWN
- [x] **Day 23:** Web Scraping - Monitor ISP outage page + alert if new outage
- [x] **Day 24:** Database - Store all logs in SQLite + query dashboard
- [x] **Day 25:** Docker - Containerize NOC Dashboard for easy deployment
- [x] **Day 26:** Telegram Bot - Get DOWN alerts directly on Telegram
- [x] **Day 27:** Role Based Access - Admin vs Viewer login for dashboard
- [x] **Day 28:** Export Tools - Download CSV + PDF reports from dashboard
- [x] **Day 29:** Smart Email Alerts - SMTP alert only when status changes UP->DOWN
- [ ] **Day 30:** Capstone - Full NOC Automation Suite with all modules integrated...


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

### **Day 12: Multi-threaded Monitor**
Cut monitoring time 10x using Python threading. 12 devices in 2.18s vs 24s single-thread.
**Tech:** `threading`, `logging`, Mock network calls, MTTR reduction

### ** Day 13: SNMP Monitor
Built multi-threaded SNMP poller for CPU/Memory. 4 devices in parallel with CRITICAL/WARNING thresholds. Tech: pysnmp, threading, CSV reports

### ** Day 14: NOC Health Dashboard**

Real-time web dashboard for monitoring network devices using SNMP data.

**Features:**
- **Secure Login**: Session-based authentication
- **Live Table**: CPU/Memory with color-coded OK/WARNING/CRITICAL status
- **Bar Chart**: Current CPU & Memory usage for all devices
- **Line Chart**: CPU Trend over last 10 polling cycles
- **Auto Refresh**: Updates every 10 seconds
- **Data Source**: Reads from `snmp_history.csv`

**Tech Stack:** `Python` `Flask` `Jinja2` `Chart.js` `pysnmp` `CSV`

**Screenshot:**
![NOC Dashboard](Day14_Dashboard/Screenshot.png)

### **Day 16: Task Scheduler**
Automated daily 9 AM email report with yesterday's uptime CSV attached.
**Tech:** `schedule` library, `smtplib`, Windows Task Scheduler

### **Day 22: Auto Ticketing**
When service goes DOWN, Python auto-creates Jira ticket with logs attached.
**Tech:** `jira` API, `requests`, Email parsing

### **Day 24: SQLite NOC DB**
Moved from CSV to SQLite. Dashboard now queries DB for 30-day history.
**Tech:** `sqlite3`, SQL, Flask

### **Day 26: Telegram Alerts**
Critical DOWN alerts go to Telegram group in <2 seconds.
**Tech:** `python-telegram-bot`, Webhooks

### **Day 29: Smart Email Alerts**
Email sent ONLY on state change. Prevents spam. Includes HTML table in email body.
**Tech:** `smtplib`, `MIMEMultipart`, State tracking dict

### **Day 30: NOC Automation Suite - CAPSTONE**
Full integrated suite: Dashboard + SNMP + Email + Telegram + Scheduler + DB + Docker
**Tech:** Everything above + Docker + Gunicorn
**Goal:** One command `docker-compose up` runs entire NOC

**How to Run:**
```bash
cd Day14_Dashboard
pip install flask pysnmp
python app.pyThen open http://127.0.0.1:5000
Login:admin/password123
## 🚀 Run Projects

### **Day 5: Log Checker**
```bash
python Day05_File_Handling/day5_log_checker.py

### **Day 13: SNMP check**
python Day13_SNMP/snmp_check.py

### Day 14: Launch Dashboard
python Day14_Dashboard/app.py
then open http://127.0.0.1:5000

### Day 16: Task Scheduler
python Day16_Scheduler/scheduler.py
Windows: Task scheduler at 9AM

### Day 29: Smart Email Dashboard
cd Day29_Email
pip install flask
python day29_app.py
then open http://127.0.0.1:5000
Login: admin/admin123

### **Day 30: NOC-BRAIN Capstone - One Command Deploy**
```bash
cd Day30_deploy
docker-compose up -d
then open http://localhost:5000
Login: admin/admin123
