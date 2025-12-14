---
id: cd9c5260-6355-4088-8fbc-694c55ce37b9
name: Demonstrate-Control-Over-Subdomain
type: procedure
verified: false
submitted: true
created_at: '2025-12-14T04:38:39.741Z'
updated_at: '2025-12-14T04:38:39.741Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - subdomain-takeover
  - proof-of-concept
  - shopify
commands: []
platforms:
  - Web
  - Shopify
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Demonstrate-Control-Over-Subdomain

## Summary

This procedure proves ownership of the taken-over subdomain by configuring and displaying custom content, such as a password-protected page, to illustrate potential for malicious use.

## Description

With control established, modify the Shopify instance to host proof-of-concept content. This finalizes the attack in web environments. Outcomes: Visible evidence of compromise. Prerequisites: Claimed instance access.

## Requirements

1. Access to Shopify admin for the claimed store
2. Basic knowledge of Shopify page creation
3. A simple password for protection (e.g., 'test')

## Defense

Defensive measures and detection strategies:

- Implement subdomain monitoring for unexpected content changes
- Use security headers and CSP to limit hosted content risks
- Alert on DNS changes or new SSL certs for subdomains

## Objectives

1. Set up custom content to prove control
2. Protect it to simulate real attack (e.g., phishing)
3. Validate the subdomain's exploitability

## Instructions

### Step 1: Create a New Page

**Context**: Add content to the store to show ownership.

In Shopify admin, go to Online Store > Pages > Add page, enter title and content (e.g., 'Proof of Takeover').

> Expected output: Page saved and ready for publishing.

### Step 2: Enable Password Protection

**Context**: Secure the store to demonstrate restricted access.

Under Online Store > Preferences, enable 'Password protection' and set password to 'test'.

> Expected output: Store now requires password on access.

### Step 3: Publish and Test

**Context**: Verify the setup on the subdomain.

Save changes, then visit https://subdomain.target.com and enter 'test'.

> Expected output: Password prompt, then your page loads, confirming control.

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
- [[proof-of-concept]]
- [[shopify]]
