---
tags:
  - xss
  - reflected-xss
  - mail.ru
  - javascript-execution
type: attack_chain
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Craft-Malicious-Search-URL-for-XSS]]'
  - '[[procedures/Access-URL-to-Observe-Payload-Reflection]]'
  - '[[procedures/Verify-XSS-Payload-Execution-Potential]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:16.146Z'
description: >-
  Multi-stage attack exploiting reflected XSS in the Mail.ru search
  functionality at go.mail.ru/search through the 'q' parameter, enabling
  JavaScript execution for session theft or phishing via shared links.
skill_level: intermediate
impact_level: high
id: 5bfbe315-4267-4d66-b381-efcf9cc4360f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Reflected XSS in Mail.ru Search via Query Parameter

Multi-stage attack chain demonstrating exploitation of a reflected XSS vulnerability in the Mail.ru search at go.mail.ru/search, where the 'q' parameter reflects user input into HTML and JSON without proper sanitization, allowing arbitrary JavaScript execution. This can lead to stealing cookies, session hijacking, or phishing when victims click shared malicious search links via email or social media.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Craft Malicious URL] --> B[Access and Render Page]
    B --> C[Verify JavaScript Execution]
    C --> D[Impact: Session Theft/Phishing]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Web-Browser]]

### Target Environment

- Web platform
- Access to internet and Mail.ru search service
- No authentication required

### Initial Access Requirements

- Public network access
- Ability to share URLs via email/social media for phishing
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Craft Malicious Search URL
procedure: [[procedures/Craft-Malicious-Search-URL-for-XSS]]

**Objective**: Create a URL with an injected XSS payload in the 'q' parameter to test reflection.

**Instructions**: Manually construct the URL by URL-encoding the payload. For example, use a simple script tag like `<script>alert(1)</script>`, encoded as `%3Cscript%3Ealert(1)%3C%2Fscript%3E`.

**Expected Output**: A valid URL like `https://go.mail.ru/search?fr=mn&q=%3Cscript%3Ealert(1)%3C%2Fscript%3E`.

**Success Indicators**:
- URL is properly formed and accessible
- Payload is URL-encoded correctly

### Step 2: Access URL to Observe Reflection
procedure: [[procedures/Access-URL-to-Observe-Payload-Reflection]]

**Objective**: Load the page to confirm the payload reflects in the HTML title, JSON state, and search results.

**Instructions**: Open the crafted URL in a web browser. Inspect the page source and network responses to see the reflection in Yandex backend API calls.

**Expected Output**: Payload appears in page title, JSON fields (e.g., escaped as `\\\u003cpayload\\\>`), and search snippets.

**Success Indicators**:
- Reflection observed in multiple contexts
- No immediate blocking or sanitization

### Step 3: Verify XSS Payload Execution Potential
procedure: [[procedures/Verify-XSS-Payload-Execution-Potential]]

**Objective**: Confirm the vulnerability allows JavaScript execution by analyzing insufficient sanitization in dynamic HTML elements.

**Instructions**: Replace the test payload with a functional one and observe if it executes (e.g., alert box pops). Check search result snippets for unescaped output.

**Expected Output**: JavaScript executes in the browser, such as an alert dialog.

**Success Indicators**:
- Arbitrary code runs without errors
- Potential for cookie theft via `document.cookie`

## Attack Chain Summary

### Key Achievements

1. Identified reflection points in HTML and JSON
2. Demonstrated payload execution in dynamic search results
3. Highlighted phishing vector via shareable links

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
