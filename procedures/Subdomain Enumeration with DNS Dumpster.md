---
id: 0c0fc5b7-6370-4cf6-8d79-00a25b7687fe
name: Subdomain Enumeration with DNS Dumpster
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.744937+00:00'
updated_at: '2023-04-10T20:25:40.123615+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Gather Victim Network Information|T1590 - Gather Victim Network Information]]'
- '[[Search Open Technical Databases|T1596 - Search Open Technical Databases]]'
tags:
- '[[Enumerate all subdomains (only if the scope is *.domain.ext)]]'
- '[[Subdomains Enumeration]]'
- '[[Using dnsdumpster]]'
commands:
- '[[Clone DNSDumpster repository from GitHub]]'
- '[[Run DNSDumpster tool for domainname.com]]'
---

# Subdomain Enumeration with DNS Dumpster

## Summary

Subdomain enumeration is the process of finding subdomains for a given domain. DNS Dumpster is a tool that can be used to perform subdomain enumeration by querying various sources such as DNS servers, search engines, and other public sources. The tool returns a list of subdomains that can be furthe

## Description

# Description

Subdomain enumeration is the process of finding subdomains for a given domain. DNS Dumpster is a tool that can be used to perform subdomain enumeration by querying various sources such as DNS servers, search engines, and other public sources. The tool returns a list of subdomains that can be further used for reconnaissance or other attacks. 

From an offensive perspective, subdomain enumeration can help an attacker to identify potential targets for further attacks. For example, subdomains can be used to identify web applications that might be vulnerable to known vulnerabilities. From a defensive perspective, subdomain enumeration can help identify potential attack surfaces and improve security posture by taking appropriate measures to secure the identified subdomains. 

In order to use DNS Dumpster, the user needs to provide the domain name and the tool will query various sources to find subdomains. The tool can be used by security researchers, penetration testers, and red teamers.

 

## Requirements

1. Access to the internet

1. DNS Dumpster tool

 

## Defense

1. Implement proper access control measures to prevent unauthorized access to DNS servers

1. Monitor DNS queries and look for any suspicious activity

1. Implement DNSSEC to prevent DNS spoofing attacks

 

## Objectives

1. Identify subdomains for a given domain

1. Identify potential targets for further attacks

1. Improve security posture by taking appropriate measures to secure the identified subdomains

 

# Instructions

1. Use the DNS Dumpster tool to perform reconnaissance on a target domain.

1. Clone the DNS Dumpster repository using the git clone command.
2. Navigate to the cloned directory.
3. Run the python script dnsdumpster.py with the -d flag followed by the target domain name.

Example:

```git clone https://github.com/nmmapper/dnsdumpster
python dnsdumpster.py -d example.com```

 



**Code**: [[git clone https://github.com/nmmapper/dnsdumpster
]]



> The DNS Dumpster tool is used to perform reconnaissance on a target domain. The tool can be used to gather information such as subdomains, IP addresses, and email addresses associated with the target domain. The git clone command is used to download the DNS Dumpster tool from the GitHub repository. The python script dnsdumpster.py is then run with the -d flag followed by the target domain name to perform the reconnaissance.



**Command** ([[Clone DNSDumpster repository from GitHub]]):

```bash
git clone https://github.com/nmmapper/dnsdumpster
```





**Command** ([[Run DNSDumpster tool for domainname.com]]):

```bash
python dnsdumpster.py -d domainname.com
```



## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Gather Victim Network Information|T1590 - Gather Victim Network Information]]
- [[Search Open Technical Databases|T1596 - Search Open Technical Databases]]

## Commands Used

- [[Clone DNSDumpster repository from GitHub]]
- [[Run DNSDumpster tool for domainname.com]]

## Tags

- [[Enumerate all subdomains (only if the scope is *.domain.ext)]]
- [[Subdomains Enumeration]]
- [[Using dnsdumpster]]


