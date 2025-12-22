---
tags:
  - burp-suite
  - request-modification
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Modify Authentication Process]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 02be3459-f608-4537-a9fc-9a66a5a7690a
created_at: '2025-12-14T17:30:58.592Z'
updated_at: '2025-12-14T17:30:58.592Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
# Configure-Burp-Suite-for-Email-Swapping

## Summary

This procedure sets up Burp Suite to intercept and modify HTTP requests during Shopify account operations, specifically swapping emails to bypass ownership checks.

## Description

Burp Suite is used as a proxy to alter email fields in requests to Shopify's admin endpoints, such as during photo uploads. This exploits inadequate validation in legacy systems, allowing the victim's email to be associated with the attacker's store without confirmation. Prerequisites include a running Burp instance and browser proxy configuration.

## Requirements

1. Burp Suite installed and running with proxy listener on port 8080
2. Browser (e.g., Firefox) set to use Burp as proxy
3. Specific email strings for replacement (attacker's vs. victim's)

## Defense

Defensive measures and detection strategies:

- Validate email changes server-side with ownership proofs (e.g., OTP)
- Log and alert on proxied or modified requests to account endpoints
- Use HSTS and certificate pinning to hinder interception tools

## Objectives

1. Enable real-time request tampering for email fields
2. Trigger modifications during non-sensitive actions like uploads
3. Maintain session integrity while altering payloads

## Instructions

### Step 1: Set Up Match and Replace Rules

**Context**: Define rules to swap emails in outgoing requests.

No specific command; Burp configuration:

- In Burp Suite, go to Proxy > Options > Match and Replace.
- Add rule: Type 'Request header', Match 'original-email@domain.com', Replace 'say_ch33se+111@wearehackerone.com'.

> Rules apply to all proxied traffic matching the pattern.

### Step 2: Refresh Account Page

**Context**: Apply changes to reflect swapped email.

No specific command; web action:

- Reload `/admin/settings/account` in the browser.

> Page now shows victim's email due to intercepted prior requests.

### Step 3: Test with Photo Upload

**Context**: Trigger a request to validate interception.

No specific command; interface interaction:

- Click 'Upload photo', select an image, and save.

> Burp intercepts and modifies the upload request's email field.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Modify Authentication Process]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[tools/Burp-Suite]]
- [[request-modification]]
