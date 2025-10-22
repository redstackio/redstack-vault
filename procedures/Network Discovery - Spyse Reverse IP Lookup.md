---
id: 035e340d-6d83-4946-876a-602051e91a8a
name: Network Discovery - Spyse Reverse IP Lookup
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.124072+00:00'
updated_at: '2023-04-10T20:25:06.204589+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Active Scanning|T1595 - Active Scanning]]'
- '[[Gather Victim Network Information|T1590 - Gather Victim Network Information]]'
tags:
- '[[Network Discovery]]'
- '[[Reverse IP Lookup]]'
- '[[Spyse]]'
commands:
- '[[Spyse Domain Lookup]]'
---

# Network Discovery - Spyse Reverse IP Lookup

## Summary

Network Discovery is a critical step in any offensive operation, as it allows an attacker to gain a better understanding of the target environment. By using Spyse's Reverse IP Lookup feature, an attacker can identify other domains and IP addresses that are hosted on the same server as the target do

## Description

# Description

Network Discovery is a critical step in any offensive operation, as it allows an attacker to gain a better understanding of the target environment. By using Spyse's Reverse IP Lookup feature, an attacker can identify other domains and IP addresses that are hosted on the same server as the target domain. This information can be used to identify potential attack vectors and to further refine the scope of the operation.

Spyse's Reverse IP Lookup feature works by querying a database of DNS records and mapping IP addresses to domain names. This allows an attacker to quickly identify other domains that are hosted on the same server as the target domain. In addition, Spyse provides additional information about each domain, such as the hosting provider, SSL certificate information, and DNS records.

From a business perspective, this procedure can help organizations identify potential security risks and take proactive measures to mitigate them. By identifying all domains hosted on a given server, organizations can ensure that all systems are properly secured and that there are no unnecessary attack vectors.

## Requirements

1. Access to the Spyse platform

1. Knowledge of the target domain

## Defense

1. Organizations can mitigate against this type of attack by implementing proper network segmentation and access controls

1. Regularly monitoring and analyzing DNS records can help identify potential security risks

1. Implementing SSL certificates and properly configuring DNS records can help prevent unauthorized access to systems

## Objectives

1. Identify other domains and IP addresses hosted on the same server as the target domain

1. Refine the scope of the operation

1. Identify potential attack vectors

# Instructions

1. This command uses the Spyse tool to look up domains associated with the IP address 52.14.144.171.

**Code**: [[spyse -target 52.14.144.171 --domains-on-ip]]

> The `spyse` command is used to perform reconnaissance on a target. The `-target` flag specifies the IP address of the target. The `--domains-on-ip` flag instructs Spyse to look up domains associated with the target IP address. This command can be useful for discovering other domains that may be associated with a target, which can be helpful in identifying potential attack vectors or expanding the scope of a reconnaissance effort.

**Command** ([[Spyse Domain Lookup]]):

```bash
spyse -target 52.14.144.171 --domains-on-ip
```

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Active Scanning|T1595 - Active Scanning]]
- [[Gather Victim Network Information|T1590 - Gather Victim Network Information]]

## Commands Used

- [[Spyse Domain Lookup]]

## Tags

- [[Network Discovery]]
- [[Reverse IP Lookup]]
- [[Spyse]]
