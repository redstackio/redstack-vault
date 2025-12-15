---
tags:
  - recon
  - web
  - endpoint-discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:35.465Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: d6b2f5e5-2db5-4ead-9058-21d1c6bb56e2
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover-Emoticon-Reporting-Endpoint

## Summary

This procedure outlines how to identify the API endpoint responsible for handling emoticon abuse reports on Chaturbate, revealing potential vulnerabilities in the reporting mechanism.

## Description

In the context of web application security testing, discovering undocumented or weakly protected endpoints is a key reconnaissance step. For Chaturbate, the emoticon reporting feature uses a GET request to `/emoticon_report_abuse/emoticon_name`, which lacks proper protections. This procedure involves legitimate user interaction to observe network behavior, applicable in bug bounty or penetration testing scenarios targeting similar features. Expected outcomes include endpoint details and initial vulnerability indicators like method type and lack of authentication tokens.

## Requirements

1. Active Chaturbate user account for authentication
2. Modern web browser with developer tools enabled
3. Basic knowledge of HTTP requests and network inspection

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to monitor unusual endpoint access patterns
- Log all reporting actions with user IP and session details for anomaly detection
- Require CSRF tokens on all state-changing endpoints, even GET methods if they trigger actions

## Objectives

1. Locate the exact URL and method for emoticon reporting
2. Document request parameters and headers
3. Identify any immediate security weaknesses like missing tokens

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Gain access to the platform and reach a context where emoticons can be reported.

Log in to Chaturbate using your credentials. Browse to a chat room or profile page displaying emoticons.

> Right-click on an emoticon and select 'Report Abuse' or similar option to trigger the report flow.

### Step 2: Inspect Network Traffic

**Context**: Capture the HTTP request sent during the report submission to reveal the endpoint.

Open browser developer tools (F12), navigate to the Network tab, and clear any existing logs. Submit a test report for an emoticon. Filter for GET requests and examine the one matching `/emoticon_report_abuse/`.

> Note the full URL, such as `https://chaturbate.com/emoticon_report_abuse/example_emoticon`, and confirm it uses GET without CSRF headers.

### Step 3: Validate Endpoint Behavior

**Context**: Test the endpoint manually to confirm its function.

Copy the request URL and paste it into a new browser tab while authenticated. Observe if the report is processed without additional prompts.

> Successful validation shows the emoticon flagged without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
- [[csrf]]
