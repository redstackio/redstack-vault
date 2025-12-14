---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - access-control
  - information-disclosure
  - api-intercept
  - hackerone
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:26:27.561Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Intercept-Participants-Endpoint-to-View-Emails

## Summary

This procedure involves intercepting the GET request to the /reports/<id>/participants endpoint on HackerOne using a proxy tool like Burp Suite, revealing collaborator email addresses in the JSON response due to absent authentication checks.

## Description

After inviting a collaborator, HackerOne fetches participant data via an API endpoint that fails to enforce proper access controls, allowing the invited email—even for non-registered users—to be exposed in plain text. This step uses network interception to capture and analyze the response, highlighting the information disclosure vulnerability.

## Requirements

1. Active invitation from prior step.
2. Burp Suite or similar proxy configured (browser proxy set to 127.0.0.1:8080).
3. Knowledge of the report ID from the URL.

## Defense

Defensive measures and detection strategies:

- Add authentication tokens and authorization middleware to sensitive API endpoints.
- Monitor for proxy-intercepted traffic or unusual GET requests to participant endpoints.

## Objectives

1. Capture the API response containing participant emails.
2. Verify lack of access controls by observing unauthorized disclosure.
3. Extract sensitive information for impact assessment.

## Instructions

### Step 1: Configure Proxy

**Context**: Set up interception for HackerOne traffic.

Launch Burp Suite, start the proxy listener on port 8080, and configure the browser to route traffic through it (e.g., in Chrome settings).

### Step 2: Trigger and Intercept Request

**Context**: Reload the report page to fetch participant data.

With proxy active, refresh the report page (https://hackerone.com/reports/<id>) or interact with the participants section. In Burp's Proxy tab, intercept the GET request to /reports/<REPORT ID>/participants.

Forward the request and inspect the response.

**Expected Output**: JSON like {"data": {"participants": [{"id": 123, "email": "test@example.com"}]}} showing the email.

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

- [[information-disclosure]]
- [[api-intercept]]
