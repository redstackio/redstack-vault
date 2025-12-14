---
id: proc-mtn-register-admin-001
tags:
  - access-control
  - admin-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.318Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register Unauthorized Admin via Hidden Endpoint

## Summary

This procedure exploits a hidden registration endpoint in the MTN Group web application to create an unauthorized admin account, bypassing the lack of visible UI registration and any intended access restrictions.

## Description

The MTN Group application features a concealed endpoint for admin signup that lacks proper authentication checks or authorization gating, allowing public access despite the portal being intended for internal use only. By sending a crafted registration request, an attacker can establish a new admin account, enabling subsequent full administrative privileges. This occurs in a web environment targeting merchant management services.

## Requirements

1. Public internet access to the target application
2. Web browser or HTTP client (e.g., curl or Postman)
3. Basic knowledge of HTTP POST requests

## Defense

Defensive measures and detection strategies:

- Implement endpoint gating with IP whitelisting or CAPTCHA for registration
- Remove or secure hidden endpoints not intended for public use
- Monitor for anomalous registration attempts via logs

## Objectives

1. Create a new admin account without authorization
2. Establish initial access to the admin portal
3. Enable escalation to full data manipulation

## Instructions

### Step 1: Identify and Access Hidden Endpoint

**Context**: Locate the hidden registration endpoint through application exploration, such as reviewing network traffic or API documentation leaks.

No specific command; use browser developer tools to inspect or directly POST to the endpoint (e.g., /api/admin/register).

> Send a POST request with JSON payload including username, email, password, and role set to 'admin'. Expected output: 201 Created response with account details.

### Step 2: Submit Registration Data

**Context**: Craft and submit the registration payload to create the account.

Example using curl (inferred for reproducibility):

```bash
curl -X POST https://target-app.com/api/admin/register \
  -H "Content-Type: application/json" \
  -d '{"username":"attacker_admin","email":"attacker@example.com","password":"strongpass123","role":"admin"}'
```

> Successful response includes a confirmation message or token. Failure indicates endpoint protection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[access-control]]
- [[web-vuln]]
