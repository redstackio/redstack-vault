---
id: proc-discover-giftcert-endpoint
tags:
  - csrf
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-endpoint-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:42.819Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover-GiftCert-Purchase-Endpoint

## Summary

This procedure involves searching for hidden or undocumented endpoints in Demandware-based eCommerce sites to identify the GiftCert-Purchase functionality, which allows adding custom gift cards to a user's cart without proper authentication checks.

## Description

In the context of Teavana and Starbucks sites, attackers search demandware.store domains for links like http://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/GiftCert-Purchase. This endpoint supports adding gift cards valued from 5 to 5000 USD directly to the cart, setting the stage for CSRF exploitation. The target environment is web-based eCommerce platforms using Salesforce Commerce Cloud (Demandware). Expected outcomes include endpoint discovery and confirmation of unauthenticated access.

## Requirements

1. Web browser or HTTP client for probing
2. Access to search tools or domain enumeration for Demandware sites
3. No authentication required for initial discovery

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to monitor unusual endpoint access
- Regularly audit hidden endpoints in eCommerce platforms
- Use rate limiting on cart modification APIs

## Objectives

1. Locate the GiftCert-Purchase endpoint
2. Verify it allows cart additions without auth
3. Prepare for further vulnerability assessment

## Instructions

### Step 1: Search for Hidden Links

**Context**: Manually or programmatically search Demandware domains for gift certificate-related endpoints.

**Command** ([[commands/curl-endpoint-test]]):
```bash
curl -X GET "http://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/GiftCert-Purchase"
```

> This GET request retrieves the endpoint page, revealing form parameters for gift card addition. Expected output: HTML form with fields for amount, recipient email, etc.

### Step 2: Confirm Functionality

**Context**: Test adding a low-value gift card to verify cart integration.

**Command** ([[commands/curl-endpoint-test]]):
```bash
curl -X POST "http://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/GiftCert-AddToBasket" \
  -d "dwfrm_giftcert_purchase_amount=5" \
  -d "dwfrm_giftcert_purchase_recipientEmail=test@example.com"
```

> Submits a minimal POST to add to cart. Expected output: Redirect or success response indicating cart update.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-endpoint-test]]

## Tools Used


## Tags

- [[csrf]]
- [[recon]]
- [[web]]
