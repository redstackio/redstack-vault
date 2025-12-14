---
tags:
  - subdomain-takeover
  - dashboard-access
  - proof-of-concept
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T04:51:10.463Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Default Accounts]]'
id: 3a1e0ddc-3254-47e8-b436-35ebad64cc5a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Demonstrate-Control-of-Subdomain

## Summary

This procedure verifies subdomain takeover by logging into the service dashboard and performing actions, such as configuring settings with a demo password, to prove full control.

## Description

After claiming, access the UptimeRobot dashboard for the subdomain to edit monitoring, add alerts, or customize responses. This demonstrates potential for real abuse like hosting phishing pages or sending emails from the domain. Applies to web-based monitoring services; low barrier as it uses basic login.

## Requirements

1. Claimed UptimeRobot account with the subdomain
2. Web browser for dashboard access
3. Demo credentials (e.g., simple password for PoC)

## Defense

Defensive measures and detection strategies:

- Enable multi-factor authentication on third-party accounts
- Monitor DNS changes and subdomain traffic anomalies
- Use certificate transparency logs to detect unauthorized certificates

## Objectives

1. Confirm administrative access and functionality
2. Highlight abuse vectors like email spoofing or XSS
3. Provide evidence for vulnerability reporting

## Instructions

### Step 1: Log into Dashboard

**Context**: Access the claimed subdomain's management interface.

Navigate to the UptimeRobot dashboard and select the subdomain (e.g., uptime.btfs.io).

> Use credentials like username from signup and password 'A123456789' for demonstration.

### Step 2: Perform Control Actions

**Context**: Execute changes to validate ownership.

In the dashboard, edit monitor settings, such as interval or alerts, for the subdomain.

> Successful changes confirm control; e.g., update to a custom HTTP endpoint and verify via browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[dashboard-access]]
- [[proof-of-concept]]
