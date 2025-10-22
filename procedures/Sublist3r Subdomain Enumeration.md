---
id: adad2428-e8bb-476d-b1fd-aef5abc5f179
name: Sublist3r Subdomain Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.474620+00:00'
updated_at: '2023-04-10T20:25:40.518108+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Gather Victim Network Information|T1590 - Gather Victim Network Information]]'
tags:
- '[[Enumerate all subdomains (only if the scope is *.domain.ext)]]'
- '[[Subdomains Enumeration]]'
- '[[Using Sublist3r]]'
commands:
- '[[Enable bruteforce module and list all subdomains of example.com]]'
- '[[Enumerate subdomains of example.com and display results in real-time]]'
- '[[Enumerate subdomains of example.com using specific engines]]'
---

# Sublist3r Subdomain Enumeration

## Summary

Sublist3r is a Python tool designed to enumerate subdomains of websites using OSINT techniques. It is capable of discovering subdomains using search engines, scraping web pages, and brute-forcing DNS records. The tool can be used offensively by attackers to discover additional entry points into a t

## Description

# Description

Sublist3r is a Python tool designed to enumerate subdomains of websites using OSINT techniques. It is capable of discovering subdomains using search engines, scraping web pages, and brute-forcing DNS records. The tool can be used offensively by attackers to discover additional entry points into a target's network. From a technical perspective, Sublist3r uses various search engines and web services to identify subdomains. Sublist3r is a valuable tool for penetration testers and security researchers to identify potential attack vectors. From a business perspective, subdomain enumeration can help organizations identify and secure all their assets on the internet, reducing their attack surface.

## Requirements

1. Access to the internet

1. Python installed on the system

1. Sublist3r tool installed on the system

## Defense

1. Implement proper access controls and authentication mechanisms to prevent unauthorized access to the target network

1. Regularly monitor DNS records for any unauthorized changes or additions

1. Implement network segmentation to limit lateral movement in case of a successful attack

## Objectives

1. Discover all subdomains associated with a target domain

1. Identify potential entry points into a target network

1. Reduce the attack surface by identifying and securing all assets

# Instructions

1. Please use one of the above commands to enumerate subdomains.

**Code**: [[To enumerate subdomains of a specific domain and s]]

> This command is used to enumerate subdomains of a specific domain. It can be used with various options to enable the bruteforce module, use specific engines, and display results in real-time.

**Command** ([[Enumerate subdomains of example.com and display results in real-time]]):

```bash
python sublist3r.py -v -d example.com
```

**Command** ([[Enable bruteforce module and list all subdomains of example.com]]):

```bash
python sublist3r.py -b -d example.com
```

**Command** ([[Enumerate subdomains of example.com using specific engines]]):

```bash
python sublist3r.py -e google,yahoo,virustotal -d example.com
```

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Gather Victim Network Information|T1590 - Gather Victim Network Information]]

## Commands Used

- [[Enable bruteforce module and list all subdomains of example.com]]
- [[Enumerate subdomains of example.com and display results in real-time]]
- [[Enumerate subdomains of example.com using specific engines]]

## Tags

- [[Enumerate all subdomains (only if the scope is *.domain.ext)]]
- [[Subdomains Enumeration]]
- [[Using Sublist3r]]
