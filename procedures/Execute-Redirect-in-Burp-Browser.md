---
id: uuid-6
tags:
  - redirect-validation
  - phishing-test
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite-Community-Edition]]'
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
updated_at: '2025-12-14T17:24:26.959Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-Redirect-in-Burp-Browser

## Summary

Opens the response link in Burp's embedded Chromium browser to confirm the redirect to the arbitrary external URL.

## Description

This final step validates the open redirect by simulating user navigation, showing how an attacker could lure victims to the malicious site via the trusted Reddit domain.

## Requirements

1. Copied response link from Burp
2. Burp's built-in browser enabled

## Defense

Defensive measures and detection strategies:

- User education on suspicious redirects
- Browser extensions to block untrusted redirects

## Objectives

1. Observe redirect execution
2. Confirm phishing potential
3. Document vulnerability impact

## Instructions

### Step 1: Open Burp Browser

**Context**: Access embedded browser.

In Burp, go to the built-in browser via the link or menu.

### Step 2: Navigate to Link

**Context**: Trigger the response view.

Paste and enter the copied link.

**Expected Output**: Browser loads the response, then redirects to http://google.com (or malicious site).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Community-Edition]]

## Tags

- [[redirect-validation]]
- [[phishing-test]]
- [[web]]
