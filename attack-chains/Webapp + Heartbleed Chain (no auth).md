---
id: 25587901-9da2-4aee-9b3a-3e80fb86d8f1
name: Webapp + Heartbleed Chain (no auth)
type: attack_chain
description: web app, linux, heartbleed, privilege escalation, CTF
verified: false
submitted: false
step_count: 9
created_at: '2019-11-08T21:15:28.072290+00:00'
updated_at: '2023-05-29T16:48:53.162677+00:00'
procedures:
- '[[Convert Hex Dump to Binary]]'
- '[[Port Scan with Vulnerability Enumeration]]'
- '[[Exploit the Heartbleed Vulnerability]]'
- '[[Basic Port Scan with Service Enumeration]]'
- '[[Attach to Existing tmux Server Socket by Path]]'
- '[[Connect to an SSH Server with a Private Key]]'
- '[[List Running Processes]]'
- '[[Directory Brute Force a Web App (Wfuzz)]]'
- '[[Decode a Base64 Encoded String]]'
tags:
- web app
- linux
- heartbleed
- privilege escalation
- CTF
---

# Webapp + Heartbleed Chain (no auth)

**Description**: web app, linux, heartbleed, privilege escalation, CTF

## Overview

This attack chain consists of 9 steps.

## Attack Steps

### Step 1: Basic Port Scan with Service Enumeration

**Procedure**: [[Basic Port Scan with Service Enumeration]]

> Perform an Nmap port scan on a target and enumerate banners of ports 1-1024, as well as popular services (a full list can be found in /usr/share/nmap/nmap-services). 

---

### Step 2: Directory Brute Force a Web App (Wfuzz)

**Procedure**: [[Directory Brute Force a Web App (Wfuzz)]]

> Enumerate a webs app's files and folders by performing a dictionary brute force attack. 

---

### Step 3: Convert Hex Dump to Binary

**Procedure**: [[Convert Hex Dump to Binary]]

> Hex dump is binary data represented in hex pairs. Data in this format can be converted back to binary using tools such as xxd. Example of data in hex pairs: 

---

### Step 4: Port Scan with Vulnerability Enumeration

**Procedure**: [[Port Scan with Vulnerability Enumeration]]

> Perform an Nmap port scan of a target's ports and enumerate with Nmap's "vuln" scripts, enumerating services for popular CVEs and misconfigurations. For a list of all scripts which are run, see the Nmap website. 

---

### Step 5: Exploit the Heartbleed Vulnerability

**Procedure**: [[Exploit the Heartbleed Vulnerability]]

> Heartbleed is a serious vulnerability found in all OpenSSL versions from 1.0.1 (released March 14, 2012)  to 1.0.1g (released April 7, 2014). This vulnerability allows remote attackers to read protected memory on the affected web server, potentially disclosing sensitive information including privat

---

### Step 6: Decode a Base64 Encoded String

**Procedure**: [[Decode a Base64 Encoded String]]

> Decode a Base64 string using Linux's base64 tool. 

---

### Step 7: Connect to an SSH Server with a Private Key

**Procedure**: [[Connect to an SSH Server with a Private Key]]

> Use SSH to connect to a remote SSH server using a private key. 

---

### Step 8: List Running Processes

**Procedure**: [[List Running Processes]]

> List processes to identify potentially vulnerable software and settings. 

---

### Step 9: Attach to Existing tmux Server Socket by Path

**Procedure**: [[Attach to Existing tmux Server Socket by Path]]

> When creating a session, tmux allows users to specify an alternate path for the socket. This opens up a vulnerability if other users are able to read/write to the socket, allowing them to attach to the session with full permissions of the user who opened it. 

---

## Chain Summary

- **Total Steps**: 9
- **Key Procedures**: 9 procedures
