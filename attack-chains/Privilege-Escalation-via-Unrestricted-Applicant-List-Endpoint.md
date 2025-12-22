---
id: ac-877300-priv-esc
tags:
  - privilege-escalation
  - broken-access-control
  - unauthorized-access
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Unrestricted-Applicant-List-Endpoint]]'
step_count: 1
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:35.975Z'
description: >-
  A multi-stage attack demonstrating privilege escalation in a web application
  by exploiting an endpoint that fails to enforce department-specific
  permissions, allowing unauthorized access to sensitive applicant data across
  the organization.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
---
---
id: ac-877300-priv-esc
name: Privilege Escalation via Unrestricted Applicant List Endpoint
type: attack_chain
description: A multi-stage attack demonstrating privilege escalation in a web application by exploiting an endpoint that fails to enforce department-specific permissions, allowing unauthorized access to sensitive applicant data across the organization.
verified: false
submitted: false
step_count: 1
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: [[procedures/Access-Unrestricted-Applicant-List-Endpoint]]
techniques: [[Exploitation for Privilege Escalation]], [[Valid Accounts]]
tactics: [[Privilege Escalation]]
tags: privilege-escalation, broken-access-control, unauthorized-access
platforms: Web
tools: []
complexity: low
skill_level: intermediate
impact_level: high
---

# Privilege Escalation via Unrestricted Applicant List Endpoint

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access] --> B[Privilege Escalation]
    B --> C[Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#3498db
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[tools/curl]]

### Target Environment

- Web application platform (e.g., Lark Technologies HR system)
- Authenticated access to the application
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Valid user credentials for a single-department account
- Network access to the web application
- No prior elevated access needed

## Detailed Attack Procedures

### Step 1: Authenticate and Access Vulnerable Endpoint
procedure: [[procedures/Access-Unrestricted-Applicant-List-Endpoint]]

**Objective**: Gain unauthorized access to applicant data from all departments using a low-privilege account.

**Instructions**: Authenticate into the web application using a user account limited to a single department. Then, navigate to or request the applicant list endpoint, which fails to enforce department-specific checks.

Use [[commands/curl-authenticated-get]] to simulate the request:

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" https://target-app.com/api/applicants
```

**Expected Output**: JSON response containing pending approval requests, email addresses, and phone numbers from all departments, not just the user's department.

**Success Indicators**:
- Response includes data from multiple departments
- Sensitive information (emails, phones) visible for unauthorized applicants

## Attack Chain Summary

### Key Achievements

1. Successful authentication with low-privilege account
2. Bypassed department permission checks to access global applicant data
3. Exposed sensitive personal information across the organization

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
