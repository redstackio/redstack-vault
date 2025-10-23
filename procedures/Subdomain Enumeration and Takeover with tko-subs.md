---
id: 5c56665b-bb89-41ae-8603-a1bdd3e91e3e
name: Subdomain Enumeration and Takeover with tko-subs
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.777352+00:00'
updated_at: '2023-04-10T20:25:36.688650+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Search Open Technical Databases|T1596 - Search Open Technical Databases]]'
- '[[Subvert Trust Controls|T1553 - Subvert Trust Controls]]'
sub_techniques:
- '[[Digital Certificates|T1596.003 - Digital Certificates]]'
- '[[Install Root Certificate|T1553.004 - Install Root Certificate]]'
tags:
- '[[Subdomains Enumeration]]'
- '[[Subdomain take over]]'
- '[[Using tko-subs]]'
commands:
- '[[Download and Run tko-subs]]'
---

# Subdomain Enumeration and Takeover with tko-subs

## Summary

Subdomain enumeration and takeover is a common technique used by attackers to gain access to sensitive information or systems. This procedure uses the tko-subs tool to enumerate subdomains and identify potential takeover opportunities. By identifying vulnerable subdomains, attackers can take contro

## Description

# Description

Subdomain enumeration and takeover is a common technique used by attackers to gain access to sensitive information or systems. This procedure uses the tko-subs tool to enumerate subdomains and identify potential takeover opportunities. By identifying vulnerable subdomains, attackers can take control of these domains and use them to launch further attacks against the target organization.

TKO-Subs is a tool that can be used to enumerate subdomains and identify potential takeover opportunities. The tool works by querying various DNS servers to identify subdomains and then checks if they are vulnerable to takeover. A subdomain takeover occurs when a domain is pointing to a service (e.g. AWS S3) that the owner of the domain no longer controls. Attackers can take advantage of this by registering the service and taking control of the subdomain.

This procedure can be used by attackers to gain access to sensitive information, exfiltrate data, or launch further attacks against the target organization.

 

## Requirements

1. Access to the internet

1. Access to the tko-subs tool

 

## Defense

1. Ensure that all subdomains are properly managed and not vulnerable to takeover

1. Implement proper DNS management to prevent subdomain takeovers

1. Monitor DNS records for changes or suspicious activity

 

## Objectives

1. Identify subdomains associated with the target organization

1. Identify potential subdomain takeover opportunities

1. Gain access to sensitive information or systems

 

# Instructions

1. To enumerate subdomains and find potential subdomain takeovers, run the following command:

 



**Code**: [[go get github.com/anshumanbh/tko-subs
./bin/tko-su]]



> - The `go get` command is used to download the `tko-subs` tool.
- The `-domains` flag specifies the location of the file containing domains to be scanned.
- The `-data` flag specifies the location of the file containing provider data.
- This tool will scan the specified domains for potential subdomain takeovers and report any findings.



**Command** ([[Download and Run tko-subs]]):

```bash
go get github.com/anshumanbh/tko-subs
./bin/tko-subs -domains=./lists/domains_tkos.txt -data=./lists/providers-data.csv
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Search Open Technical Databases|T1596 - Search Open Technical Databases]]
- [[Subvert Trust Controls|T1553 - Subvert Trust Controls]]

### Sub-Techniques

- [[Digital Certificates|T1596.003 - Digital Certificates]]
- [[Install Root Certificate|T1553.004 - Install Root Certificate]]

## Commands Used

- [[Download and Run tko-subs]]

## Tags

- [[Subdomains Enumeration]]
- [[Subdomain take over]]
- [[Using tko-subs]]


