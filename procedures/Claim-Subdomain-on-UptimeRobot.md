---
tags:
  - subdomain-takeover
  - account-claim
  - web
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
updated_at: '2025-12-14T04:51:10.465Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: bb85ffa6-341a-4aea-b1b6-1541e87237c6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim-Subdomain-on-UptimeRobot

## Summary

This procedure claims control of an unclaimed subdomain by creating an account on UptimeRobot and reassigning the dangling DNS pointer, exploiting their policy of no verification for inactive sites.

## Description

UptimeRobot allows users to monitor websites via subdomains, but unclaimed pointers can be taken over by anyone signing up. This grants control over HTTP responses, email, and configurations for the subdomain (e.g., uptime.btfs.io), enabling abuse like phishing or XSS. Targets web apps with forgotten DNS setups; requires only a free account.

## Requirements

1. Internet access to UptimeRobot signup page
2. Email for account verification
3. Identified vulnerable subdomain from prior recon

## Defense

Defensive measures and detection strategies:

- Claim and delete unused service accounts promptly
- Use DNSSEC and monitor for unauthorized claims via service alerts
- Audit third-party integrations regularly

## Objectives

1. Gain administrative control of the subdomain
2. Redirect or configure the subdomain for malicious use
3. Demonstrate proof-of-concept ownership

## Instructions

### Step 1: Create UptimeRobot Account

**Context**: Register a new account to access claiming features.

Visit https://uptimerobot.com/signup and complete registration with an email and password.

> Upon verification, log in to access the dashboard.

### Step 2: Claim the Subdomain

**Context**: Use the dashboard to associate the unclaimed subdomain with your account.

In the UptimeRobot dashboard, search for or enter the subdomain (e.g., uptime.btfs.io) in the 'Add Monitor' or claiming section.

> The service reassigns it due to policy, providing immediate control without further checks.

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
- [[account-claim]]
- [[web]]
