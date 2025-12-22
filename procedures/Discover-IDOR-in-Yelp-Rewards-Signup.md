---
id: discover-yelp-idor-rewards
tags:
  - idor
  - discovery
  - yelp
  - web-testing
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:47.504Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover-IDOR-in-Yelp-Rewards-Signup

## Summary

This procedure identifies an Insecure Direct Object Reference (IDOR) in Yelp's /rewards/signup endpoint by testing for missing authorization checks when associating credit card identifiers during the rewards signup process.

## Description

In the attack scenario, a tester with a valid Yelp account navigates the rewards signup flow and attempts to input external or randomly generated credit card identifiers that belong to other users or are deregistered. The endpoint fails to validate ownership, allowing association without proper access controls. This was discovered during manual testing on May 27, 2018, leading to potential privacy violations by exposing transaction history. Prerequisites include a logged-in Yelp session and basic web inspection tools.

## Requirements

1. Authenticated Yelp account
2. Browser with developer tools or HTTP proxy (e.g., Burp Suite)
3. Knowledge of credit card identifier format from prior enumeration

## Defense

Defensive measures and detection strategies:

- Implement server-side ownership validation for object references
- Use indirect references or UUIDs instead of predictable IDs
- Monitor for anomalous card associations in logs

## Objectives

1. Confirm lack of authorization on /rewards/signup endpoint
2. Identify vulnerable parameters for card association
3. Assess potential data exposure from linked cards

## Instructions

### Step 1: Inspect Rewards Signup Flow

**Context**: Examine the normal signup process to understand the card association mechanism.

Navigate to the Yelp rewards signup page in a browser, open developer tools (Network tab), and attempt a legitimate card addition. Note the request to /rewards/signup and the parameters used, such as card_id.

**Expected Output**: HTTP POST request with JSON payload including card details.

### Step 2: Test with External Card Identifier

**Context**: Attempt association with a non-owned, deregistered card ID to detect IDOR.

In the developer tools or proxy, intercept the request and modify the card_id to a random or known external identifier (e.g., from testing data). Replay the request and observe the response.

**Expected Output**: 200 OK response without authorization errors, confirming IDOR.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- idor
- yelp
- web-vulnerability
