---
id: 01de6a66-8c6e-4dca-a82e-d86c437594ae
name: Subdomain Enumeration with Subbrute
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.342730+00:00'
updated_at: '2023-05-26T00:59:20.707380+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Gather Victim Network Information|T1590 - Gather Victim Network Information]]'
sub_techniques:
- '[[DNS|T1590.002 - DNS]]'
tags:
- '[[Enumerate all subdomains (only if the scope is *.domain.ext)]]'
- '[[Subdomains Enumeration]]'
- '[[Using Subbrute]]'
commands:
- '[[Clone subbrute repository]]'
- '[[Run subbrute against domain.example.com]]'
---

# Subdomain Enumeration with Subbrute

## Summary

Subdomain Enumeration is the process of finding subdomains of a domain. Subbrute is a tool that uses a brute force technique to discover subdomains. It works by querying a DNS server and checking for valid responses. Subbrute has a list of common subdomain names that it uses to brute force the subd

## Description

# Description

Subdomain Enumeration is the process of finding subdomains of a domain. Subbrute is a tool that uses a brute force technique to discover subdomains. It works by querying a DNS server and checking for valid responses. Subbrute has a list of common subdomain names that it uses to brute force the subdomains. The tool is useful for discovering subdomains that are not easily found in public records.

From an offensive perspective, subdomain enumeration can be used to find potential targets for further attacks. It can also be used to discover hidden services or infrastructure that may be vulnerable to attack. From a defensive perspective, subdomain enumeration can be used to identify potential attack surfaces and prioritize security efforts.

## Requirements

1. Access to a DNS server

1. Permission to perform subdomain enumeration

1. Subbrute tool installed

## Defense

1. Monitor DNS queries for suspicious activity

1. Implement rate limiting on DNS queries to prevent abuse

1. Use DNSSEC to protect against DNS spoofing attacks

## Objectives

1. Discover subdomains of a domain

1. Identify potential targets for further attacks

1. Identify hidden services or infrastructure

# Instructions

1. This command is used for subdomain enumeration. It clones the subbrute tool from the GitHub repository and runs it against the specified domain. 

**Code**: [[git clone https://github.com/TheRook/subbrute
pyth]]

> The 'git clone' command is used to download the subbrute tool from the GitHub repository. The 'python subbrute.py' command is then used to run the tool against the specified domain. This command will generate a list of subdomains for the specified domain.

**Command** ([[Clone subbrute repository]]):

```bash
git clone https://github.com/TheRook/subbrute
```

**Command** ([[Run subbrute against domain.example.com]]):

```bash
python subbrute.py domain.example.com
```

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Gather Victim Network Information|T1590 - Gather Victim Network Information]]

### Sub-Techniques

- [[DNS|T1590.002 - DNS]]

## Commands Used

- [[Clone subbrute repository]]
- [[Run subbrute against domain.example.com]]

## Tags

- [[Enumerate all subdomains (only if the scope is *.domain.ext)]]
- [[Subdomains Enumeration]]
- [[Using Subbrute]]
