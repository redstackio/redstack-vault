---
id: proc-120312-capture-request
tags:
  - recon
  - web
  - http-interception
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:23.346Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Capture Original Venue Creation Request

## Summary

This procedure intercepts the HTTP request sent during a legitimate venue creation in the Veris application, capturing the structure including the 'parent' parameter for later modification in an IDOR attack.

## Description

In the context of exploiting IDOR in Veris, capturing the original request is essential to identify the exact format, headers, and parameters used in venue creation. This step assumes an authenticated session and uses a proxy to monitor traffic without alerting the application. Expected outcome is a complete request template that can be replayed with modifications.

## Requirements

1. Authenticated access to Veris with venue creation permissions
2. Proxy tool (e.g., Burp Suite) configured between browser and application
3. Knowledge of the venue creation endpoint URL

## Defense

Defensive measures and detection strategies:

- Monitor for unusual proxy traffic or request patterns from user agents
- Implement request logging to detect interception attempts

## Objectives

1. Obtain baseline HTTP request for venue creation
2. Identify authorized 'parent' parameter value
3. Prepare for parameter tampering

## Instructions

### Step 1: Configure Proxy and Perform Legitimate Creation

**Context**: Set up interception and trigger a standard venue creation to capture the request.

Navigate to the venue creation form in Veris, fill in basic details with an authorized parent, and submit. Ensure the proxy is active to capture the POST request to the endpoint (e.g., /api/venues).

**Expected Output**: Intercepted request in proxy history showing method: POST, headers (including Authorization or cookies), and body with parameters like name, parent=123.

### Step 2: Export Request for Analysis

**Context**: Save the captured request for editing.

Copy the full request details from the proxy tool, including URL, method, headers, and body.

**Expected Output**: Raw HTTP request text ready for modification.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
- [[http-interception]]
