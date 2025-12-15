---
id: proc-877300-access-endpoint
tags:
  - privilege-escalation
  - broken-access-control
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-authenticated-get]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:35.960Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
---
---
id: proc-877300-access-endpoint
name: Access-Unrestricted-Applicant-List-Endpoint
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Privilege Escalation]]
techniques: [[Exploitation for Privilege Escalation]], [[Valid Accounts]]
sub_techniques: []
tags: privilege-escalation, broken-access-control
commands: [[commands/curl-authenticated-get]]
platforms: Web
tools: [[tools/curl]]
skill_level: intermediate
impact_level: high
detection_risk: low
---

# Access-Unrestricted-Applicant-List-Endpoint

## Summary

This procedure exploits a privilege escalation vulnerability in a web application's applicant list endpoint by using a valid low-privilege account from a single department to access sensitive data from all departments, bypassing authorization checks and exposing pending approvals, emails, and phone numbers.

## Description

In the context of an HR or applicant management system like Lark Technologies, the endpoint responsible for retrieving applicant lists does not properly verify the user's department permissions. An attacker with access to a legitimate but restricted account can request the full applicant dataset, leading to unauthorized disclosure of personal information. This is a classic broken access control issue, enabling horizontal privilege escalation within the application. Prerequisites include valid credentials for a department-limited user and network access to the web app. Expected outcomes include retrieval of cross-department data without errors.

## Requirements

1. Valid authentication token or session for a single-department user account
2. Network access to the target web application (HTTPS)
3. Tools like curl or a browser for making authenticated requests

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) with strict department scoping on all endpoints
- Log and monitor API requests for anomalies, such as low-priv users accessing high-volume data
- Use input validation and authorization middleware to enforce permission checks at the server level

## Objectives

1. Authenticate as a low-privilege user and retrieve unauthorized applicant data
2. Expose sensitive information like emails and phone numbers from other departments
3. Demonstrate the impact of missing permission enforcement on data privacy

## Instructions

### Step 1: Authenticate to the Application

**Context**: Obtain a valid session or token using the low-privilege account to establish authenticated access.

Log in via the web interface or API to get your bearer token. This step ensures the request is authenticated but restricted by department.

### Step 2: Request the Applicant List Endpoint

**Context**: Send a GET request to the vulnerable endpoint, which fails to check department permissions, returning data from all departments.

**Command** ([[commands/curl-authenticated-get]]):
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" https://target-app.com/api/applicants
```

> This command sends an authenticated GET request to the applicants endpoint. Expected output is a JSON array of applicant objects, including those from unauthorized departments, with fields like pending_status, email, and phone_number. If successful, the response will contain more data than expected for a single-department user.

### Step 3: Validate Unauthorized Access

**Context**: Inspect the response to confirm exposure of cross-department data.

Parse the JSON output and search for department indicators or known data from other areas. Success is indicated by presence of unfamiliar applicant details.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-authenticated-get]]

## Tools Used

- [[tools/curl]]

## Tags

- privilege-escalation
- broken-access-control
- web-application
