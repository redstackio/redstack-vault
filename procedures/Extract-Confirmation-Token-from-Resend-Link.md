---
tags:
  - token-leak
  - extraction
  - shopify
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.281Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 567d7e2d-ce01-4677-971a-63fa869e966a
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Confirmation-Token-from-Resend-Link

## Summary

This procedure details the inspection and extraction of the leaked confirmation token from the resend link displayed after initiating an email change on Shopify's account page.

## Description

Following the submission of a new email, Shopify displays a message with a resend link that embeds the sensitive confirmation token in the URL path. This leakage violates secure token handling by exposing it client-side without protection. The procedure involves manual URL inspection, enabling the subsequent bypass. Prerequisites include having completed the email change initiation.

## Requirements

1. Active session from email change initiation
2. Web browser developer tools or URL bar access
3. The verification message visible on the page

## Defense

Defensive measures and detection strategies:

- Obfuscate or hash tokens in client-side links
- Use short-lived tokens with server-side validation only
- Log and alert on resend link accesses

## Objectives

1. Identify the resend link in the UI
2. Parse the URL to isolate the token
3. Prepare token for reuse in confirmation

## Instructions

### Step 1: Observe Verification Message

**Context**: The message post-submission contains the exploitable link.

After submitting the email, note the displayed text and embedded resend option.

> The message includes: options to resend or cancel, with the resend as a hyperlink.

### Step 2: Copy Resend URL

**Context**: Capture the full link to access the token.

Right-click the resend link and select 'Copy link address' or inspect the element to get the href.

> URL format: https://accounts.shopify.com/email-change/<Confirmation-TOKEN>/resend, where <TOKEN> is a unique string like abc123def456.

### Step 3: Extract Token Value

**Context**: Isolate the token from the path for direct use.

From the copied URL, copy the segment between /email-change/ and /resend.

> Token is now available for the next step, e.g., abc123def456.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- token-leak
- extraction
- shopify
