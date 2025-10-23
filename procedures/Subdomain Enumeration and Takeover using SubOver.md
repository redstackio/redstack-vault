---
id: 4580bc90-1e62-4f50-ac1b-90a68da04c84
name: Subdomain Enumeration and Takeover using SubOver
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.839553+00:00'
updated_at: '2023-04-10T20:25:39.144648+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
- '[[Resource Development|TA0042 - Resource Development]]'
techniques:
- '[[Acquire Infrastructure|T1583 - Acquire Infrastructure]]'
- '[[Active Scanning|T1595 - Active Scanning]]'
- '[[Search Open Technical Databases|T1596 - Search Open Technical Databases]]'
tags:
- '[[Subdomains Enumeration]]'
- '[[Subdomain Takeover]]'
- '[[Using SubOver]]'
commands:
- '[[Install SubOver]]'
- '[[Run SubOver]]'
---

# Subdomain Enumeration and Takeover using SubOver

## Summary

Subdomain Enumeration is the process of finding subdomains of a domain. SubOver is a tool that can identify subdomains that are vulnerable to subdomain takeover. Subdomain takeover is a type of vulnerability that occurs when a subdomain is pointing to a service that is no longer in use, but the DNS

## Description

# Description

Subdomain Enumeration is the process of finding subdomains of a domain. SubOver is a tool that can identify subdomains that are vulnerable to subdomain takeover. Subdomain takeover is a type of vulnerability that occurs when a subdomain is pointing to a service that is no longer in use, but the DNS record still exists. An attacker can take over that subdomain and use it to launch attacks against the organization. The technical explanation is that SubOver automates the process of finding subdomains and checks if they are vulnerable to subdomain takeover. The business value of this procedure is that it helps organizations identify and secure their subdomains, reducing the risk of attacks.

 

## Requirements

1. Access to the target domain's DNS records

1. SubOver tool installed

 

## Defense

1. Regularly monitor subdomains to identify any changes

1. Remove DNS records for services that are no longer in use

1. Implement DNSSEC to prevent DNS spoofing attacks

 

## Objectives

1. Identify subdomains of a domain

1. Identify subdomains that are vulnerable to subdomain takeover

1. Secure vulnerable subdomains to prevent takeover

 

# Instructions

1. To perform subdomain enumeration using SubOver, follow these steps:
1. Install SubOver by running 'go get github.com/Ice3man543/SubOver' command.
2. Run the command './SubOver -l subdomains.txt' to enumerate subdomains from the specified list.

 



**Code**: [[go get github.com/Ice3man543/SubOver
./SubOver -l ]]



> The 'SubOver' tool is used for subdomain enumeration. The command 'go get github.com/Ice3man543/SubOver' installs the tool. The argument '-l' specifies the path to the file containing a list of subdomains to be enumerated. This tool can help identify potential attack vectors and vulnerabilities in the target system.



**Command** ([[Install SubOver]]):

```bash
go get github.com/Ice3man543/SubOver
```





**Command** ([[Run SubOver]]):

```bash
./SubOver -l subdomains.txt
```



## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]
- [[Resource Development|TA0042 - Resource Development]]

### Techniques

- [[Acquire Infrastructure|T1583 - Acquire Infrastructure]]
- [[Active Scanning|T1595 - Active Scanning]]
- [[Search Open Technical Databases|T1596 - Search Open Technical Databases]]

## Commands Used

- [[Install SubOver]]
- [[Run SubOver]]

## Tags

- [[Subdomains Enumeration]]
- [[Subdomain Takeover]]
- [[Using SubOver]]


