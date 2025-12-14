---
id: proc-setup-email-server
name: Set-Up-Email-Server-on-Hijacked-Subdomain
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.653Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Command-Line Interface]]'
tags:
  - email-server
  - persistence
platforms:
  - Web
tools: []
commands: []
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---

# Set-Up-Email-Server-on-Hijacked-Subdomain

## Summary

This procedure configures the mail service on the hijacked subdomain to handle incoming and outgoing emails, enabling full functionality for @mail.starbucks.bg.

## Description

In the icn.bg panel, enable mail routing, set MX records, and configure SMTP/IMAP settings. This allows the attacker to operate a legitimate-looking email server, facilitating phishing. Targets mail-specific subdomains in takeover scenarios.

## Requirements

1. Claimed and credentialed service access
2. Understanding of email protocols (SMTP, MX)
3. Optional: Custom domain verification

## Defense

Defensive measures and detection strategies:

- Block emails from suspicious subdomains via SPF/DKIM/DMARC
- Monitor email logs for anomalous sending patterns
- Audit third-party mail services regularly

## Objectives

1. Activate email handling capabilities
2. Ensure seamless integration with DNS
3. Prepare for operational use

## Instructions

### Step 1: Enable Mail Routing

**Context**: In panel, toggle mail services on.

Select options for inbound/outbound.

> Expected output: Configuration applied.

### Step 2: Verify DNS Integration

**Context**: Check MX records post-setup.

Use dig MX mail.starbucks.bg

> Expected output: MX points to configured server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[email-server]]
- [[Persistence]]
