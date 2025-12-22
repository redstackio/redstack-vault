---
id: proc-observe-legit-request
tags:
  - observation
  - request-intercept
  - csrf
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
updated_at: '2025-12-14T17:27:57.322Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe-Legitimate-Donation-Settings-Request

## Summary

This procedure involves intercepting a legitimate POST request to the Streamlabs donation settings API to capture the exact payload, headers, and response, providing the blueprint for CSRF exploitation.

## Description

To exploit the CSRF vulnerability, attackers must first understand the normal request flow. Using browser tools, monitor the network while updating donation settings, noting the JSON body (e.g., username, amount, clips visibility) and required headers like X-CSRF and X-XSRF. This step confirms the endpoint's behavior in a valid scenario before testing bypasses.

## Requirements

1. Configured Streamlabs account with donations enabled
2. Browser with network interception (e.g., DevTools)
3. Active session as the target user

## Defense

Defensive measures and detection strategies:

- Implement request logging at the API level to detect anomalous payloads.
- Use web application firewalls (WAF) to inspect intercepted traffic patterns.

## Objectives

1. Capture the full legitimate request structure.
2. Identify CSRF headers for later removal testing.
3. Verify endpoint functionality.

## Instructions

### Step 1: Open Developer Tools

**Context**: Prepare to monitor network activity.

In your browser, open DevTools (F12) and switch to the Network tab.

### Step 2: Trigger Donation Update

**Context**: Perform an action that invokes the API.

In the Streamlabs dashboard, modify donation settings (e.g., change username to 'shirley', set amount to null in USD, enable clips visibility) and submit.

### Step 3: Inspect Captured Request

**Context**: Analyze the POST details.

Locate the POST to /api/v6/viewer-portal/viewer-settings/donation_settings, note the JSON body and headers including X-CSRF and X-XSRF, and confirm 200 OK response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- observation
- request-intercept
- csrf
