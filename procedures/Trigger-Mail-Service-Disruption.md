---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Trigger-Mail-Service-Disruption
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:28:36.700Z'
tactics:
  - '[[Impact]]'
techniques:
  - '[[Network Denial of Service]]'
sub_techniques: []
tags:
  - mail-disruption
  - service-denial
  - phabricator
commands: []
platforms:
  - Web
  - Network
tools: []
skill_level: medium
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---

# Trigger-Mail-Service-Disruption

## Summary

This procedure induces or exploits a temporary failure in Phabricator's mail delivery system (SMTP), preventing password reset emails from being sent and causing sensitive links to be logged in daemon logs instead.

## Description

Phabricator relies on external mail services like SMTP for notifications, including password resets. When delivery fails—due to invalid credentials, firewall blocks, or service downtime—the reset token is logged in plain text in the daemon logs, which are accessible via the web UI. This step can be passive (waiting for a known outage) or active (if the attacker has network influence). It sets up the condition for information disclosure in the subsequent log viewing step.

## Requirements

1. Knowledge of Phabricator's mail configuration (e.g., using Gmail SMTP)
2. Ability to monitor or induce temporary disruptions (e.g., via firewall rules or credential changes)
3. Access to verify mail failure (e.g., admin email or Phabricator error logs)

## Defense

Defensive measures and detection strategies:

- Configure redundant mail services with failover to prevent single points of failure
- Sanitize logs to remove sensitive tokens before storage or exposure
- Monitor for repeated mail delivery failures and alert on potential abuse

## Objectives

1. Prevent email delivery of password reset links
2. Force logging of reset tokens in accessible daemon logs
3. Maintain disruption briefly without causing full service outage

## Instructions

### Step 1: Identify Mail Configuration

**Context**: Determine the mail setup to target the disruption effectively.

No command required; review Phabricator config files or UI if accessible, noting SMTP server (e.g., Gmail) and credentials.

> Look for entries like smtp-host = smtp.gmail.com. Expected output: Confirmation of vulnerable mail setup.

### Step 2: Induce or Await Disruption

**Context**: Create the failure condition to block outbound mail.

No command required; options include temporarily blocking SMTP port (e.g., 587) via firewall, using invalid credentials, or waiting for scheduled downtime.

> Verify by sending a test email from Phabricator; failure logs an error like 'Gmail rejected SMTP credentials'. Success: No emails delivered.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[mail-disruption]]
- [[service-denial]]
- [[phabricator]]
