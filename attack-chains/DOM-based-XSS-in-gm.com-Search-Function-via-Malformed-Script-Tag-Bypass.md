---
tags:
  - xss
  - dom-xss
  - internet-explorer
  - javascript
  - bypass
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Identify-Vulnerable-Search-Parameter-for-DOM-XSS]]'
  - '[[procedures/Craft-XSS-Payload-to-Bypass-Filters-in-Internet-Explorer]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
description: >-
  A multi-step attack exploiting a DOM-based XSS vulnerability in the gm.com
  search function, specific to Internet Explorer, by identifying the vulnerable
  parameter and crafting a payload to bypass filters for JavaScript execution.
skill_level: intermediate
impact_level: high
id: fe3228cf-cfb3-4d86-bdde-b708fd0ccff5
created_at: '2025-12-14T03:15:31.128Z'
updated_at: '2025-12-14T03:15:31.128Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# DOM-based XSS in gm.com Search Function via Malformed Script Tag Bypass

## Overview

This attack chain demonstrates a DOM-based Cross-Site Scripting (XSS) vulnerability in the search function of gm.com, exploitable specifically in Internet Explorer. The vulnerability arises from non-encoded GET parameters that allow malicious input to be directly injected into the DOM without sanitization. By identifying the vulnerable search parameter and crafting a payload using a malformed <script> tag (with an extra parameter and no closing tag), an attacker can bypass the site's XSS filters and execute arbitrary JavaScript in the victim's browser upon loading the search results page. This could lead to session hijacking, data theft, or further exploitation. The issue was reported via HackerOne (Report #142078) and remediated by fixing the parameter encoding.

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
    A[Identify Vulnerable Parameter] --> B[Craft and Inject Payload]
    B --> C[JavaScript Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (Internet Explorer for exploitation)
- URL encoding tools (manual or browser dev tools)

### Target Environment

- Web platform
- gm.com search function
- Internet Explorer browser

### Initial Access Requirements

- Public access to gm.com
- No credentials needed
- Victim must load the manipulated search URL in IE

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Search Parameter
procedure: [[procedures/Identify-Vulnerable-Search-Parameter-for-DOM-XSS]]

**Objective**: Test the search input to confirm non-encoded GET parameters allow DOM injection in Internet Explorer.

**Instructions**: Navigate to the gm.com search page and append a test payload to the search GET parameter, such as ?search=<script>alert(1)</script>. Observe if the input is reflected without encoding in the DOM using browser developer tools (F12 in IE). Check for direct insertion into JavaScript contexts or HTML without sanitization.

**Expected Output**: The payload appears unescaped in the page source or DOM, confirming vulnerability.

**Success Indicators**:
- Payload reflected without encoding
- No filter blocks basic script injection in IE

### Step 2: Craft and Inject XSS Payload
procedure: [[procedures/Craft-XSS-Payload-to-Bypass-Filters-in-Internet-Explorer]]

**Objective**: Develop and test a payload that evades the site's XSS filters to execute arbitrary JavaScript.

**Instructions**: Modify the payload to use a malformed <script> tag, e.g., ?search=<script xxx>alert(document.cookie)</script> (extra 'xxx' parameter and no closing tag). URL-encode if necessary and load in IE. Verify execution via alert or console log in dev tools.

**Expected Output**: JavaScript executes, displaying an alert with cookie data or similar.

**Success Indicators**:
- Filter bypassed
- Arbitrary JS runs in victim's context

## Attack Chain Summary

### Key Achievements

1. Identified DOM-based XSS in search parameter specific to IE.
2. Bypassed filters with malformed script tag for JS execution.
3. Demonstrated potential for session hijacking or data theft.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01*
