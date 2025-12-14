---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: >-
  Deny Admin Access to LinkedIn Company Page Lead Gen Forms via Unauthorized API
  Manipulation
tags:
  - linkedin
  - api
  - access-control
  - dos
  - improper-authorization
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T12:00:00Z'
procedures:
  - >-
    [[procedures/Manipulate-LinkedIn-Company-Page-Settings-via-Unauthorized-API-Call]]
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:56.908Z'
description: >-
  An attack chain exploiting improper access control in LinkedIn's API to
  manipulate Lead Gen Form visibility on company pages, denying admins the
  ability to enable or disable forms and disrupting administrative control.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Deny Admin Access to LinkedIn Company Page Lead Gen Forms via Unauthorized API Manipulation

Multi-stage attack chain demonstrating a complete attack workflow exploiting improper access control in LinkedIn's API.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via API] --> B[Manipulate Settings]
    B --> C[Deny Admin Control]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#e67e22
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- LinkedIn company page API
- Web platform with access to Voyager API endpoints
- No specific ports required (HTTPS on 443)

### Initial Access Requirements

- Valid LinkedIn session or API access (attacker must be authenticated but without admin privileges on the target company page)
- Knowledge of the target company ID
- Network access to LinkedIn's API (public internet)

## Detailed Attack Procedures

### Step 1: Manipulate Company Page Settings
procedure: [[procedures/Manipulate-LinkedIn-Company-Page-Settings-via-Unauthorized-API-Call]]

**Objective**: Send an unauthorized POST request to the LinkedIn API endpoint to modify Lead Gen Form visibility, preventing page admins from enabling or disabling the forms.

**Instructions**: Identify the target company ID (e.g., via LinkedIn URL or prior reconnaissance). Then, use [[commands/curl-linkedin-api-manipulate]] to send a POST request with payload that alters the visibility settings:

```bash
curl -X POST 'https://www.linkedin.com/voyager/api/voyagerOrganizationDashCompanies/{id}' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: JSESSIONID=your_session; li_at=your_li_at_token' \
  -d '{"leadGenFormsVisibility": "disabled"}'
```

Replace `{id}` with the actual company ID and include valid authentication cookies or tokens from a LinkedIn session. The payload disables the Lead Gen Forms visibility.

**Expected Output**: HTTP 200 OK response indicating successful update, though the attacker lacks admin rights.

**Success Indicators**:
- API returns success without authorization error
- Admins on the company page can no longer toggle Lead Gen Form settings
- Verification by logging in as an admin and attempting to edit page features

## Attack Chain Summary

### Key Achievements

1. Bypassed access controls to modify sensitive company page settings
2. Denied administrative control over Lead Gen Forms, potentially disrupting lead generation and business operations
3. Demonstrated improper authorization in LinkedIn's Voyager API

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T12:00:00Z*
