---
tags:
  - subdomain-takeover
  - shopify
  - poc
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 77c84bc5-0e53-4a07-b40d-717de2c672d5
created_at: '2025-12-14T04:51:10.894Z'
updated_at: '2025-12-14T04:51:10.894Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure Proof-of-Concept on Taken Over Subdomain

## Summary

This procedure sets up custom content on the claimed subdomain to prove control, simulating attacks like phishing or malware hosting under the legitimate domain.

## Description

After claiming, the attacker configures the Shopify store to display custom pages or themes. This includes adding text, images, or videos as proof-of-concept (PoC). Initial password protection can be applied for stealth, later removed. Shopify-specific issues, like theme compatibility, may require troubleshooting. The result is the subdomain serving attacker-controlled content, enabling deception of users who trust the domain.

## Requirements

1. Claimed Shopify store associated with the subdomain
2. Basic Shopify admin knowledge for theme and page editing
3. Assets like images or videos for PoC

## Defense

Defensive measures and detection strategies:

- Implement certificate pinning or HSTS to detect subdomain anomalies
- Regularly scan subdomains for unauthorized content changes
- Use web application firewalls to block unexpected redirects or content

## Objectives

1. Deploy custom PoC content to demonstrate control
2. Simulate malicious payloads like defacement or phishing
3. Capture evidence of successful hosting

## Instructions

### Step 1: Access Store Admin

**Context**: Log into the claimed store to edit content.

Go to the Shopify admin panel for the associated store.

> Admin dashboard loads with full editing capabilities.

### Step 2: Create Custom Page

**Context**: Add PoC elements to the site.

Create a new page or edit the theme, inserting text like 'A-p0c Subdomain Takeover PoC', uploading images/videos, and publishing. Remove any password protection after setup.

> The subdomain now displays the custom content upon access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[shopify]]
- [[poc]]
