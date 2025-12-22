---
tags:
  - authentication
  - web-access
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:46:37.318Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 0e705a3d-6953-4c37-8b23-7375236b892a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-and-Setup-lemlist-Campaign

## Summary

This procedure outlines gaining authenticated access to the lemlist web application and navigating to the campaign creation or editing interface, serving as the initial setup for exploiting vulnerabilities in campaign management.

## Description

In the context of a stored XSS attack on lemlist, this procedure establishes a legitimate user session and positions the attacker to interact with the vulnerable Campaign Name field. It requires valid credentials and assumes no additional privileges. The expected outcome is access to the editable campaign form, enabling subsequent payload injection without raising immediate suspicions.

## Requirements

1. Valid lemlist account credentials (email and password)
2. Web browser with JavaScript enabled
3. Network access to https://app.lemlist.com

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent unauthorized access
- Monitor login attempts for anomalies, such as unusual IP locations
- Use web application firewalls (WAF) to detect suspicious navigation patterns

## Objectives

1. Establish an authenticated session in lemlist
2. Reach the campaigns section for creation or editing
3. Prepare the environment for payload injection

## Instructions

### Step 1: Log In to lemlist

**Context**: Authenticate to gain access to the dashboard.

Navigate to https://app.lemlist.com/login in your browser and enter your credentials.

> Upon successful login, you will be redirected to the main dashboard.

### Step 2: Navigate to Campaigns

**Context**: Access the area for managing campaigns.

From the dashboard sidebar, click on 'Campaigns' and then select 'Create new' or edit an existing one.

> The campaign form opens, displaying input fields including the vulnerable Campaign Name.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[web-setup]]
