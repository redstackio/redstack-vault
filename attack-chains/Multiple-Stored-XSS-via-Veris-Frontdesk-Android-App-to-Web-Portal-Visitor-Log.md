---
tags:
  - xss
  - stored-xss
  - android-app
  - web-portal
  - javascript-execution
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Android
  - Web
submitted: true
complexity: medium
procedures:
  - '[[procedures/Inject-Stored-XSS-in-Veris-Frontdesk-App]]'
  - '[[procedures/Trigger-Stored-XSS-in-Veris-Web-Portal]]'
step_count: 9
techniques:
  - '[[JavaScript]]'
description: >-
  A multi-stage attack exploiting stored XSS vulnerabilities in the Veris
  Frontdesk Android App, where payloads injected during visitor check-in are
  stored and executed in the web portal's visitor log, allowing arbitrary
  JavaScript execution against authenticated users.
skill_level: intermediate
impact_level: high
id: c81804f5-eb80-4dd1-b78e-39d99adde6e7
created_at: '2025-12-14T03:15:26.755Z'
updated_at: '2025-12-14T03:15:26.755Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Multiple Stored XSS via Veris Frontdesk Android App to Web Portal Visitor Log

Multi-stage attack chain demonstrating a complete stored XSS workflow from mobile app injection to web portal exploitation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 9 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[App Injection] --> B[Payload Storage]
    B --> C[Portal Access]
    C --> D[XSS Execution]
    D --> E[Data Theft/Session Hijack]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e67e22
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Android device or emulator with Veris Frontdesk App installed
- Web browser for accessing the portal

### Target Environment

- Veris Frontdesk Android App (version vulnerable to unsanitized inputs)
- Web portal at https://sandbox.veris.in/portal/visitor-log/
- Network access to app backend and web portal

### Initial Access Requirements

- Ability to perform visitor check-in via the app (no special credentials needed for injection)
- Valid login credentials for the web portal to view the visitor log

## Detailed Attack Procedures

### Step 1: Open the Veris Front Desk App
procedure: [[procedures/Inject-Stored-XSS-in-Veris-Frontdesk-App]]

**Objective**: Launch the app to begin the check-in process and prepare for payload injection.

**Instructions**: Install and open the Veris Frontdesk Android App on a device or emulator.

**Expected Output**: App interface loads, displaying options like Check In.

**Success Indicators**:
- App opens successfully without errors
- Check In section is accessible

### Step 2: Navigate to the Check In section
procedure: [[procedures/Inject-Stored-XSS-in-Veris-Frontdesk-App]]

**Objective**: Access the visitor check-in feature where vulnerable input fields are located.

**Instructions**: Tap on the Check In option within the app's main menu.

**Expected Output**: Check-in form appears with fields for visitor details.

**Success Indicators**:
- Check-in form loads
- Input fields for name, phone, etc., are visible

### Step 3: Enter required details such as first name, last name, and phone number
procedure: [[procedures/Inject-Stored-XSS-in-Veris-Frontdesk-App]]

**Objective**: Fill mandatory fields with legitimate data to advance to vulnerable sections.

**Instructions**: Input valid test values, e.g., First Name: "Test", Last Name: "User", Phone: "1234567890".

**Expected Output**: Form validates the inputs and allows progression.

**Success Indicators**:
- No validation errors
- Next button becomes active

### Step 4: Proceed to the next step
procedure: [[procedures/Inject-Stored-XSS-in-Veris-Frontdesk-App]]

**Objective**: Advance to the fields vulnerable to XSS injection.

**Instructions**: Tap the "Next" button to proceed.

**Expected Output**: Additional form fields load, including "Who do you wish to meet?" and "Additional Information".

**Success Indicators**:
- Vulnerable input fields appear
- Form submission is possible

### Step 5: Inject the payload into the vulnerable input fields
procedure: [[procedures/Inject-Stored-XSS-in-Veris-Frontdesk-App]]

**Objective**: Insert malicious JavaScript payloads into unsanitized fields to store XSS.

**Instructions**: In "Who do you wish to meet?", enter `<img src=x onerror=alert(3)>`. In "Additional Information", enter `<img src=x onerror=alert(4)>`.

**Expected Output**: Payloads are accepted without sanitization errors.

**Success Indicators**:
- Payloads entered successfully
- No immediate execution or blocking

### Step 6: Submit the check-in
procedure: [[procedures/Inject-Stored-XSS-in-Veris-Frontdesk-App]]

**Objective**: Store the injected payloads in the backend database.

**Instructions**: Complete any remaining fields and tap Submit to finalize check-in.

**Expected Output**: Check-in confirmation message; payload is persisted server-side.

**Success Indicators**:
- Submission succeeds
- Visitor record is created

### Step 7: Login to the account on sandbox.veris.in
procedure: [[procedures/Trigger-Stored-XSS-in-Veris-Web-Portal]]

**Objective**: Authenticate to the web portal to access the visitor log.

**Instructions**: Open a browser, navigate to https://sandbox.veris.in, and log in with valid credentials.

**Expected Output**: Successful login; dashboard appears.

**Success Indicators**:
- Authentication passes
- Portal dashboard loads

### Step 8: Navigate to the visitor log page
procedure: [[procedures/Trigger-Stored-XSS-in-Veris-Web-Portal]]

**Objective**: Reach the page where stored payloads are reflected.

**Instructions**: Click on the Visitor Log link or navigate to https://sandbox.veris.in/portal/visitor-log/.

**Expected Output**: Visitor log table loads, displaying recent entries including the injected one.

**Success Indicators**:
- Page loads without errors
- Injected visitor entry is visible in the log

### Step 9: Observe the XSS trigger
procedure: [[procedures/Trigger-Stored-XSS-in-Veris-Web-Portal]]

**Objective**: Execute the stored JavaScript payloads to demonstrate arbitrary code execution.

**Instructions**: View the visitor log entry containing the payloads; no further action needed as reflection is automatic.

**Expected Output**: JavaScript alerts pop up (e.g., alert(3) and alert(4)) upon rendering the log.

**Success Indicators**:
- Alerts execute in the browser context
- Console shows JavaScript errors or execution traces

## Attack Chain Summary

### Key Achievements

1. Successful injection of stored XSS payloads via Android app inputs
2. Persistence of unsanitized data in the backend
3. Arbitrary JavaScript execution in the web portal, enabling session hijacking or data theft for any authenticated viewer

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01*
