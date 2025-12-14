---
id: proc-redirect-internal-ssrf
tags:
  - ssrf
  - redirect
  - internal-access
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T04:08:46.070Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
---
# Respond-with-Redirect-to-Internal-Endpoint

## Summary

This procedure responds to the intercepted request with a 302 redirect to internal endpoints, exploiting SSRF to leak responses from ports like 80, 8080, or 22, and potentially cloud metadata.

## Description

GitLab follows the redirect without validation, making requests to 127.0.0.1 or cloud metadata services (e.g., AWS IMDS at 169.254.169.254). The leaked content appears in GitLab UI error messages. Target: Internal services. Prerequisites: Intercepted request. Outcome: Arbitrary internal POST access, enabling further attacks like command execution.

## Requirements

1. Ability to craft HTTP responses on the attacker server
2. Knowledge of target internal ports/services
3. Access to observe GitLab UI

## Defense

Defensive measures and detection strategies:

- Implement redirect validation in HTTP clients (e.g., block localhost/private IPs)
- Monitor for internal requests from application servers
- Use network segmentation to isolate metadata services

## Objectives

1. Force GitLab to request internal resources
2. Leak service responses via UI
3. Access cloud metadata for privilege escalation

## Instructions

### Step 1: Craft 302 Response

**Context**: Send a redirect to an internal target.

Respond: HTTP/1.1 302 Found\r\nLocation: http://127.0.0.1:80\r\nConnection: Close\r\nContent-Length: 0

> Use server response; vary Location for ports like :8080 or :22.

### Step 2: Observe Leaked Response

**Context**: Check GitLab UI for error message containing internal content.

Refresh the integration settings page.

> Expected output: Error displays response from internal service (e.g., web server on port 80 or SSH banner on 22).

### Step 3: Target Cloud Metadata

**Context**: Redirect to instance metadata for exfiltration.

Use Location: http://169.254.169.254/latest/meta-data/ (for AWS IMDS).

> Expected output: Metadata leaked in UI, potentially including IAM roles for RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[System Information Discovery]] System Information Discovery

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[ssrf]]
- [[redirect]]
- [[internal-access]]
