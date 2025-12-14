---
id: proc-wakatime-observe-response
tags:
  - data-exfiltration
  - response-analysis
  - api
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Automated Collection]]'
updated_at: '2025-12-14T17:25:47.924Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Automated Collection]]'
---
# Observe-Unauthorized-Response

## Summary

This procedure analyzes the API response after IDOR exploitation to extract and verify sensitive user profile information from WakaTime.

## Description

Upon sending the modified request, the server returns the target user's data due to missing checks, exposing privacy-sensitive fields. This step focuses on response inspection in a web API context. Prerequisites: Modified request sent. Outcomes: Confirmation of data leak and potential for further misuse.

## Requirements

1. Sent modified request in Burp Repeater
2. Ability to parse JSON responses
3. Documentation tools for logging exposed data

## Defense

Defensive measures and detection strategies:

- Return 403/404 for unauthorized object access attempts
- Sanitize responses to exclude sensitive fields by default
- Implement data loss prevention (DLP) monitoring on API outputs

## Objectives

1. Confirm successful unauthorized access
2. Extract personal details for impact assessment
3. Identify exposed data types

## Instructions

### Step 1: Send Request

**Context**: Execute the modified request.

Click Send in Burp Repeater.

> HTTP 200 response received.

### Step 2: Analyze Response

**Context**: Inspect JSON for sensitive fields.

View response body for bio, location, social media links, etc.

> Example output: {"name": "Target Name", "bio": "...", "city": "...", "github": "..."}

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Automated Collection]] Automated Collection

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[data-exfiltration]]
- [[response-analysis]]
