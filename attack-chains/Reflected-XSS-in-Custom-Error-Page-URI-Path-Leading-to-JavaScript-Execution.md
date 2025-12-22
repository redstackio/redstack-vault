---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - xss
  - reflected-xss
  - javascript-injection
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Exploit-Reflected-XSS-in-Custom-Error-URI-Path]]'
step_count: 4
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:26.613Z'
description: >-
  A multi-step attack exploiting a reflected XSS vulnerability in the URI path
  of the /customerror endpoint on a U.S. Department of Defense website, allowing
  arbitrary JavaScript execution in the victim's browser.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Reflected XSS in Custom Error Page URI Path Leading to JavaScript Execution

Multi-stage attack chain demonstrating a complete attack workflow exploiting a reflected Cross-Site Scripting (XSS) vulnerability in the URI path parameter of the /customerror page on a U.S. Department of Defense website. The attack involves navigating to the error endpoint and appending a malicious JavaScript payload to the URL path, which is reflected unsanitized, enabling arbitrary code execution in the victim's browser. This can lead to session hijacking, phishing, or data theft.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Visit Base Domain] --> B[Navigate to Error Page]
    B --> C[Append Malicious Payload to URI]
    C --> D[Access Malicious URL and Execute XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web platform
- Access to public-facing DoD website
- No specific ports or services required beyond HTTP/HTTPS

### Initial Access Requirements

- No credentials needed
- Direct network access to the target domain
- No prior access required

## Detailed Attack Procedures

### Step 1: Visit the Base Domain
procedure: [[procedures/Exploit-Reflected-XSS-in-Custom-Error-URI-Path]]

**Objective**: Access the main website to confirm scope and establish a baseline.

**Instructions**: Open a web browser and navigate to the target base URL.

**Expected Output**: The main website loads successfully.

**Success Indicators**:
- Website accessible without errors
- Domain confirmed in scope

### Step 2: Navigate to the Error Page
procedure: [[procedures/Exploit-Reflected-XSS-in-Custom-Error-URI-Path]]

**Objective**: Trigger the custom error handling mechanism to reach the vulnerable endpoint.

**Instructions**: Append `/customerror` to the base URL and load it in the browser.

**Expected Output**: The custom error page displays, potentially showing error details.

**Success Indicators**:
- Error page loads without redirection
- No immediate sanitization observed

### Step 3: Append the Malicious Payload to the URI
procedure: [[procedures/Exploit-Reflected-XSS-in-Custom-Error-URI-Path]]

**Objective**: Inject a JavaScript payload into the URI path to test for reflection.

**Instructions**: Modify the URL by appending the URL-encoded payload `<Svg OnLoad=alert(1)>` (encoded as `%3CSvg%20OnLoad=alert(1)%3E`) directly to the path after `/customerror`.

**Expected Output**: The modified URL is formed, ready for execution.

**Success Indicators**:
- Payload appended without URL parsing errors
- Browser accepts the malformed path

### Step 4: Access the Final Malicious URL
procedure: [[procedures/Exploit-Reflected-XSS-in-Custom-Error-URI-Path]]

**Objective**: Load the tampered URL to execute the injected JavaScript.

**Instructions**: Enter and load the complete URL: `https://███████████████%3CSvg%20OnLoad=alert(1)%3E` in the browser.

**Expected Output**: An alert box pops up displaying '1', confirming JavaScript execution.

**Success Indicators**:
- Alert dialog appears
- No sanitization blocks the payload
- Arbitrary JS executes in victim context

## Attack Chain Summary

### Key Achievements

1. Successful identification of reflected XSS in URI path
2. Execution of arbitrary JavaScript via simple URL manipulation
3. Potential for phishing, session hijacking, or data exfiltration on DoD site

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T12:00:00Z*
