---
id: proc-uuid-123
tags:
  - dos
  - resource-exhaustion
  - input-validation
  - web
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.175Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Submit-Oversized-Bounty-Value-to-Trigger-Server-Hang

## Summary

This procedure exploits uncontrolled resource consumption in the HackerOne team creation process by submitting an excessively large bounty value, causing the server to perform prolonged processing and resulting in a denial of service condition for approximately 1.5 minutes.

## Description

The vulnerability stems from a lack of input validation or length limits on the bounty amount field in the team creation form at hackerone.com/teams/new. By providing a bounty value exceeding 1,000,000 digits, the server engages in excessive computation or string handling, leading to a hang. This impacts the website's availability, rendering it unresponsive until an error is eventually displayed. The attack requires no authentication and can be executed from any web browser, targeting the public-facing web application.

## Requirements

1. Web browser or HTTP client capable of submitting POST requests with large payloads
2. Internet access to reach hackerone.com
3. Ability to generate or input a large string (e.g., 1,000,000+ digits)

## Defense

Defensive measures and detection strategies:

- Implement server-side input length validation on numeric fields (e.g., limit bounty to reasonable digit counts like 10-15)
- Use rate limiting on form submissions to prevent abuse
- Monitor server resource usage spikes correlated with form submissions and log oversized inputs for alerting

## Objectives

1. Cause temporary denial of service on the team creation endpoint
2. Demonstrate the impact of missing input sanitization on web forms
3. Highlight resource exhaustion risks in user-input processing

## Instructions

### Step 1: Access the Target Form

**Context**: Navigate to the vulnerable team creation page to prepare the form submission.

Open a web browser and visit https://hackerone.com/teams/new. This loads the form without requiring login.

### Step 2: Prepare Oversized Input

**Context**: Generate an input string large enough to trigger excessive processing.

Create a string of over 1,000,000 digits, such as by repeating the character '1' in a text editor or script (e.g., Python: print('1' * 1000001)). Copy this string for use in the bounty field.

### Step 3: Submit the Form

**Context**: Inject the oversized value into the bounty field and submit to initiate the resource exhaustion.

In the form, locate the bounty amount field (typically a numeric input). Paste the oversized string into it, complete any other required fields minimally if needed, and click submit. Alternatively, use browser developer tools to modify the form data before submission.

**Expected Output**: The page will freeze or show a persistent loading state for about 1.5 minutes, after which an error message like a timeout or invalid input may appear. During this time, the endpoint is effectively unavailable.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos
- resource-exhaustion
- input-validation
- web
