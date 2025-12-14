---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - xss
  - intercept
  - proxy
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-09-18T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.846Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Intercept-Save-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to capture the HTTP POST request generated when saving a survey question in Crowdsignal, allowing inspection and modification of parameters for XSS injection.

## Description

Burp Suite acts as a man-in-the-middle proxy to intercept traffic between the browser and the Crowdsignal server. By configuring the browser to use Burp's proxy and triggering the save action, the request containing the media shortcode is captured. This is crucial for identifying and altering the vulnerable media parameter. Prerequisites include Burp Suite running with the proxy listener active on port 8080. The outcome is a paused request ready for editing.

## Requirements

1. Burp Suite installed and running with proxy enabled
2. Browser proxy settings pointed to 127.0.0.1:8080
3. Active survey question editor in Crowdsignal

## Defense

Defensive measures and detection strategies:

- Deploy web application firewalls (WAF) to inspect and block anomalous requests
- Log and alert on proxy-like traffic patterns from user IPs

## Objectives

1. Capture the exact save request structure
2. Identify the media parameter for modification
3. Ensure interception without disrupting the session

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up Burp to intercept HTTP traffic from the browser.

Launch Burp Suite, navigate to the Proxy tab, and ensure the Intercept is on. Confirm the listener is active on 127.0.0.1:8080.

> Browser traffic will now route through Burp.

### Step 2: Trigger Save Action

**Context**: Generate the request by attempting to save the question.

In the Crowdsignal question editor, with media inserted, click the "Save" button.

> Burp will pause the outgoing POST request to /quizzes/{survey-id}/question.

### Step 3: Inspect Request

**Context**: Verify the request contains the expected media parameters.

In Burp's Intercept tab, review the POST body for parameters like media[11111111] with the shortcode value.

> Confirm the request is modifiable before proceeding.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[intercept]]
