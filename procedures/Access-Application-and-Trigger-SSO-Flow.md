---
tags:
  - sso
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 3bf6343d-3d0c-4daf-a170-bbd016ceb0f1
created_at: '2025-12-13T09:01:26.700Z'
updated_at: '2025-12-13T09:01:26.700Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access Application and Trigger SSO Flow

## Summary

This procedure involves accessing the Trint application as a logged-in user and navigating to the Support section to initiate the Zendesk SSO flow, allowing observation of the JWT generation process.

## Description

In this step, the attacker logs into the Trint web application and triggers the SSO integration with Zendesk by clicking on the Support link. This exposes the client-side JWT generation logic, which relies on a hardcoded secret. The target environment is a web-based application using JavaScript and React, with expected outcomes including the initiation of an SSO request that can be intercepted.

## Requirements

1. Valid Trint account credentials for initial login
2. Web browser with developer tools enabled
3. Network access to app.trint.com

## Defense

Defensive measures and detection strategies:

- Implement server-side JWT generation and validation instead of client-side
- Monitor for unusual SSO initiations or traffic to Zendesk endpoints

## Objectives

1. Trigger the SSO flow to expose JWT handling
2. Prepare for traffic interception
3. Confirm client-side vulnerabilities in authentication

## Instructions

### Step 1: Login and Navigate

**Context**: Access the application and initiate the support flow.

Navigate to https://app.trint.com, log in, and press 'Support' to trigger the SSO flow.

> This loads the Zendesk integration and generates a JWT in the browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[sso]]
- [[initial-access]]
