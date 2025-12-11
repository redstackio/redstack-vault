---
tags:
  - interception
  - burp-suite
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: a42f0a59-d4dc-4b14-ac6c-ca68b8c8c1df
created_at: '2025-12-11T06:10:28.983Z'
updated_at: '2025-12-11T06:10:28.983Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
---
# Setup Burp Suite for Request Interception

## Summary

This procedure sets up Burp Suite to intercept and monitor HTTP requests, enabling the capture of API calls for further analysis and modification in web application testing.

## Description

Burp Suite is configured as a proxy to sit between the browser and the target application, such as Snapchat's web interface. This allows for the interception of requests like GraphQL mutations, which can reveal vulnerabilities like IDOR when modified. Prerequisites include an installed Burp Suite and a browser configured to use the proxy.

## Requirements
1. Burp Suite installed and running.
2. Browser proxy configured to 127.0.0.1:8080.
3. Access to the target web application (e.g., https://my.snapchat.com).

## Defense

Defensive measures and detection strategies:
- Use HTTPS and certificate pinning to prevent interception.
- Monitor for anomalous proxy traffic or tool signatures in logs.

## Objectives
1. Enable request interception for analysis.
2. Prepare for capturing specific API requests.
3. Ensure no disruption to normal application access.

## Instructions

### Step 1: Launch Burp Suite and Enable Proxy

**Context**: Start Burp Suite and activate the proxy listener.

Launch Burp Suite and navigate to the Proxy tab. Ensure the intercept is on.

> This sets up the proxy to capture all traffic routed through it.

### Step 2: Configure Browser Proxy

**Context**: Route browser traffic through Burp Suite.

In your browser settings, set the HTTP proxy to 127.0.0.1:8080 and install the Burp CA certificate if needed.

> This allows interception of requests to sites like Snapchat.

## MITRE ATT&CK Mapping

### Tactics
- [[Execution]]

### Techniques
- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used

## Tools Used
- [[tools/Burp-Suite]]

## Tags
- interception
- burp-suite
