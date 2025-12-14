---
tags:
  - intercept
  - proxy
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Account Discovery]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 2d013422-59c9-43ad-abe7-d764b8ea73c3
created_at: '2025-12-14T17:25:47.353Z'
updated_at: '2025-12-14T17:25:47.353Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Intercept-Review-Submission-Request

## Summary

This procedure captures the HTTP POST request to the /hacker_reviews endpoint during feedback submission, allowing inspection of vulnerable parameters like hacker_username.

## Description

In the IDOR attack on HackerOne, a proxy tool intercepts the request after entering review details. The request includes parameters such as hacker_username=jong_jong&report_id=<redacted>&positive=true&behavior=friendly&private_feedback=Thanks+for+your+report. This step targets the web traffic from the review submission. Prerequisites include proxy setup (e.g., Burp Suite). Expected outcome is the full request visible for modification.

## Requirements

1. Proxy tool like Burp Suite configured as browser proxy
2. Security team session active
3. Review process initiated

## Defense

Defensive measures and detection strategies:

- Implement client-side request signing or CSRF tokens
- Monitor for proxy-intercepted traffic patterns in logs

## Objectives

1. Capture the vulnerable POST request
2. Identify IDOR parameter (hacker_username)
3. Prepare for modification without alerting

## Instructions

### Step 1: Configure Proxy

**Context**: Set up interception before submitting the review.

Configure browser to route through Burp Suite proxy (e.g., 127.0.0.1:8080).

### Step 2: Submit Review to Intercept

**Context**: Trigger the request and pause it in proxy.

Click submit on the review form; intercept the POST /hacker_reviews in Burp.

**Expected Output**: HTTP/1.1 POST request with form parameters displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[proxy]]
- [[web]]
