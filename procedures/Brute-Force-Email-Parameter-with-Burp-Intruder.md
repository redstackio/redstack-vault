---
tags:
  - brute-force
  - enumeration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:24:45.231Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1087.002]]'
id: bad2a8b1-5718-4b63-b2a3-133d7f1b724c
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Brute Force]]'
---
# Brute-Force-Email-Parameter-with-Burp-Intruder

## Summary

Use Burp Suite's Intruder module to automate brute-forcing of the email parameter in the Curve waitlist API, enumerating valid waitlisted users and triggering PII disclosure for each match.

## Description

This procedure exploits the lack of authentication and rate limiting on the API by sending rapid requests with varying email payloads from a wordlist. Each valid email returns full user PII. Applicable in API security testing; prepare a list of potential emails (e.g., from public breaches).

## Requirements

1. Intercepted base request in Burp
2. Payload list file (e.g., emails.txt with one email per line)
3. Burp Suite Professional or Community with Intruder

## Defense

Defensive measures and detection strategies:

- Apply rate limiting (e.g., 5 req/min per IP)
- Validate email domains or require CAPTCHA
- Monitor for high-volume similar requests and block IPs

## Objectives

1. Enumerate all valid waitlist emails
2. Collect PII for matched users
3. Assess scale of disclosure

## Instructions

### Step 1: Send Request to Intruder

**Context**: Prepare the base request for payload insertion.

Right-click the intercepted request in Burp Proxy or Repeater and select 'Send to Intruder'.

> Clear any existing positions; mark the email value with §.

### Step 2: Configure and Launch Attack

**Context**: Set up payloads and execute the brute-force.

In Intruder, add payload set from file (e.g., emails.txt), set attack type to Sniper on the email position. Start the attack and monitor progress.

> Use response length or grep for 'phoneNumber' to identify hits.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery
- [[Brute Force]] Brute Force

### Sub-Techniques

- [[T1087.002]] Domain Account

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[brute-force]]
- [[enumeration]]
