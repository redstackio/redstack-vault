---
tags:
  - android
  - purchase
  - initial-access
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.551Z'
skill_level: beginner
impact_level: low
sub_techniques: []
id: 022853f0-0d33-421b-8992-f0162e746a55
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Reddit-Coin-Purchase

## Summary

This procedure outlines completing a coin purchase in the Reddit Android app to generate the necessary verification request for subsequent exploitation.

## Description

In the context of exploiting a race condition, this step simulates a legitimate user purchase to obtain purchase artifacts like transaction_id and token. It targets the Reddit app's integration with Google Play, where the app sends a verification request post-payment. Prerequisites include an Android device with the app installed and Google Play billing enabled. Expected outcome: A pending verification that can be intercepted.

## Requirements

1. Android device with Reddit app (vulnerable version, e.g., 2020.5.0)
2. Google Play account with valid payment method
3. Network connectivity

## Defense

Defensive measures and detection strategies:

- Monitor for unusual purchase patterns in app analytics
- Implement client-side purchase idempotency checks

## Objectives

1. Generate a valid Google Play purchase token and transaction ID
2. Trigger the verification endpoint call
3. Prepare for request interception without immediate credit

## Instructions

### Step 1: Launch App and Navigate to Purchase

**Context**: Open the app and access the coin store to select a package.

No command; perform in-app: Launch Reddit app, tap coin icon, select 50 coins package (product_id: com.reddit.coins_1).

> This prepares the purchase flow.

### Step 2: Complete Purchase via Google Play

**Context**: Finalize payment to receive confirmation.

No command; in-app: Confirm purchase in Google Play Store dialog.

> Expected: Transaction completes, app attempts verification (intercepted in next procedure).

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

- android
- purchase
