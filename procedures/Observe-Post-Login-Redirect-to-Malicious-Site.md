---
id: proc-observe-shopify-redirect
tags:
  - open-redirect
  - post-auth
  - phishing
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:30.634Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe-Post-Login-Redirect-to-Malicious-Site

## Summary

This procedure involves monitoring the attacker-controlled site for redirects from Shopify after the victim authenticates, capturing any exposed data or enabling further attacks like phishing.

## Description

Once the victim logs in via the malicious URL, Shopify's lack of validation causes an automatic redirect to the specified external domain (e.g., evil.com). The attacker observes incoming traffic, potentially stealing sessions or credentials if a phishing page is hosted. This concludes the chain in web environments targeting authenticated Shopify sessions.

## Requirements

1. Attacker-controlled domain set up to log traffic (e.g., simple web server)
2. Successful victim login from prior steps
3. Monitoring capability on the malicious site

## Defense

Defensive measures and detection strategies:

- Log and alert on redirects to untrusted domains
- Use referrer headers to detect anomalous post-login traffic
- Implement CSP or redirect policies to block external jumps

## Objectives

1. Confirm successful exploitation of the open redirect
2. Capture victim data or session post-auth
3. Facilitate secondary attacks like credential theft

## Instructions

### Step 1: Set Up Malicious Site Monitoring

**Context**: Prepare the attacker domain to receive and log redirects.

Host a simple page on evil.com that logs visitor IP, user-agent, and referrer.

> Use server logs or analytics to track hits.

### Step 2: Await Victim Authentication

**Context**: Wait for the victim to complete login on the legitimate page.

No active action; the redirect triggers automatically upon successful auth.

> The browser will navigate to https://evil.com/ seamlessly.

### Step 3: Analyze Incoming Redirect Traffic

**Context**: Review logs for evidence of the victim's redirect and any exposed data.

Check server access logs for requests from the victim's IP post-Shopify login.

> Expected: New session from victim, potentially with cookies or params if not sanitized.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- open-redirect
- monitoring
- shopify
