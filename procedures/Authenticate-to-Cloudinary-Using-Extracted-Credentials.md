---
tags:
  - cloudinary
  - authentication
  - api
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Cloud
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: cb09f3f5-ad89-4676-9622-edb6c39958c8
created_at: '2025-12-14T17:32:48.326Z'
updated_at: '2025-12-14T17:32:48.326Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-to-Cloudinary-Using-Extracted-Credentials

## Summary

This procedure uses extracted API credentials to perform basic authentication against the Cloudinary service, granting access to the account dashboard and enabling further operations like file management.

## Description

Cloudinary's API supports basic authentication via api_key and api_secret. In the Reverb.com case, these were hardcoded in the Android app, allowing direct use in tools like curl or a browser. Upon successful auth, the attacker accesses the 'reverb' cloud account, violating documentation that recommends keeping secrets server-side. Prerequisites: Valid credentials and network access. Outcomes include dashboard login and API endpoint usability.

## Requirements

1. Extracted api_key and api_secret from the app.
2. API client (e.g., curl, Postman) or web browser.
3. HTTPS access to api.cloudinary.com.

## Defense

Defensive measures and detection strategies:

- Rotate credentials immediately upon exposure detection.
- Enable API key restrictions (e.g., IP whitelisting) in Cloudinary settings.
- Monitor login attempts and anomalous access from non-server IPs.

## Objectives

1. Validate credentials for basic auth.
2. Gain entry to the Cloudinary dashboard.
3. Prepare for resource manipulation.

## Instructions

### Step 1: Prepare Authentication

**Context**: Format the credentials for basic auth (api_key:api_secret).

Use base64 encoding if needed, but tools like curl handle it directly.

### Step 2: Test Authentication

**Context**: Send a simple authenticated request to verify access.

Example with curl to a basic endpoint:

```bash
curl -u '434762629765715:█████' https://api.cloudinary.com/v1_1/reverb/resources
```

> Returns a list of resources if auth succeeds, or 401 error if failed.

**Expected Output**: 200 OK with account resources.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[cloudinary]]
- [[authentication]]
- [[api]]
