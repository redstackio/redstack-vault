---
id: 26933c78-ecde-48e6-b025-e68c73554e55
name: Subdomain Enumeration with Findomain
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.550491+00:00'
updated_at: '2023-04-10T20:25:38.783459+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
- '[[Gather Victim Network Information|T1590 - Gather Victim Network Information]]'
tags:
- '[[Enumerate all subdomains (only if the scope is *.domain.ext)]]'
- '[[Subdomains Enumeration]]'
- '[[Using Findomain]]'
commands:
- '[[Download findomain-linux]]'
- '[[Make findomain-linux executable]]'
- '[[Run findomain-linux to find subdomains of example.com]]'
- '[[Set up findomain API tokens]]'
---

# Subdomain Enumeration with Findomain

## Summary

Subdomain enumeration is a reconnaissance technique used by attackers to discover subdomains of a target domain. This information can be used to identify potential targets for further attacks. Findomain is a tool used for subdomain enumeration. It discovers subdomains by brute-forcing common subdom

## Description

# Description

Subdomain enumeration is a reconnaissance technique used by attackers to discover subdomains of a target domain. This information can be used to identify potential targets for further attacks. Findomain is a tool used for subdomain enumeration. It discovers subdomains by brute-forcing common subdomain names and checking their DNS records. This technique can be used by attackers to gather information about a target's infrastructure and identify potential vulnerabilities.

From a technical perspective, Findomain uses a combination of DNS queries and brute-force techniques to discover subdomains. The tool is easy to use and can be run from the command line. It can output results in various formats, including CSV and JSON.

Business value of subdomain enumeration is to help organizations understand their attack surface and identify potential vulnerabilities before attackers can exploit them.

 

## Requirements

1. Access to the target domain

1. Findomain tool installed on the attacker's machine

 

## Defense

1. Use strong passwords and multi-factor authentication to prevent unauthorized access to DNS records

1. Monitor DNS records for changes and unauthorized modifications

1. Implement network segmentation to limit the impact of a successful attack

 

## Objectives

1. Discover subdomains of a target domain

1. Identify potential targets for further attacks

 

# Instructions

1. To install and use Findomain, follow the below instructions:

 



**Code**: [[$ wget https://github.com/Edu4rdSHL/findomain/rele]]



> 1. Download the latest version of Findomain with the command: $ wget https://github.com/Edu4rdSHL/findomain/releases/latest/download/findomain-linux
2. Make the downloaded file executable with the command: $ chmod +x findomain-linux
3. Set the required access tokens for various services such as Spyse, VirusTotal, and Facebook with the commands: $ findomain_spyse_token="YourAccessToken"
$ findomain_virustotal_token="YourAccessToken" 
$ findomain_fb_token="YourAccessToken"
4. Run the tool with the command: $ ./findomain-linux -t example.com -o

The -t flag specifies the target domain and -o specifies the output file. You can also use other flags such as -u for subdomain enumeration, -r for recursive subdomain enumeration, and -q for quiet mode.



**Command** ([[Download findomain-linux]]):

```bash
$ wget https://github.com/Edu4rdSHL/findomain/releases/latest/download/findomain-linux
```





**Command** ([[Make findomain-linux executable]]):

```bash
$ chmod +x findomain-linux
```





**Command** ([[Set up findomain API tokens]]):

```bash
$ findomain_spyse_token="YourAccessToken"
$ findomain_virustotal_token="YourAccessToken" 
$ findomain_fb_token="YourAccessToken"
```





**Command** ([[Run findomain-linux to find subdomains of example.com]]):

```bash
$ ./findomain-linux -t example.com -o
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]
- [[Gather Victim Network Information|T1590 - Gather Victim Network Information]]

## Commands Used

- [[Download findomain-linux]]
- [[Make findomain-linux executable]]
- [[Run findomain-linux to find subdomains of example.com]]
- [[Set up findomain API tokens]]

## Tags

- [[Enumerate all subdomains (only if the scope is *.domain.ext)]]
- [[Subdomains Enumeration]]
- [[Using Findomain]]


