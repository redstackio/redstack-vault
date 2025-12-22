---
tags:
  - oauth
  - referer-leakage
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 42fa03b0-5a72-42bf-843e-6aa65840bd65
created_at: '2025-12-14T17:24:35.792Z'
updated_at: '2025-12-14T17:24:35.792Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Referer-Leakage-in-SocialClub-Facebook-OAuth-Flow

## Summary

This procedure exploits the lack of referer policy enforcement in Rockstar Games' SocialClub Facebook OAuth flow, causing the authorization code to be leaked in the referer header during the callback, enabling potential token theft.

## Description

In the OAuth 2.0 flow, after user authentication on Facebook, the browser redirects back to SocialClub with an authorization code in the query parameters. Due to missing Referrer-Policy headers or meta tags, this code is included in the referer header when subsequent requests are made, exposing it to third-party sites. This was identified in HackerOne report #342709, where a POC demonstrated the leakage. The target environment is the web-based SocialClub platform, requiring only a browser to initiate the login. Expected outcome is interception of the code, which can then be exchanged for an access token via Facebook's API.

## Requirements

1. Access to a web browser with network inspection capabilities (e.g., Chrome DevTools).
2. Valid SocialClub account to initiate login.
3. Network connectivity to socialclub.rockstargames.com and developers.facebook.com.

## Defense

Defensive measures and detection strategies:

- Implement strict Referrer-Policy: 'strict-origin-when-cross-origin' on OAuth endpoints.
- Monitor for anomalous referer headers in logs containing OAuth codes.
- Use short-lived authorization codes and validate referers server-side.

## Objectives

1. Expose the Facebook OAuth authorization code in the referer header.
2. Capture the leaked code for further exploitation.
3. Gain unauthorized access to linked Facebook accounts.

## Instructions

### Step 1: Initiate Facebook OAuth Login

**Context**: Start the authentication flow to trigger the callback where leakage occurs.

Navigate to the SocialClub login page and select Facebook login. This redirects to Facebook's OAuth endpoint (`https://www.facebook.com/vXX.X/dialog/oauth?client_id=...&redirect_uri=...`). Complete authentication on Facebook to receive the code in the redirect back to SocialClub.

**Expected Output**: Browser redirects to `https://socialclub.rockstargames.com/auth/facebook/callback?code=ABC123...`.

### Step 2: Inspect and Capture Referer Leakage

**Context**: Monitor the network request during the callback to observe the referer header.

Open browser developer tools (F12 > Network tab). Reload or trigger a sub-request (e.g., load an image) from the callback page. The referer will include the full callback URL with the code.

For advanced capture, proxy traffic through Burp Suite:

- Set browser proxy to 127.0.0.1:8080.
- Filter for requests to socialclub.rockstargames.com.
- Observe referer in intercepted HTTP headers.

**Expected Output**: HTTP request headers showing `Referer: https://socialclub.rockstargames.com/auth/facebook/callback?code=leaked_code_here`.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth]]
- [[referer-leakage]]
- [[information-disclosure]]
