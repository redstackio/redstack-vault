---
id: proc-steam-intercept-artwork
tags:
  - idor
  - steam
  - intercept
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Firefox-Quantum]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:29.163Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Comment-Post-from-Unrestricted-Artwork

## Summary

This procedure captures an HTTP POST request for commenting on an unrestricted Steam artwork item, providing a template for IDOR modification in the subsequent steps.

## Description

Using Burp Suite as a proxy, post a test comment on an artwork (e.g., ID 1406988713) where no ownership is required. This isolates the comment submission mechanics, including parameters like extended_data, for later tampering to target restricted workshop items.

## Requirements

1. Burp Suite running and browser proxied to it
2. Access to unrestricted sharedfiles (artwork)
3. Test comment text prepared

## Defense

Defensive measures and detection strategies:

- Inspect traffic for proxy anomalies
- Validate all comment requests server-side

## Objectives

1. Post legitimate comment
2. Capture full request details
3. Analyze parameters for modification points

## Instructions

### Step 1: Navigate to Artwork

**Context**: Load an item allowing comments.

Use the browser to visit https://steamcommunity.com/sharedfiles/filedetails/?id=1406988713.

> Artwork page loads.

### Step 2: Post and Intercept

**Context**: Submit comment while capturing in Burp.

Enter 'testrestriction' in the comment box and submit; in Burp Proxy, intercept or view the POST request.

> Request details captured, including sessionid and extended_data JSON.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Firefox-Quantum]]

## Tags

- intercept
- artwork
- post
