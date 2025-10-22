---
id: 89c90a79-b6ab-4dab-bab8-8c138f9adf40
name: Subdomain Enumeration with Aquatone Scan
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.637285+00:00'
updated_at: '2023-04-10T20:25:37.378453+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Search Open Technical Databases|T1596 - Search Open Technical Databases]]'
sub_techniques:
- '[[Digital Certificates|T1596.003 - Digital Certificates]]'
- '[[DNS/Passive DNS|T1596.001 - DNS/Passive DNS]]'
tags:
- '[[Enumerate all subdomains (only if the scope is *.domain.ext)]]'
- '[[Subdomains Enumeration]]'
- '[[Using Aquatone - new version (Go)]]'
commands:
- '[[Amass and Aquatone]]'
- '[[Subfinder and Aquatone]]'
---

# Subdomain Enumeration with Aquatone Scan

## Summary

Subdomain enumeration is a technique used by attackers to identify subdomains of a target domain. Aquatone is a tool that can be used to automate the process of subdomain enumeration and scanning. It is a new version of Aquatone written in Go, which is faster and more efficient. The tool uses vario

## Description

# Description

Subdomain enumeration is a technique used by attackers to identify subdomains of a target domain. Aquatone is a tool that can be used to automate the process of subdomain enumeration and scanning. It is a new version of Aquatone written in Go, which is faster and more efficient. The tool uses various techniques to discover subdomains, including active scanning and passive information discovery. Once the subdomains are discovered, Aquatone can scan them for open ports, HTTP(S) servers, and other information.

From an offensive perspective, subdomain enumeration can be used to identify potential attack vectors and targets. It can also be used to gather information about a target's infrastructure and architecture. From a defensive perspective, subdomain enumeration can help organizations identify and mitigate potential vulnerabilities and attack vectors.

## Requirements

1. Access to the target domain

1. Aquatone tool installed on the system

## Defense

1. Implement strict access controls to restrict access to sensitive information

1. Regularly monitor and log network traffic to detect any suspicious activity

1. Use intrusion detection and prevention systems to detect and prevent attacks

## Objectives

1. Identify all subdomains of a target domain

1. Scan the discovered subdomains for open ports and HTTP(S) servers

1. Gather information about a target's infrastructure and architecture

# Instructions

1. This command is used for subdomain enumeration and Aquatone scan. It uses the Subfinder and Amass tools for subdomain enumeration and Aquatone for scanning the discovered subdomains. 

The command takes a single argument which is the target domain to be scanned. 

The command first uses Subfinder to enumerate subdomains of the target domain by querying the DNS servers 8.8.8.8 and 1.1.1.1. The results are saved in the file /tmp/subresult$1. 

Next, the command uses Aquatone to scan the discovered subdomains by running the command 'cat /tmp/subresult$1 | ./Aquatone/aquatone -ports large -out /tmp/aquatone$1'. This generates an HTML report of the scan results in the directory /tmp/aquatone$1.

Finally, the command uses Amass to perform active brute force subdomain enumeration and saves the results in the file /tmp/hosts.txt. The file is then scanned using Aquatone to generate an HTML report in the directory /tmp/aquatone$1.

**Code**: [[# Subfinder version
./Subfinder/subfinder -d $1 -r]]

> The command uses Subfinder and Amass for subdomain enumeration and Aquatone for scanning the discovered subdomains. 

The '-d' option in the Subfinder command specifies the target domain to be scanned. The '-r' option specifies the DNS servers to be queried for subdomain enumeration. The '-nW' option disables wildcard subdomain enumeration. The '-o' option specifies the output file for the subdomain enumeration results. 

The '-active' and '-brute' options in the Amass command specify active brute force subdomain enumeration. The '-o' option specifies the output file for the subdomain enumeration results. 

The 'cat' command is used to concatenate the contents of the output files and pipe them to Aquatone for scanning. The '-ports' option in the Aquatone command specifies the ports to be scanned. The '-out' option specifies the output directory for the scan results.

**Command** ([[Subfinder and Aquatone]]):

```bash
./Subfinder/subfinder -d $1 -r 8.8.8.8,1.1.1.1 -nW -o /tmp/subresult$1
cat /tmp/subresult$1 | ./Aquatone/aquatone -ports large -out /tmp/aquatone$1
```

**Command** ([[Amass and Aquatone]]):

```bash
./Amass/amass -active -brute -o /tmp/hosts.txt -d $1
cat /tmp/hosts.txt | ./Aquatone/aquatone -ports large -out /tmp/aquatone$1
```

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Search Open Technical Databases|T1596 - Search Open Technical Databases]]

### Sub-Techniques

- [[Digital Certificates|T1596.003 - Digital Certificates]]
- [[DNS/Passive DNS|T1596.001 - DNS/Passive DNS]]

## Commands Used

- [[Amass and Aquatone]]
- [[Subfinder and Aquatone]]

## Tags

- [[Enumerate all subdomains (only if the scope is *.domain.ext)]]
- [[Subdomains Enumeration]]
- [[Using Aquatone - new version (Go)]]
