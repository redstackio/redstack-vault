---
tags:
  - proof-of-concept
  - impersonation
  - phishing-setup
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Resource Hijacking]]'
updated_at: '2025-12-14T04:38:39.439Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: aba5d417-d692-453f-b565-e82cbb1eb7af
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Resource Hijacking]]'
---
# Configure-Proof-of-Concept-Storefront

## Summary

This procedure outlines setting up custom content on a claimed Shopify store to demonstrate subdomain control, such as creating a fake storefront for impersonation or phishing.

## Description

Once ownership is gained, Shopify's admin tools allow theme customization, product addition, and script injection. This step proves takeover by altering the subdomain's visible content. Target environment is the web-facing Shopify store. Expected outcomes: Visible changes on the subdomain, enabling attacks like phishing users to the impersonated site.

## Requirements

1. Admin access to the claimed Shopify store
2. Basic web development knowledge for customizations
3. Target subdomain mapped correctly

## Defense

Defensive measures and detection strategies:

- Implement certificate pinning or HSTS for subdomains
- Monitor content changes on third-party hosted subdomains
- Use web application firewalls to detect anomalous content

## Objectives

1. Customize store to mimic target organization
2. Host proof-of-concept malicious content
3. Validate full control for phishing or malware

## Instructions

### Step 1: Access Store Admin

**Context**: Log into the Shopify dashboard for the claimed store.

Navigate to the admin panel via Shopify's login.

> Expected output: Full access to themes, products, and settings.

### Step 2: Customize Theme and Content

**Context**: Edit the storefront to add custom elements.

In the admin, go to Online Store > Themes, edit the theme, and add custom HTML/JS for impersonation (e.g., fake login form).

> No command; UI-based. Expected output: Preview shows custom content.

### Step 3: Publish and Verify

**Context**: Make changes live and test the subdomain.

Publish the theme and access the subdomain URL.

> Expected output: Subdomain displays attacker-controlled page, confirming takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Resource Hijacking]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[Phishing]]
