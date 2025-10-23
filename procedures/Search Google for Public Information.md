---
id: 2517b61e-7360-4e76-9735-d62ff3593a34
name: Search Google for Public Information
type: procedure
verified: true
submitted: true
created_at: '2019-09-11T23:44:59.419106+00:00'
updated_at: '2023-05-26T00:53:00.909585+00:00'
tactics:
- '[[Organizational Information Gathering|TA0017 - Organizational Information Gathering]]'
techniques:
- '[[Acquire OSINT data sets and information|T1277 - Acquire OSINT data sets and information]]'
platforms:
- Web
tags:
- '[[data exposure]]'
- '[[OSINT]]'
- '[[public]]'
commands:
- '[[Search OSINT for an Entity using theHarvester]]'
---

# Search Google for Public Information

**Status**: ✓ Verified

## Summary

Scrape Google search results for references to a target, including their known IP addresses, domain, users, e-mail addresses and more. 

## Description

# Description

Scrape Google search results for references to a target, including their known IP addresses, domain, users, e-mail addresses and more.



# Instructions





**Command** ([[Search OSINT for an Entity using theHarvester]]):

```bash
theHarvester -d $_DOMAIN -l 50 -b google -f $_OUTPUT.txt
```





## Platforms

- Web

## MITRE ATT&CK Mapping

### Tactics

- [[Organizational Information Gathering|TA0017 - Organizational Information Gathering]]

### Techniques

- [[Acquire OSINT data sets and information|T1277 - Acquire OSINT data sets and information]]

## Commands Used

- [[Search OSINT for an Entity using theHarvester]]

## Tags

- [[data exposure]]
- [[OSINT]]
- [[public]]


