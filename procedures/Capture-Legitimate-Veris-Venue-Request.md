---
id: proc-uuid-1
tags:
  - recon
  - web
  - api
  - proxy
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
updated_at: '2025-12-14T17:25:23.380Z'
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
# Capture-Legitimate-Veris-Venue-Request

## Summary

This procedure involves intercepting a legitimate HTTP request to the Veris application's venue data endpoint using the attacker's own credentials, establishing the baseline request structure for subsequent IDOR exploitation.

## Description

In the context of the Veris IDOR vulnerability, attackers first need to capture a valid request to their own organization's venue data. This is done by proxying traffic through a tool like Burp Suite while authenticated in the application. The captured request reveals the API endpoint (e.g., /api/venues/{venue_id}) and parameters, including the user's own venue_id. No exploitation occurs here, but it sets up the manipulation in later steps. Prerequisites include a valid Veris account and network access to the API.

## Requirements

1. Valid authenticated session in Veris application
2. Proxy tool (e.g., Burp Suite) configured to intercept browser traffic
3. Knowledge of the venue data retrieval feature in Veris

## Defense

Defensive measures and detection strategies:

- Implement client-side certificate pinning to prevent proxy interception
- Monitor for unusual proxy traffic patterns in network logs
- Use API gateways with request logging to detect interception attempts

## Objectives

1. Obtain the exact format of the venue data API request
2. Identify the venue_id parameter location
3. Verify legitimate response for comparison

## Instructions

### Step 1: Configure Proxy Interception

**Context**: Set up Burp Suite to capture HTTPS traffic from the browser interacting with Veris.

No specific command; configure Burp Suite proxy listener on 127.0.0.1:8080 and set browser to use it as proxy. Install Burp CA certificate in browser.

> Expected output: All traffic routed through Burp, visible in Proxy > HTTP history.

### Step 2: Trigger Legitimate Venue Data Request

**Context**: Authenticate in Veris and access the venue data page to generate the request.

Navigate to the venue management section in the Veris web app and click to view your organization's venue details.

> Expected output: Intercepted request in Burp showing GET/POST to /api/venues/{own_venue_id} with auth headers, and response with own data.

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
- [[web]]
- [[api]]
