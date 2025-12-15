---
tags:
  - intercept
  - burp-suite
  - request-capture
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
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:57.153Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 1169b531-eb34-4cb7-acbb-5d855d93b10e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Intercept Deactivation Request with Burp Suite

## Summary

This procedure uses Burp Suite to intercept and pause the HTTP POST request sent when attempting to deactivate an Evernote account, allowing analysis of the vulnerable endpoint.

## Description

With Burp Suite configured as a proxy, the attacker simulates a deactivation attempt to capture the exact request structure. This reveals the absence of CSRF tokens and the form data required for exploitation. The target environment is the web browser proxied through Burp, and success is indicated by the request appearing in the intercept tab.

## Requirements

1. Burp Suite installed and running
2. Browser proxy set to Burp (e.g., 127.0.0.1:8080)
3. Authenticated Evernote session

## Defense

Defensive measures and detection strategies:

- Detect proxy usage via inconsistent headers (e.g., missing or altered User-Agent)
- Rate-limit attempts on deactivation endpoints

## Objectives

1. Capture the full POST request details
2. Identify exploitable parameters
3. Avoid actual deactivation during capture

## Instructions

### Step 1: Configure Burp Intercept

**Context**: Enable interception to pause outgoing requests from the browser.

In Burp Suite:

1. Go to Proxy > Options > Intercept Client Requests: On
2. Ensure the browser is proxied correctly

> Scope set to include evernote.com; test with a simple page load.

### Step 2: Trigger Deactivation Attempt

**Context**: Perform the action that generates the vulnerable request.

In the browser on the deactivation page:

1. Press 'Deactivate your Evernote account'
2. Acknowledge the confirmation popup
3. Select a reason (e.g., 'different app')
4. Press 'Deactivate account'

> Request halts in Burp Intercept tab; review but do not forward yet to analyze.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- intercept
- burp-suite
- request-capture
