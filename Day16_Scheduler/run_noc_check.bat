@echo off
echo [%date% %time%] Starting NOC Health Check...

cd C:\Users\Santhiya R\python-noc-journey\Day13_SNMP
C:\python\python3.9.1\python.exe day13_snmp.py

REM Latest CSV file copy
for /f "delims=" %%i in ('dir /b /o-d snmp_report_*.csv') do (
    copy "%%i" ..\Day14_Dashboard\noc_report.csv /Y
    goto :next
)
:next

cd C:\Users\Santhiya R\python-noc-journey\Day15_Email_Alerts
C:\python\python3.9.1\python.exe email_alert.py

echo [%date% %time%] NOC Check Complete
