---
tags:
  - xss
  - setup
  - oauth
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:30.449Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 1b90cb66-a1be-4ca3-aa32-c30a329c15d9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-OWOX-BI-Data-Source-Setup

## Summary

This procedure initiates the OWOX BI connected services setup for Google Analytics, navigating to the vulnerable OAuth callback endpoint where the reflected XSS can be prepared.

## Description

In the context of exploiting a reflected XSS in OWOX BI, this step involves accessing the data source setup page, selecting Google Analytics, and providing Gmail credentials to trigger the OAuth flow. This exposes the callback URL at https://bi.owox.com/ui/callbacks/google-supervisors/, which lacks path sanitization. Prerequisites include a browser and valid Gmail access for simulation; the outcome is reaching the error/redirect step for payload injection.

## Requirements

1. Web browser (Firefox or Chrome) with internet access
2. Valid Gmail credentials for OAuth simulation
3. Target OWOX BI instance accessible at https://bi.owox.com

## Defense

Defensive measures and detection strategies:

- Implement URL path validation and sanitization in OAuth callbacks
- Use Content Security Policy (CSP) to block inline script execution
- Monitor for anomalous setup page accesses and OAuth redirects

## Objectives

1. Reach the Google Analytics integration setup endpoint
2. Trigger the OAuth authorization flow
3. Expose the vulnerable callback URL structure

## Instructions

### Step 1: Navigate to Setup Page

**Context**: Load the OWOX BI connected services configuration to begin the data source addition process.

In Firefox or Chrome, visit https://bi.owox.com/ui/settings/connected-services/setup/ and log in if prompted.

> Expected: The setup interface displays available data sources.

### Step 2: Select and Initiate Google Analytics

**Context**: Choose the vulnerable integration and start the OAuth process to generate the callback.

Select "Google Analytics" from the data sources, enter your Gmail credentials when redirected, and authorize the connection.

> Expected: Redirect to Google's OAuth page, followed by an error link back to OWOX BI's callback endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- xss
- oauth
- setup
