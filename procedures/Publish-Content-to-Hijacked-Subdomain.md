---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - content-injection
  - defacement
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T04:39:01.938Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Publish-Content-to-Hijacked-Subdomain

## Summary

This procedure demonstrates control over the hijacked subdomain by publishing custom HTML content via Instapage, proving takeover for defacement or phishing.

## Description

With the subdomain claimed, custom landing pages are created and deployed. In a web environment, this serves attacker-controlled content on the official subdomain. Outcomes include visible changes verifiable by site access, with prerequisites being a successful claim.

## Requirements

1. Active Instapage account with claimed subdomain.
2. Basic HTML knowledge for custom content.
3. Browser to verify publication.

## Defense

Defensive measures and detection strategies:

- Implement content security policies (CSP) on subdomains.
- Use web application firewalls to detect anomalous content.
- Regularly verify subdomain content against expected templates.

## Objectives

1. Create and customize a landing page.
2. Publish to the hijacked subdomain.
3. Validate control through external access.

## Instructions

### Step 1: Create Custom Landing Page

**Context**: Build HTML content in Instapage editor.

Use the drag-and-drop builder or HTML block to add proof-of-concept text (e.g., "Subdomain Taken Over").

> Expected: Page preview shows custom content.

### Step 2: Publish and Verify

**Context**: Deploy the page to the subdomain.

Click Publish, select the custom domain, and save.

> Then visit www.hacker.one; expected output: Custom HTML displayed, confirming control.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Defacement]]
- [[web]]
