---
id: ac-uuid-001
tags:
  - privilege-escalation
  - api-vulnerability
  - authorization-bypass
  - linkedin
  - voyager-api
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-LinkedIn-Company-Admin-Tools]]'
  - '[[procedures/Intercept-Voyager-API-Request]]'
  - '[[procedures/Modify-Request-for-Analyst-Privileges]]'
  - '[[procedures/Execute-Modified-Request-and-Analyze-Response]]'
step_count: 4
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:07.508Z'
description: >-
  Demonstrates privilege escalation vulnerability in LinkedIn's Voyager API
  where an Analyst role user can access sensitive company email domain mappings
  restricted to higher privileges by modifying intercepted API requests.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
---
# Privilege Escalation in LinkedIn Voyager API Allowing Analyst Access to Company Email Domains

Multi-stage attack chain demonstrating a complete privilege escalation workflow in LinkedIn's Voyager API, enabling lower-privileged users (Analyst role) to access sensitive company email domain mappings.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Login and Navigate] --> B[Discovery: Intercept API]
    B --> C[Privilege Escalation: Modify Credentials]
    C --> D[Collection: Access Sensitive Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform (LinkedIn.com)
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to LinkedIn

### Initial Access Requirements

- Valid LinkedIn account with access to a company page (e.g., admin or member)
- Second account with Analyst role privileges
- Network position: Direct internet access
- Prior access needed: None, but company affiliation helpful

## Detailed Attack Procedures

### Step 1: Access Company Admin Tools
procedure: [[procedures/Access-LinkedIn-Company-Admin-Tools]]

**Objective**: Gain initial access to the company's admin section to trigger the vulnerable API endpoint.

**Instructions**: Log in to LinkedIn with a test account that has company access. Navigate to the company management section and access Admin Tools for Employee Verification.

**Expected Output**: Page loads with Employee Verification interface, triggering the initial API request.

**Success Indicators**:
- Company page accessible
- Admin Tools menu visible
- API request observed in proxy

### Step 2: Intercept Voyager API Request
procedure: [[procedures/Intercept-Voyager-API-Request]]

**Objective**: Capture the legitimate API request to the Voyager endpoint using a proxy tool.

**Instructions**: Configure your browser to route traffic through Burp Suite. Navigate to Employee Verification to trigger the GET request to /voyager/api/voyagerOrganizationDashEmailDomainMappings.

**Expected Output**: Intercepted HTTP GET request with full headers, including cookies and CSRF token.

**Success Indicators**:
- Request captured in Burp Suite
- Parameters like company URN visible
- Response contains email domain data (for higher-priv user)

### Step 3: Modify Request for Analyst Privileges
procedure: [[procedures/Modify-Request-for-Analyst-Privileges]]

**Objective**: Alter the request to use credentials from a lower-privileged Analyst account, bypassing authorization checks.

**Instructions**: In Burp Suite, replace the Cookie header and CSRF-Token with values from an Analyst session. Keep the URL and other parameters intact.

**Expected Output**: Modified request ready for forwarding.

**Success Indicators**:
- Cookies and CSRF token updated to Analyst values
- No syntax errors in modified request

### Step 4: Execute Modified Request and Analyze Response
procedure: [[procedures/Execute-Modified-Request-and-Analyze-Response]]

**Objective**: Send the tampered request and retrieve unauthorized sensitive data.

**Instructions**: Forward the modified request in Burp Suite and inspect the JSON response for email domain mappings.

**Expected Output**: JSON array listing approved email domains, disclosing internal verification configs.

**Success Indicators**:
- HTTP 200 response
- Response contains sensitive email domains not visible in UI
- Data matches higher-priv access

## Attack Chain Summary

### Key Achievements

1. Bypassed UI restrictions to access hidden API data
2. Demonstrated privilege escalation from Analyst to effective admin-level access
3. Exposed company email verification configurations

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
