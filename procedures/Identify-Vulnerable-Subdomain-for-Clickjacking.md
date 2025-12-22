---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - clickjacking
  - subdomain
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:04.543Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify Vulnerable Subdomain for Clickjacking

## Summary

This procedure involves scouting for web subdomains, particularly non-production ones, that lack clickjacking protections like X-Frame-Options headers, setting the stage for UI redressing attacks.

## Description

In a typical attack scenario, the tester enumerates subdomains of the target domain to find services like email interfaces in UAT environments. Using browser tools or curl, check response headers for the absence of frame-busting mechanisms. This vulnerability allows embedding the site in external iframes, enabling overlays that trick users into performing actions such as clicking hidden links on an email server page. Prerequisites include public access to the target and basic web knowledge; expected outcomes are identification of exploitable endpoints.

## Requirements

1. Access to a web browser or curl for header inspection
2. Knowledge of the target domain (e.g., legalrobot-uat.com)
3. No special credentials needed for public subdomains

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN headers
- Use Content-Security-Policy (CSP) frame-ancestors directive
- Monitor for anomalous iframe embeddings via web application firewalls (WAF)

## Objectives

1. Discover subdomains vulnerable to iframing
2. Verify missing protections
3. Assess potential for UI manipulation

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Manually or via tools, list potential subdomains related to services like email.

Focus on non-production variants (e.g., -uat.com). For this case, target http://mailboxes.legalrobot-uat.com/.

### Step 2: Check Headers for Protections

**Context**: Inspect HTTP response headers to confirm vulnerability.

Use browser dev tools (Network tab) or curl to fetch headers:

Open the URL and check for X-Frame-Options.

**Expected Output**: Response without X-Frame-Options, allowing iframing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[subdomain-enumeration]]
