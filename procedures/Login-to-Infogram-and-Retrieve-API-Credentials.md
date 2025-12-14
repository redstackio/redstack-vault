---
id: proc-infogram-login-api-001
tags:
  - authentication
  - api-credentials
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[T1078.004]]'
updated_at: '2025-12-14T17:32:10.740Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1078.004]]'
---
# Login-to-Infogram-and-Retrieve-API-Credentials

## Summary

This procedure authenticates to the Infogram platform and retrieves necessary API credentials to enable programmatic interaction with the service's REST API for infographic creation.

## Description

In the context of exploiting Infogram's API vulnerabilities, initial access requires a valid user account. This step involves logging into the web interface, navigating to API settings, and extracting the key and secret, which are used to initialize API clients. Without these, API requests will fail authentication. The target environment is the Infogram web app, and outcomes include readiness for API-based attacks like payload injection.

## Requirements

1. Valid Infogram account email and password
2. Web browser with access to https://infogram.com
3. No special permissions beyond standard user access

## Defense

Defensive measures and detection strategies:

- Enforce MFA for account logins to prevent unauthorized access
- Monitor API key generation and usage logs for anomalous patterns
- Use API rate limiting to detect scripted access attempts

## Objectives

1. Gain authenticated access to Infogram dashboard
2. Obtain API credentials for REST API calls
3. Prepare for payload injection without manual UI interaction

## Instructions

### Step 1: Access and Authenticate to Infogram

**Context**: Log into the platform to reach protected settings.

Navigate to https://infogram.com and enter your credentials to authenticate.

> Successful login redirects to the dashboard at https://infogram.com/app.

### Step 2: Retrieve API Credentials

**Context**: Access the API settings page to copy key and secret.

Go to https://infogram.com/app/#settings/api, generate or copy the existing API Key and API Secret.

> Credentials are displayed as strings; store securely for Java code use. Expected: Two alphanumeric strings (e.g., Key: abc123, Secret: def456).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1078.004]] Cloud Accounts

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- authentication
- api-setup
