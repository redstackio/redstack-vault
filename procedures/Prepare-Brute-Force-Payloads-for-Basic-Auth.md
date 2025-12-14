---
tags:
  - brute-force
  - payloads
  - base64
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Password Guessing]]'
updated_at: '2025-12-14T17:31:43.022Z'
sub_techniques:
  - '[[Password Guessing]]'
id: 06058b92-2f8c-43f2-a273-7d3ef554b027
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Password Guessing]]'
---
# Prepare-Brute-Force-Payloads-for-Basic-Auth

## Summary

This procedure generates a list of potential passwords, combines them with the known username, and encodes them as Base64 for use in Basic Auth headers during a brute force attack on Nextcloud WebDAV.

## Description

With the username extracted, create a wordlist of common or targeted passwords (e.g., from leaks or defaults). For each, form the string 'username:password' and Base64-encode it to replace the Authorization header value. This prepares payloads for automated testing, exploiting the unlimited attempts allowed due to no rate limiting.

## Requirements

1. Known username from previous step
2. Password wordlist (e.g., rockyou.txt or custom list)
3. Base64 encoding tool (built into Burp or external like base64 command)

## Defense

Defensive measures and detection strategies:

- Implement account lockout after failed login attempts on WebDAV
- Use strong, unique passwords and enforce password policies
- Monitor for Base64 decoding patterns in proxy logs if using WAF

## Objectives

1. Create username:password combinations
2. Encode payloads for Basic Auth
3. Load payloads into attack tool

## Instructions

### Step 1: Generate Password List

**Context**: Compile a list of potential passwords for the target user.

No command required; manual or scripted:

- Create a text file with passwords (e.g., password123, admin, etc.)
- Tailor to user if possible (e.g., from social media)

> Expected output: File with 100+ passwords, one per line.

### Step 2: Encode Payloads

**Context**: Prepend username and Base64-encode each combination.

Use Burp or command line (example with bash base64):

For each password in list:

```bash
echo -n 'username:password' | base64
```

> Expected output: Base64 string like `aGEuY2tpdGJoYXJhdDNAZ21haWwuY29tOnBhc3N3b3Jk` for each.

In Burp: Use Payloads tab to generate or import encoded list.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[brute-force]]
- [[base64]]
