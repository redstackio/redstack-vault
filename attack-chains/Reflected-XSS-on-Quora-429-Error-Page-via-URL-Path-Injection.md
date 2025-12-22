---
id: 728608a9-23f4-4684-8332-55719d7dc4bb
name: Reflected XSS on Quora 429 Error Page via URL Path Injection
type: attack_chain
description: >-
  A multi-step attack exploiting a reflected XSS vulnerability on Quora's rate
  limit error page by injecting JavaScript into the Google Analytics script,
  enabling arbitrary code execution in the victim's browser.
verified: false
submitted: true
step_count: 2
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.421Z'
procedures:
  - '[[procedures/Trigger-Rate-Limit-on-Quora-Controls-Endpoint]]'
  - '[[procedures/Exploit-Reflected-XSS-via-Crafted-URL]]'
techniques:
  - '[[JavaScript]]'
tactics:
  - '[[Execution]]'
tags:
  - xss
  - reflected-xss
  - quora
  - rate-limit
  - google-analytics
  - javascript-injection
platforms:
  - Web
tools:
  - '[[tools/Firefox]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Reflected XSS on Quora 429 Error Page via URL Path Injection

Multi-stage attack chain demonstrating a complete attack workflow exploiting a reflected XSS on the 429 Too Many Requests error page of controlsyou.quora.com. The attack involves triggering the rate limit to display the vulnerable error page, then crafting a URL that injects malicious JavaScript into the Google Analytics tracking script, leading to arbitrary code execution such as alerting the document domain or stealing session data.

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
    A[Trigger Rate Limit] --> B[Inject XSS Payload]
    B --> C[Execute JavaScript]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Firefox]]

### Target Environment

- Web platform
- Access to https://controlsyou.quora.com/
- No specific services or ports required beyond standard HTTP/HTTPS

### Initial Access Requirements

- Public internet access
- No credentials needed
- Ability to make multiple HTTP requests to the target endpoint

## Detailed Attack Procedures

### Step 1: Trigger Rate Limit
procedure: [[procedures/Trigger-Rate-Limit-on-Quora-Controls-Endpoint]]

**Objective**: Exceed the rate limit on the controlsyou.quora.com endpoint to display the vulnerable 429 error page.

**Instructions**: Send a high volume of requests to any endpoint on https://controlsyou.quora.com/, such as the root path, using a browser or scripting tool. For manual testing, repeatedly refresh the page or navigate to it multiple times in quick succession until the 429 error is triggered.

**Expected Output**: The browser displays the 429 Too Many Requests error page.

**Success Indicators**:
- HTTP 429 status code received
- Error page with Google Analytics script loaded

### Step 2: Exploit Reflected XSS
procedure: [[procedures/Exploit-Reflected-XSS-via-Crafted-URL]]

**Objective**: Inject a malicious JavaScript payload into the URL path, which gets reflected unescaped into the Google Analytics script on the error page, executing arbitrary code in the victim's browser.

**Instructions**: Once the 429 error page is accessible, construct and access a URL like https://controlsyou.quora.com/'-alert(document.domain)-' using [[tools/Firefox]]. The payload in the path ('-alert(document.domain)-') breaks out of the JavaScript string in the ga('set', 'dimension1', 'board-...') call and executes the alert.

**Expected Output**: A JavaScript alert box pops up displaying the document domain (e.g., "controlsyou.quora.com").

**Success Indicators**:
- Alert executes confirming XSS
- Potential for further payloads to steal cookies or session tokens

## Attack Chain Summary

### Key Achievements

1. Successfully triggered the 429 error page exposing the vulnerable reflection point.
2. Injected and executed JavaScript via URL path manipulation in the Google Analytics script.
3. Demonstrated potential for session hijacking or data theft through arbitrary code execution.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
