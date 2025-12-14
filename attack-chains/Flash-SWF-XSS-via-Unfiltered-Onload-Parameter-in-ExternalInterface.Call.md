---
tags:
  - xss
  - flash
  - swf
  - javascript
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Exploit-Flash-SWF-XSS-with-Onload-Payload]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
description: >-
  A client-side XSS attack exploiting a Flash SWF file on polldaddy.com by
  injecting JavaScript via the onload parameter, leading to arbitrary code
  execution in the browser context.
skill_level: beginner
impact_level: high
id: fa8d3957-c7f8-47f9-be6d-9fbc52cbbe0a
created_at: '2025-12-14T03:15:53.225Z'
updated_at: '2025-12-14T03:15:53.225Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Flash SWF XSS via Unfiltered Onload Parameter in ExternalInterface.Call

## Overview

This attack chain demonstrates a Flash-based Cross-Site Scripting (XSS) vulnerability in the storage.swf file hosted on polldaddy.com. The flaw occurs because the 'onload' parameter is passed without filtering to the ExternalInterface.call function within the SWF, allowing attackers to inject and execute arbitrary JavaScript in the context of any webpage that loads the SWF. Discovered via direct testing of the SWF URL with a payload like 'alert(1)', this can lead to session hijacking, cookie theft, or other client-side attacks. The chain involves a single step to load the malicious URL, exploiting the lack of input validation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Load Malicious SWF URL] --> B[JavaScript Execution]
    B --> C[Data Theft or Session Hijack]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox) capable of loading Flash content (note: Flash is deprecated, but for historical testing, enable via legacy plugins)

### Target Environment

- Web platform
- Access to polldaddy.com's storage.swf endpoint
- No specific services or ports required beyond standard HTTP/HTTPS (port 80/443)

### Initial Access Requirements

- Public internet access
- No credentials needed; the SWF is publicly accessible
- Victim must load the SWF in their browser context (e.g., via an iframe or direct embed on a malicious site)

## Detailed Attack Procedures

### Step 1: Inject and Execute XSS Payload
procedure: [[procedures/Exploit-Flash-SWF-XSS-with-Onload-Payload]]

**Objective**: Load the SWF with a malicious 'onload' parameter to trigger arbitrary JavaScript execution in the browser.

**Instructions**: Open a web browser and navigate directly to the vulnerable SWF URL with the injected payload. For testing, use a simple alert to confirm execution. In a real attack, replace with payloads for data exfiltration (e.g., sending cookies to an attacker-controlled server).

```url
https://polldaddy.com/swf/storage.swf?onload=alert(1)
```

If Flash is disabled, embed the SWF in an HTML page for testing:

```html
<iframe src="https://polldaddy.com/swf/storage.swf?onload=alert(document.cookie)"></iframe>
```

**Expected Output**: An alert box pops up displaying '1' or the document's cookies, confirming JavaScript execution in the page context.

**Success Indicators**:
- Alert dialog appears with the payload output
- Browser console shows no errors, and JS executes without restrictions
- In advanced tests, network requests to attacker server confirm data theft

## Attack Chain Summary

### Key Achievements

1. Successful injection of JavaScript via the unfiltered 'onload' parameter
2. Arbitrary code execution in the victim's browser context
3. Potential for session hijacking or sensitive data theft from pages embedding the SWF

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
