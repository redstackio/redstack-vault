---
tags:
  - cors
  - headers
  - inspection
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:20.447Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: e50beb7f-600d-4794-86d4-b9be96c6b3f1
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
---
# Inspect-Response-Headers-for-CORS-Policy

## Summary

This procedure examines HTTP response headers from the WordPress REST API to confirm a permissive CORS configuration that enables cross-origin credentialed requests.

## Description

Permissive CORS headers like Access-Control-Allow-Origin: * and Access-Control-Allow-Credentials: true allow any domain to access the API with user cookies, leading to potential data leakage. This step follows POC testing and uses browser tools to validate the misconfiguration, providing evidence for the vulnerability.

## Requirements

1. Browser with developer tools (e.g., Chrome DevTools)
2. Active POC or direct access to the endpoint
3. Basic understanding of HTTP headers

## Defense

Defensive measures and detection strategies:

- Audit and harden CORS headers using server configuration (e.g., Apache/Nginx)
- Use security plugins like Wordfence to enforce strict policies
- Regularly scan for misconfigurations with tools like OWASP ZAP

## Objectives

1. Identify unsafe CORS settings
2. Document headers for vulnerability reporting
3. Assess risk of cross-origin attacks

## Instructions

### Step 1: Trigger the Request

**Context**: Perform a request to the endpoint using the POC or direct access to generate response headers.

Load the POC HTML or use curl with verbose output.

```bash
curl -v https://lonestarcell.com/wp-json/wp/v2/users/
```

> The -v flag shows headers. Look for CORS-related lines in the output.

### Step 2: Inspect in Browser

**Context**: Use developer tools to view full headers post-request.

In Chrome: Open DevTools > Network tab > Select the request > Headers tab.

> Expected: Access-Control-Allow-Origin: *, Access-Control-Allow-Credentials: true. These indicate the misconfiguration allowing arbitrary origins.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[headers]]
- [[inspection]]
- [[cors]]
