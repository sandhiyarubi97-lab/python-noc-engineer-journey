import smtplib, logging, csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logging.basicConfig(level=logging.INFO)
# ===== CONFIG =====
EMAIL_FROM = "nocalert@gmail.com"
EMAIL_PASS = "xiei gecb peui nalb"
EMAIL_TO = "sandhiyarubi97@gmail.com"


def check_devices():
    critical_list = []
    with open('devices.csv', 'r') as f:
        reader = csv.DictReader(f)
        print("CSV Columns:", reader.fieldnames)

        for row in reader:
            cpu_str = row.get('CPU') or row.get('CPU_%') or row.get('cpu')
            cpu = int(cpu_str) if cpu_str else 0

            status = row.get('Status') or row.get('status')

            if cpu > 80 or status == 'CRITICAL':
                critical_list.append(row)
    return critical_list


def send_email_alert(critical_list):
    if not critical_list:
        logging.info("All devices OK. No email sent.")
        return

    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM  #  quotes + variable
    msg['To'] = EMAIL_TO  #  quotes + variable
    msg['Subject'] = f"NOC CRITICAL ALERT: {len(critical_list)} Device(s)"

    body = "The following devices need attention:\n\n"
    for d in critical_list:
        body += f"- {d['Device']} | {d['IP']} | Status: {d['Status']} | CPU: {d['CPU']}%\n"

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASS)  #  same variable
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        server.quit()
        logging.info("Email Alert Sent Successfully!")
    except Exception as e:
        logging.error(f"Email Failed: {e}")

critical_list = check_devices()
print("Critical devices:", critical_list)
send_email_alert(critical_list)