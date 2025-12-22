---
id: proc-uuid-002
tags:
  - reconnaissance
  - api-interception
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:30:07.504Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Intercept-Voyager-API-Request

## Summary

This procedure details capturing the HTTP GET request to LinkedIn's Voyager API endpoint using a proxy tool like Burp Suite, allowing inspection of parameters and headers for modification in privilege escalation tests.

## Description

During a security assessment, navigating to Employee Verification in LinkedIn's admin tools sends a GET request to /voyager/api/voyagerOrganizationDashEmailDomainMappings. This step intercepts it to reveal authentication tokens and company-specific parameters. Target environment is web-based with HTTPS. Outcomes include full request details for tampering.

## Requirements

1. Burp Suite or similar proxy running and browser configured to use it
2. Active LinkedIn session from previous access
3. Knowledge of target company URN (e.g., urn:li:fsd_company:81541206)

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and monitor for proxy-intercepted traffic via certificate pinning
- Rate-limit API calls from admin tools
- Log unusual request patterns in Voyager endpoints

## Objectives

1. Capture legitimate API request
2. Identify key headers like Cookie and CSRF-Token
3. Extract parameters for reuse

## Instructions

### Step 1: Configure Proxy

**Context**: Set up interception to route LinkedIn traffic through Burp.

No specific command; in browser settings, set proxy to 127.0.0.1:8080 and install Burp CA certificate.

> Expected output: Traffic routed; no connection errors.

### Step 2: Trigger and Intercept Request

**Context**: Perform action that issues the API call and pause it in proxy.

Navigate to Employee Verification; in Burp, intercept the GET request with path /voyager/api/voyagerOrganizationDashEmailDomainMappings?decorationId=com.linkedin.voyager.dash.deco.organization.FullOrganizationEmailDomainMapping-2&company=urn%3Ali%3Afsd_company%3A81541206&count=100&q=organization&start=0.

> Expected output: Request details visible, including Host: www.linkedin.com, Accept: application/vnd.linkedin.normalized+json+2.1, and redacted Cookie/CSRF-Token.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- reconnaissance
- api-interception
- burp-suite
