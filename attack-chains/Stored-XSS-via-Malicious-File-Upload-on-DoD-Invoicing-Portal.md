---
tags:
  - xss
  - stored-xss
  - file-upload
  - web
  - asp.net
  - dod
type: attack_chain
tools:
  - '[[tools/Mozilla-Firefox]]'
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Stored-XSS-via-File-Upload]]'
step_count: 5
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:08.413Z'
description: >-
  A multi-step attack exploiting a stored XSS vulnerability in a file upload
  form on a U.S. Department of Defense website, allowing arbitrary JavaScript
  execution to steal cookies or deface the site.
skill_level: intermediate
impact_level: high
id: fb9640f5-00f9-42d2-a359-3671c708f2f2
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Stored XSS via Malicious File Upload on DoD Invoicing Portal

Multi-stage attack chain demonstrating exploitation of a stored XSS vulnerability through file upload on the WFDPMMiscInvoicingDocuments.aspx page of a U.S. Department of Defense website. The attack involves navigating to the vulnerable form, uploading a file with embedded JavaScript, inspecting the reflected file path in the DOM, and observing the execution of the payload, which can lead to cookie theft, site defacement, or other client-side attacks on users viewing the content.

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
    A[Navigate to Vulnerable Page] --> B[Fill Form and Upload Malicious File]
    B --> C[Access Developer Tools]
    C --> D[Inspect Uploaded File Path in DOM]
    D --> E[Observe XSS Payload Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#f39c12
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Mozilla-Firefox]]

### Target Environment

- Web platform
- ASP.NET-based application
- Access to public-facing DoD website (no authentication required for initial upload)

### Initial Access Requirements

- Internet access to the target URL
- No credentials needed
- Browser with developer tools enabled

## Detailed Attack Procedures

### Step 1: Navigate to Vulnerable Page
procedure: [[procedures/Exploit-Stored-XSS-via-File-Upload]]

**Objective**: Access the file upload form on the target invoicing documents page to begin the exploitation process.

**Instructions**: Open [[tools/Mozilla-Firefox]] and navigate to the vulnerable URL.

**Expected Output**: The WFDPMMiscInvoicingDocuments.aspx page loads, displaying the file upload form.

**Success Indicators**:
- Page loads without errors
- Form fields for uploading documents are visible

### Step 2: Fill Form and Upload Malicious File
procedure: [[procedures/Exploit-Stored-XSS-via-File-Upload]]

**Objective**: Submit a form with a file containing JavaScript payload to store the malicious content on the server.

**Instructions**: Complete the required form fields (e.g., invoice details) and prepare a text file with embedded JavaScript, such as creating a file named "testing-new.html" containing `<script>alert('XSS')</script>`. Upload the file via the form's upload mechanism and submit.

**Expected Output**: Upload succeeds, and the page refreshes or redirects, potentially displaying a confirmation.

**Success Indicators**:
- File upload completes without validation errors
- No server-side rejection of the file content

### Step 3: Access Developer Tools
procedure: [[procedures/Exploit-Stored-XSS-via-File-Upload]]

**Objective**: Prepare to inspect the page source for the reflected malicious file path.

**Instructions**: After submission, right-click on the page and select "Inspect Element" or press F12 to open Developer Tools in Firefox.

**Expected Output**: Developer Tools panel opens, showing the Elements tab with the page's DOM.

**Success Indicators**:
- Dev Tools launch successfully
- Page elements are inspectable

### Step 4: Inspect Uploaded File Path in DOM
procedure: [[procedures/Exploit-Stored-XSS-via-File-Upload]]

**Objective**: Locate the unsanitized file path in the DOM where the JavaScript payload is reflected.

**Instructions**: In the Elements tab, search for the uploaded file reference, such as a path like `https://www.██████.mil/jppso/vendor/Data/cme1rjjcnjhnvdzhf5lgfbge-01192021-065856_testing-new.html`, where the filename includes the payload.

**Expected Output**: The file path appears in the HTML, with the malicious JavaScript embedded or executable upon rendering.

**Success Indicators**:
- Malicious filename/path visible in DOM
- No escaping applied to the path

### Step 5: Observe XSS Payload Execution
procedure: [[procedures/Exploit-Stored-XSS-via-File-Upload]]

**Objective**: Verify the stored XSS by triggering and observing the JavaScript execution.

**Instructions**: Interact with the page element containing the file path (e.g., click a link or refresh) to render the content, or directly access the file URL if exposed.

**Expected Output**: The JavaScript payload executes, e.g., an alert box pops up with 'XSS', or in a real attack, cookies are stolen via network requests.

**Success Indicators**:
- Alert or other payload effect triggers
- Console logs show JavaScript execution
- Potential for further actions like cookie exfiltration

## Attack Chain Summary

### Key Achievements

1. Successful upload of JavaScript-laden file without sanitization
2. Reflection of malicious path in DOM leading to stored XSS
3. Demonstration of client-side execution impacting viewers

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
