---
id: proc-uuid-3
tags:
  - email-spam
  - automation
  - intruder-attack
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:48.233Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Automate-Email-Spam-with-Burp-Intruder

## Summary

This procedure automates repeated password reset requests using Burp Suite's Intruder to spam the target's email inbox, exploiting the lack of rate limiting.

## Description

In scenarios where password reset endpoints lack frequency controls, attackers can flood the system with requests, causing inbox overload and potential phishing vectors. Using the captured request, Intruder is configured for a sniping attack on the email payload, replacing it with null or repeated values. Launching with high thread counts sends unlimited emails rapidly. The target is web apps integrated with mail services; outcomes include hundreds of emails in minutes, slowing delivery as resources deplete.

## Requirements

1. Captured request from previous step
2. Burp Suite with Intruder module
3. Target email address for spamming

## Defense

Defensive measures and detection strategies:

- Deploy rate limiting (e.g., 5 requests per IP per minute)
- Monitor email queue logs for burst volumes
- Use spam filters on mail servers to quarantine bulk resets

## Objectives

1. Generate unlimited reset emails to spam inbox
2. Demonstrate absence of rate limits
3. Enable follow-on phishing via spam

## Instructions

### Step 1: Send to Intruder

**Context**: Load the captured request into Burp Intruder for configuration.

Right-click the request in Proxy and select 'Send to Intruder'.

> Intruder tab opens with the request loaded. Expected: Positions marked with § for payload insertion.

### Step 2: Configure and Launch

**Context**: Set up sniping on the email field and run the attack.

Clear positions, mark the email value with §, select null payloads or simple list, set threads to 1-5, and start attack.

> Requests fire rapidly; monitor emails arriving. Success: 100+ emails in 2-3 minutes without blocking.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[email-spam]]
- [[automation]]
- [[intruder-attack]]
