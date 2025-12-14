---
id: proc-replace-fb-token-001
tags:
  - token-replacement
  - bypass
  - oauth
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:34.461Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Replace-fb_token-with-External-Token

## Summary

This procedure modifies an intercepted Facebook login request by replacing the Reverb app's fb_token with a valid access token from another Facebook app, exploiting the lack of origin validation to impersonate users.

## Description

The Reverb API at /api/auth/facebook does not verify that the fb_token belongs to the expected app ID, allowing tokens from apps like Lyst to be used. This step occurs in Burp Suite's Repeater after interception, targeting the JSON payload. Prerequisites include a valid external token obtained via Facebook's developer tools or another app's login flow.

## Requirements

1. Intercepted request from previous procedure
2. Valid fb_token from a different Facebook app (e.g., Lyst: EAAJ8Of8DF2IBAL5wChKjuRHSV2VEWpm7eCz2IMqqJy1lJJq8ooyQuKHcOXn6aZCZAIrCtClbrZBdUGhC3FbvncNYk1E0k7AOktEhDjUPwHPOh3x29JURSGIGPBlZCj5WlBHhHzI5KYAPbuXKiZBGTkKZABZATh9JjTqEDhRubYSEiTmhjeytx5moFH9naZB6XjZBRUMkmcbucFD9Vf8IoFZAD1LGngi6j5pXFGcTFPfBEudAZDZD)
3. Burp Suite Repeater tab access

## Defense

Defensive measures and detection strategies:

- Validate token's app_id against expected values on the server side using Facebook's Graph API
- Implement token introspection endpoints to check issuer and audience claims
- Rate-limit login attempts and monitor for token anomalies in logs

## Objectives

1. Substitute the token to bypass app-specific validation
2. Maintain request integrity for seamless submission
3. Enable unauthorized access to target accounts

## Instructions

### Step 1: Load Request into Repeater

**Context**: Transfer the intercepted request to Burp's Repeater for editing.

In Burp Proxy, right-click the captured request and select "Send to Repeater." Switch to the Repeater tab to view the raw request.

### Step 2: Edit JSON Payload

**Context**: Replace the fb_token value while preserving the rest of the structure.

Locate the JSON body in the request pane, change {"fb_token": "original"} to {"fb_token": "EAAJ8Of8DF2IBAL5wChKjuRHSV2VEWpm7eCz2IMqqJy1lJJq8ooyQuKHcOXn6aZCZAIrCtClbrZBdUGhC3FbvncNYk1E0k7AOktEhDjUPwHPOh3x29JURSGIGPBlZCj5WlBHhHzI5KYAPbuXKiZBGTkKZABZATh9JjTqEDhRubYSEiTmhjeytx5moFH9naZB6XjZBRUMkmcbucFD9Vf8IoFZAD1LGngi6j5pXFGcTFPfBEudAZDZD"}. Verify JSON validity.

**Expected Output**: Updated request body with new token embedded.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[token-replacement]]
- [[bypass]]
