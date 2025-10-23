---
id: 75436540-8c96-4524-876c-e65e93d01e2b
name: Subdomain Enumeration using Subfinder
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.509044+00:00'
updated_at: '2023-04-10T20:25:39.498551+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Search Open Technical Databases|T1596 - Search Open Technical Databases]]'
sub_techniques:
- '[[DNS/Passive DNS|T1596.001 - DNS/Passive DNS]]'
tags:
- '[[Enumerate all subdomains (only if the scope is *.domain.ext)]]'
- '[[Subdomains Enumeration]]'
- '[[Using Subfinder]]'
commands:
- '[[Install subfinder]]'
- '[[Run subfinder]]'
- '[[Set Censys credentials]]'
- '[[Set Passivetotal credentials]]'
- '[[Set Riddler credentials]]'
- '[[Set Security Trails credentials]]'
---

# Subdomain Enumeration using Subfinder

## Summary

Subdomain enumeration is the process of discovering subdomains for a given domain. Subdomains can be used to target specific systems or services within an organization's infrastructure. Subfinder is a popular tool used for subdomain enumeration. It works by querying various public sources to gather

## Description

# Description

Subdomain enumeration is the process of discovering subdomains for a given domain. Subdomains can be used to target specific systems or services within an organization's infrastructure. Subfinder is a popular tool used for subdomain enumeration. It works by querying various public sources to gather information about subdomains. By using subfinder, an attacker can gather a list of subdomains that can be used for further attacks.

Technical Explanation: Subfinder is a command-line tool that uses various techniques to discover subdomains. It uses multiple sources such as Certificate Transparency Logs, DNSDumpster, and Virustotal. It also has the ability to use brute force techniques to discover subdomains. Subfinder is written in Go, which makes it fast and efficient.

Business Value: Subdomain enumeration is an essential part of the reconnaissance phase of an attack. It helps an attacker to identify potential targets within an organization's infrastructure. By using subfinder, an attacker can gather a list of subdomains that can be used for further attacks. This information can be used to launch targeted attacks, such as phishing attacks, against specific systems or services within an organization.

 

## Requirements

1. Access to the command-line interface

1. Installation of Subfinder

 

## Defense

1. Ensure that the scope of the subdomain enumeration is limited to the target organization

1. Monitor DNS queries for suspicious activity

1. Implement DNSSEC to prevent DNS spoofing attacks

 

## Objectives

1. Discover subdomains for a given domain

1. Identify potential targets within an organization's infrastructure

 

# Instructions

1. To configure and run Subfinder for scanning a domain, follow these steps:
1. Install Subfinder using the command 'go get github.com/subfinder/subfinder'
2. Configure the required API keys by running the following commands:
   ./Subfinder/subfinder --set-config PassivetotalUsername='USERNAME',PassivetotalKey='KEY'
   ./Subfinder/subfinder --set-config RiddlerEmail="EMAIL",RiddlerPassword="PASSWORD"
   ./Subfinder/subfinder --set-config CensysUsername="USERNAME",CensysSecret="SECRET"
   ./Subfinder/subfinder --set-config SecurityTrailsKey='KEY'
3. Run Subfinder to scan a domain using the command './Subfinder/subfinder -d example.com -o /tmp/results_subfinder.txt'

 



**Code**: [[go get github.com/subfinder/subfinder
./Subfinder/]]



> This command is used to configure and run Subfinder for scanning a domain. The 'go get' command is used to install Subfinder. The subsequent commands are used to configure the required API keys for different services. Finally, the last command is used to run Subfinder for scanning a domain and saving the results to a file. The '-d' option is used to specify the domain to scan and the '-o' option is used to specify the output file path. Users can replace 'example.com' with the domain they want to scan and '/tmp/results_subfinder.txt' with the desired output file path.



**Command** ([[Install subfinder]]):

```bash
go get github.com/subfinder/subfinder
```





**Command** ([[Set Passivetotal credentials]]):

```bash
./Subfinder/subfinder --set-config PassivetotalUsername='USERNAME',PassivetotalKey='KEY'
```





**Command** ([[Set Riddler credentials]]):

```bash
./Subfinder/subfinder --set-config RiddlerEmail="EMAIL",RiddlerPassword="PASSWORD"
```





**Command** ([[Set Censys credentials]]):

```bash
./Subfinder/subfinder --set-config CensysUsername="USERNAME",CensysSecret="SECRET"
```





**Command** ([[Set Security Trails credentials]]):

```bash
./Subfinder/subfinder --set-config SecurityTrailsKey='KEY'
```





**Command** ([[Run subfinder]]):

```bash
./Subfinder/subfinder -d example.com -o /tmp/results_subfinder.txt
```



## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Search Open Technical Databases|T1596 - Search Open Technical Databases]]

### Sub-Techniques

- [[DNS/Passive DNS|T1596.001 - DNS/Passive DNS]]

## Commands Used

- [[Install subfinder]]
- [[Run subfinder]]
- [[Set Censys credentials]]
- [[Set Passivetotal credentials]]
- [[Set Riddler credentials]]
- [[Set Security Trails credentials]]

## Tags

- [[Enumerate all subdomains (only if the scope is *.domain.ext)]]
- [[Subdomains Enumeration]]
- [[Using Subfinder]]


