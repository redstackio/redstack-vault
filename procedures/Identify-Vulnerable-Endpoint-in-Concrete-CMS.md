---
id: proc-identify-csrf-endpoint-concrete
tags:
  - csrf
  - recon
  - concrete-cms
  - web
type: procedure
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:15:31.895Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Identify Vulnerable Endpoint in Concrete CMS

## Summary

This procedure involves reconnaissance of the Concrete CMS admin dashboard to identify the community points actions creation endpoint lacking CSRF protection, enabling subsequent exploitation.

## Description

In Concrete CMS, the endpoint `/index.php/dashboard/users/points/actions/save` handles POST requests for creating points actions without requiring CSRF tokens or validating inputs like `upaName` and `upaHandle`. This procedure outlines manual inspection or proxy-based analysis to confirm the vulnerability, setting the stage for CSRF and XSS attacks in an admin context. Expected outcomes include verification of unprotected access, allowing arbitrary data storage.

## Requirements

1. Access to a Concrete CMS instance with admin privileges or network visibility
2. Web proxy tool (e.g., Burp Suite) for traffic inspection
3. Basic knowledge of HTTP requests and PHP web apps

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Use web application firewalls (WAF) to detect anomalous POST patterns to admin paths
- Log and monitor admin dashboard access for unusual parameter values

## Objectives

1. Confirm absence of CSRF protection on the save endpoint
2. Identify unsanitized parameters for payload injection
3. Map the output rendering path for XSS confirmation

## Instructions

### Step 1: Access Admin Dashboard

**Context**: Log in as an admin or observe traffic to locate points management features.

Navigate to `/dashboard/users/points/actions` in the Concrete CMS interface and attempt to create a benign points action, inspecting the form submission.

> No specific command; use browser dev tools to view the POST action URL and parameters.

### Step 2: Inspect Endpoint for Protections

**Context**: Verify lack of CSRF and sanitization by testing direct requests.

Use a proxy to capture the legitimate POST, then replay it without any token field. Check server response for acceptance.

> Example test payload: POST with `upaName=test` and `upaHandle=test-handle`.

### Step 3: Confirm Output Rendering

**Context**: Ensure injected data is displayed unsanitized.

Submit a test payload and view `/dashboard/users/points/actions/action_saved` to see if inputs are echoed back without escaping.

> Look for raw HTML reflection in the page source.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- Burp Suite (for proxying)

## Tags

- csrf
- recon
- concrete-cms
