---
tags:
  - api-verification
  - access-token
  - oauth
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/generate-facebook-app-access-token]]'
platforms:
  - Windows
techniques:
  - '[[Credentials In Files]]'
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 204f772d-ebd3-4cdc-b95b-75c5b641e679
created_at: '2025-12-14T17:32:20.717Z'
updated_at: '2025-12-14T17:32:20.717Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Credentials In Files]]'
  - '[[Valid Accounts]]'
---
# Verify-Facebook-Credentials-with-Graph-API

## Summary

This procedure uses the extracted Facebook credentials to request an app access token via the Graph API, verifying their validity and enabling potential unauthorized modifications to the app settings.

## Description

Following credential extraction, this step employs the OAuth client credentials grant to generate a bearer token. It targets the Facebook Graph API endpoint and assumes possession of the App ID and Secret, demonstrating the impact of the hardcoded storage by allowing token generation without additional authentication.

## Requirements

1. Extracted credentials: App ID 660471650708388 and Secret 71a2d003a5ecfab4f4ad86dfb70b74e0
2. Internet access to reach graph.facebook.com
3. curl tool installed

## Defense

Defensive measures and detection strategies:

- Rotate app secrets immediately upon exposure
- Monitor API access logs for anomalous token requests
- Implement rate limiting and IP whitelisting on API endpoints

## Objectives

1. Generate a valid app access token
2. Confirm credentials functionality
3. Enable further API abuse like app setting modifications

## Instructions

### Step 1: Prepare API Request

**Context**: Construct the OAuth request using client credentials flow, with empty redirect_uri as it's not needed.

No command; note the parameters: client_id=660471650708388, client_secret=71a2d003a5ecfab4f4ad86dfb70b74e0, grant_type=client_credentials.

### Step 2: Execute Token Request

**Context**: Send the HTTP request to obtain the bearer token.

**Command** ([[commands/generate-facebook-app-access-token]]):

```bash
curl "https://graph.facebook.com/oauth/access_token?client_id=660471650708388&client_secret=71a2d003a5ecfab4f4ad86dfb70b74e0&redirect_uri=&grant_type=client_credentials"
```

> This queries the /oauth/access_token endpoint. A successful response includes the access_token, confirming the credentials work.

**Expected Output**: {"access_token":"660471650708388|jboBZgqj64W1JXIAKIbtVz24FlQ","token_type":"bearer"}

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Credentials In Files]]
- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/generate-facebook-app-access-token]]

## Tools Used

- [[tools/curl]]

## Tags

- [[api-verification]]
- [[access-token]]

