---
id: ac-uuid-001
tags:
  - idor
  - web
  - dod
  - phi
  - pii
  - authentication
  - cac
  - medical-records
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Authenticate-to-DoD-Application-with-CAC]]'
  - '[[procedures/Access-Authorized-Shot-Records-with-Burp-Suite]]'
  - '[[procedures/Manipulate-ID-Parameter-for-Unauthorized-Access]]'
  - '[[procedures/Extract-PDF-from-302-Response]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:25:30.022Z'
description: >-
  An attack chain exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in a U.S. Department of Defense web application to access
  unauthorized medical shot records, disclosing Protected Health Information
  (PHI) and Personally Identifiable Information (PII) via CAC-authenticated
  access.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
  - '[[Data from Information Repositories]]'
---
# IDOR in DoD Medical Shot Records Endpoint Leading to Unauthorized PHI/PII Disclosure

Multi-stage attack chain demonstrating a complete workflow to exploit an IDOR vulnerability in a DoD web application for viewing medical shot records, requiring CAC authentication. The attack allows authenticated users to access and extract vaccination records (PDFs) of unauthorized individuals, such as dependents or unrelated personnel, by manipulating URL parameters. This leads to the unauthorized disclosure of sensitive PHI and PII.

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
    A[Authenticate with CAC] --> B[Access Authorized Records]
    B --> C[Manipulate ID Parameter]
    C --> D[Extract Unauthorized PDF]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application platform
- HTTPS endpoints for DoD medical records
- CAC-enabled authentication

### Initial Access Requirements

- Valid CAC credentials for a sponsor account
- Network access to the DoD application (e.g., via VPN or authorized connection)
- Proxy tool like Burp Suite configured to intercept traffic

## Detailed Attack Procedures

### Step 1: Authenticate to the Application
procedure: [[procedures/Authenticate-to-DoD-Application-with-CAC]]

**Objective**: Gain authenticated access to the DoD web application using CAC credentials to establish a session for subsequent requests.

**Instructions**: Navigate to the login endpoint and insert CAC for authentication. Configure Burp Suite as a proxy if needed to monitor the session.

**Expected Output**: Successful login redirect to the dashboard or main application page, with session cookies established.

**Success Indicators**:
- Authentication successful without errors
- Access to authorized user dashboard granted

### Step 2: Access the Shot Records Endpoint for Authorized Records
procedure: [[procedures/Access-Authorized-Shot-Records-with-Burp-Suite]]

**Objective**: Retrieve the authorized shot record to understand the response format, confirming the endpoint behavior with a 302 redirect containing PDF data.

**Instructions**: Browse to the endpoint with your own ID parameter (e.g., https://███████=[own_id]). Intercept the request/response using Burp Suite to observe the 302 redirect and embedded PDF in the body.

**Expected Output**: HTTP 302 response with the authorized PDF embedded in the body, redirecting to a success page.

**Success Indicators**:
- PDF content visible in the response body
- No access denial for authorized ID

### Step 3: Manipulate the ID Parameter to Access Unauthorized Records
procedure: [[procedures/Manipulate-ID-Parameter-for-Unauthorized-Access]]

**Objective**: Exploit the IDOR by altering the ID parameter to request records of other users, bypassing authorization checks.

**Instructions**: In Burp Suite, modify the ID in the intercepted request (e.g., change [own_id] to [own_id +1] or [own_id -1]) and forward the request to https://███████=[manipulated_id]. Observe the response.

**Expected Output**: HTTP 302 redirect with the unauthorized PDF embedded in the body, without any denial.

**Success Indicators**:
- Unauthorized PDF content returned in response body
- No 403 or access denied error

### Step 4: Extract the PDF from the 302 Response
procedure: [[procedures/Extract-PDF-from-302-Response]]

**Objective**: Save the unauthorized shot record PDF for analysis or exfiltration, confirming the disclosure of PHI/PII.

**Instructions**: In Burp Suite, intercept the 302 response, right-click the response body, and use 'Copy to File' to save it as a .pdf file.

**Expected Output**: A valid PDF file containing vaccination details, names, and other PII of the unauthorized individual.

**Success Indicators**:
- PDF opens correctly with sensitive data
- Data matches an unrelated individual's records

## Attack Chain Summary

### Key Achievements

1. Authenticated access to DoD medical records system via CAC
2. Exploitation of IDOR to access arbitrary user records without authorization
3. Extraction of PHI/PII in PDF format, enabling potential further misuse

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Discovery]] Account Discovery
- [[Data from Information Repositories]] Data from Information Repositories

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
