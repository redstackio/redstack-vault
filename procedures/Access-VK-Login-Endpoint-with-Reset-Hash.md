---
id: proc-vk-login-access-001
tags:
  - login-endpoint
  - session-reset
  - web
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
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:47.841Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Access VK Login Endpoint with Reset Hash

## Summary

This procedure involves navigating to VK.com's login endpoint using the obtained reset_hash to initiate a session reset without user verification, setting the stage for 2FA bypass.

## Description

The login.vk.com endpoint processes reset_hash parameters to terminate and recreate sessions but fails to verify if the requester owns the hash. In a web-based attack on VK.com, an attacker appends the hash to the URL, triggering an unverified reset. This leads to a partial login state. Prerequisites include a valid reset_hash; outcomes are progression to full access without additional auth checks.

## Requirements

1. Valid reset_hash from the target user
2. Web browser with internet access
3. No VPN or proxy restrictions on VK.com

## Defense

Defensive measures and detection strategies:

- Add requester identity checks (e.g., email confirmation) before processing reset_hash
- Log and alert on reset_hash usage from unfamiliar IPs
- Rate-limit reset endpoint accesses

## Objectives

1. Trigger session reset via the login endpoint
2. Avoid identity verification prompts
3. Establish a session context for the target account

## Instructions

### Step 1: Construct the Reset URL

**Context**: Build the URL incorporating the reset_hash to target the vulnerable endpoint.

In a web browser, form the URL as `https://login.vk.com?reset_hash=YOUR_HASH_HERE`, replacing `YOUR_HASH_HERE` with the actual hash string.

> Ensure the URL is accessed over HTTPS to match VK.com's protocol.

### Step 2: Submit the Request

**Context**: Load the endpoint to process the hash and initiate reset.

Enter the URL in the browser address bar and press Enter. The page should load a reset interface without prompting for user details.

> Observe for any errors; a successful load indicates the hash was accepted without verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[login-endpoint]]
- [[session-reset]]
