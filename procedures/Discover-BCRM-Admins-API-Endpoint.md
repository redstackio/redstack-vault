---
tags:
  - api-discovery
  - recon
  - bcrm
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
updated_at: '2025-12-14T17:32:48.286Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ec81a318-9e8b-4086-9b5c-15c025e7cfd2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover-BCRM-Admins-API-Endpoint

## Summary

This procedure identifies the publicly accessible /admins API endpoint in BCRM services, which is intended for inviting regular admins but lacks proper validation, enabling further exploitation.

## Description

In the context of BCRM (Business Communication and Relationship Management) integrated with LINE Official Account, the /admins endpoint is exposed publicly to allow customer invitations. Attackers can discover this by reviewing API documentation, testing common paths, or using network reconnaissance. No authentication is required, making it a low-hanging fruit for identifying access control weaknesses. Successful discovery confirms the endpoint's vulnerability to unauthorized admin creation.

## Requirements

1. Network access to the target BCRM instance
2. Basic knowledge of REST APIs and HTTP methods
3. HTTP client like curl or browser developer tools

## Defense

Defensive measures and detection strategies:

- Implement API gateway with rate limiting and authentication on all endpoints
- Monitor API logs for anomalous GET requests to admin paths
- Use web application firewalls (WAF) to block unauthenticated access attempts

## Objectives

1. Locate and verify the /admins endpoint's public accessibility
2. Gather details on its intended functionality for invitation
3. Prepare for exploitation by understanding response schema

## Instructions

### Step 1: Probe for the /admins Endpoint

**Context**: Send a simple GET request to check if the endpoint is publicly accessible and retrieve any descriptive information.

**Command** (using curl):
```bash
curl -X GET https://target-bcrm-instance.com/admins -v
```

> This command performs a verbose GET request. Expected output includes HTTP 200 status and details about admin management, confirming no auth checks.

### Step 2: Analyze Response for Vulnerabilities

**Context**: Inspect the response to identify invitation features and lack of role restrictions.

No specific command; manually review the JSON response for fields like email, role, or invite options.

> Look for indications that the endpoint supports POST for creation without super-admin validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- api-discovery
- recon
- bcrm
