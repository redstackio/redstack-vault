---
id: proc-uuid-2
tags:
  - phishing
  - social-engineering
  - redirect
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
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:27:57.300Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Trick-Victim-into-Redirecting-to-Attacker-App

## Summary

This procedure uses social engineering via a malicious HTML page to trick the victim into opening a redirect to the attacker's Shopify app support page, initiating the authentication flow.

## Description

The attacker hosts a simple HTML page with JavaScript that automatically opens a new window or iframe to the app's support interactions endpoint (e.g., https://apps.shopify.com/[app_id]/support_interactions/new). This prompts the victim to log in if not authenticated, leading to the token-leaking redirect. Delivery can be via phishing email or link.

## Requirements

1. Control over a web server to host the HTML page
2. Knowledge of the attacker's app ID
3. Victim's email or communication channel for luring

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious links and pop-ups
- Implement browser pop-up blockers and same-origin policies
- Log and alert on unexpected redirects to partner apps

## Objectives

1. Lure victim to controlled page
2. Force interaction with Shopify login flow
3. Position for token exposure on redirect

## Instructions

### Step 1: Host Malicious HTML Page

**Context**: Create and deploy an HTML file that uses JavaScript to open the target URL in a new context.

No specific command; write HTML like: <html><body><script>window.open('https://apps.shopify.com/[app_id]/support_interactions/new', '_blank');</script></body></html> and host on attacker's domain (e.g., via GitHub Pages or VPS).

> Expected output: Page loads and immediately opens new window to Shopify endpoint.

### Step 2: Deliver Page to Victim

**Context**: Send the link via email, chat, or other means, disguising it as legitimate (e.g., "Check this app support").

No specific command; use email client or messaging app to share the URL, ensuring the victim clicks and loads the page.

> Expected output: Victim's browser executes the script and redirects.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.002]] Spearphishing Link

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- phishing
- social-engineering
- redirect
