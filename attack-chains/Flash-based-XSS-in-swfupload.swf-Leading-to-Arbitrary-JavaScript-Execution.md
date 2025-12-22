---
id: ac-flash-xss-swfuplad
name: Flash-based XSS in swfupload.swf Leading to Arbitrary JavaScript Execution
tags:
  - xss
  - flash
  - swf
  - javascript
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Flash-XSS-via-movieName-Parameter]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.218Z'
description: >-
  A cross-site scripting attack exploiting improper input handling in the
  movieName parameter of a Flash SWF file, allowing arbitrary JavaScript
  execution in the victim's browser context.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Flash-based XSS in swfupload.swf Leading to Arbitrary JavaScript Execution

Multi-stage attack chain demonstrating a complete attack workflow exploiting a Flash-based XSS vulnerability in the swfupload.swf file hosted on app.mavenlink.com.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Vulnerable SWF] --> B[Inject Malicious Payload]
    B --> C[Execute Arbitrary JavaScript]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser supporting Flash (e.g., older versions of Chrome or Firefox with Flash enabled)

### Target Environment

- Web platform
- Flash-enabled environment
- Access to https://app.mavenlink.com/flash/swfupload.swf

### Initial Access Requirements

- No credentials required
- Public internet access to the target URL
- No prior access needed

## Detailed Attack Procedures

### Step 1: Exploit Flash XSS
procedure: [[procedures/Exploit-Flash-XSS-via-movieName-Parameter]]

**Objective**: Inject a malicious payload into the movieName parameter to break out of the string context in the Flash file and execute arbitrary JavaScript, such as alerting the document domain to demonstrate control.

**Instructions**: Craft a URL with the injected payload targeting the vulnerable SWF file. Open the URL in a Flash-enabled browser to trigger the execution.

The payload breaks out of the expected string by closing quotes and injecting JavaScript code.

**Expected Output**: An alert box displaying the document domain (e.g., "app.mavenlink.com"), confirming JavaScript execution in the site's context.

**Success Indicators**:
- Alert dialog appears showing the document domain
- No Flash errors; payload executes silently in background for stealthier attacks

## Attack Chain Summary

### Key Achievements

1. Successful injection and execution of arbitrary JavaScript via Flash parameter
2. Demonstration of potential for session hijacking or data theft
3. Exploitation affects all users across browsers supporting Flash

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
