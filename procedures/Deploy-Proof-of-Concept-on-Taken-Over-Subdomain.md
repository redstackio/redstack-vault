---
tags:
  - deployment
  - poc
  - phishing
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/Heroku-Dashboard]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Cloud (Heroku)
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T04:39:01.804Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 79d41e18-834f-44d9-95a9-9acfa69b61aa
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Deploy-Proof-of-Concept-on-Taken-Over-Subdomain

## Summary

This procedure deploys arbitrary content to the taken-over subdomain, demonstrating control through HTML uploads and configurations like redirects and SSL.

## Description

After claiming the subdomain, attackers deploy files via Heroku to host proof-of-concept pages. For competition.shopify.com, an HTML file is uploaded to a path, the index redirects to shopify.com, and SSL is enabled via Let's Encrypt. Target is the claimed Heroku app. Outcomes: Full site control for phishing or malware. Prerequisites: Claimed subdomain and Heroku access.

## Requirements

1. Ownership of the Heroku app with the subdomain
2. Basic web development knowledge for HTML/redirects
3. Optional: ACME client for SSL if not using Heroku's built-in

## Defense

Defensive measures and detection strategies:

- Monitor subdomain traffic for anomalies post-takeover
- Use content security policies and certificate pinning
- Regularly scan for subdomain takeovers with tools like Subjack

## Objectives

1. Upload and serve custom content
2. Configure redirects and SSL for realism
3. Validate control for further exploitation

## Instructions

### Step 1: Deploy HTML File

**Context**: Upload a proof-of-concept page to demonstrate access.

In the Heroku Dashboard, use the deployment interface to push an HTML file to /329a01fddb5a552265170b02c579c85f.html containing control proof.

> Example HTML content: <html><body>Proof of takeover</body></html>

### Step 2: Configure Root Redirect

**Context**: Set up the index page to redirect, mimicking legitimate behavior.

Deploy a redirect configuration or HTML meta-refresh to https://shopify.com for the root path.

> Use Heroku's routing or simple HTML:

```html
<meta http-equiv="refresh" content="0; url=https://shopify.com">
```

> Expected output: Visiting the subdomain redirects immediately.

### Step 3: Enable SSL

**Context**: Add trusted HTTPS to increase phishing efficacy.

In Heroku settings, enable Automated Certificate Management (ACM) with Let's Encrypt.

> Initially enable, then disable if needed for testing.

> Expected output: Valid SSL certificate issued for the subdomain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Heroku-Dashboard]]

## Tags

- [[deployment]]
- [[poc]]
- [[Phishing]]
- [[subdomain-takeover]]
