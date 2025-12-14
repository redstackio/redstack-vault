---
tags:
  - idor
  - modify
  - parameter
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
updated_at: '2025-12-14T05:32:10.237Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 09b93151-a99d-4110-b7d5-d74cb8060bc6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-personId-Parameter-for-IDOR

## Summary

This procedure tampers with the 'personId' parameter in the intercepted upload request to target another user's account, exploiting the IDOR to bypass authorization checks.

## Description

By changing 'personId' from the attacker's account to a victim's (e.g., 'account2'), the request uploads the image to the unauthorized profile. This targets the DoD app's lack of server-side validation, leading to data tampering. Requires intercepted request; outcome is a modified payload exploitable for impersonation.

## Requirements

1. Intercepted request from Burp Suite
2. Knowledge of target account ID (e.g., sequential or enumerated)
3. Burp Suite Repeater or Proxy for editing

## Defense

Defensive measures and detection strategies:

- Enforce server-side authorization checks comparing session user ID to 'personId'
- Validate and log parameter changes, alerting on mismatches

## Objectives

1. Alter the target identifier
2. Exploit authorization flaw
3. Enable unauthorized upload

## Instructions

### Step 1: Edit Parameter in Burp

**Context**: Locate and change the 'personId' to the victim's ID.

In the intercepted request, find 'personId={original_id}' and replace with 'personId={target_id}' (e.g., account2).

> Use Burp's text editor. Expected output: Updated request body showing new value.

### Step 2: Validate Modification

**Context**: Ensure the request remains well-formed.

Re-parse the request in Burp.

> Expected output: No errors; image file and other params intact.

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

- [[idor]]
- [[modify]]
- [[parameter]]
