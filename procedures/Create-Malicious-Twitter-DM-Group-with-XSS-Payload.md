---
id: proc-create-dm-xss-payload
tags:
  - xss
  - payload-creation
  - twitter-dm
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
updated_at: '2025-12-14T03:16:07.997Z'
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
# Create-Malicious-Twitter-DM-Group-with-XSS-Payload

## Summary

This procedure creates a Twitter DM group with a malicious XSS payload embedded in the group name, exploiting the lack of sanitization to store executable JavaScript persistently on Twitter's platform for later execution in TweetDeck.

## Description

The attack targets the 9-character limit on Twitter DM group names by using simple payloads like `<script>alert(1);//` or multi-stage techniques: create one group named `</script>hi` to close potential open tags, followed by another `<script>alert(1);//` to inject and execute the script. This setup allows the payload to persist and render unsafely in TweetDeck, enabling JavaScript execution in the victim's browser context. Prerequisites include a valid Twitter account; no additional tools are needed as it uses the web interface.

## Requirements

1. Valid Twitter account with DM creation privileges.
2. Access to twitter.com via a web browser.
3. Knowledge of basic XSS payloads to fit character limits.

## Defense

Defensive measures and detection strategies:

- Sanitize all user-input group names on both Twitter and TweetDeck sides using HTML entity encoding or Content Security Policy (CSP).
- Implement client-side validation to reject script tags in DM names.
- Monitor for anomalous DM group creations with suspicious characters.

## Objectives

1. Store a persistent XSS payload in a Twitter DM group name.
2. Bypass length restrictions for effective payload delivery.
3. Prepare the group for victim invitations to propagate the vulnerability.

## Instructions

### Step 1: Log In and Navigate to DMs

**Context**: Access the Twitter DM interface to initiate group creation.

Log into twitter.com and click the envelope icon to open Messages. Ensure you are on the web version, not mobile.

### Step 2: Create New Group DM

**Context**: Start a new group conversation and set the malicious name.

Click the new message icon, select multiple participants if needed (or start solo), and name the group. Enter the payload `<script>alert(1);//` (fits within 9 characters). If longer payloads are required, create a preliminary group named `</script>hi` first.

### Step 3: Verify Payload Storage

**Context**: Confirm the name is stored without sanitization.

View the group in your DM list; the name should display as entered, including the script tag. Test by creating a second group if using multi-stage: name it `<script>alert(1);//` and merge or reference as needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[xss]]
- [[twitter-dm]]
- [[payload-injection]]
