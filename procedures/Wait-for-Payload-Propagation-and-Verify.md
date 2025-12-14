---
tags:
  - propagation
  - verification
  - shopify
type: procedure
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-13T23:52:21.010Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: cdb53211-34ef-454c-9423-4e5e2001841b
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Wait-for-Payload-Propagation-and-Verify

## Summary

This procedure involves waiting for the injected XSS payload to sync from the Shopify admin to the public apps.shopify.com domain and verifying its presence in the shop profile.

## Description

After saving the payload in the admin email field, Shopify's backend requires approximately 60 minutes to propagate changes to public profiles. Visit the shop's page on apps.shopify.com to inspect the HTML source or rendered content for the unsanitized email. This step confirms the vulnerability's stored nature and public exposure. No tools needed beyond a browser; success indicates the payload is live and ready for exploitation.

## Requirements

1. Injected payload from prior step
2. Shop ID or name for public URL
3. Browser with inspect element capability

## Defense

Defensive measures and detection strategies:

- Implement real-time sanitization during propagation
- Rate-limit or delay public updates for admin changes
- Log and alert on email field modifications
- Regularly audit public profile content

## Objectives

1. Allow backend sync time
2. Confirm payload visibility publicly
3. Validate lack of sanitization

## Instructions

### Step 1: Initiate Wait Period

**Context**: Do not interact further; allow natural propagation.

Wait approximately 60 minutes after saving the admin changes.

### Step 2: Verify on Public Profile

**Context**: Check the shop's app profile for the updated email.

Visit `https://apps.shopify.com/shops/<shopId>` (replace <shopId> with your store's ID). Inspect the page source or rendered sidebar for the email field containing the payload.

**Expected Output**: Email renders with injected HTML, e.g., visible img tag or JS in source.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[propagation]]
- [[verification]]
- [[shopify]]
