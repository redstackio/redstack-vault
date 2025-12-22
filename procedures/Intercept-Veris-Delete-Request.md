---
tags:
  - recon
  - intercept
  - web
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:23.228Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 60afb3e1-b2b1-469d-b9fe-8e77f251c8d1
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Intercept Veris Delete Request

## Summary

This procedure captures a legitimate delete request in the Veris application to analyze its structure, particularly the ID parameter used for terminals or gatekeepers, setting the stage for IDOR exploitation.

## Description

In the Veris web application, delete operations for assets like terminals or gatekeepers are performed via HTTP requests containing an ID parameter. By intercepting a user's own legitimate delete action using a proxy, attackers can inspect the request format, headers, and payload. This is essential for subsequent modification in an IDOR attack. The target environment is the authenticated Veris web interface, assuming standard HTTPS traffic. Expected outcome: Full request details for replication.

## Requirements

1. Authenticated session in Veris application
2. Proxy tool (e.g., Burp Suite) installed and configured as the browser's proxy
3. Access to perform a legitimate asset deletion

## Defense

Defensive measures and detection strategies:

- Monitor proxy traffic anomalies or unusual request patterns
- Implement client-side certificate pinning to prevent proxy interception
- Log all delete requests with user and IP context for anomaly detection

## Objectives

1. Capture the exact structure of a delete request
2. Identify the ID parameter location (query, path, or body)
3. Prepare for request modification without alerting defenses

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept HTTPS traffic from the browser accessing Veris.

No specific command; configure Burp Suite listener on 127.0.0.1:8080 and set browser proxy accordingly. Install Burp's CA certificate in the browser to handle HTTPS.

> Expected output: All traffic routed through proxy; no certificate errors.

### Step 2: Perform Legitimate Deletion

**Context**: Trigger a delete action on your own terminal or gatekeeper to capture the request.

Navigate to the asset in Veris UI and initiate deletion. Intercept the request in Burp's Proxy > HTTP history or Intercept tab.

> Expected output: Captured request showing method (e.g., DELETE /api/terminals/{own-id}), headers (Authorization: Bearer {token}), and body if applicable.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[recon]]
- [[intercept]]
- [[web]]
