---
tags:
  - shopify
  - email-reception
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8e1a2e8f-cf1c-4c8d-9a39-0af2c4515935
created_at: '2025-12-13T09:01:26.841Z'
updated_at: '2025-12-13T09:01:26.841Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Receive Shopify Confirmation Email at Original Address

## Summary

This procedure involves checking the original email for the misdirected confirmation link.

## Description

Due to the vulnerability, the link for the new email arrives at the old, controlled inbox.

## Requirements

1. Access to original email inbox
2. Email change previously submitted

## Defense

Defensive measures and detection strategies:

- Fix email routing to send to the intended address
- Monitor email delivery logs for anomalies

## Objectives

1. Retrieve the confirmation email
2. Obtain the verification link

## Instructions

### Step 1: Check Inbox

**Context**: Wait and access the email.

The confirmation email from mailer@shopify.com arrives at the original email (attacker@gmail.com) containing the link for the new email.

> Extract the link from the email body.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- shopify
- email-reception
