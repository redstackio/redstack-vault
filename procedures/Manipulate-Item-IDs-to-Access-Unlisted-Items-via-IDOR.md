---
id: p-manipulate-item-ids-idor
tags:
  - idor
  - access-bypass
  - api
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-view-item]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:29.372Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Manipulate Item IDs to Access Unlisted Items via IDOR

## Summary

This procedure exploits the IDOR vulnerability by directly referencing arbitrary item IDs in API requests to retrieve details of unlisted items that are not visible in the Instacart web catalog.

## Description

Instacart's API allows authenticated requests to item endpoints using direct object references (item IDs) without checking if the item is publicly listed or accessible to the user via the web interface. By manipulating IDs (e.g., incrementing from known values), attackers can discover and view hidden items. This targets the /v2/items/{id} endpoint and assumes prior identification of the API structure. Outcomes include unauthorized item data exposure, enabling further exploitation.

## Requirements

1. Authenticated session token from Instacart login.
2. Known base item ID from catalog (e.g., via web inspection).
3. HTTP client like curl for sequential ID testing.

## Defense

Defensive measures and detection strategies:

- Validate item ID against user permissions and catalog visibility in API logic.
- Implement ID obfuscation or indirect references (e.g., slugs).
- Monitor for sequential or out-of-range ID requests in logs.

## Objectives

1. Bypass web catalog controls to view unlisted item details.
2. Confirm IDOR by accessing non-public objects.
3. Gather data for cart addition in next steps.

## Instructions

### Step 1: Guess Initial Manipulated ID

**Context**: Start with a known visible item ID and increment (e.g., +1 or to high numbers like 99999) to probe for unlisted items.

No command; manually select ID based on patterns observed in catalog.

> Expected: Prepare ID list for batch testing if needed.

### Step 2: Request Unlisted Item Details

**Context**: Send API request with manipulated ID to retrieve hidden item info.

**Command** ([[commands/curl-view-item]]):
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" https://api.instacart.com/v2/items/99999
```

> Success if JSON returns item name, price, etc., not shown in web; failure if 404 or auth error.

### Step 3: Validate Visibility Bypass

**Context**: Cross-check the retrieved item against web catalog search to confirm it's unlisted.

Use browser search; no command.

> Expected: Item not found in web but accessible via API.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques

-

## Commands Used

- [[commands/curl-view-item]]

## Tools Used

-

## Tags

- [[idor]]
- [[access-bypass]]
- [[api]]
