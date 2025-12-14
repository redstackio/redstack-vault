---
tags:
  - crlf-injection
  - xss
  - web-vulnerability
  - header-injection
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-crlf-injection-test]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Exploit-CRLF-Injection-in-File-Name-Parameter]]'
  - '[[procedures/Inject-Headers-for-Reflected-XSS]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
description: >-
  A chained vulnerability exploiting CRLF injection in the file_name parameter
  to inject arbitrary HTTP headers, enabling reflected XSS on the internal
  PangleGlobal system.
skill_level: intermediate
impact_level: high
id: 634d2148-076d-414a-854d-a27781e1246a
created_at: '2025-12-13T23:55:37.795Z'
updated_at: '2025-12-13T23:55:37.795Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# CRLF Injection via File Name Parameter Leading to Internal XSS on PangleGlobal

## Overview

This attack chain exploits a CRLF injection vulnerability in the 'file_name' parameter of a Pangle endpoint, allowing attackers to inject arbitrary HTTP headers. By injecting a newline and crafting a malicious header, the attack escalates to a reflected cross-site scripting (XSS) vulnerability, enabling the execution of JavaScript payloads in the context of another user's browser on the internal PangleGlobal system. The chain demonstrates how unescaped user input reflection can lead to severe client-side code execution, potentially compromising user sessions or stealing sensitive data.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: CRLF Injection] --> B[Execution: Header Injection for XSS]
    B --> C[Objective: Script Execution in Victim Browser]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or proxy tool like Burp Suite for intercepting requests

### Target Environment

- Web platform with Pangle endpoints
- Access to the 'file_name' parameter in HTTP requests
- Network access to the PangleGlobal internal system

### Initial Access Requirements

- Valid user session or public access to the endpoint
- No special credentials required beyond basic user input submission
- Ability to craft and send HTTP requests with manipulated parameters

## Detailed Attack Procedures

### Step 1: Exploit CRLF Injection
procedure: [[procedures/Exploit-CRLF-Injection-in-File-Name-Parameter]]

**Objective**: Identify and confirm the CRLF injection vulnerability in the 'file_name' parameter to inject newline characters and split HTTP responses.

**Instructions**: Use [[commands/curl-crlf-injection-test]] to submit a payload with CRLF characters in the file_name parameter:

```bash
curl -X POST 'https://pangle-endpoint.example.com/upload' -d 'file_name=malicious%0d%0aTest: Injected' -v
```

Monitor the response headers for evidence of injection, such as duplicated or malformed headers.

**Expected Output**: Server response showing injected headers, e.g., a new 'Test: Injected' header appearing in the HTTP response.

**Success Indicators**:
- Injected header visible in response
- No sanitization of CRLF characters

### Step 2: Inject Headers for Reflected XSS
procedure: [[procedures/Inject-Headers-for-Reflected-XSS]]

**Objective**: Leverage the CRLF injection to add a malicious Content-Type header that reflects user input as HTML, enabling XSS payload execution.

**Instructions**: Build on the CRLF injection by crafting a payload that injects a 'Content-Type: text/html' header followed by a script tag. Submit via a tool like curl or a proxy:

```bash
curl -X POST 'https://pangle-endpoint.example.com/upload' -d 'file_name=malicious%0d%0aContent-Type:%20text/html%0d%0a%0d%0a<script>alert(document.domain)</script>' -v
```

Observe the response body for the reflected script execution when viewed in a browser context.

**Expected Output**: Response body containing the injected HTML/script, leading to JavaScript execution in the victim's browser.

**Success Indicators**:
- Malicious script reflected without escaping
- Alert or payload executes in browser

## Attack Chain Summary

### Key Achievements

1. Confirmed CRLF injection allowing arbitrary header manipulation
2. Escalated to reflected XSS via header injection
3. Achieved potential session hijacking or data theft on PangleGlobal

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01*
