@echo off
echo [%date% %time%] Updating Dashboard...

REM Copy latest CSV from Day13 to here
copy "C:\Users\Santhiya R\python-noc-journey\Day13_SNMP\snmp_report_latest.csv" "C:\Users\Santhiya R\python-noc-journey\Day17_Dashboard\" /Y

REM Run dashboard
C:\python\python3.9.1\python.exe dashboard.py

echo Dashboard ready. Open noc_dashboard.html
pause