---
tags:
  - xss
  - reflected-xss
  - javascript
  - cookie-theft
  - web-vulnerability
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
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Reflected-XSS-via-userId-Parameter]]'
step_count: 3
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:31.284Z'
description: >-
  A multi-step attack exploiting a reflected XSS vulnerability in the dochelper
  endpoint of a U.S. Department of Defense domain to execute arbitrary
  JavaScript and steal user cookies.
skill_level: intermediate
impact_level: high
id: 6e8bd3af-3123-43ba-a9d4-4184becbd550
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Reflected XSS in dochelper Endpoint to Steal User Cookies

Multi-stage attack chain demonstrating exploitation of a reflected XSS vulnerability in the 'dochelper' endpoint on a U.S. Department of Defense domain, allowing arbitrary JavaScript execution to steal user cookies and enable further compromise.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Visit Endpoint] --> B[Execution: Inject XSS Payload]
    B --> C[Collection: Steal Cookies via JavaScript]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web application on a public-facing domain (e.g., U.S. DoD domain)
- Access to the 'dochelper' endpoint
- No special ports or services required beyond HTTP/HTTPS

### Initial Access Requirements

- Public network access to the target URL
- No credentials needed for initial visit
- Ability to craft and load URLs in a browser

## Detailed Attack Procedures

### Step 1: Visit the dochelper Endpoint
procedure: [[procedures/Exploit-Reflected-XSS-via-userId-Parameter]]

**Objective**: Access the vulnerable endpoint to observe normal behavior and confirm the 'userId' parameter is reflected without sanitization.

**Instructions**: Navigate to the base URL of the dochelper endpoint with an empty or basic 'userId' parameter to inspect how user input is handled in the page output.

**Expected Output**: The page loads normally, displaying content that includes the reflected 'userId' value in HTML without encoding.

**Success Indicators**:
- Page loads without errors
- 'userId' parameter value appears in the HTML source

### Step 2: Craft and Append XSS Payload to the userId Parameter
procedure: [[procedures/Exploit-Reflected-XSS-via-userId-Parameter]]

**Objective**: Construct a malicious payload that breaks out of the HTML context and injects executable JavaScript to test for XSS.

**Instructions**: Modify the URL by appending a crafted payload to the 'userId' parameter. The payload '</b><script>alert(document.cookie)</script><b><!--' closes any existing bold tag, injects a script tag to alert cookies, and comments out subsequent content to prevent page breakage.

Full crafted URL example: https://████████/dochelper?userId=%3C%2Fb%3E%3Cscript%3Ealert(document.cookie)%3C%2Fscript%3E%3Cb%3E%3C%21-- (URL-encoded for transmission).

**Expected Output**: The payload is reflected in the page source without sanitization, confirming vulnerability.

**Success Indicators**:
- Payload visible in HTML source
- No server-side filtering applied

### Step 3: Open the Crafted Link in a Browser
procedure: [[procedures/Exploit-Reflected-XSS-via-userId-Parameter]]

**Objective**: Execute the injected JavaScript to demonstrate impact, such as stealing cookies, and validate the full exploitation chain.

**Instructions**: Load the crafted URL directly in a web browser. The reflected input triggers JavaScript execution, displaying an alert with the document's cookies.

**Expected Output**: A browser alert pops up revealing session cookies and other client-side data.

**Success Indicators**:
- JavaScript alert executes
- Cookies are displayed, confirming theft potential

## Attack Chain Summary

### Key Achievements

1. Confirmed reflected XSS in 'userId' parameter due to lack of input sanitization and output encoding.
2. Executed arbitrary JavaScript to alert and potentially exfiltrate cookies.
3. Demonstrated high-impact risks including account compromise, data theft, and unauthorized actions.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
