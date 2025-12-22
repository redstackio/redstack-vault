---
tags:
  - parameter-tampering
  - injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[T1659]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: a769279d-cd7d-48d7-b75a-3efe80dad879
created_at: '2025-12-11T06:10:15.795Z'
updated_at: '2025-12-11T06:10:15.795Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1659]]'
---
# Prepare Email for Parameter Injection

## Summary

This procedure involves changing the Steam account email to a specially crafted format that allows injection of additional parameters into the payment request hash concatenation, enabling tampering without invalidating the signature.

## Description

By setting the email to something like 'brixamount100abc@domain', the attacker can later split it during request modification to inject fields such as 'amount=100'. This exploits the lack of delimiters in the hash generation. The target environment is the Steam web platform, and the expected outcome is a prepared account ready for payment tampering.

## Requirements

1. Valid Steam account with ability to change email
2. Access to an email domain for crafting the address
3. No special tools required

## Defense

Defensive measures and detection strategies:

- Implement strict input validation on user-controlled fields like email
- Use proper delimiters and ordering in hash generation to prevent injection

## Objectives

1. Enable parameter injection in subsequent requests
2. Preserve hash validity during tampering
3. Prepare for amount modification in payment process

## Instructions

### Step 1: Access Steam Account Settings

**Context**: Navigate to account settings to change the email.

Log in to Steam and go to account details to update the email address.

> Set the email to 'brixamount100abc@domain' or similar injectable format.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1659]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- parameter-tampering
- injection
