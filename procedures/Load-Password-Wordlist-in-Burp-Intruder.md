---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567895
tags:
  - wordlist
  - payloads
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
updated_at: '2025-12-14T17:31:42.734Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Password Guessing]]'
---
# Load Password Wordlist in Burp Intruder

## Summary

Load a list of common passwords as payloads for the brute-force attack on the old_password field.

## Description

In Intruder's Payloads tab, use a Simple list type to import a wordlist (e.g., rockyou.txt or custom common passwords). This allows trying thousands of guesses without limits.

## Requirements

1. Password wordlist file (e.g., common passwords like 'password123')
2. Intruder configured with position

## Defense

Defensive measures and detection strategies:

- Strengthen password policies to resist common wordlists
- Implement account lockout after failures
- Analyze logs for wordlist-like attempt patterns

## Objectives

1. Populate payloads for automation
2. Cover likely passwords
3. Enable rapid testing

## Instructions

### Step 1: Select Payload Type

**Context**: Choose simple list for passwords.

In Payloads tab > Payload Sets > Add > Simple list.

> Expected output: Empty payload list ready for load.

### Step 2: Load Wordlist

**Context**: Import the file of potential passwords.

Click Load > Select file (e.g., passwords.txt with entries like '123456', 'password').

> Expected output: Payload count (e.g., 10000) shown.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Password Guessing]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- wordlist
