---
tags:
  - idor
  - privilege-escalation
  - backdoor
  - shopify
  - access-control-bypass
type: attack_chain
tools:
  - '[[tools/Browser-Developer-Tools]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Persistence]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Create-POS-User-via-Stocky-App-Login]]'
  - '[[procedures/Extract-POS-User-ID-from-Users-Management]]'
  - '[[procedures/Access-Hidden-Edit-Endpoint-for-POS-User]]'
  - '[[procedures/Modify-POS-User-Email-to-Attacker-Controlled]]'
  - '[[procedures/Intercept-Save-Request-and-Inject-Admin-Flag]]'
step_count: 5
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:28:59.149Z'
description: >-
  An administrator exploits a hidden edit endpoint in the Stocky Shopify app to
  elevate a POS user's privileges to admin, creating a persistent backdoor
  account for regaining access post-revocation.
skill_level: intermediate
impact_level: high
id: 6dbf36bb-0f0e-4016-af41-0788fc1bf4a6
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Stocky App Backdoor Admin Creation via POS User Privilege Escalation

Multi-stage attack chain demonstrating privilege escalation in the Stocky Shopify app by exploiting an undocumented edit endpoint to modify a POS user's role to admin, enabling persistent backdoor access even after original admin revocation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create POS User] --> B[Extract User ID]
    B --> C[Access Edit Endpoint]
    C --> D[Modify Email]
    D --> E[Inject Admin Flag]
    E --> F[Backdoor Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Browser-Developer-Tools]]
- [[tools/Burp-Suite]]

### Target Environment

- Shopify-integrated web application (Stocky App)
- Required services: Shopify API, Stocky backend
- Network access: Direct browser access to https://stocky.shopifyapps.com

### Initial Access Requirements

- Valid Stocky App Administrator credentials
- Access to Point of Sale (POS) mobile application
- No prior revocation of admin role

## Detailed Attack Procedures

### Step 1: Create POS User
procedure: [[procedures/Create-POS-User-via-Stocky-App-Login]]

**Objective**: Establish a base POS user account in the Stocky backend for subsequent manipulation.

**Instructions**: Log into the Stocky App directly from the POS mobile application to trigger automatic user creation.

**Expected Output**: A new POS User entry appears in the Stocky App's users list upon backend verification.

**Success Indicators**:
- POS User listed in https://stocky.shopifyapps.com/preferences/users
- User ID becomes available for extraction

### Step 2: Extract User ID
procedure: [[procedures/Extract-POS-User-ID-from-Users-Management]]

**Objective**: Identify the specific user_id of the created POS User for targeting the edit endpoint.

**Instructions**: As an admin, navigate to the users management page and use browser tools to inspect the delete button for the POS User, revealing the user_id in the URL or attributes.

**Expected Output**: Numeric user_id value, e.g., 12345, extracted from HTML.

**Success Indicators**:
- User ID visible in developer console or element inspector
- No errors on page load

### Step 3: Access Edit Endpoint
procedure: [[procedures/Access-Hidden-Edit-Endpoint-for-POS-User]]

**Objective**: Reach the undocumented edit page for the POS User without standard UI controls.

**Instructions**: Construct the URL https://stocky.shopifyapps.com/users/{user_id}/edit using the extracted ID and open it in the browser.

**Expected Output**: Edit form loads for the POS User, allowing field modifications.

**Success Indicators**:
- Form page accessible without 404 or auth errors
- User details pre-populated in form

### Step 4: Modify Email
procedure: [[procedures/Modify-POS-User-Email-to-Attacker-Controlled]]

**Objective**: Update the POS User's email to one under attacker control for potential password resets or login.

**Instructions**: In the loaded edit form, change the email field to an attacker-owned address, optionally retaining the original name for legitimacy.

**Expected Output**: Email field updated in the form preview.

**Success Indicators**:
- Email change reflected in form without validation errors
- Form remains submittable

### Step 5: Inject Admin Flag
procedure: [[procedures/Intercept-Save-Request-and-Inject-Admin-Flag]]

**Objective**: Bypass restrictions by adding an unauthorized admin parameter during form submission to elevate privileges.

**Instructions**: Submit the form while intercepting the POST request with a proxy tool, then append 'user[admin]=1' to the payload before forwarding.

**Expected Output**: User updated successfully with admin role; verifiable by logging in with new credentials.

**Success Indicators**:
- No backend rejection of the admin flag
- Elevated user can access admin-only features post-save

## Attack Chain Summary

### Key Achievements

1. Creation of a modifiable POS User account
2. Access to hidden endpoint for unauthorized edits
3. Privilege escalation to admin via payload manipulation
4. Persistent backdoor for regaining access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Manipulation]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]
- [[Persistence]]

---

*Last updated: 2024-01-01T00:00:00Z*
