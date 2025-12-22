---
tags:
  - settings
  - notification
  - uber
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:10.984Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7a48bd46-4932-4ff7-8f26-f9a45009c497
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Email-Subscription-Settings

## Summary

This procedure loads the Uber notification settings page, which uses a URL-based token for access control, revealing the authentication flaw.

## Description

From the profile, selecting email subscriptions reaches a page where preferences like promo emails can be toggled. The vulnerability lies in the URL's random token serving as the sole authenticator. Prerequisites include profile access; outcome is an editable settings interface.

## Requirements

1. Access to profile menu
2. Web browser session
3. JavaScript enabled for dynamic UI

## Defense

Defensive measures and detection strategies:

- Enforce session-based auth over URL tokens
- Expire tokens on logout
- Audit settings changes

## Objectives

1. Load settings page
2. Observe URL structure
3. Confirm editability

## Instructions

### Step 1: Select Settings Link

**Context**: Trigger navigation to the vulnerable page.

In the profile menu, click "Manage your email subscription settings" or similar under privacy options.

> The page loads with toggles for email types (e.g., rides, promotions).

### Step 2: Inspect URL

**Context**: Identify the token for later exploitation.

Check the address bar for a long random string in the query parameters (e.g., ?token=longrandomvalue).

> Note the full URL for copying.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[settings]]
- [[notification]]
- [[uber]]
