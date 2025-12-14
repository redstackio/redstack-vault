---
tags:
  - xss
  - web
  - intercept
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:38.111Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 452e68ee-b217-4877-8304-0240cb1a9fbb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access-Imgur-Profile-and-Intercept-Request

## Summary

This procedure covers logging into Imgur, navigating to a target profile, and intercepting the API request triggered by the emerald gifting action to expose the vulnerable redirect parameter.

## Description

In the context of exploiting reflected XSS on Imgur, this initial procedure establishes authenticated access and captures the POST request to the gifting endpoint. The request contains a JSON payload with an unsanitized 'redirect_url' that includes the 'redirect' parameter, which is later tampered with. This step requires a proxy for interception and assumes the attacker has a valid Imgur account. Expected outcome is the full request details for further manipulation, enabling the chain toward JavaScript execution.

## Requirements

1. Valid Imgur account credentials for authentication
2. Web browser with developer tools or a proxy like Burp Suite for request interception
3. Network access to imgur.com and api.imgur.com

## Defense

Defensive measures and detection strategies:

- Implement client-side request monitoring or CSP to block suspicious API calls
- Log and alert on anomalous POST requests to gifting endpoints
- Use WAF rules to detect proxy interception patterns

## Objectives

1. Achieve authenticated access to target profile
2. Capture the vulnerable API request payload
3. Prepare for parameter extraction and modification

## Instructions

### Step 1: Log In and Navigate to Profile

**Context**: Authenticate and reach the point where the gifting feature can be triggered.

No specific command; manually log in via browser at https://imgur.com/signin and navigate to https://imgur.com/user/[username].

> Ensure session is active before proceeding.

### Step 2: Trigger and Intercept Gifting Request

**Context**: Initiate the emerald purchase flow to capture the POST request.

Click 'Give Emerald' on the profile and intercept using proxy tools.

> The request targets /account/v1/gifting/purchase?client_id=546c25a59c58ad7 on api.imgur.com with JSON body including 'redirect_url'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- web
- authentication
