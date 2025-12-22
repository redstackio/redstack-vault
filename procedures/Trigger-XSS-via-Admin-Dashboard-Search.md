---
tags:
  - xss-trigger
  - admin-dashboard
  - search-functionality
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ffa8bf2f-46f9-4f09-879e-d7015d73ed51
created_at: '2025-12-13T23:52:55.559Z'
updated_at: '2025-12-13T23:52:55.559Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Admin-Dashboard-Search

## Summary

This procedure triggers DOM-based XSS by accessing the vulnerable admin dashboard and performing searches that load unsanitized user data, executing injected JavaScript in the admin's browser context.

## Description

Targeting Shopify's Device Manager at https://devicemanager.shopifycloud.com/admin, the search functionality fetches and renders user profiles (including injected payloads) directly into the DOM without output encoding. This leads to arbitrary code execution, potentially stealing session data or dashboard contents. The attack assumes admin access but can be triggered passively if admins search for the affected profiles.

## Requirements

1. URL access to the admin dashboard
2. Knowledge of injected profile identifiers (e.g., email or store name)
3. Browser capable of executing JavaScript (for testing)

## Defense

Defensive measures and detection strategies:

- Encode all output when rendering user data in the DOM (e.g., use textContent instead of innerHTML)
- Implement search query logging and anomaly detection for frequent or scripted searches
- Deploy Web Application Firewall (WAF) rules to block known XSS patterns in search results

## Objectives

1. Execute JavaScript in authenticated admin session
2. Access sensitive data displayed in the dashboard
3. Demonstrate vulnerability impact on confidentiality

## Instructions

### Step 1: Access Admin Dashboard

**Context**: Navigate to the vulnerable endpoint to prepare for triggering.

Open a browser and go to https://devicemanager.shopifycloud.com/admin. If testing ethically, use a controlled environment or report without full execution.

> Dashboard loads; ensure logged in as admin if simulating.

### Step 2: Perform Vulnerable Search

**Context**: Search for profiles containing injected payloads to trigger DOM rendering.

Enter the injected profile details (e.g., search for 'samudra+lp@wearehackerone.com' or store 'uji150') in the search bar and submit.

> The search results render the payload, executing JavaScript (e.g., prompt appears for simple payload; exfiltration for advanced).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[admin-dashboard]]
