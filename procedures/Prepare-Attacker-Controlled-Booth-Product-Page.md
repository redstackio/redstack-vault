---
id: proc-prepare-booth-page
tags:
  - setup
  - booth.pm
  - analytics
type: procedure
tools:
  - '[[tools/Google-Analytics]]'
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
updated_at: '2025-12-14T17:30:58.431Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare Attacker-Controlled Booth Product Page

## Summary

This procedure sets up an attacker-controlled product page on Booth.pm, configured with Google Analytics to capture query parameters from redirected OAuth flows.

## Description

In the context of exploiting Pixiv's OAuth path traversal vulnerability, the attacker creates a public shop and product on Booth.pm. The product page serves as the landing spot for victims after authentication, where the leaked OAuth code appears in the URL query string. Google Analytics is integrated to track and exfiltrate this data in real-time. This requires a Booth.pm account and basic web setup knowledge. Expected outcome: A trackable page ready for receiving malicious redirects.

## Requirements

1. Active Booth.pm account with ability to create shops and products
2. Google Analytics account and tracking ID
3. Public accessibility of the product page

## Defense

Defensive measures and detection strategies:

- Monitor for unusual product page creations on integrated platforms like Booth.pm
- Implement query string sanitization or logging on OAuth callbacks
- Use web application firewalls (WAF) to detect path traversal in redirect parameters

## Objectives

1. Establish a controlled endpoint for capturing leaked data
2. Enable real-time monitoring of victim interactions
3. Prepare for code exfiltration without direct server access

## Instructions

### Step 1: Create and Publicize Booth.pm Shop

**Context**: Register a shop to host the product page that will receive redirects.

No specific command; perform via Booth.pm web interface:

- Log in to Booth.pm and create a new shop.
- Set the shop to public visibility.

> This ensures the shop is accessible without authentication barriers.

### Step 2: Register Product and Obtain ID

**Context**: Add a product to the shop, noting its unique ID for use in the path traversal payload.

No specific command; use Booth.pm dashboard:

- Create a new product (e.g., digital item) in the shop.
- Note the product ID (e.g., 4503924) from the URL: https://booth.pm/ja/items/4503924.

> The product page must be public to allow victim redirects.

### Step 3: Configure Google Analytics Tracking

**Context**: Embed analytics to capture query strings from incoming URLs.

No specific command; integrate via Booth.pm settings:

- Obtain a Google Analytics tracking ID (e.g., UA-XXXXX-Y).
- Add the tracking script to the product page HTML or via Booth.pm's analytics integration.

> This setup exposes query parameters like the OAuth code in real-time reports.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Analytics]]

## Tags

- [[setup]]
- [[booth.pm]]
- [[analytics]]
