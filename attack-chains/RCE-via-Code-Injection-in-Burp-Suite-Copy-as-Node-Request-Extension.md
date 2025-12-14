---
tags:
  - rce
  - code-injection
  - burp-suite
  - node-js
  - cookie-injection
type: attack_chain
tools:
  - '[[tools/Copy-as-Node-Request]]'
  - '[[tools/Burp-Suite]]'
  - '[[tools/Node-js]]'
  - '[[tools/Browser-DevTools]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/set-malicious-cookie]]'
verified: false
platforms:
  - Web
  - Java
  - Node.js
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-Copy-as-Node-Request-Extension]]'
  - '[[procedures/Inject-Malicious-Cookie-via-DevTools]]'
  - '[[procedures/Intercept-Request-in-Burp-Suite]]'
  - '[[procedures/Copy-Request-as-Node-js-Code]]'
  - '[[procedures/Execute-Injected-Node-js-Code]]'
  - '[[procedures/Observe-RCE-Impact]]'
step_count: 7
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:53.873Z'
description: >-
  Multi-stage attack exploiting a code injection vulnerability in the Burp Suite
  'Copy as Node Request' extension to achieve remote code execution on the
  developer's machine through malicious cookie injection.
skill_level: intermediate
impact_level: high
id: d17b5be3-0bee-4d10-b760-6f9f995290fc
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[JavaScript]]'
---
# RCE via Code Injection in Burp Suite Copy as Node Request Extension

Multi-stage attack chain demonstrating exploitation of a code injection vulnerability in the 'Copy as Node Request' Burp Suite extension, allowing arbitrary Node.js code execution on the attacker's machine when processing a maliciously crafted HTTP request with injected cookie values.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Install Extension] --> B[Inject Cookie]
    B --> C[Intercept Request]
    C --> D[Copy as Node.js]
    D --> E[Execute Code]
    E --> F[Observe RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Copy-as-Node-Request]]
- [[tools/Burp-Suite]]
- [[tools/Node-js]]
- [[tools/Browser-DevTools]]

### Target Environment

- Burp Suite Professional or Community Edition
- Node.js runtime installed
- Web browser (e.g., Chrome) with DevTools
- Windows OS for calc.exe demonstration (adaptable to other OS)

### Initial Access Requirements

- Local machine access for tool installation and execution
- No remote network access needed; targets local developer workflow
- Basic knowledge of Burp Suite proxy setup

## Detailed Attack Procedures

### Step 1: Install Extension
procedure: [[procedures/Install-Copy-as-Node-Request-Extension]]

**Objective**: Set up the vulnerable Burp Suite extension to enable request copying as Node.js code.

**Instructions**: Download and install the 'Copy as Node Request' extension from the BApp Store.

**Expected Output**: Extension loaded in Burp Suite without errors.

**Success Indicators**:
- Extension appears in Burp's Extender tab
- No installation warnings

### Step 2: Open Target Website
**Objective**: Prepare a browser session to send a request with a malicious cookie.

**Instructions**: Launch a browser and navigate to a target site like https://example.com/.

**Expected Output**: Website loads successfully.

**Success Indicators**:
- Page accessible
- Browser proxy configured to route through Burp if needed

### Step 3: Inject Malicious Cookie
procedure: [[procedures/Inject-Malicious-Cookie-via-DevTools]]

**Objective**: Set a cookie with a payload that escapes the single-quote delimiter in the extension's generated code.

**Instructions**: Open DevTools and execute the cookie-setting command using [[commands/set-malicious-cookie]]:

```javascript
document.cookie = "test='/require('child_process').exec('calc.exe')//"
```

**Expected Output**: Cookie set; verify with `console.log(document.cookie)` showing the payload.

**Success Indicators**:
- Cookie value includes the injection payload
- No JavaScript errors in console

### Step 4: Intercept Request
procedure: [[procedures/Intercept-Request-in-Burp-Suite]]

**Objective**: Capture the HTTP request containing the malicious cookie using Burp proxy.

**Instructions**: Enable interception in Burp Suite Proxy tab, then reload the browser page to trigger the request.

**Expected Output**: Request appears in Burp's Proxy > Intercept tab with Cookie header containing payload.

**Success Indicators**:
- Request intercepted
- Cookie header visible and unescaped

### Step 5: Copy as Node.js Code
procedure: [[procedures/Copy-Request-as-Node-js-Code]]

**Objective**: Generate Node.js code from the intercepted request, embedding the injected payload.

**Instructions**: Right-click the request in Burp and select 'Copy as Node.js Request' via the extension.

**Expected Output**: Clipboard contains Node.js code with unescaped single quotes, allowing code breakout.

**Success Indicators**:
- Code copied successfully
- Inspect code for injected `require('child_process').exec('calc.exe')`

### Step 6: Execute Code
procedure: [[procedures/Execute-Injected-Node-js-Code]]

**Objective**: Run the generated Node.js code to trigger the injected RCE payload.

**Instructions**: Paste the code into a Node.js REPL or file and execute it (e.g., `node script.js`).

**Expected Output**: Node.js script runs, executing the payload.

**Success Indicators**:
- No syntax errors
- Payload executes without interruption

### Step 7: Observe Impact
procedure: [[procedures/Observe-RCE-Impact]]

**Objective**: Verify remote code execution on the local machine.

**Instructions**: Monitor for the execution of `calc.exe` or equivalent command.

**Expected Output**: Calculator application launches on Windows.

**Success Indicators**:
- calc.exe process starts
- Arbitrary code confirmed executable

## Attack Chain Summary

### Key Achievements

1. Successful injection of malicious JavaScript into a cookie to exploit single-quote escaping flaw
2. Generation of vulnerable Node.js code via Burp extension
3. Achievement of RCE leading to command execution like launching calc.exe

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Software
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Execution]] Execution

---

*Last updated: 2023-10-01T00:00:00Z*
