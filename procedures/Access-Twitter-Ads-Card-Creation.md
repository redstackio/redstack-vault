---
id: proc-uuid-1
tags:
  - xss
  - twitter-ads
  - initial-access
type: procedure
tools: []
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
updated_at: '2025-12-14T03:15:53.096Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Twitter-Ads-Card-Creation

## Summary

This procedure outlines navigating to the Twitter Ads card creation page, setting the stage for injecting malicious payloads in subsequent steps of a persistent XSS attack.

## Description

In the context of exploiting a persistent XSS vulnerability on ads.twitter.com, this initial step involves authenticating and accessing the card creation endpoint. The target environment is the web-based Twitter Ads platform, where users with account access can create promotional cards. Prerequisites include valid credentials for a Twitter Ads account. Expected outcomes include loading the editable form without restrictions, allowing payload injection in fields like card[name].

## Requirements

1. Authenticated session to Twitter Ads (ads.twitter.com)
2. Web browser capable of handling form interactions
3. Knowledge of the specific account ID (e.g., 18ce53wrkma) and card type (e.g., card_type=7)

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit card creation to trusted users
- Monitor access logs for unusual navigation patterns to admin endpoints

## Objectives

1. Gain access to the card creation interface
2. Verify form availability for payload injection
3. Establish a persistent session for follow-on exploitation

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Log in to the Twitter Ads dashboard to reach the card management section.

No specific command; use browser navigation to https://ads.twitter.com and authenticate with valid credentials.

> Upon successful login, the dashboard loads, allowing access to account-specific features.

### Step 2: Initiate Card Creation

**Context**: Direct to the new card endpoint for the desired type.

Manually enter or bookmark the URL: https://ads.twitter.com/accounts/18ce53wrkma/cards/new?card_type=7.

> The form loads with fields for card details, including the vulnerable card[name].

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[twitter-ads]]
