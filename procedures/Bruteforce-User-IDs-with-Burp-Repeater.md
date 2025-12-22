---
id: proc-002
tags:
  - enumeration
  - bruteforce
  - idor
type: procedure
tools:
  - '[[tools/Burp-Suite-Repeater]]'
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
updated_at: '2025-12-14T17:25:12.691Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Bruteforce-User-IDs-with-Burp-Repeater

## Summary

This procedure demonstrates manually bruteforcing user_ids in the Manage Users endpoint using Burp Repeater to identify valid accounts, exploiting the lack of access controls for enumeration.

## Description

Targeted at web applications with sequential or predictable user IDs, this involves sending modified requests with varying user_id values (e.g., 1, 514755). The staging.seatme.us environment returns different responses for valid vs. invalid IDs, enabling discovery. Prerequisites include endpoint access from the prior procedure; outcomes are lists of valid IDs for further exploitation.

## Requirements

1. Burp Suite Repeater active with intercepted request
2. Knowledge of expected ID range (e.g., sequential integers)
3. Time for manual testing (automation possible but manual here)

## Defense

Defensive measures and detection strategies:

- Enforce authorization on user queries
- Implement ID obfuscation or non-sequential numbering
- Detect sequential request patterns via WAF

## Objectives

1. Test multiple user_id values
2. Distinguish valid from invalid accounts
3. Build a set of enumerable user IDs

## Instructions

### Step 1: Load Request in Repeater

**Context**: Prepare the tool for parameter modification.

Paste the intercepted request from the Manage Users endpoint into Burp Repeater.

> Expected output: Request ready for sending, displaying raw HTTP.

### Step 2: Modify and Send Sequential IDs

**Context**: Simulate bruteforcing by testing values like 1, 514755, 514775, 514764.

Edit the user_id parameter in the request body or query string, then click 'Send' for each variation. Observe response codes and content.

> Expected output: Valid IDs yield user details (e.g., 200 with data); invalid return 404 or empty.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Repeater]]

## Tags

- [[enumeration]]
- [[bruteforce]]
- [[idor]]
