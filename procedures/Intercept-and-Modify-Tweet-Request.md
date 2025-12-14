---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - parameter-tampering
  - bypass
  - impersonation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:36.732Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Intercept-and-Modify-Tweet-Request

## Summary

This procedure intercepts the promoted tweet creation request using a proxy tool and removes the nullcast_flag parameter, transforming it into a regular tweet post on the account owner's timeline, bypassing authorization controls.

## Description

The vulnerability stems from server-side reliance on the client-supplied nullcast_flag=1 without validating the user's role for non-promoted content. By using Burp Suite's Repeater, the parameter is removed, exploiting the flaw to post unauthorized tweets. This occurs in the Twitter Ads web API at /tweet_box/create_tweet, leading to impersonation risks.

## Requirements

1. Burp Suite proxy intercepting browser traffic
2. Active session in target ads dashboard
3. Knowledge of the request structure from prior composition

## Defense

Defensive measures and detection strategies:

- Enforce server-side role checks for all tweet types
- Sanitize and validate all incoming parameters
- Detect proxy-intercepted requests via timing or header anomalies

## Objectives

1. Bypass promoted-only restriction
2. Post regular tweet as account owner
3. Achieve unauthorized content publication

## Instructions

### Step 1: Intercept the Request

**Context**: Configure Burp to capture the POST during tweet submission.

Submit the promoted tweet; request appears in Burp Proxy history.

> Captured request shows POST body with nullcast_flag=1.

### Step 2: Modify and Resend in Repeater

**Context**: Edit the request to remove the flag.

Send to Repeater, delete 'nullcast_flag=1' from body, and forward.

> Response indicates successful post; tweet appears on timeline.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- request-modification
- nullcast-flag
- authorization-bypass
