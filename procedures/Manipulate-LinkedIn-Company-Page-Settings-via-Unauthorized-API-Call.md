---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Manipulate-LinkedIn-Company-Page-Settings-via-Unauthorized-API-Call
tags:
  - linkedin
  - api
  - access-control
  - dos
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-linkedin-api-manipulate]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:56.903Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manipulate-LinkedIn-Company-Page-Settings-via-Unauthorized-API-Call

## Summary

This procedure exploits improper access control in LinkedIn's Voyager API to send unauthorized POST requests that modify Lead Gen Form visibility on company pages, denying page admins the ability to enable or disable these forms and disrupting administrative functions.

## Description

The vulnerability stems from a lack of proper authorization checks in the POST /voyager/api/voyagerOrganizationDashCompanies/{id} endpoint, allowing any authenticated user (without admin privileges) to alter company page settings. In an attack scenario, the adversary authenticates to LinkedIn, identifies a target company ID, and submits a JSON payload to disable Lead Gen Form visibility. This prevents legitimate admins from managing these features, potentially halting lead generation efforts. The target environment is LinkedIn's web platform, requiring only a standard browser session for authentication. Expected outcomes include successful API modification and admin denial of access, verifiable by admin login attempts.

## Requirements

1. Valid LinkedIn authentication (session cookies or API tokens from a non-admin account)
2. Target company ID (obtainable from LinkedIn company page URLs, e.g., /company/{id})
3. Network access to LinkedIn's API over HTTPS
4. HTTP client like curl for sending requests

## Defense

Defensive measures and detection strategies:

- Implement strict authorization checks on API endpoints to validate user permissions for company-specific modifications
- Monitor API logs for anomalous POST requests to /voyager/api/voyagerOrganizationDashCompanies/{id} from non-admin users
- Use rate limiting and anomaly detection on company page API calls to identify unauthorized manipulations
- Regularly audit access logs for changes to Lead Gen Form settings

## Objectives

1. Bypass access controls to modify company page features without authorization
2. Deny admins control over Lead Gen Forms to disrupt business operations
3. Demonstrate API vulnerability for reporting or exploitation

## Instructions

### Step 1: Authenticate and Gather Target ID

**Context**: Obtain a valid LinkedIn session and identify the company ID to target.

Log in to LinkedIn via browser, extract session cookies (e.g., JSESSIONID, li_at). Navigate to the target company page and note the ID from the URL (e.g., https://www.linkedin.com/company/{id}).

**Expected Output**: Session cookies and company ID.

### Step 2: Send Manipulative POST Request

**Context**: Use the API endpoint to submit a payload that disables Lead Gen Form visibility.

**Command** ([[commands/curl-linkedin-api-manipulate]]):
```bash
curl -X POST 'https://www.linkedin.com/voyager/api/voyagerOrganizationDashCompanies/{id}' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: JSESSIONID=your_session; li_at=your_li_at_token' \
  -d '{"leadGenFormsVisibility": "disabled"}'
```

> This command sends a POST request with a JSON payload setting visibility to disabled. Replace {id} with the company ID and insert real session cookies. On success, the API processes the change without error, altering the settings. Verify by checking the company page as an admin.

**Expected Output**: HTTP 200 response with updated settings confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-linkedin-api-manipulate]]

## Tools Used


## Tags

- [[linkedin]]
- [[api]]
- [[access-control]]
- [[dos]]
