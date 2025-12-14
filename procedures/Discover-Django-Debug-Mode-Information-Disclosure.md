---
id: 123e4567-e89b-12d3-a456-426614174001
tags:
  - django
  - debug-mode
  - information-disclosure
  - misconfiguration
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-trigger-error]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Client Configurations]]'
updated_at: '2025-12-14T17:25:22.816Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Client Configurations]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174001
name: Discover-Django-Debug-Mode-Information-Disclosure
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Reconnaissance]], [[Collection]]
techniques: [[Gather Victim Host Information]], [[Client Configurations]]
sub_techniques: []
tags: django, debug-mode, information-disclosure, misconfiguration, reconnaissance
commands: [[commands/curl-trigger-error]]
platforms: Web
tools: []
---

# Discover-Django-Debug-Mode-Information-Disclosure

## Summary

This procedure outlines the detection of Django applications running with debug mode enabled in a production environment, which exposes sensitive information such as stack traces, configuration variables, installed packages, and source code snippets. It was used to identify a misconfiguration on api.wwm-dev.autodesk.com, rated medium severity (CVSS 5.3), allowing reconnaissance without authentication.

## Description

Django's debug mode, when enabled (DEBUG=True in settings.py), provides verbose error pages for development but poses a security risk in production by leaking internal details. This procedure involves passive or active probing of web subdomains to trigger error responses and inspect for debug output. In the Autodesk case, reconnaissance revealed the api.wwm-dev.autodesk.com subdomain running Django with debug activated, disclosing potential paths to source code and configs. Prerequisites include public access to the target; no exploits are needed, just error induction. Expected outcomes: Confirmation of exposure and reportable vulnerability.

## Requirements

1. Public network access to the target subdomain (e.g., https://api.wwm-dev.autodesk.com)
2. HTTP client like curl or a web browser
3. Basic understanding of HTTP status codes and error pages

## Defense

Defensive measures and detection strategies:

- Ensure DEBUG=False in production Django settings and use ALLOWED_HOSTS properly
- Implement web application firewall (WAF) to block error page exposure
- Monitor server logs for 500 errors triggered by invalid requests
- Regular vulnerability scanning for debug mode on public-facing apps

## Objectives

1. Identify Django-based endpoints with debug mode enabled
2. Extract and document disclosed information for reporting
3. Assess impact on confidentiality of internal configurations

## Instructions

### Step 1: Probe for Django Presence

**Context**: Send a basic request to the suspected subdomain to confirm Django is in use, looking for characteristic headers or responses.

**Command** ([[commands/curl-trigger-error]]):
```bash
curl -v -H "User-Agent: Mozilla/5.0" "https://api.wwm-dev.autodesk.com/"
```

> This command performs a HEAD-like verbose request to the root path. Expected output includes Django-specific headers like Server: gunicorn or X-Frame-Options, confirming the framework.

### Step 2: Trigger Error to Expose Debug Info

**Context**: Request an invalid endpoint to force a 500 Internal Server Error, revealing the debug page if enabled.

**Command** ([[commands/curl-trigger-error]]):
```bash
curl -v "https://api.wwm-dev.autodesk.com/invalid_endpoint"
```

> This induces a TemplateDoesNotExist or similar error. Successful execution shows a detailed HTML page with yellow debug styling, stack traces, installed apps list (e.g., django.contrib.admin), and settings excerpts. In the Autodesk report, this exposed paths like /app/wwm/ and package versions.

### Step 3: Analyze and Document Disclosure

**Context**: Review the response for sensitive data and assess severity.

No specific command; manually inspect output for elements like DEBUG=True, SQL queries, or file paths. Document findings for disclosure report.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Collection]] Collection

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Client Configurations]] Client Configurations

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-trigger-error]]

## Tools Used

- None

## Tags

- [[django]]
- [[debug-mode]]
- [[information-disclosure]]
- [[misconfiguration]]
- [[Reconnaissance]]
