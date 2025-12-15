---
id: proc-romit-access-pii-001
name: Access-Disclosed-User-Information-from-Operator-Wallet
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.202Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[T1213.003]]'
tags:
  - information-disclosure
  - pii-access
  - wallet-exploitation
platforms:
  - Web
commands:
  - '[[commands/curl-wallet-query]]'
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1213.003]]'
---

# Access-Disclosed-User-Information-from-Operator-Wallet

## Summary

This procedure retrieves the victim's sensitive PII (verification documents, email, DOB, etc.) automatically added to the attacker's operator wallet immediately after successful PIN brute-force, bypassing SMS/GA verification.

## Description

Post-PIN success, the Romit app adds the victim's full profile to the attacker's wallet without additional checks, exposing PII via the web interface or API. This targets the operator wallet feature and requires a valid session from brute-force. Outcome: Complete data exfiltration with high impact on privacy.

## Requirements

1. Successful PIN authentication session
2. Access to app.romit.io operator wallet view
3. Optional API proxy for querying wallet data

## Defense

Defensive measures and detection strategies:

- Delay wallet addition until full multi-factor verification (SMS/GA)
- Encrypt PII in transit/storage and audit wallet access logs
- Alert on rapid profile additions to new wallets

## Objectives

1. View and extract victim PII from wallet
2. Confirm no further auth required
3. Exfiltrate data (docs, email, DOB)

## Instructions

### Step 1: Refresh Wallet View

**Context**: Log in to app and navigate to operator wallet post-PIN success.

Use the app UI to view 'Operator Wallet' section.

> Victim profile appears automatically.

### Step 2: Query Wallet API

**Context**: Directly fetch data via API if UI insufficient.

Execute [[commands/curl-wallet-query]]:

```bash
curl -X GET https://api.romit.io/v0/wallet/operator \
  -H "Authorization: Bearer <session_token_from_pin>"
```

> Expected output: JSON with user array including {"email":"victim@example.com","dob":"YYYY-MM-DD","documents":["url1","url2"] }.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[T1213.003]] Data from Web Service

### Sub-Techniques


## Commands Used

- [[commands/curl-wallet-query]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[pii-access]]
- [[wallet-exploitation]]
