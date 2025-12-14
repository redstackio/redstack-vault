---
id: proc-uuid-4
tags:
  - redemption
  - abuse
  - unlimited-generation
  - web
type: procedure
tools: []
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.628Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Generate-and-Redeem-Unlimited-Invites

## Summary

This procedure uses tampered referral URLs to repeatedly generate and redeem gift invites, accumulating unlimited travel credits through IDOR abuse.

## Description

Once parameters are manipulated, the system accepts invalid tokens as valid, allowing indefinite generation of $30+ gift cards redeemable across accounts, exploiting the lack of rate limits or uniqueness checks.

## Requirements

1. Fully modified referral URL (IDOR and spoofed)
2. Secondary Airbnb account for redemption testing
3. Browser sessions for generation and redemption

## Defense

Defensive measures and detection strategies:

- Implement per-account and global rate limits on invite generations
- Require unique referral tokens with expiration and one-time use
- Detect and flag repeated redemptions from similar IP/user patterns

## Objectives

1. Produce multiple valid gift cards from a single tampered link
2. Successfully redeem for account credits
3. Demonstrate unbounded abuse potential

## Instructions

### Step 1: Generate Invite from Tampered URL

**Context**: Load the URL to create a new invite or gift code.

Paste the modified URL (e.g., `https://www.airbnb.com/c/fun?euid=2&ri=14052213&s=30`) into a browser and follow prompts to generate the invite link or code.

### Step 2: Redeem the Gift Card

**Context**: Apply the generated code to an account to verify and gain credits.

Open the invite link in a new tab or incognito window, sign in with a test account, and complete redemption. Repeat by reloading the tampered URL.

**Expected Output**: $30 credit added to account; process repeatable.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[redemption]]
- [[abuse]]
- [[unlimited-generation]]
- [[web]]
