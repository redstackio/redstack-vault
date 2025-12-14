---
tags:
  - authentication
  - web-login
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: bdf68fdd-8a84-4d22-9442-290c45fcfa45
created_at: '2025-12-13T23:52:50.027Z'
updated_at: '2025-12-13T23:52:50.027Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-to-Acronis-Console

## Summary

This procedure establishes a valid session in the Acronis Cyber Protect Console using provided credentials, serving as the entry point for exploiting vulnerabilities in the web interface.

## Description

The Acronis Cyber Protect Console is a web-based management interface for backup and cybersecurity operations. Authentication occurs via a standard login form at https://mc-beta-cloud.acronis.com/ui/. Successful login grants access to administrative features like protection plans. This step is prerequisite for any console interactions and assumes legitimate credentials; in a real attack, these could be phished or brute-forced.

## Requirements

1. Valid username and password for an Acronis account with plan creation permissions
2. Web browser with JavaScript enabled
3. Network access to https://mc-beta-cloud.acronis.com/ui/

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent credential-based access
- Monitor login attempts for anomalies (e.g., unusual IP addresses) using console logs
- Use web application firewalls (WAF) to detect suspicious login patterns

## Objectives

1. Establish authenticated session for subsequent actions
2. Access the Plans section under Protection
3. Prepare for vulnerability exploitation

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the console's entry point to begin authentication.

Open a web browser and visit https://mc-beta-cloud.acronis.com/ui/.

> The login form should load, prompting for credentials.

### Step 2: Enter Credentials and Submit

**Context**: Provide authentication details to gain session access.

Enter the username and password in the respective fields, then click the login button.

> Upon success, the dashboard loads, confirming session establishment.

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
- [[web-access]]
