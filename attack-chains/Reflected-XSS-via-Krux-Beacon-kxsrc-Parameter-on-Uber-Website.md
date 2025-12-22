---
tags:
  - xss
  - reflected-xss
  - javascript
  - web
  - uber
  - krux
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Trigger-Reflected-XSS-via-kxsrc-Parameter]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:50.078Z'
description: >-
  A multi-stage attack chain exploiting a reflected XSS vulnerability in the
  kxsrc parameter on Uber's website, leveraging the third-party Krux beacon
  service to execute arbitrary JavaScript.
skill_level: intermediate
impact_level: high
id: e1093c9d-b004-4a9a-b622-4891c6b54496
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reflected XSS via Krux Beacon kxsrc Parameter on Uber Website

Multi-stage attack chain demonstrating a complete attack workflow exploiting a reflected Cross-Site Scripting (XSS) vulnerability in Uber's website through the 'kxsrc' parameter, which interacts with the third-party Krux beacon service (beacon.krxd.net). This allows arbitrary JavaScript execution in the victim's browser, potentially leading to session hijacking, data theft, or phishing attacks across multiple Uber subdomains including partners.uber.com, getrush.uber.com, rush.uber.com, people.uber.com, get.uber.com, and help.uber.com.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Craft Malicious URL] --> B[Execution: Load Page and Trigger Beacon]
    B --> C[Impact: Observe JavaScript Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox) for manual testing

### Target Environment

- Web platform
- Access to Uber website (www.uber.com and subdomains)
- No specific services/ports required beyond standard HTTPS (443)
- Network access to beacon.krxd.net

### Initial Access Requirements

- No credentials required
- Public internet access
- Victim must visit the crafted URL (e.g., via phishing or direct link)

## Detailed Attack Procedures

### Step 1: Craft and Visit Malicious URL
procedure: [[procedures/Trigger-Reflected-XSS-via-kxsrc-Parameter]]

**Objective**: Construct a URL with a malicious payload in the kxsrc parameter to inject JavaScript via the Krux beacon callback.

**Instructions**: Encode the malicious callback in the kxsrc parameter. For example, use a payload like alert('/XSSED/') to test execution. The full URL is: https://www.uber.com/?kxsrc=https%3A//beacon.krxd.net/optout_check%3Fcallback%3Dalert%28/XSSED/.source%29. Open this URL in a browser targeting the vulnerable endpoint.

**Expected Output**: The page loads with the Uber homepage, but the beacon service processes the callback.

**Success Indicators**:
- URL loads without errors
- Browser console shows no blocking (e.g., no CSP violations in test)

### Step 2: Wait for Page Load and Beacon Processing
procedure: [[procedures/Trigger-Reflected-XSS-via-kxsrc-Parameter]]

**Objective**: Allow the page to fully render, enabling the third-party Krux beacon to fetch and execute the injected JavaScript.

**Instructions**: After visiting the URL, wait for the page to complete loading. The beacon service at beacon.krxd.net will automatically process the optout_check endpoint with the callback parameter, injecting the JavaScript into the page context.

**Expected Output**: JavaScript from the callback executes seamlessly as part of the page load.

**Success Indicators**:
- Page fully renders without interruptions
- Network tab in browser dev tools shows request to beacon.krxd.net

### Step 3: Observe XSS Execution and Impact
procedure: [[procedures/Trigger-Reflected-XSS-via-kxsrc-Parameter]]

**Objective**: Confirm arbitrary JavaScript execution, demonstrating potential for data theft or session hijacking.

**Instructions**: Monitor the browser for the alert dialog or console output from the payload. In a real attack, replace the alert with code to steal cookies (e.g., document.cookie) or redirect to a phishing site.

**Expected Output**: Alert box pops up with '/XSSED/', confirming execution in the browser's context.

**Success Indicators**:
- Alert or custom JS effect triggers
- No sanitization blocks the callback

## Attack Chain Summary

### Key Achievements

1. Successful injection of arbitrary JavaScript via unsanitized kxsrc parameter
2. Execution across multiple Uber subdomains, expanding attack surface
3. Demonstration of high-impact risks like session hijacking and data exfiltration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
