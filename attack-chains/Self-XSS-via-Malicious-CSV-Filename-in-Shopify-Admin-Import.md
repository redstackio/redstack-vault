---
tags:
  - xss
  - self-xss
  - shopify
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Trigger-Self-XSS-via-CSV-Upload]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.450Z'
description: >-
  Demonstrates a self-XSS vulnerability in Shopify's admin interface by
  uploading a CSV file with a malicious filename, leading to JavaScript
  execution in the attacker's own browser session.
skill_level: beginner
impact_level: low
id: 9ca7238c-4ddb-4cb1-b499-31a1f07168b5
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Self XSS via Malicious CSV Filename in Shopify Admin Import

Multi-stage attack chain demonstrating a complete attack workflow for exploiting a self-XSS vulnerability in Shopify's app import feature.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Admin Dashboard] --> B[Navigate to App Import] --> C[Upload Malicious CSV]
    C --> D[JavaScript Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Shopify admin interface
- Authenticated session as store admin
- No specific services/ports beyond standard HTTPS (443)

### Initial Access Requirements

- Valid Shopify admin credentials for the target store
- Direct network access to the Shopify domain (e.g., yourstore.myshopify.com/admin)
- No prior access beyond authentication needed

## Detailed Attack Procedures

### Step 1: Access Admin Dashboard

procedure: [[procedures/Trigger-Self-XSS-via-CSV-Upload]]

**Objective**: Gain entry to the Shopify admin interface to begin the import process.

**Instructions**: Open a web browser and navigate to the store's admin dashboard URL.

**Expected Output**: Successful login and display of the admin dashboard.

**Success Indicators**:
- Admin dashboard loads without errors
- User is authenticated as store admin

### Step 2: Navigate to App Import Feature

procedure: [[procedures/Trigger-Self-XSS-via-CSV-Upload]]

**Objective**: Locate the app import functionality within settings to prepare for file upload.

**Instructions**: From the admin dashboard, go to Settings > Apps, then select the Import option. If prompted, choose any platform to proceed to the upload interface.

**Expected Output**: The app import page loads, showing the CSV upload form at /admin/apps/import-store/.

**Success Indicators**:
- Import page accessible
- Upload interface visible

### Step 3: Upload Malicious CSV File

procedure: [[procedures/Trigger-Self-XSS-via-CSV-Upload]]

**Objective**: Upload a CSV file with a filename containing an XSS payload to trigger JavaScript execution.

**Instructions**: Create or prepare a simple CSV file (e.g., with dummy data like a header row). Rename it to include the payload, such as 'payload.csv"><img src=xx onerror=alert(document.domain)>'. Select and upload the file via the import interface.

**Expected Output**: The filename is reflected unsanitized in the page, executing the JavaScript payload, resulting in an alert popup showing the document domain.

**Success Indicators**:
- Alert popup appears in the browser
- JavaScript executes, confirming the self-XSS

## Attack Chain Summary

### Key Achievements

1. Successful navigation to the vulnerable import endpoint
2. Upload of a maliciously named CSV file
3. Execution of arbitrary JavaScript in the authenticated user's browser session

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
