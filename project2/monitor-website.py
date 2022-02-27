import requests
import smtplib
import os
import paramiko
import linode_api4
import time
import schedule

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
RECEIVER_ADDRESS = os.environ.get('RECEIVER_ADDRESS')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')


def restart_server_and_container():
    # restart linode server
    print('Rebooting the server....')
    client = linode_api4.LinodeClient(LINODE_TOKEN)
    nginx_server = client.load(linode_api4.Instance, 35017864)
    nginx_server.reboot()

    # restart the application
    while True:
        # waiting till the server is rebooted and started running
        nginx_server = client.load(linode_api4.Instance, 35017864)
        if nginx_server.status == 'running':
            time.sleep(5)
            restart_container()
            break


def send_notification(message):
    # send email to collage id
    print('Sending an email....')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, RECEIVER_ADDRESS, message)


def restart_container():
    print('Restarting the Application....')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='170.187.232.102', username='root', key_filename='C:/Users/maashree/.ssh/id_rsa')
    stdin, stdout, stderr = ssh.exec_command('docker start 25bf83df38d3')
    print(stdout.readlines())
    ssh.close()


def monitor_application():
    try:
        response = requests.get('http://170-187-232-102.ip.linodeusercontent.com:8080/')
        if response.status_code == 200:
            print("Application is running successfully!")
        else:
            print("Application Down, Fix it!")
            msg = f"Subject: SITE DOWN\nApplication returned {response.status_code}."
            send_notification(msg)

            # restart the application
            restart_container()

    except Exception as ex:
            print(f'Connection error: {ex}')
            msg = "Subject: SITE DOWN\nApplication not accessible at all."
            send_notification(msg)

            restart_server_and_container()


schedule.every(5).minutes.do(monitor_application)

while True:
    schedule.run_pending()
