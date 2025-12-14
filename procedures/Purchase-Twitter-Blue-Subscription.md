---
tags:
  - twitter
  - subscription
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:35.426Z'
skill_level: beginner
impact_level: low
sub_techniques: []
id: 0371c8c6-6720-4dcf-bcc2-737c6bfffb50
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Purchase Twitter Blue Subscription

## Summary

This procedure initiates a legitimate Twitter Blue subscription to obtain the verified badge, serving as the entry point for exploiting the verification review process.

## Description

In the context of the Twitter verified badge exploit, purchasing Twitter Blue provides initial access to the premium feature. The subscription activates the blue checkmark, which is then manipulated via timing with profile changes. This step requires a valid payment method and occurs through the Twitter app or website, targeting iOS users via App Store for later cancellation.

## Requirements

1. Active Twitter account with credentials.
2. Payment method (credit card) for initial purchase.
3. Twitter app or web access on iOS or browser.

## Defense

Defensive measures and detection strategies:

- Monitor subscription purchase patterns for anomaly detection.
- Implement rate limiting on profile changes tied to subscriptions.

## Objectives

1. Activate verified badge for the account.
2. Note the exact expiration timestamp for timing subsequent steps.
3. Establish baseline for review process exploitation.

## Instructions

### Step 1: Subscribe to Twitter Blue

**Context**: Access subscription settings to purchase the service.

Navigate to Twitter settings > Twitter Blue and select subscribe. Complete payment via App Store or web.

> Expected output: Confirmation email and badge appearance on profile.

### Step 2: Verify Activation

**Context**: Confirm the subscription is active.

Check profile for blue verified badge and review subscription details in App Store.

> Expected output: Badge visible; expiration date displayed (e.g., 30 days from purchase).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[twitter]]
- [[subscription]]
