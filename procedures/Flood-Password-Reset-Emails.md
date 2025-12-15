---
tags:
  - nextcloud
  - email-flood
  - dos
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/IP-Rotate]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:28:28.118Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 514367bb-3bce-447a-98e9-e950577b707d
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Flood-Password-Reset-Emails

## Summary

This procedure executes a high-volume attack on Nextcloud's password reset to flood the target email, exploiting the bypassed rate limit for DoS on email services.

## Description

With IP rotation active in Burp Intruder, run the attack for many iterations (e.g., 100+), targeting the same email. Each request triggers an email send, leading to inbox overload, API costs for paid services, storage increase, and user dissatisfaction. Impacts include service slowdowns and business risks. Expected outcome: Excessive emails received.

## Requirements

1. Configured Intruder from bypass procedure
2. Target email monitored
3. Sufficient proxies for rotation

## Defense

Defensive measures and detection strategies:

- Limit total resets per user daily
- Integrate email rate limiting at SMTP/API level
- Block suspicious IP patterns or high-volume senders

## Objectives

1. Cause email service abuse
2. Demonstrate impact
3. Highlight business risks

## Instructions

### Step 1: Launch Extended Attack

**Context**: Scale the bypass to flood level.

In Intruder, set threads to 1-5, iterations to 100+, and start with IP Rotate on.

### Step 2: Monitor Emails

**Context**: Validate flooding success.

Check target email inbox periodically during attack.

> Expected output: 100+ reset emails arrive, no 429 errors in Burp logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/IP-Rotate]]

## Tags

- [[nextcloud]]
- [[email-flood]]
