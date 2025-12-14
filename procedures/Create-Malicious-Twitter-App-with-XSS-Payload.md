---
id: proc-uuid-1
tags:
  - xss
  - twitter-api
  - app-creation
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
updated_at: '2025-12-13T23:52:44.232Z'
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
# Create-Malicious-Twitter-App-with-XSS-Payload

## Summary

This procedure creates a Twitter application with a name containing an XSS payload, allowing the malicious code to be embedded in tweets posted via the app without sanitization.

## Description

In the attack scenario, an attacker registers a new Twitter app via the Developer Portal. The app name is controllable and not sanitized, enabling injection of HTML/JavaScript like an SVG onload payload. This name populates the 'source' field in tweet metadata. Prerequisites include a Twitter developer account. Expected outcome: Payload ready for use in tweets, leading to DOMXSS when processed in clients like TweetDeck.

## Requirements

1. Active Twitter developer account with API access
2. Internet access to the Twitter Developer Portal
3. Basic knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Sanitize app names on Twitter's end to prevent HTML injection
- Monitor for suspicious app creations with script-like names
- Implement CSP to block inline script execution in TweetDeck

## Objectives

1. Inject XSS payload into tweet source metadata
2. Prepare for delivery via tweet posting
3. Enable arbitrary code execution in victim browsers

## Instructions

### Step 1: Access Twitter Developer Portal

**Context**: Log in to create a new app.

Navigate to https://developer.twitter.com and sign in with developer credentials. Create a new app/project.

### Step 2: Set Malicious App Name

**Context**: Input the XSS payload as the app name to embed it in metadata.

In the app creation form, set the name to `<svg onload=alert(document.domain)>`. Complete registration without triggering any validation errors.

> This payload uses SVG to bypass potential filters and execute JS on load.

### Step 3: Verify App Details

**Context**: Confirm the payload is stored unsanitized.

Retrieve app details via API or portal to ensure the name includes the full payload.

**Expected Output**: App name reflected exactly as entered, including tags and script.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- twitter-api
