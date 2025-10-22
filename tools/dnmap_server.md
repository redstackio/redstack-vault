---
id: f534f6c5-5c6b-4c98-b77e-5d152b5a9f83
name: dnmap_server
type: tool
verified: false
created_at: '2019-08-28T21:17:36.954532+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# dnmap_server

## Overview

dnmap is a framework to distribute nmap scans among several clients. It reads an already created file with nmap commands and send those commands to each client connected to it.The framework use a client/server architecture. The server knows what to do and the clients do it. All the logic and statis

## Description

dnmap is a framework to distribute nmap scans among several clients. It reads an already created file with nmap commands and send those commands to each client connected to it.The framework use a client/server architecture. The server knows what to do and the clients do it. All the logic and statistics are managed in the server. Nmap output is stored on both server and client. Usually you would want this if you have to scan a large group of hosts and you have several different internet connections (or friends that want to help you).
