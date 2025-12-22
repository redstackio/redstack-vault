---
tags:
  - auth-bypass
  - openid
  - apache-airflow
  - flask-appbuilder
type: attack_chain
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
procedures:
  - '[[procedures/Access-Apache-Airflow-Login-Page]]'
  - '[[procedures/Intercept-and-Modify-OpenID-Request]]'
  - '[[procedures/Complete-Authentication-with-Arbitrary-IDP]]'
  - '[[procedures/Access-Dashboard-as-Impersonated-User]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
description: >-
  Exploits an authentication bypass in Apache Airflow's legacy OpenID 2.0 by
  using an arbitrary Identity Provider to impersonate users and gain
  unauthorized access.
skill_level: intermediate
impact_level: high
id: 81044353-1ac0-46f3-870e-5707e7970375
created_at: '2025-12-14T17:31:42.541Z'
updated_at: '2025-12-14T17:31:42.541Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Apache-Airflow-Authentication-Bypass-via-Arbitrary-OpenID-Provider

Multi-stage attack chain demonstrating a complete authentication bypass workflow in Apache Airflow using legacy OpenID 2.0.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Login Page] --> B[Modify OpenID Request]
    B --> C[Forge Authentication]
    C --> D[Access Dashboard]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Firefox or Chrome with developer tools)
- Proxy tool for request interception (e.g., Burp Suite or similar)

### Target Environment

- Apache Airflow instance with AUTH_TYPE = AUTH_OID (legacy OpenID 2.0 enabled)
- Web platform accessible over HTTP/HTTPS
- No specific ports required beyond standard web (80/443)

### Initial Access Requirements

- Network access to the Airflow login page
- Knowledge of an existing user account in Airflow
- Access to an arbitrary OpenID 2.0 Identity Provider (e.g., https://openstackid.org) that can forge responses

## Detailed Attack Procedures

### Step 1: Access the Login Page
procedure: [[procedures/Access-Apache-Airflow-Login-Page]]

**Objective**: Reach the Airflow login interface to initiate the OpenID authentication flow.

**Instructions**: Open a web browser and navigate to the Airflow instance's login URL, typically http://target-airflow.com/login/. The page should display a form with a dropdown for selecting allowed OpenID providers. Select any provider from the dropdown to trigger the initial POST request preparation.

**Expected Output**: Login form loads, showing OpenID provider options.

**Success Indicators**:
- Login page renders successfully
- Dropdown with predefined IDPs is visible

### Step 2: Intercept and Modify the Request
procedure: [[procedures/Intercept-and-Modify-OpenID-Request]]

**Objective**: Alter the OpenID provider URL in the authentication request to point to an untrusted IDP, bypassing the allowed list validation.

**Instructions**: Configure a proxy tool to intercept traffic from the browser. Submit the login form by selecting an IDP, then intercept the POST request to /login/. In the request body, locate the 'openid' parameter (e.g., openid=https://allowed-idp.com) and modify it to an arbitrary URL like https://openstackid.org. Forward the modified request to proceed.

**Expected Output**: Modified POST request sent to /login/ with arbitrary 'openid' value.

**Success Indicators**:
- Request interception successful
- 'openid' parameter updated without errors

### Step 3: Complete Authentication with Arbitrary IDP
procedure: [[procedures/Complete-Authentication-with-Arbitrary-IDP]]

**Objective**: Use the arbitrary IDP to forge an authentication response that matches an existing Airflow user, tricking the backend into granting access.

**Instructions**: After forwarding the modified request, the Airflow backend will redirect to the arbitrary IDP. Control the IDP to generate a forged OpenID response containing the claimed user's identity (e.g., matching an existing Airflow username and email). Ensure the response includes valid OpenID 2.0 attributes like openid.claimed_id and openid.identity that align with the target user.

**Expected Output**: Backend receives and trusts the forged response, proceeding to session creation.

**Success Indicators**:
- Redirect to arbitrary IDP occurs
- Forged response accepted without validation errors

### Step 4: Access Dashboard as Impersonated User
procedure: [[procedures/Access-Dashboard-as-Impersonated-User]]

**Objective**: Gain full access to the Airflow dashboard and functionalities as the impersonated user.

**Instructions**: Upon acceptance of the forged authentication, the user is redirected back to the Airflow homepage or dashboard. Verify access by navigating to sensitive areas like DAG management or user settings, confirming elevated privileges.

**Expected Output**: Successful login and dashboard access with the targeted user's permissions.

**Success Indicators**:
- Redirect to /home/ or dashboard
- Ability to perform actions as the impersonated user (e.g., view/edit workflows)

## Attack Chain Summary

### Key Achievements

1. Bypassed OpenID provider validation in Flask-AppBuilder
2. Impersonated arbitrary Airflow users without credentials
3. Achieved full account hijacking and privilege escalation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2024-01-01T00:00:00Z*
