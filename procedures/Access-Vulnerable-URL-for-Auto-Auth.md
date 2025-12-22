---
id: proc-uuid-1-1991214
tags:
  - access-control
  - auth-bypass
  - oracle-apex
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
updated_at: '2025-12-14T17:29:56.801Z'
skill_level: beginner
impact_level: critical
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Vulnerable-URL-for-Auto-Auth

## Summary

This procedure exploits improper access control in an Oracle APEX web application by directly accessing a specific URL that triggers automatic authentication as an administrative user, granting immediate elevated privileges without requiring any credentials.

## Description

In the context of a U.S. Department of Defense web application, the vulnerability stems from a lack of proper authentication checks on certain URL parameters. Visiting `https://███.mil/apexcrrel/f?p=150:24:23467499301323::NO:::` creates a session and logs in the user as 'ben auto log user', an admin account. This allows attackers to perform critical actions such as uploading files, viewing historical submissions from 2012 onward, managing users (including adding admins), sending spam emails, and using admin tools to publish or remove data. The root cause is likely hardcoded session creation or unvalidated URL parameters in the Oracle APEX framework, compromising the application's integrity, confidentiality, and availability.

## Requirements

1. Web browser with internet access
2. Knowledge of the target URL (publicly accessible .mil domain)
3. No authentication tokens or prior sessions needed

## Defense

Defensive measures and detection strategies:

- Implement strict URL parameter validation and authentication checks on all endpoints
- Use session management best practices, such as requiring explicit login for admin pages
- Monitor access logs for anomalous direct URL accesses without prior authentication events
- Apply web application firewalls (WAF) to block suspicious parameter patterns in Oracle APEX apps

## Objectives

1. Gain unauthorized administrative access to the target application
2. Establish a persistent session for further exploitation
3. Enable data exfiltration and manipulation without detection

## Instructions

### Step 1: Navigate to Vulnerable URL

**Context**: Directly access the URL to trigger the auto-authentication mechanism, exploiting the lack of validation.

No specific command required; use a standard web browser.

Open your browser and enter the following URL:

```
https://███.mil/apexcrrel/f?p=150:24:23467499301323::NO:::
```

> This URL's parameters (e.g., p=150:24:23467499301323) bypass authentication, logging you in as 'ben auto log user'. Successful execution loads the admin interface without login prompts.

### Step 2: Confirm Session Establishment

**Context**: Verify that the session is active and privileges are granted by observing the page behavior.

No command; inspect the loaded page.

Look for immediate redirection to the application dashboard and absence of credential prompts.

> Expected behavior: The page renders with admin features visible, confirming the exploit success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[access-control]]
- [[auth-bypass]]
- [[oracle-apex]]
