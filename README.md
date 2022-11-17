# KeySniff
A multi threaded script for sniffing clear-text (HTTP) data and sending filtered keywords to a remote server.

KeySniff has two parts:
1. Agent - a python script that uses scapy to capture packets from a specific port and filter for a filtered keyword (like "password"). After finding the keyword, the agent will send it over HTTP to a remote server.
2. Server - a NodeJS server that waits for POST requests that contain a client's key for validating the source, and if the key is valid, the server stores the data from the client in a text file on the server.

# Usage

## On Server Side
1. Install NodeJS on your server.
```bash
curl -sL https://deb.nodesource.com/setup_16.x -o /tmp/nodesource_setup.sh;
chmod +x /tmp/nodesource_setup.sh
/tmp/nodesource_setup.sh
sudo apt install nodejs -y
```

2. Clone the server repository and CD into the server directory.

3. Install the server NPM dependencies:
```bash
sudo npm install
```

4. Initiating the server:
```bash
sudo node server.js --port 8080 --key secret-key --output passowrds.txt
```
