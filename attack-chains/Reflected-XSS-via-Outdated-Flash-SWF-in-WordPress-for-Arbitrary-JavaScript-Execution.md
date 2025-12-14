---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - xss
  - reflected-xss
  - wordpress
  - flash
  - swf
  - javascript-injection
type: attack_chain
tools:
  - '[[tools/Google-Chrome]]'
  - '[[tools/Mozilla-Firefox]]'
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
  - '[[procedures/Exploit-Reflected-XSS-in-Flashmediaelement-SWF]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.673Z'
description: >-
  A multi-step attack exploiting a reflected XSS vulnerability in an outdated
  Flash media element on a WordPress site, allowing arbitrary JavaScript
  execution in the victim's browser.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Reflected XSS via Outdated Flash SWF in WordPress for Arbitrary JavaScript Execution

Multi-stage attack chain demonstrating exploitation of a reflected XSS vulnerability in the flashmediaelement.swf file on a WordPress site, leading to arbitrary JavaScript execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Browsers] --> B[Navigate to Vulnerable URL]
    B --> C[Execute and Observe Payload]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Google-Chrome]]
- [[tools/Mozilla-Firefox]]

### Target Environment

- Web platform with WordPress (version prior to 4.5.2)
- Outdated flashmediaelement.swf (version prior to 2.21.1)
- No specific ports or services required beyond HTTP/HTTPS access

### Initial Access Requirements

- Direct network access to the target site (https://business-blog.zomato.com)
- No credentials needed
- Victim must access the crafted URL (e.g., via phishing)

## Detailed Attack Procedures

### Step 1: Prepare Browsers

procedure: [[procedures/Exploit-Reflected-XSS-in-Flashmediaelement-SWF]]

**Objective**: Launch compatible browsers to test the vulnerability.

**Instructions**: Open the latest versions of Chrome and Firefox to ensure the Flash SWF file loads and processes the payload correctly in modern browsers.

**Expected Output**: Browsers are open and ready for navigation.

**Success Indicators**:
- Chrome and Firefox launched successfully
- No browser errors on startup

### Step 2: Navigate to Vulnerable URL

procedure: [[procedures/Exploit-Reflected-XSS-in-Flashmediaelement-SWF]]

**Objective**: Craft and access the URL with the injected JavaScript payload to trigger the reflected XSS.

**Instructions**: In either browser, navigate to the following URL: https://business-blog.zomato.com/wp-includes/js/mediaelement/flashmediaelement.swf?jsinitfunctio%gn=alert%601%60. The parameter 'jsinitfunctio%gn' is URL-encoded to inject 'alert(1)', which bypasses validation in the outdated SWF file.

**Expected Output**: The page loads the SWF file, and the payload is processed.

**Success Indicators**:
- URL accessed without errors
- SWF file loads in the browser

### Step 3: Execute and Observe Payload

procedure: [[procedures/Exploit-Reflected-XSS-in-Flashmediaelement-SWF]]

**Objective**: Confirm arbitrary JavaScript execution in the victim's browser context.

**Instructions**: Upon loading the URL, the SWF file improperly handles the 'jsinitfunction' parameter, executing the injected JavaScript. Observe the alert box popping up with '1'.

**Expected Output**: An alert dialog appears displaying '1', confirming JS execution.

**Success Indicators**:
- Alert box triggered
- No blocking by browser security features

## Attack Chain Summary

### Key Achievements

1. Successful injection and execution of arbitrary JavaScript via reflected XSS in an outdated Flash SWF.
2. Demonstration of impact including potential session hijacking or phishing.
3. Validation across multiple modern browsers (Chrome, Firefox).

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T12:00:00Z*
