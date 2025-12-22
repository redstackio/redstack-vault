---
tags:
  - ntlm
  - recon
  - enumeration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/ntlm-trigger-get-request]]'
platforms:
  - Web
  - Windows
techniques:
  - '[[Gather Victim Network Information]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9343cf78-6128-4c22-a58e-423ddff8054a
created_at: '2025-12-14T17:31:19.110Z'
updated_at: '2025-12-14T17:31:19.110Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Network Information]]'
---
# Repeat-NTLM-Extraction-on-Additional-Endpoints

## Summary

This procedure extends the initial NTLM challenge extraction by targeting multiple protected web paths or servers, compiling a broader view of internal network components through repeated decoding.

## Description

By iterating the trigger and decode process on various internal blog or application endpoints, attackers can discover diverse domains and hosts, such as different Active Directory realms, enhancing the reconnaissance footprint without alerting defenses.

## Requirements

1. List of additional protected endpoints (e.g., other internal blogs)
2. Burp Suite for batch request handling
3. Prior success on initial endpoint to validate approach

## Defense

Defensive measures and detection strategies:

- Centralize authentication logging across IIS instances
- Rate-limit requests to protected paths
- Audit server configurations for uniform NTLM handling

## Objectives

1. Collect info from multiple sources for comprehensive mapping
2. Identify cross-domain relationships
3. Increase dataset for vulnerability correlation

## Instructions

### Step 1: Identify Additional Targets

**Context**: Scan or enumerate other internal paths using Burp's site map or manual testing.

**Command** (No direct; use Burp Spider):
```bash
# In Burp: Target > Site map > Crawl protected sections
```

> Focus on paths like /blog/protected or similar.

### Step 2: Send Repeated Requests

**Context**: Craft and send GET requests to new endpoints, mirroring the initial trigger.

**Command** ([[commands/ntlm-trigger-get-request]] variant):
```bash
GET /blog/protected HTTP/1.1
Host: another-internal-server
Authorization: NTLM
```

> Capture and decode as before. Expected: Target: MTNGROUPSA, MsvAvNbComputerName: PSWSPEMVA21, MsvAvDnsDomainName: mtn.co.za.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Network Information]] Gather Victim Network Information

### Sub-Techniques

- None

## Commands Used

- [[commands/ntlm-trigger-get-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- ntlm-repeat
- network-mapping
