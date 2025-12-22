---
id: ac-stored-xss-drive2-business
tags:
  - xss
  - stored-xss
  - web-vulnerability
  - javascript-injection
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
  - '[[procedures/Register-on-drive2-and-Connect-Business-Account]]'
  - '[[procedures/Access-Business-Account-Management-Panel]]'
  - '[[procedures/Inject-XSS-Payload-into-Company-Name]]'
  - '[[procedures/Save-Malicious-Company-Data]]'
  - '[[procedures/Trigger-XSS-on-Company-Profile-Page]]'
step_count: 5
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:33.555Z'
description: >-
  Multi-stage exploitation of a stored XSS vulnerability in the drive2.ru
  business account feature, allowing arbitrary JavaScript execution on company
  profile pages visited by users.
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in drive2.ru Business Account Company Name Field

Multi-stage attack chain demonstrating the exploitation of a stored cross-site scripting (XSS) vulnerability in the business account feature of drive2.ru, where unsanitized user input in the 'Company Name' field is persisted and rendered on public company profile pages, leading to automatic JavaScript execution for any visitor.

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
    A[Register Business Account] --> B[Access Management Panel]
    B --> C[Inject XSS Payload]
    C --> D[Save Data]
    D --> E[Trigger on Company Page]
    E --> F[Execute JS and Exfil]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools)

### Target Environment

- Web platform: drive2.ru website
- Required services/ports: Standard HTTP/HTTPS (ports 80/443)
- Network access requirements: Internet access to register and interact with the site

### Initial Access Requirements

- No prior credentials needed; public registration available
- Network position: External attacker
- Prior access needed: None

## Detailed Attack Procedures

### Step 1: Register Business Account
procedure: [[procedures/Register-on-drive2-and-Connect-Business-Account]]

**Objective**: Gain access to the business account features by creating a standard account and enabling business functionality.

**Instructions**: Navigate to drive2.ru, create a new user account via the registration form, then access the business account setup to connect it.

**Expected Output**: Successful account creation and business feature activation, with access to the management panel.

**Success Indicators**:
- Confirmation email or page indicating account setup complete
- Redirect to business dashboard

### Step 2: Access Management Panel
procedure: [[procedures/Access-Business-Account-Management-Panel]]

**Objective**: Enter the business account control panel to prepare for inputting company details.

**Instructions**: Log in to the newly created account, navigate to the business section, and open the company registration or editing form.

**Expected Output**: Company management interface loaded, with fields like 'Company Name' visible for input.

**Success Indicators**:
- Form fields populated and editable
- No errors in loading the panel

### Step 3: Inject XSS Payload
procedure: [[procedures/Inject-XSS-Payload-into-Company-Name]]

**Objective**: Insert a malicious JavaScript payload into the unsanitized 'Company Name' field to enable stored XSS.

**Instructions**: In the 'Название компании' (Company Name) field, enter the payload `<svg/onload=confirm(document.domain)>` and fill other required fields minimally.

**Expected Output**: Payload entered without immediate errors or sanitization visible in the form.

**Success Indicators**:
- Payload text appears in the input field as entered
- Form validation passes for other fields

### Step 4: Save Malicious Data
procedure: [[procedures/Save-Malicious-Company-Data]]

**Objective**: Persist the injected payload in the backend database for later rendering on the company page.

**Instructions**: Submit the company registration or update form to save the details.

**Expected Output**: Success message confirming data saved, with option to view the company profile.

**Success Indicators**:
- No submission errors
- Company profile link generated or accessible

### Step 5: Trigger XSS Execution
procedure: [[procedures/Trigger-XSS-on-Company-Profile-Page]]

**Objective**: Visit the company profile page to execute the stored payload, demonstrating arbitrary JavaScript execution.

**Instructions**: Navigate to the public company profile URL and observe the automatic execution of the onload event.

**Expected Output**: Alert dialog (confirm) popping up with the domain name, indicating successful XSS.

**Success Indicators**:
- JavaScript alert or confirm dialog appears
- No additional user interaction required beyond page load

## Attack Chain Summary

### Key Achievements

1. Persistent storage of malicious JavaScript via business account input
2. Automatic execution on public company pages, affecting any visitor
3. Potential for cookie theft, phishing, or redirects without victim interaction

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
