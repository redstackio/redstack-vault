---
id: b2177d32-ab8b-4626-95f0-228601d3e970
name: Active Recon - DNS Zone Transfer Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.785986+00:00'
updated_at: '2023-04-10T20:21:18.268597+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Password Policy Discovery|T1201 - Password Policy Discovery]]'
tags:
- '[[Active recon]]'
- '[[Bug Hunting Methodology and Enumeration]]'
- '[[Network discovery]]'
commands:
- '[[Check Master Server IP]]'
- '[[Check Name Servers]]'
- '[[Zone Transfer]]'
---

# Active Recon - DNS Zone Transfer Enumeration

## Summary

DNS Zone Transfer is a technique used to discover subdomains of a target domain. This technique can be used to identify potential attack surfaces and vulnerabilities. By requesting a DNS zone transfer, an attacker can obtain a list of all subdomains associated with a target domain. This information

## Description

# Description

DNS Zone Transfer is a technique used to discover subdomains of a target domain. This technique can be used to identify potential attack surfaces and vulnerabilities. By requesting a DNS zone transfer, an attacker can obtain a list of all subdomains associated with a target domain. This information can be used to launch targeted attacks against specific subdomains or to identify potential targets for further reconnaissance.

From a technical perspective, DNS zone transfers are performed by requesting the transfer of a DNS zone from a primary DNS server to a secondary DNS server. If the primary DNS server is not configured to restrict zone transfers to authorized servers, the secondary server will receive a copy of the entire zone file, including all subdomains associated with the target domain.

The business value of DNS Zone Transfer Enumeration lies in its ability to identify potential attack surfaces before they are exploited by attackers. By identifying all subdomains associated with a target domain, defenders can prioritize their efforts and implement appropriate security measures to protect their assets.

## Requirements

1. Access to a DNS server for the target domain

1. Tools such as dig or nslookup

## Defense

1. Configure DNS servers to restrict zone transfers to authorized servers only

1. Implement network segmentation to limit the impact of a successful DNS zone transfer

1. Regularly monitor DNS logs for suspicious activity

## Objectives

1. Identify all subdomains associated with a target domain

1. Discover potential attack surfaces and vulnerabilities

1. Prioritize security efforts and implement appropriate security measures

# Instructions

1. To view the DNS Zone Transfer results, run the following commands:
1. host -t ns domain.local
2. host master.domain.local
3. dig axfr domain.local @192.168.1.1

**Code**: [[host -t ns domain.local
domain.local name server m]]

> The 'host' command is used to perform DNS lookups and query the DNS servers for information about various DNS records. The '-t ns' option specifies that we are looking for the name servers for the specified domain. The 'dig' command is used to perform DNS queries and retrieve DNS records. The 'axfr' option is used to perform a DNS zone transfer and retrieve all the DNS records for the specified domain. Running these commands will provide you with information about the DNS servers and records for the specified domain.

**Command** ([[Check Name Servers]]):

```bash
host -t ns domain.local
```

**Command** ([[Check Master Server IP]]):

```bash
host master.domain.local
```

**Command** ([[Zone Transfer]]):

```bash
dig axfr domain.local @192.168.1.1
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Password Policy Discovery|T1201 - Password Policy Discovery]]

## Commands Used

- [[Check Master Server IP]]
- [[Check Name Servers]]
- [[Zone Transfer]]

## Tags

- [[Active recon]]
- [[Bug Hunting Methodology and Enumeration]]
- [[Network discovery]]
