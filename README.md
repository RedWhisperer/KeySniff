# KeySniff
A multi threaded script for sniffing clear-text (HTTP) data and sending filtered keywords to a remote server.

KeySniff has two parts:
1. Agent - a python script that uses scapy to capture packets from a specific port and filter for a filtered keyword (like "password"). After finding the keyword, the agent will send it over HTTP to a remote server.
2. Server - a NodeJS server that waits for POST requests that contain a client's key for validating the source, and if the key is valid, the server stores the data from the client in a text file on the server.

# Usage

<h2>On Server Side</h2>
