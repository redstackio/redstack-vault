---
tags:
  - privilege-escalation
  - shopify
  - oauth
  - google-apps
  - web
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Bypass-Shopify-UI-Restrictions-for-Login-Services-Update]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:58.349Z'
description: >-
  Demonstrates how a shop admin can escalate privileges to enable and configure
  Google Apps OAuth login services, bypassing UI restrictions through direct API
  manipulation.
skill_level: intermediate
impact_level: high
id: 1e6a40df-4666-4f68-b857-740b9799cfdc
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploitation for Privilege Escalation]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174000
name: Shopify Privilege Escalation via Unauthorized Google Apps Login Configuration
type: attack_chain
description: "Demonstrates how a shop admin can escalate privileges to enable and configure Google Apps OAuth login services, bypassing UI restrictions through direct API manipulation."
verified: false
submitted: false
step_count: 4
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: [[procedures/Bypass-Shopify-UI-Restrictions-for-Login-Services-Update]]
techniques: [[Valid Accounts]], [[Exploitation for Privilege Escalation]]
tactics: [[Privilege Escalation]]
tags: [privilege-escalation, shopify, oauth, google-apps, web]
platforms: [Web]
tools: []
---

# Shopify Privilege Escalation via Unauthorized Google Apps Login Configuration

Multi-stage attack chain demonstrating a complete privilege escalation workflow in Shopify, allowing shop admins to modify owner-restricted external login configurations.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Admin Login] --> B[UI Observation]
    B --> C[Direct POST Bypass]
    C --> D[Verification]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or HTTP client (e.g., curl, Burp Suite)

### Target Environment

- Shopify admin panel (Web platform)
- Active shop admin account with full access
- Valid session cookies and authenticity token

### Initial Access Requirements

- Logged-in shop admin credentials
- Network access to Shopify admin URL (e.g., https://example.myshopify.com/admin)
- No prior owner access needed

## Detailed Attack Procedures

### Step 1: Log in as a Shop Admin

procedure: [[procedures/Bypass-Shopify-UI-Restrictions-for-Login-Services-Update]]

**Objective**: Gain initial access to the Shopify admin panel as a staff member with full permissions.

**Instructions**: Use admin credentials to authenticate and access the dashboard. No special commands required; perform standard login via the web interface.

**Expected Output**: Successful login to https://seclearn.myshopify.com/admin, with admin session established (cookies set).

**Success Indicators**:
- Admin dashboard loads
- User role confirmed as shop admin

### Step 2: Navigate to Settings and Observe UI Restriction

procedure: [[procedures/Bypass-Shopify-UI-Restrictions-for-Login-Services-Update]]

**Objective**: Identify the UI-level restriction on 'Login Services' to confirm the intended access control.

**Instructions**: In the admin interface, navigate to Settings > Account. Observe that the 'Login Services' section is hidden or inaccessible to admins.

**Expected Output**: UI shows restricted view; no option to modify external logins like Google Apps.

**Success Indicators**:
- 'Login Services' section not visible
- Confirms owner-only intended access

### Step 3: Send POST Request to Update Google Apps Login Settings

procedure: [[procedures/Bypass-Shopify-UI-Restrictions-for-Login-Services-Update]]

**Objective**: Bypass UI restrictions by directly calling the backend endpoint to enable and configure Google Apps OAuth.

**Instructions**: Extract session cookies and authenticity_token from the logged-in session. Then execute the following command using [[commands/shopify-update-google-apps-login-post]] to send a crafted POST request:

```bash
curl -X POST 'https://seclearn.myshopify.com/admin/login_services/google_apps/update' \
  -H 'Host: seclearn.myshopify.com' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0' \
  -H 'Cookie: ...' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'utf8=%E2%9C%93&_method=patch&authenticity_token=xxxxxPaAQQFSKgdwaJr6XWqFbBkQ%3D&shop%5Bgoogle_apps_login_enabled%5D=0&shop%5Bgoogle_apps_login_enabled%5D=1&shop%5Bgoogle_apps_domain%5D=securitylearn.net&commit=Save'
```

**Expected Output**: HTTP 200 or redirect response indicating successful update; no error on unauthorized access.

**Success Indicators**:
- Request succeeds without authorization denial
- Settings updated in backend

### Step 4: Verify the Change as Account Owner

procedure: [[procedures/Bypass-Shopify-UI-Restrictions-for-Login-Services-Update]]

**Objective**: Confirm the privilege escalation by checking the updated settings from an owner perspective.

**Instructions**: Log in as the account owner and navigate to Settings > Account > Login Services. No command needed; inspect the UI.

**Expected Output**: Google Apps integration enabled with custom domain (e.g., securitylearn.net) visible.

**Success Indicators**:
- Owner UI shows enabled OAuth for the specified domain
- Potential for unauthorized domain users to log in

## Attack Chain Summary

### Key Achievements

1. Bypassed UI restrictions using direct API calls
2. Enabled owner-only feature (Google Apps OAuth) as a shop admin
3. Configured custom domain for potential unauthorized access
4. Demonstrated high-impact privilege escalation in SaaS environment

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
