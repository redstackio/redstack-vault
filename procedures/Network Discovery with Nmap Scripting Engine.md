---
id: 412f7248-33a0-4e65-bf39-eb5b527d64a1
name: Network Discovery with Nmap Scripting Engine
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.067874+00:00'
updated_at: '2023-04-10T20:25:05.010903+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Network Discovery]]'
- '[[Nmap]]'
commands:
- '[[List Nmap scripts]]'
- '[[nmap -sC : equivalent to --script=default]]'
- '[[nmap --script ''http-enum'' -v web.xxxx.com -p80 -oN http-enum.nmap]]'
- '[[nmap --script smb-enum-users.nse -p 445 [target host]]]'
---

# Network Discovery with Nmap Scripting Engine

## Summary

Network Discovery with Nmap Scripting Engine is a technique used by attackers to identify network hosts and services, as well as vulnerabilities and misconfigurations. The Nmap Scripting Engine is a powerful tool that can be used to automate the discovery process and gather valuable information abo

## Description

# Description

Network Discovery with Nmap Scripting Engine is a technique used by attackers to identify network hosts and services, as well as vulnerabilities and misconfigurations. The Nmap Scripting Engine is a powerful tool that can be used to automate the discovery process and gather valuable information about the target network.

From a technical perspective, Nmap Scripting Engine allows users to write and execute custom scripts that can be used to automate tasks such as version detection, vulnerability scanning, and service enumeration. These scripts can be used to identify potential attack vectors and weaknesses in the target network.

The business value of this technique lies in the ability to identify and address security risks before they can be exploited by attackers. By conducting regular network discovery scans, organizations can proactively identify and remediate vulnerabilities, reducing the risk of a security breach.

## Requirements

1. Access to the target network

1. Authentication credentials (if required)

1. Nmap Scripting Engine installed on the attacker's machine

## Defense

1. Regularly conduct network discovery scans to identify and remediate vulnerabilities

1. Implement strong authentication measures to prevent unauthorized access to the network

1. Monitor network traffic for suspicious activity and take immediate action if an attack is detected

## Objectives

1. Identify all hosts and services running on the target network

1. Identify vulnerabilities and misconfigurations on the target network

1. Gather intelligence on the target network for future attacks

# Instructions

1. To use Nmap Scripting Engine, use the command nmap with the option --script, followed by the name of the script you want to run. You can also use the option -sC to run the default scripts. Use the -v option for verbose output and -oN to save the output to a file. To list all available scripts, use the command ls /usr/share/nmap/scripts/

**Code**: [[nmap -sC : equivalent to --script=default

nmap --]]

> -sC: equivalent to --script=default
--script: run the specified NSE script
-v: increase verbosity level
-oN: save output to a file with the given name
-p: specify the port to scan
ls: list files in a directory

**Command** ([[nmap -sC : equivalent to --script=default]]):

```bash
nmap -sC : equivalent to --script=default
```

**Command** ([[nmap --script 'http-enum' -v web.xxxx.com -p80 -oN http-enum.nmap]]):

```bash
nmap --script 'http-enum' -v web.xxxx.com -p80 -oN http-enum.nmap
```

**Command** ([[nmap --script smb-enum-users.nse -p 445 [target host]]]):

```bash
nmap --script smb-enum-users.nse -p 445 [target host]
```

**Command** ([[List Nmap scripts]]):

```bash
ls /usr/share/nmap/scripts/
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[List Nmap scripts]]
- [[nmap -sC : equivalent to --script=default]]
- [[nmap --script 'http-enum' -v web.xxxx.com -p80 -oN http-enum.nmap]]
- [[nmap --script smb-enum-users.nse -p 445 [target host]]]

## Tags

- [[Network Discovery]]
- [[Nmap]]
