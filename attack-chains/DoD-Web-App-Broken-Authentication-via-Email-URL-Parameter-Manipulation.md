---
id: 8aba8b46-789b-4ba8-b3b0-1354034dc36b
name: DoD Web App Broken Authentication via Email URL Parameter Manipulation
type: attack_chain
description: >-
  Multi-stage attack exploiting a broken authentication mechanism in a U.S.
  Department of Defense web application by manipulating the email parameter in
  the URL to access other users' accounts without credentials.
verified: false
submitted: true
step_count: 5
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.531Z'
procedures:
  - '[[procedures/Register-for-DoD-Web-App-Account]]'
  - '[[procedures/Authenticate-and-Capture-Email-Parameter]]'
  - '[[procedures/Manipulate-Email-Parameter-for-Account-Takeover]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
tactics:
  - '[[Initial Access]]'
tags:
  - authentication-bypass
  - broken-auth
  - account-takeover
  - information-disclosure
  - web
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---

# DoD Web App Broken Authentication via Email URL Parameter Manipulation

Multi-stage attack chain demonstrating a complete attack workflow exploiting broken authentication in a DoD web application, allowing unauthorized access to other users' sensitive data via URL parameter manipulation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Visit Target] --> B[Register Account]
    B --> C[Login and Capture Parameter]
    C --> D[Modify Email Parameter]
    D --> E[Access Targeted Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]] (optional for parameter fuzzing)
- Web browser (e.g., Chrome or Firefox)

### Target Environment

- Web platform
- Access to DoD web application at https://██████
- No specific ports or services required beyond standard HTTPS (443)

### Initial Access Requirements

- Internet access
- Valid email address for initial registration
- Knowledge of target user's email (e.g., DoD employee emails like ag3nt-z3@███ or ██████@██████.com)
- No prior credentials needed beyond initial registration

## Detailed Attack Procedures

### Step 1: Visit the Target Website
procedure: [[procedures/Register-for-DoD-Web-App-Account]]

**Objective**: Gain initial access to the DoD web application to begin the registration process.

**Instructions**: Open a web browser and navigate to the main URL of the target DoD web application.

**Expected Output**: The homepage or login/registration page loads successfully.

**Success Indicators**:
- Page loads without errors
- Registration or login options are visible

### Step 2: Register for an Account
procedure: [[procedures/Register-for-DoD-Web-App-Account]]

**Objective**: Create a legitimate account to establish a valid session and trigger the authentication flow.

**Instructions**: Proceed to the registration form, provide a new email address, and complete the signup. This will require email verification, but note the flow for later bypass.

**Expected Output**: Registration confirmation and a verification email sent.

**Success Indicators**:
- Account created successfully
- Email verification prompt appears

### Step 3: Login with a Valid Account
procedure: [[procedures/Authenticate-and-Capture-Email-Parameter]]

**Objective**: Authenticate with your own credentials to generate a URL containing the email parameter for manipulation.

**Instructions**: Enter your registered email and password at the login endpoint (https://██████/███). Upon successful login, observe the redirect URL, which includes the email parameter (e.g., https://█████████/████?email=your-email@domain.com).

**Expected Output**: Successful login and a dashboard or profile page loads with the email parameter in the URL.

**Success Indicators**:
- Authentication succeeds
- URL contains the 'email' parameter with your email value

### Step 4: Modify the Email Parameter
procedure: [[procedures/Manipulate-Email-Parameter-for-Account-Takeover]]

**Objective**: Alter the email parameter to target another user's valid email, bypassing authentication checks.

**Instructions**: Edit the email value in the URL to a known valid DoD email (e.g., change to ag3nt-z3@███ or another employee email like ██████@██████.com). Reload the page by pressing Enter. Optionally, use [[tools/Burp-Suite]] Intruder for fuzzing with email wordlists to identify valid ones.

**Expected Output**: The page reloads as if authenticated for the target email, without requiring credentials or verification.

**Success Indicators**:
- No authentication prompt for the target email
- Target user's profile or data loads

### Step 5: Access the Targeted Account Data
procedure: [[procedures/Manipulate-Email-Parameter-for-Account-Takeover]]

**Objective**: Retrieve sensitive information from the targeted account, achieving information disclosure and potential takeover.

**Instructions**: Once the page loads for the target, view the disclosed personal information such as name, surname, and potentially SSNs. The application treats you as the target user without further checks.

**Expected Output**: Disclosure of PII including names, surnames, and other sensitive data.

**Success Indicators**:
- Unauthorized access to target account data
- No logout or re-authentication required

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication for any valid email via URL manipulation
2. Achieved information disclosure of sensitive DoD user PII
3. Enabled potential full account takeover without credentials

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
