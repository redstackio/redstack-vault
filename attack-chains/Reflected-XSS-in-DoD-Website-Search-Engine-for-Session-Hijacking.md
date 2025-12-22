---
id: ac-reflected-xss-dod-search
tags:
  - xss
  - reflected-xss
  - javascript
  - web
  - dod
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Reflected-XSS-in-Search-Engine]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:38.299Z'
description: >-
  A multi-step attack exploiting a reflected XSS vulnerability in a U.S.
  Department of Defense website's search functionality to execute arbitrary
  JavaScript and potentially steal session data.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Reflected XSS in DoD Website Search Engine for Session Hijacking

Multi-stage attack chain demonstrating exploitation of a reflected cross-site scripting vulnerability in the search engine of a U.S. Department of Defense website, allowing arbitrary JavaScript execution to steal cookies or hijack sessions.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Navigate to Target] --> B[Inject Payload]
    B --> C[Submit Search]
    C --> D[Trigger Execution]
    D --> E[Session Hijack]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web platform
- Publicly accessible DoD website with search functionality
- No specific ports or services required beyond HTTP/HTTPS

### Initial Access Requirements

- Direct network access to the internet
- No credentials needed for initial access
- Victim must interact with the crafted link or page

## Detailed Attack Procedures

### Step 1: Navigate to the Target Website
procedure: [[procedures/Exploit-Reflected-XSS-in-Search-Engine]]

**Objective**: Access the vulnerable DoD website and locate the search engine feature to prepare for payload injection.

**Instructions**: Open a web browser and navigate to the target URL https://███/unit/███. Identify the search input field on the page.

**Expected Output**: The website loads, displaying the search bar.

**Success Indicators**:
- Page loads without errors
- Search input field is visible and functional

### Step 2: Inject Payload into the Search Field
procedure: [[procedures/Exploit-Reflected-XSS-in-Search-Engine]]

**Objective**: Insert a malicious JavaScript payload into the search input to test for reflection without sanitization.

**Instructions**: Enter the payload `<script>alert(document.domain)</script>` or `<script>alert(document.cookie)</script>` directly into the search input field. This payload will be reflected in the page content if vulnerable.

**Expected Output**: The payload appears in the input field as typed.

**Success Indicators**:
- Payload is accepted without immediate rejection
- No client-side validation blocks the input

### Step 3: Submit the Search
procedure: [[procedures/Exploit-Reflected-XSS-in-Search-Engine]]

**Objective**: Perform the search to cause the user input to be reflected unsanitized in the page content.

**Instructions**: Press Enter or click the search button to submit the query. The reflected input should appear below the 'Term:' label in the search results section.

**Expected Output**: Search results page loads with the injected payload visible in the HTML as plain text under the 'Term:' label.

**Success Indicators**:
- Reflected payload is displayed in the page source without escaping
- No server-side sanitization applied

### Step 4: Trigger the Payload Execution
procedure: [[procedures/Exploit-Reflected-XSS-in-Search-Engine]]

**Objective**: Interact with page elements to execute the reflected JavaScript payload, demonstrating arbitrary code execution.

**Instructions**: Scroll down below the reflected search term to locate the three icons (likely navigation or action icons). Hover the mouse over each of the three icons in sequence. This interaction triggers the script execution.

**Expected Output**: An alert popup appears displaying the document domain or cookie contents, confirming JavaScript execution.

**Success Indicators**:
- Alert box pops up with sensitive data (e.g., domain or cookies)
- Browser console shows no errors; payload executes successfully

## Attack Chain Summary

### Key Achievements

1. Successful injection and reflection of unsanitized user input in a government website.
2. Triggered execution of arbitrary JavaScript via mouse hover interaction.
3. Demonstrated potential for session theft or content manipulation in a high-impact environment.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
