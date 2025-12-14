---
id: proc-port-scan-xspa
tags:
  - port-scanning
  - xspa
  - discovery
type: procedure
tools:
  - '[[tools/nc-netcat]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/echo-nc-ssrf-trigger]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T04:39:10.083Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Port-Scan-Internal-Services-via-XSPA

## Summary

Exploit SSRF to perform Cross-Site Port Attack (XSPA) for scanning internal ports and identifying services like FTP, SSH, LDAP, and MSSQL on the target's network.

## Description

By crafting SSRF requests to internal addresses and ports (e.g., 127.0.0.1:20), responses like 503 or timeouts reveal open services behind the ProxySG.

## Requirements

1. Confirmed SSRF from prior steps
2. List of target ports (20,21,22,387,389,1431,1433)
3. Netcat for payload delivery

## Defense

Defensive measures and detection strategies:

- Firewall internal ports from proxy outbound
- Rate-limit or WAF-block suspicious URI patterns
- Log and alert on port-specific internal requests

## Objectives

1. Identify open internal ports
2. Discover running services
3. Map internal network footprint

## Instructions

### Step 1: Craft Port-Specific Requests

**Context**: Target each port with an absolute URI SSRF payload.

For FTP port 20:

**Command** ([[commands/echo-nc-ssrf-trigger]]):
```bash
echo -ne "GET http://127.0.0.1:20/ HTTP/1.1\\r\\n\\r\\n" | nc target-ip 80
```

> 503 response indicates open port. Repeat for other ports, noting timeouts (closed) vs. 503 (open).

### Step 2: Analyze Responses

**Context**: Interpret results to identify services.

503 for ports 20,22,389,1433 suggests FTP, SSH, LDAP, MSSQL active.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used

- [[commands/echo-nc-ssrf-trigger]]

## Tools Used

- [[tools/nc-netcat]]

## Tags

- [[port-scanning]]
- [[xspa]]
- [[Discovery]]
