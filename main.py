import os
import subprocess
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv


load_dotenv()


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'


user = os.getenv('USER')
recipients = os.getenv("recipients")
password = os.getenv('password')

ip_1 = os.getenv('IP1')
ip_2 = os.getenv('IP2')
server_1 = os.getenv('NAME1')
server_2 = os.getenv('NAME2')
server_3 = os.getenv('NAME3')


def send_email(subject, body):
    sender = user

    # Créer le message
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = recipients
    msg['Subject'] = subject
    msg.set_content(body)
    context = ssl.create_default_context()

    # Envoyer l'email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(user, password)
        smtp.sendmail(user, recipients, msg.as_string())


def check_server(server_name, ip_address):
    # Vérifier le ping
    print("\n----------PING----------")
    ping_cmd = ['ping', '-c', '1', ip_address]
    ping_result = subprocess.run(ping_cmd, capture_output=True, text=True)
    if ping_result.returncode != 0:
        error_message = f"Le serveur {server_name} est inaccessible. Ping Failed.\n\n"
        error_message += f"Résultat du ping :\n{ping_result}"
        send_email('Serveur inaccessible', error_message)
        print(Colors.RED, ping_result, Colors.RESET)
    else:
        print(Colors.GREEN, ping_result, Colors.RESET)

    # Vérifier le DNS
    print("\n----------DNS----------")
    dns_cmd = ['nslookup', server_name]
    dns_result = subprocess.run(dns_cmd, capture_output=True, text=True)
    if dns_result.returncode != 0:
        error_message = f"Le serveur {server_name} rencontre un problème de résolution DNS. nslookup failed.\n\n"
        error_message += f"Résultat de nslookup :\n{dns_result}"
        send_email('Problème DNS', error_message)
        print(Colors.RED, dns_result, Colors.RESET)
    else:
        print(Colors.GREEN, dns_result, Colors.RESET)

    # Vérifier la connexion HTTPS
    print("\n----------HTTPS----------")
    curl_cmd = ['curl', '-I', f'https://{server_name}:443']
    curl_result = subprocess.run(curl_cmd, capture_output=True, text=True)
    print(curl_result)
    if curl_result.returncode != 0:
        error_message = f"La connexion HTTPS au serveur {server_name} a échoué. curl failed.\n\n"
        error_message += f"Résultat de curl :\n{curl_result}"
        send_email('Connexion HTTPS échouée', error_message)
        print(Colors.RED, curl_result, Colors.RESET)
        print(test)
    else:
        print(Colors.GREEN, curl_result, Colors.RESET)


check_server(server_1, ip_1)
check_server(server_2, ip_2)
check_server(server_3, ip_2)
