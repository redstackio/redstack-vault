---
tags:
  - burp-suite
  - interception
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
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:18.311Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 03165482-6d0a-4c97-9a6f-f2b1e680a8c8
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Configure-Burp-Suite-for-Request-Interception

## Summary

This procedure sets up Burp Suite to proxy and intercept HTTP requests from a target web application, enabling inspection and modification for vulnerability discovery, such as identifying error tracking integrations.

## Description

In scenarios involving web application testing, intercepting traffic is essential to analyze requests and responses. This procedure focuses on configuring Burp Suite's proxy to capture application traffic, particularly useful for spotting misconfigurations like exposed Sentry endpoints. Prerequisites include a running Burp Suite instance and browser proxy configuration. Expected outcomes include full visibility into request flows, facilitating further exploitation steps.

## Requirements

1. Burp Suite Professional or Community edition installed
2. Target web application accessible via browser
3. Browser (e.g., Firefox or Chrome) configured to use Burp proxy at 127.0.0.1:8080
4. No special credentials; assumes public access to the application

## Defense

Defensive measures and detection strategies:

- Monitor proxy traffic anomalies using network IDS like Snort
- Enforce certificate pinning in applications to block unauthorized proxies
- Log all intercepted requests server-side for anomaly detection

## Objectives

1. Establish proxy interception for all application traffic
2. Capture initial requests to baseline normal behavior
3. Prepare for request modification in subsequent steps

## Instructions

### Step 1: Launch and Configure Burp Proxy

**Context**: Start Burp Suite and enable the proxy listener to route browser traffic through it.

Open Burp Suite, navigate to the Proxy tab, and ensure the Intercept is on. In Options > Proxy Listeners, confirm 127.0.0.1:8080 is running. No command needed; this is GUI-based.

> Burp will now intercept requests; turn off intercept for passive monitoring if needed.

### Step 2: Route Browser Traffic

**Context**: Configure the browser to send requests via Burp proxy.

In browser settings, set HTTP proxy to 127.0.0.1:8080. Install Burp's CA certificate to handle HTTPS. Navigate to the target application to generate traffic.

> Requests appear in Proxy > HTTP history; toggle Intercept to capture specific ones.

### Step 3: Intercept Initial Request

**Context**: Capture a live request to verify setup.

With Intercept on, perform an action in the application (e.g., trigger an error). The request pauses in Burp for inspection.

> Successful interception shows full request details, including headers and body.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[tools/Burp-Suite]]
- [[interception]]
- [[proxy]]
