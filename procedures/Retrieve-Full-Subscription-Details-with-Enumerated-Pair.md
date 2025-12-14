---
id: proc-uuid-006
name: Retrieve-Full-Subscription-Details-with-Enumerated-Pair
tags:
  - idor
  - data-exfiltration
  - privacy
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-full-details-retrieve]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.684Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Retrieve-Full-Subscription-Details-with-Enumerated-Pair

## Summary

This procedure combines an enumerated user_id with its corresponding subscription_id to access complete details, including user photos, names, and membership information via the IDOR endpoint.

## Description

Using pairs from enumeration (e.g., user_id=███████, subscription_id=179268), the endpoint returns full profile data without authorization, leading to severe privacy violations.

## Requirements

1. Enumerated user_id and subscription_id pair
2. HTTP client for detailed response capture

## Defense

Defensive measures and detection strategies:

- Enforce strict ownership validation on all parameters
- Encrypt or anonymize sensitive user data in responses
- Alert on mismatched user_id/subscription_id pairs

## Objectives

1. Exfiltrate full user subscription details
2. Obtain photos and personal info
3. Complete the privacy attack chain

## Instructions

### Step 1: Request with Paired Parameters

**Context**: Send request with both IDs to retrieve comprehensive data.

**Command** ([[commands/curl-full-details-retrieve]]):
```bash
curl -X GET "https://www.zomato.com/gold/payment-success?subscription_id=179268&user_id=███████" -i
```

> Expected output: HTML/JSON with photo URL, name, membership ID, dates, and plan.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-full-details-retrieve]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- data-exfiltration
- privacy-violation
