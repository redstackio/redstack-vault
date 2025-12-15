---
tags:
  - shopify
  - webhook-verification
  - invisibility-check
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/list-shopify-webhooks]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:11.023Z'
sub_techniques: []
id: cfe02921-1567-4f4c-a6d7-967cbffd23eb
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-Hidden-Webhook-in-Listing

## Summary

This procedure queries the Shopify API for webhooks after permission revocation to confirm they are filtered out and invisible, highlighting the detection evasion aspect.

## Description

Post-revocation, the API listing endpoint returns an empty result due to insufficient permissions, while the webhook remains operational. This exploits the vulnerability in /admin/webhooks.json, targeting Shopify's RESTful API. Prerequisites include revoked permissions and API credentials. Expected outcome is an empty array response, proving the webhook's hidden state.

## Requirements

1. API credentials file post-revocation
2. curl for API calls
3. Knowledge of webhook creation timestamp for filtering

## Defense

Defensive measures and detection strategies:

- Implement comprehensive webhook inventories beyond standard API calls, e.g., database queries
- Monitor for discrepancies between permission scopes and active event deliveries
- Use Shopify's audit logs to track permission changes and cross-reference with external traffic
- Deploy WAF rules to inspect outbound webhook traffic for unauthorized patterns

## Objectives

1. Query webhooks list via API
2. Confirm empty response despite active webhook
3. Validate invisibility for evasion

## Instructions

### Step 1: Query Webhooks Endpoint

**Context**: Use GET request to fetch webhooks with a since parameter to filter recent ones.

**Command** ([[commands/list-shopify-webhooks]]):

```bash
#!/bin/bash
creds=`cat ../creds`

curl "$creds/admin/webhooks.json?since=1" \
  -H "Content-Type: application/json" 

printf "\n"
```

> This authenticates and requests webhooks since timestamp 1, expecting an empty array [] as output, indicating the webhook is hidden.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/list-shopify-webhooks]]

## Tools Used

- [[tools/curl]]

## Tags

- shopify
- webhook-verification
- invisibility-check
