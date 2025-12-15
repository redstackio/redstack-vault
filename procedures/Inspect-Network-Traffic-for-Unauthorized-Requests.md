---
tags:
  - network-inspection
  - csrf
type: procedure
tools:
  - '[[tools/Developer-Tools]]'
  - '[[tools/Intercepting-Proxy]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:27:50.494Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c81f6f7e-49ad-4136-adb1-a6cc16e979a8
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Inspect-Network-Traffic-for-Unauthorized-Requests

## Summary

This procedure uses developer tools or a proxy to monitor HTTP traffic and detect unauthorized GET requests to internal paths triggered by path traversal.

## Description

After accessing a vulnerable URL, the application makes unintended requests due to path manipulation. Inspecting traffic reveals GETs to paths like /test.json, confirming the traversal and highlighting CSRF risks on GET endpoints lacking protection. This is key for validating web vulnerabilities in bug bounty or pentesting scenarios.

## Requirements

1. Browser with developer tools (e.g., Chrome DevTools)
2. Optional: Intercepting proxy setup (e.g., Burp Suite)
3. Vulnerable URL from prior procedure

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens on all state-changing endpoints, even GET
- Log and alert on internal requests from user-facing paths
- Use WAF rules to block traversal patterns in parameters

## Objectives

1. Capture proof of unauthorized internal access
2. Identify CSRF potential in GET requests
3. Document for vulnerability reporting

## Instructions

### Step 1: Enable Network Monitoring

**Context**: Prepare tools to capture traffic during URL access.

Open browser developer tools (F12) and navigate to the Network tab, or configure proxy to intercept traffic to https://hackerone.com.

> Ensure filtering is set to show all requests, including XHR/Fetch.

### Step 2: Trigger and Inspect Request

**Context**: Reload the vulnerable URL and analyze captured traffic.

Reload https://hackerone.com/users/confirmation?confirmation_token=z2-aaa&invitation_token=/../../test and search logs for GET to https://hackerone.com/test.json.

> The request should appear as unauthorized, originating from the app but targeting the traversed path. Note status, headers, and response.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Developer-Tools]]
- [[tools/Intercepting-Proxy]]

## Tags

- [[network-inspection]]
- [[csrf]]
