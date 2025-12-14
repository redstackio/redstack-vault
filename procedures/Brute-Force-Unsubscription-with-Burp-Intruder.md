---
tags:
  - brute-force
  - rate-limit-bypass
  - automation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:25:30.034Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 8959f8fe-4f8d-4951-8c51-2b121695e02c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Brute-Force-Unsubscription-with-Burp-Intruder

## Summary

This procedure uses Burp Suite's Intruder to send rapid unsubscribe requests, proving the absence of rate limiting and enabling mass unsubscription attacks on email lists.

## Description

With no rate limiting, the endpoint allows high-volume requests; over 60 unsubscriptions in under a minute all succeed with 200 OK responses. This scales the IDOR to affect large user bases, such as from leaked email lists, causing widespread disruption to Nextcloud's newsletter engagement without detection.

## Requirements

1. Burp Suite Professional with Intruder module
2. Captured unsubscribe request
3. List of target emails (payloads)

## Defense

Defensive measures and detection strategies:

- Implement strict rate limiting (e.g., 5 requests/min per IP)
- Use CAPTCHA or token-based throttling for repeated actions
- Deploy WAF rules to block high-frequency POST/GET to unsubscribe paths

## Objectives

1. Simulate mass unsubscription
2. Confirm no throttling
3. Quantify abuse potential

## Instructions

### Step 1: Capture Base Request

**Context**: Intercept a manual unsubscribe submission.

Use Burp Proxy to capture the POST or GET to https://newsletter.nextcloud.com/?p=unsubscribe.

> Mark the email parameter as a payload position.

### Step 2: Configure Intruder

**Context**: Set up payloads for brute-force.

In Intruder, load a wordlist of emails into the payload section, set attack type to Sniper, and launch against 60+ targets.

> Expected output: All responses 200 OK in under 1 minute, no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- brute-force
- automation
