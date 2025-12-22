---
id: proc-configure-custom-content
tags:
  - content-injection
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T04:51:26.591Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Configure Custom Content on Takenover Subdomain

## Summary

This procedure sets up a custom application on the claimed subdomain via Modulus.io, allowing the serving of arbitrary content such as phishing pages or malicious scripts under the trusted domain.

## Description

With the wildcard domain added, configure a simple Node.js or static app in Modulus.io to host custom HTML. In this case, a 'Hello World!' page with '<!--FRANS ROSEN-->' comment demonstrates control. This enables impersonation of LegalRobot's API endpoint. Target environment: Modulus.io app deployment. Prerequisites: Claimed domain. Expected outcomes: Subdomain serves attacker-controlled content, high impact for phishing or data exfiltration.

## Requirements

1. Claimed wildcard domain in Modulus.io
2. Basic app code (e.g., HTML file)
3. Deployment knowledge for Modulus.io

## Defense

Defensive measures and detection strategies:

- Monitor subdomains for unexpected content changes via uptime tools
- Use content security policies (CSP) on main domain
- Scan for takeovers with tools like dnsrecon or takeoverscan

## Objectives

1. Deploy custom content to prove control
2. Enable malicious use cases like phishing
3. Demonstrate full subdomain hijacking

## Instructions

### Step 1: Create Application

**Context**: Build a simple app to host on Modulus.io.

Prepare an index.html with 'Hello World!<!--FRANS ROSEN-->'.

> Expected output: App files ready for upload.

### Step 2: Deploy and Associate Domain

**Context**: Push the app to Modulus.io and link the wildcard.

Use Modulus CLI or dashboard to deploy and set the domain.

> Expected output: App live, serving content on api.legalrobot.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[content-injection]]
- [[subdomain-takeover]]
