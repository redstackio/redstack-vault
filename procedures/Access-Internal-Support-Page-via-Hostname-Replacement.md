---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
tags:
  - information-disclosure
  - internal-access
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:06.259Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Internal-Support-Page-via-Hostname-Replacement

## Summary

This procedure uses an exfiltrated internal URL from the agent's browser to access restricted support pages by replacing the localhost hostname with the public domain.

## Description

The XSS exfiltration reveals agent URLs like https://localhost:3000/support/review/{hash}, intended for internal use. By substituting localhost:3000 with the public domain h1-415.h1ctf.com, the endpoint becomes accessible externally without authentication, exposing chat reviews and potentially other internal features. This leverages misconfigured internal routing that doesn't enforce origin checks.

## Requirements

1. Exfiltrated internal URL (e.g., from XSS)
2. Public domain knowledge (h1-415.h1ctf.com)

## Defense

Defensive measures and detection strategies:

- Bind internal services to localhost only with firewall rules
- Implement origin-based access controls on internal endpoints
- Log access to /support/review paths and alert on external IPs
- Use VPN or IP whitelisting for agent tools

## Objectives

1. Gain access to internal support interfaces
2. View sensitive chat logs
3. Prepare for authorization bypass

## Instructions

### Step 1: Parse Exfiltrated URL

**Context**: Extract the path from beacon data.

From ?loc=https://localhost:3000/support/review/{hash}, note the path.

### Step 2: Reconstruct Public URL

**Context**: Replace hostname to access publicly.

Navigate to https://h1-415.h1ctf.com/support/review/{hash}.

> Page loads if routing allows. Expected output: Chat review interface visible.

### Step 3: Verify Access

**Context**: Confirm internal content exposure.

Inspect for agent-only features or data.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- information-disclosure
- internal-access
