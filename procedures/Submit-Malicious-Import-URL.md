---
id: proc-gitlab-submit-url-001
tags:
  - ssrf
  - gitlab
  - url-injection
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
updated_at: '2025-12-14T04:08:47.805Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Malicious-Import-URL

## Summary

This procedure involves submitting a specially crafted URL in GitLab's 'Repo by URL' import to trigger SSRF, directing requests to localhost or internal addresses.

## Description

The GitLab import feature fetches the provided URL without validating against localhost or internal IPs, allowing SSRF. An attacker with project creation access can submit URLs like `http://localhost:<port>` to proxy requests through the GitLab server to internal services. This targets web-based GitLab instances where backend services are bound to local interfaces on non-standard ports.

## Requirements

1. Access to the configured 'Repo by URL' import interface from Step 1
2. Knowledge of target internal ports/services (e.g., via prior recon)
3. Valid GitLab session

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all import URLs to block private IPs (RFC 1918) and localhost
- Use network segmentation to isolate GitLab from internal services
- Log and alert on import attempts with internal destinations

## Objectives

1. Trigger GitLab to make an internal request on behalf of the attacker
2. Bypass external firewall restrictions
3. Confirm SSRF vector for further interaction

## Instructions

### Step 1: Craft the Malicious URL

**Context**: Identify a vulnerable internal endpoint and format the URL to target it.

Construct a URL such as `http://127.0.0.1:8080` or `http://localhost:3000/internal` based on known local services.

> Ensure the URL mimics a git repo URL if needed, but GitLab fetches it directly.

### Step 2: Submit and Monitor

**Context**: Enter the URL in the import form and observe the backend request.

In the 'Repo by URL' field, paste the malicious URL and click 'Create project'. Check the import job status or error messages for signs of internal access.

> Errors may reveal internal service responses, confirming successful SSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- gitlab
- url-injection
