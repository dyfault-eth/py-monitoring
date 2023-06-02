# py-monitoring

py-monitoring is a small project that allows monitoring the connectivity to one or multiple servers, as well as their DNS redirection and web servers. If your server times out, you will receive an email. Otherwise, you will have the command output in your terminal.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.

```bash
pip install -r requirements.txt
```

Or 

```bash
pip3 install -r requirements.txt
```

Make sure to create a .env file and add the following variables:
```
# server info (you can remove or add more as needed)
IP1 = your-first-server-ip-addr
IP2 = your-second-server-ip-addr
NAME1 = your-first-server-domain-name
NAME2 = your-second-server-domain-name
NAME3 = your-third-server-domain-name

# mail info
USER = your-email-sender
password = your-google-app-password # you can activate it at : https://myaccount.google.com/apppasswords
recipients = your-receiver-email-addr
```

## Usage

To run the project, you can use the following command:

```bash
python your-path/py-monitoring/main.py
```
Or
```bash
python3 your-path/py-monitoring/main.py
```

### Run the project at regular intervals using a bash script

Create a bash script file named my-bash-file.sh and write the following code:

```
#!/bin/bash

while true; do
  python3 ./python-monitoring/main.py
  sleep 300  # Sleep for 5 minutes (300 seconds)
done
```
Save the file and make it executable using the following command:
```bash
chmod +x my-bash-file.sh
```

Now you can run the project using the following command:
```bash
./my-bash-file.sh
```

### Run the project at regular intervals using crontab
Edit the crontab file by running the following command:
```bash
crontab -e
```

Add the following rule:
```
*/5 * * * * python3 /your-path/py-monitoring/main.py >> /your-path/py-monitoring/log/log.txt 2>&1
```
Save the crontab file. Now the project will run every 5 minutes, and the output will be saved in `/py-monitoring/log/log.txt`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
