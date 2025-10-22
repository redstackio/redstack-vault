---
id: 276ba921-9b6b-4612-920a-63c5a0f54702
name: Subdomain Enumeration using Nmap and CRTSH Scan
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.720613+00:00'
updated_at: '2023-04-10T20:25:38.092343+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Gather Victim Network Information|T1590 - Gather Victim Network Information]]'
tags:
- '[[Enumerate all subdomains (only if the scope is *.domain.ext)]]'
- '[[Subdomains Enumeration]]'
- '[[Using Nmap]]'
commands:
- '[[Hostmap-crtsh scan]]'
---

# Subdomain Enumeration using Nmap and CRTSH Scan

## Summary

Subdomain enumeration is an important phase of reconnaissance for an attacker. This procedure uses Nmap and CRTSH Scan to enumerate all subdomains of a given domain. Nmap is used to perform a DNS resolution and identify all the subdomains that are currently active. CRTSH Scan is used to search for 

## Description

# Description

Subdomain enumeration is an important phase of reconnaissance for an attacker. This procedure uses Nmap and CRTSH Scan to enumerate all subdomains of a given domain. Nmap is used to perform a DNS resolution and identify all the subdomains that are currently active. CRTSH Scan is used to search for subdomains that have been issued SSL certificates. The combination of these two techniques provides a comprehensive list of subdomains that can be used for further attacks. This procedure can be used by an attacker to gather intelligence on a target and identify potential attack vectors.

From a technical standpoint, Nmap performs a DNS resolution of the domain and its subdomains. The output is then filtered to identify the subdomains that are currently active. CRTSH Scan searches for subdomains that have been issued SSL certificates. The output of both tools is combined to provide a comprehensive list of subdomains.

The business value of this procedure is that it can help organizations identify potential attack vectors and take proactive measures to secure their infrastructure.

## Requirements

1. Access to the target domain

1. Nmap

1. CRTSH Scan

## Defense

1. Implement proper access controls to prevent unauthorized access to the target domain

1. Monitor DNS requests and SSL certificate issuances for suspicious activity

1. Regularly scan for subdomains and remove any that are no longer in use to reduce the attack surface

## Objectives

1. Identify all subdomains of a given domain

1. Gather intelligence on a target

1. Identify potential attack vectors

# Instructions

1. This command uses Nmap to perform a ping scan (-sn) on the specified host and runs the hostmap-crtsh script to find subdomains associated with the target domain using the Certificate Transparency logs. Replace 'host_to_scan.tld' with the target domain you want to scan.

**Code**: [[nmap -sn --script hostmap-crtsh host_to_scan.tld]]

> The -sn option tells Nmap to skip the port scan and only perform a ping scan. The hostmap-crtsh script is a Nmap script that queries the Certificate Transparency logs to find subdomains associated with the target domain. This can be useful for discovering additional attack surface. The argument 'host_to_scan.tld' should be replaced with the domain name you want to scan.

**Command** ([[Hostmap-crtsh scan]]):

```bash
nmap -sn --script hostmap-crtsh host_to_scan.tld
```

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Gather Victim Network Information|T1590 - Gather Victim Network Information]]

## Commands Used

- [[Hostmap-crtsh scan]]

## Tags

- [[Enumerate all subdomains (only if the scope is *.domain.ext)]]
- [[Subdomains Enumeration]]
- [[Using Nmap]]
