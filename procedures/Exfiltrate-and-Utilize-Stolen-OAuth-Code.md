---
id: proc-uuid-3
tags:
  - token-exfiltration
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:24:38.973Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Exfiltrate-and-Utilize-Stolen-OAuth-Code

## Summary

This procedure captures the OAuth authorization code from the referer header sent to the attacker's server and exchanges it for access tokens to achieve account takeover.

## Description

Upon img load, the victim's browser sends a GET request to the attacker's domain with the referer header containing the OAuth code. The attacker logs this, extracts the code, and immediately POSTs it to Facebook's token endpoint (https://graph.facebook.com/vXX/oauth/access_token) along with client_id, redirect_uri, and client_secret (if known or phished). Successful exchange yields an access_token for impersonating the user on Rockstar's services.

## Requirements

1. Server logging referer headers from incoming requests
2. Knowledge of the target's OAuth client_id and redirect_uri (from site inspection)
3. Access to Facebook app credentials or ability to replay the code

## Defense

Defensive measures and detection strategies:

- Use short-lived OAuth codes with state parameters for validation
- Implement PKCE for OAuth flows to prevent code interception
- Monitor for anomalous token exchanges from unknown IPs

## Objectives

1. Collect and parse leaked authorization codes
2. Convert codes to persistent access tokens
3. Enable unauthorized account actions or data access

## Instructions

### Step 1: Set Up Exfiltration Endpoint

**Context**: Prepare server to log referer headers.

Configure a simple HTTP server (e.g., using Python's http.server) on your domain to log all incoming requests, focusing on the Referer header.

### Step 2: Extract OAuth Code from Logs

**Context**: Parse the referer URL for the code parameter.

Review server access logs for entries like GET /steal HTTP/1.1 with Referer: https://support.rockstargames.com/?code=ABC123DEF. Extract code=ABC123DEF.

> Use regex or manual inspection to isolate the code.

### Step 3: Exchange Code for Access Token

**Context**: Replay the code at Facebook's endpoint.

Send a POST request: client_id=ROCKSTAR_APP_ID&client_secret=SECRET&redirect_uri=TARGET_URI&code=EXTRACTED_CODE&grant_type=authorization_code.

> Expected: Response with access_token; test by querying user info via Graph API.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[token-exfiltration]]
- [[account-takeover]]
