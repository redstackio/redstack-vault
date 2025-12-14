---
id: proc-acronis-extract-data
tags:
  - data-exfiltration
  - idor
  - collection
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-acronis-lead-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:32:29.032Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Extract User Data via Acronis IDOR Endpoint

## Summary

This procedure retrieves private business user information from the exploited Acronis API endpoint using a validly guessed token, exposing sensitive details without authentication.

## Description

Once a correct integer is brute-forced, the /api/v1/lead/ endpoint returns JSON with company names, usernames, surnames, telephone numbers, and other registration data. This affects multiple account types, including Cyber Cloud, due to absent authorization checks.

## Requirements

1. Valid modified token URL from brute-force
2. Tool for API requests (e.g., curl or browser)
3. Storage for exfiltrated data

## Defense

Defensive measures and detection strategies:

- Add JWT or session-based auth to API endpoints
- Encrypt sensitive fields and log access attempts
- Use WAF rules to block anomalous API patterns

## Objectives

1. Access unauthorized user profiles
2. Collect and exfiltrate private information
3. Demonstrate impact of IDOR on business data

## Instructions

### Step 1: Access Valid Endpoint

**Context**: Use the successful token to query the lead.

Navigate to or request the modified URL.

> Ensure the lead ID matches the token context.

### Step 2: Fetch and Parse Data

**Context**: Retrieve the response containing user details.

Execute [[commands/curl-acronis-lead-request]] on the valid token:

```bash
curl -X GET "https://www.acronis.com/en-us/api/v1/lead/id:929-HVV-335&token:_mch-acronis.com-<timestamp>-84755"
```

> Expected output: JSON with fields like {"company": "Example Inc.", "username": "user", "surname": "Doe", "telephone": "123-456-7890"}.

### Step 3: Document Exfiltration

**Context**: Save and review the stolen data for impact assessment.

Parse the JSON and note sensitive elements.

> Success: Private info from unrelated accounts obtained.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used

- [[commands/curl-acronis-lead-request]]

## Tools Used


## Tags

- data-extraction
- user-enumeration
