---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - idor
  - web
  - unauthorized-access
  - publitas
  - publication
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Publitas-Account]]'
  - '[[procedures/Generate-Offline-Publication-and-Extract-sourceDocumentId]]'
  - '[[procedures/Send-IDOR-Request-to-Vulnerable-Endpoint]]'
  - '[[procedures/Parse-API-Response-for-Cover-Page-URL]]'
  - '[[procedures/Access-Retrieved-Cover-Page-URL]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:18.354Z'
description: >-
  Multi-stage attack exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in the Publitas platform to gain unauthorized access to other
  users' offline publication cover pages by manipulating the SOURCE_DOCUMENT_ID
  parameter.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# IDOR in Publitas Allowing Unauthorized Access to Offline Publication Cover Pages via SOURCE_DOCUMENT_ID

Multi-stage attack chain demonstrating a complete workflow to exploit an IDOR vulnerability in the Publitas platform, enabling unauthorized disclosure of sensitive cover page content from other users' offline publications.

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
    A[Create Account] --> B[Generate Offline Publication]
    B --> C[Send IDOR Request]
    C --> D[Parse Response]
    D --> E[Access Cover Page]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#f39c12
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)
- Command-line tool like curl for API requests

### Target Environment

- Publitas web platform
- Internet access to https://publitas.com
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- No prior credentials needed; attack begins with legitimate account creation
- Attacker must be able to register on the platform
- Basic knowledge of web APIs and parameter manipulation

## Detailed Attack Procedures

### Step 1: Create Account
procedure: [[procedures/Create-Publitas-Account]]

**Objective**: Establish a legitimate user presence on the Publitas platform to enable further interactions.

**Instructions**: Navigate to the Publitas registration page and complete the signup process with valid email and password.

**Expected Output**: Confirmation email and access to the user dashboard.

**Success Indicators**:
- Account creation successful
- Login functional

### Step 2: Generate Offline Publication and Extract sourceDocumentId
procedure: [[procedures/Generate-Offline-Publication-and-Extract-sourceDocumentId]]

**Objective**: Create a test offline publication to understand the ID structure and obtain a valid sourceDocumentId for reference.

**Instructions**: From the dashboard, initiate the creation of an offline publication and inspect the response or page source to extract the sourceDocumentId.

**Expected Output**: A new offline publication with an associated sourceDocumentId (e.g., a numeric or UUID value).

**Success Indicators**:
- Publication created successfully
- sourceDocumentId captured

### Step 3: Send IDOR Request to Vulnerable Endpoint
procedure: [[procedures/Send-IDOR-Request-to-Vulnerable-Endpoint]]

**Objective**: Exploit the IDOR by submitting a request with an arbitrary SOURCE_ID from another user's publication to bypass authorization.

**Instructions**: Use a tool like curl to send a GET or POST request to the vulnerable endpoint, replacing the SOURCE_ID with a target value obtained from other observations (e.g., via browser dev tools on public pages).

Execute [[commands/curl-publitas-idor-request]]:

```bash
curl -X GET "https://api.publitas.com/vulnerable-endpoint?SOURCE_ID=TARGET_SOURCE_ID" -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json"
```

**Expected Output**: API response containing a URL to the target cover page, including embedded user ID and publication ID.

**Success Indicators**:
- Response returns data without ownership errors
- URL for unauthorized content provided

### Step 4: Parse API Response for Cover Page URL
procedure: [[procedures/Parse-API-Response-for-Cover-Page-URL]]

**Objective**: Extract the accessible URL from the vulnerable API response to prepare for direct access.

**Instructions**: Review the JSON response from the previous request and locate the field containing the cover page URL (e.g., "cover_url": "https://...").

**Expected Output**: Isolated URL string pointing to the offline cover page.

**Success Indicators**:
- URL successfully parsed
- URL contains sensitive identifiers like user ID

### Step 5: Access Retrieved Cover Page URL
procedure: [[procedures/Access-Retrieved-Cover-Page-URL]]

**Objective**: Directly view the unauthorized cover page content to confirm disclosure.

**Instructions**: Open the extracted URL in a web browser or use curl to fetch the content.

**Expected Output**: Rendered cover page from the target offline publication, revealing sensitive design or content elements.

**Success Indicators**:
- Page loads without authentication prompts
- Content belongs to another user

## Attack Chain Summary

### Key Achievements

1. Legitimate account setup for platform access
2. IDOR exploitation to access non-owned publications
3. Disclosure of sensitive offline cover pages

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2024-01-01T00:00:00Z*
