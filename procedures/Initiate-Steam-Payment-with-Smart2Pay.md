---
tags:
  - payment-initiation
  - web-navigation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: bf3be760-0082-49f3-ab26-4ea4ce4b6563
created_at: '2025-12-11T06:10:15.792Z'
updated_at: '2025-12-11T06:10:15.792Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Initiate Steam Payment with Smart2Pay

## Summary

This procedure guides the user through navigating the Steam store to add funds using a Smart2Pay payment method, setting up the vulnerable transaction.

## Description

Access the add funds page on Steam and select a payment method like Przelewy24 that routes through Smart2Pay. This triggers the POST request that can be intercepted. The target is the Steam web application, and success leads to the payment request being generated.

## Requirements

1. Steam account with prepared email
2. Web browser access to Steam store
3. Selection of Smart2Pay-compatible payment method

## Defense

Defensive measures and detection strategies:

- Monitor unusual payment initiations
- Rate limit fund additions

## Objectives

1. Trigger the vulnerable payment request
2. Prepare for interception
3. Advance to the tampering phase

## Instructions

### Step 1: Navigate to Add Funds Page

**Context**: Access the Steam wallet funding page.

Go to https://store.steampowered.com/steamaccount/addfunds and select the amount to add.

### Step 2: Choose Payment Method

**Context**: Select Smart2Pay method.

Proceed to payment and choose Przelewy24 or equivalent.

> This initiates the POST to Smart2Pay.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- payment-initiation
- web-navigation
