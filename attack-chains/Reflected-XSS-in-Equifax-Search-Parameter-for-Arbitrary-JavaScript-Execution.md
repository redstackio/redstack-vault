---
tags:
  - xss
  - reflected-xss
  - javascript-injection
  - equifax
type: attack_chain
tools: []
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
  - '[[procedures/Exploit-Reflected-XSS-in-Search-Parameter]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:43.560Z'
description: >-
  A multi-step attack chain exploiting a reflected XSS vulnerability in the
  Equifax personal help search functionality to inject and execute arbitrary
  JavaScript in the victim's browser.
skill_level: intermediate
impact_level: high
id: 900f9d51-f230-4b91-a825-c3430c11ee61
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
---

# Reflected XSS in Equifax Search Parameter for Arbitrary JavaScript Execution

Multi-stage attack chain demonstrating a complete reflected XSS exploitation workflow on Equifax's personal help search page.

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
    A[Access Search Page] --> B[Inspect for Reflection]
    B --> C[Craft XSS Payload]
    C --> D[Inject and Execute Payload]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with Developer Tools)

### Target Environment

- Web platform
- Access to https://www.equifax.com/personal/help/search
- No authentication required

### Initial Access Requirements

- Public internet access
- No credentials needed
- Victim must visit the crafted malicious URL

## Detailed Attack Procedures

### Step 1: Access the Search Page with a Test Search Term
procedure: [[procedures/Exploit-Reflected-XSS-in-Search-Parameter]]

**Objective**: Submit a benign search term to the Equifax help search page to observe normal behavior and prepare for inspection.

**Instructions**: Open a web browser and navigate to the search URL with a test term like "broook".

**Expected Output**: The search page loads, performs the search, and displays results (or no results for an invalid term).

**Success Indicators**:
- Page loads without errors
- Search term is processed

### Step 2: Inspect the Page Source Code to Identify Reflection
procedure: [[procedures/Exploit-Reflected-XSS-in-Search-Parameter]]

**Objective**: Examine the rendered page source to confirm how the user-supplied search term is reflected into client-side JavaScript code.

**Instructions**: After submitting the test search, right-click on the page and select "View Page Source" (or use Ctrl+U). Search for the test term "broook" in the source code to locate the reflection point.

**Expected Output**: The term appears unsanitized in a JavaScript snippet, such as `Analytics.trackEvent('emptySearch',{internalSearchTerm: "broook" , numOfSearchResultsReturned: 0});`.

**Success Indicators**:
- Reflection identified in inline JavaScript
- No escaping observed around the user input

### Step 3: Craft and Inject the XSS Payload
procedure: [[procedures/Exploit-Reflected-XSS-in-Search-Parameter]]

**Objective**: Develop a payload that breaks out of the JavaScript string context and injects executable code to alter the Analytics.trackEvent function parameters.

**Instructions**: Construct a URL-encoded payload to inject JavaScript, such as `%22%20%2C%20internalSearchTerm%3A%20%5B7%5D.map%28alert%29%20%2C%20numOfSearchResultsReturned%3A%20%22b`. This modifies the function call to include `[7].map(alert)` for execution.

**Expected Output**: The payload is ready for injection into the search parameter.

**Success Indicators**:
- Payload syntax validated (e.g., via a local test or decoder)
- Expected JavaScript injection logic confirmed

### Step 4: Access the URL with the Payload to Trigger the XSS
procedure: [[procedures/Exploit-Reflected-XSS-in-Search-Parameter]]

**Objective**: Deliver the malicious URL to a victim (e.g., via phishing) to execute the injected JavaScript in their browser.

**Instructions**: Navigate to the full URL: `https://www.equifax.com/personal/help/search?search=%22%20%2C%20internalSearchTerm%3A%20%5B7%5D.map%28alert%29%20%2C%20numOfSearchResultsReturned%3A%20%22b`.

**Expected Output**: An alert popup executes, confirming arbitrary JavaScript runs (e.g., `alert` function triggers).

**Success Indicators**:
- JavaScript alert or other payload executes
- No server-side blocking observed

## Attack Chain Summary

### Key Achievements

1. Identified reflection point in client-side JavaScript without sanitization
2. Crafted payload to inject and execute arbitrary code via parameter modification
3. Demonstrated potential for cookie theft or session hijacking

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
