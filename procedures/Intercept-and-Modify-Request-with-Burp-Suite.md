---
tags:
  - intercept
  - modification
  - burp-suite
  - dom-clobbering
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:26:56.266Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 147f1dd6-659d-4859-86bd-0cdb355e983b
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Drive-by Compromise]]'
---
# Intercept-and-Modify-Request-with-Burp-Suite

## Summary

This procedure details using Burp Suite to capture and alter the Slack POST request during hyperlink submission, injecting a DOM clobbering payload to override document methods.

## Description

Targeted at Slack's post creation API, this intercepts the request containing the link parameter and replaces it with HTML elements (e.g., <img name="write">) that become document properties upon rendering, causing JS failures. Prerequisites include proxy configuration. Outcomes: Modified request submits malicious content leading to DoS.

## Requirements

1. Burp Suite installed and running as proxy
2. Browser or Slack client configured to route through proxy (e.g., 127.0.0.1:8080)
3. Knowledge of HTTP POST structure for Slack

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS with certificate pinning to hinder proxy interception
- Server-side validation of link parameters to reject HTML content
- Log and alert on modified requests with unusual payloads

## Objectives

1. Capture the exact POST request for post submission
2. Inject multiple named HTML elements to clobber document functions
3. Ensure payload evades basic client-side checks

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp to intercept Slack traffic.

In Burp, go to Proxy > Options and ensure it's listening on the correct port. Configure your client to use the proxy.

> Traffic now routes through Burp.

### Step 2: Trigger and Intercept Request

**Context**: Perform the action in Slack to generate the POST.

From the link dialog, submit the placeholder URL; Burp intercepts the POST to Slack's API.

> Request body contains 'link' parameter with benign URL.

### Step 3: Modify Payload

**Context**: Replace the link value with clobbering HTML.

Edit the 'link' parameter to: https://example.com"><img src=x name=\"constructor\" /><img src=x name=\"createElement\" /><img src=x name=\"write\" /><img src=x name=\"writeln\" /><img src=x name=\"open\" /><img src=x name=\"close\" /> (add more for comprehensive clobbering, e.g., alert, eval).

> Payload injects after the benign URL, closing the href properly.

### Step 4: Forward Request

**Context**: Release the modified request.

Click Forward in Burp to send it to Slack.

> Submission completes.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[payload-injection]]
