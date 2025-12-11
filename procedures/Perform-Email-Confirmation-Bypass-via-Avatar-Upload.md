---
tags:
  - authentication-bypass
  - avatar-upload
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 017b4c4a-7b81-49cf-9ebf-dc6144d3cd8a
created_at: '2025-12-11T06:10:22.795Z'
updated_at: '2025-12-11T06:10:22.795Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1078]]'
---
# Perform Email Confirmation Bypass via Avatar Upload

## Summary

This procedure uses avatar uploads and confirmation link manipulation with Burp Suite to bypass email verification in Shopify legacy accounts.

## Description

By uploading photos during the confirmation process while substituting emails via Burp, attackers can confirm arbitrary emails. This exploits improper validation in avatar upload and confirmation flows, leading to privilege escalation. The target is Shopify's account confirmation page, resulting in verified victim email without actual access.

## Requirements

1. Burp Suite configured for email replacement
2. Attacker's email with confirmation link
3. Logged-in Shopify browser session

## Defense

Defensive measures and detection strategies:

- Require confirmation codes for all verifications
- Remove legacy email flows and enforce SSO

## Objectives

1. Upload avatar with modified requests
2. Click manipulated confirmation link
3. Achieve verification bypass

## Instructions

### Step 1: Upload Initial Photo

**Context**: Upload photo with Burp active.

Click upload photo, select an image, and save changes with Burp intercepting.

### Step 2: Click Confirmation Link

**Context**: Open and click link with replacement enabled.

Click the confirmation link in the attacker's email in the logged-in browser.

### Step 3: Upload Second Photo

**Context**: Upload on verification page.

On the verification Roshi, upload another image.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- authentication-bypass
- avatar-upload
