---
id: cdc344a7-2d6d-49d4-9c4b-2b7b6f94a7e4
name: Create-Uber-Rider-Account
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.412Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
tags:
  - account-creation
  - uber
  - mobile
platforms:
  - Mobile (iOS)
commands: []
tools: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Create-Uber-Rider-Account

## Summary

This procedure involves registering a new rider account using the Uber iOS app with a disposable phone number to initialize the passwordless signup workflow and observe the API endpoint behavior for later exploitation.

## Description

In the context of exploiting Uber's improper authentication vulnerability, creating a new rider account allows the attacker to replicate the legitimate signup flow. This step is crucial for understanding the state transitions in the /rt/users/passwordless-signup endpoint, which lacks proper verification, enabling subsequent password resets on arbitrary accounts. The target environment is the Uber mobile app, and success grants insight into the vulnerable workflow without alerting defenses.

## Requirements

1. Uber iOS app installed on a device or emulator
2. Disposable phone number for registration (e.g., via virtual SMS service)
3. Network access to Uber services (HTTPS)

## Defense

Defensive measures and detection strategies:

- Monitor for unusual account creation patterns from disposable numbers
- Implement rate limiting on signup endpoints
- Log and alert on rapid successive registrations

## Objectives

1. Establish a baseline for the passwordless signup API flow
2. Confirm endpoint accessibility and response formats
3. Prepare for workflow state replay in exploitation

## Instructions

### Step 1: Launch Uber App and Start Signup

**Context**: Open the app to initiate the rider registration process, providing a phone number to trigger the passwordless flow.

No command required; use the app UI to enter phone number and receive verification code.

> Enter the verification code to proceed to the password creation state. Observe network traffic (e.g., via proxy) to capture initial requests to /rt/users/passwordless-signup.

### Step 2: Complete Initial Registration

**Context**: Set up the account minimally to reach the CREATE_NEW_PASSWORD state without setting a password yet.

No command; app-driven.

> Expected: App advances to password setup, confirming workflow state is manipulable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[uber]]
- [[mobile]]
