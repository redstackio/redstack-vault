---
id: proc-intercept-burp-form
tags:
  - proxy
  - interception
  - web
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:26:30.694Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Intercept-Form-Submission-with-Burp

## Summary

This procedure details using Burp Suite to intercept an HTTP POST request from a profile update form, allowing inspection and modification for vulnerability testing, such as injection attacks.

## Description

Burp Suite acts as a man-in-the-middle proxy to capture web traffic. In this scenario, it traps the POST to /internal_api/v0.2/savePublicInformation sent as application/x-www-form-urlencoded. The target is a web application like Semmle, and the outcome is a paused request ready for editing. Prerequisites include proxy configuration in the browser and Burp running.

## Requirements

1. Burp Suite installed and running with Proxy listener on 127.0.0.1:8080
2. Browser proxy settings updated to route through Burp
3. Active session in the target application

## Defense

Defensive measures and detection strategies:

- Enforce certificate pinning to detect proxy interception
- Log and alert on requests from proxy-like user-agents or IPs
- Use HSTS to prevent downgrading to interceptable connections

## Objectives

1. Capture the form submission request for analysis
2. Pause traffic to enable payload insertion
3. Verify request structure before modification

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up Burp to listen for traffic.

No command; GUI configuration:

- Launch Burp Suite.
- Go to Proxy > Options > Add listener on 127.0.0.1:8080.

> Listener active; confirm in Intercept tab.

### Step 2: Route Browser Traffic

**Context**: Direct application traffic through the proxy.

No command; browser settings:

- In browser (e.g., Firefox), set HTTP Proxy to 127.0.0.1:8080.
- Install Burp's CA certificate to handle HTTPS.

> Traffic now proxied; test with a simple page load.

### Step 3: Submit Form to Intercept

**Context**: Trigger the request to capture it.

No command; form interaction:

- Fill and submit the profile form.

> Request appears in Burp Proxy > Intercept; forward or drop as needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Network Sniffing]] Network Sniffing

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- proxy
- interception
