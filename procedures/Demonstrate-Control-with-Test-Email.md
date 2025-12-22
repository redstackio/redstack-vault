---
id: proc-demonstrate-test-email
name: Demonstrate-Control-with-Test-Email
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.652Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Phishing]]'
sub_techniques:
  - '[[T1566.001]]'
tags:
  - phishing
  - impersonation
platforms:
  - Web
tools: []
commands: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Phishing]]'
---

# Demonstrate-Control-with-Test-Email

## Summary

This procedure sends a test email from the hijacked @mail.starbucks.bg address to prove control, highlighting potential for phishing or impersonation attacks.

## Description

Using the configured email server, compose and dispatch a simple message. This validates the takeover and demonstrates impact, such as spoofing Starbucks communications. Applies to any email takeover scenario post-configuration.

## Requirements

1. Fully set up email server
2. Recipient email address
3. Email client access via panel or SMTP

## Defense

Defensive measures and detection strategies:

- Implement strict email authentication (SPF, DKIM, DMARC)
- Train users on phishing indicators
- Monitor for sudden email volume from subdomains

## Objectives

1. Validate email functionality
2. Showcase impersonation risk
3. Collect evidence of control

## Instructions

### Step 1: Compose Test Email

**Context**: Use the service's webmail or SMTP client.

Enter from: test@mail.starbucks.bg, to: external@test.com, subject: Test.

> Expected output: Email queued.

### Step 2: Send and Confirm Delivery

**Context**: Dispatch and check recipient inbox.

Hit send.

> Expected output: Email received, headers show @mail.starbucks.bg.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques

- [[T1566.001]] Spearphishing Attachment

## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[impersonation]]
