---
tags:
  - email-interception
  - phishing
  - exfiltration
type: procedure
tools:
  - '[[tools/SendGrid]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
updated_at: '2025-12-14T04:38:39.373Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: 601ed92f-1c3e-4045-863b-b8f70915c83c
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
---
# Intercept-or-Manipulate-Emails

## Summary

Post-takeover, this procedure configures the subdomain to capture or redirect inbound emails, enabling interception of sensitive communications or phishing setups.

## Description

With control over the subdomain on SendGrid, attackers set up inbound email parsing or webhooks to route messages to their servers. This can expose credentials or user data sent to the subdomain. For phishing, custom responses or forwards can be implemented. Requires taken-over domain; high risk of detection if monitored.

## Requirements

1. Control of the subdomain via third-party service
2. Attacker endpoint (e.g., webhook URL)
3. Knowledge of email routing configurations

## Defense

Defensive measures and detection strategies:

- Implement email security gateways to validate sender domains
- Monitor for anomalous email traffic from trusted subdomains
- Use DMARC/SPF/DKIM to prevent spoofing post-takeover

## Objectives

1. Capture inbound emails to the subdomain
2. Analyze or exfiltrate email content
3. Launch secondary attacks like phishing

## Instructions

### Step 1: Configure Inbound Parse

**Context**: Set up SendGrid to parse emails sent to the subdomain.

In SendGrid dashboard, enable Inbound Parse and point to an attacker URL.

> Emails to @email.smule.com are POSTed to the URL with content.

### Step 2: Test Interception

**Context**: Send a test email to verify capture.

Send email to test@email.smule.com and check webhook receipt.

> Expected: Full email body, headers, and attachments received.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exfiltration Over Alternative Protocol]] Exfiltration Over Alternative Protocol

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/SendGrid]]

## Tags

- [[email-interception]]
- [[Phishing]]
- [[Exfiltration]]
