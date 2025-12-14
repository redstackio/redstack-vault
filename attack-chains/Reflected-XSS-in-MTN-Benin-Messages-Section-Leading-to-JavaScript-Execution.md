---
tags:
  - xss
  - reflected-xss
  - javascript-execution
  - web-vulnerability
type: attack_chain
tools: []
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
  - '[[procedures/Navigate-to-MTN-Benin-Website]]'
  - '[[procedures/Access-Messages-Section]]'
  - '[[procedures/Inject-XSS-Payload-into-Messages-Input]]'
  - '[[procedures/Trigger-Reflected-XSS-Payload]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.901Z'
description: >-
  A multi-step attack demonstrating reflected XSS vulnerability in the Messages
  section of the MTN Benin website, allowing arbitrary JavaScript execution via
  unsanitized input reflection.
skill_level: beginner
impact_level: high
id: 6e421c25-823f-4908-89a3-d4a6a97419f4
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reflected XSS in MTN Benin Messages Section Leading to JavaScript Execution

Multi-stage attack chain demonstrating a complete reflected XSS workflow on the MTN Benin website.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Navigate to Site] --> B[Access Messages]
    B --> C[Inject Payload]
    C --> D[Trigger Execution]
    D --> E[JavaScript Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web platform
- Access to https://www.mtn.bj/
- No special services or ports required

### Initial Access Requirements

- Public internet access
- No credentials needed for initial navigation

## Detailed Attack Procedures

### Step 1: Navigate to Target Website
procedure: [[procedures/Navigate-to-MTN-Benin-Website]]

**Objective**: Gain initial access to the vulnerable website to begin the attack surface exploration.

**Instructions**: Open a web browser and directly access the target URL.

**Expected Output**: The homepage of https://www.mtn.bj/ loads successfully.

**Success Indicators**:
- Website homepage is accessible
- No access restrictions encountered

### Step 2: Access Messages Section
procedure: [[procedures/Access-Messages-Section]]

**Objective**: Locate and enter the vulnerable Messages feature where user input is processed.

**Instructions**: From the homepage, navigate to the Messages section by selecting the appropriate menu or link.

**Expected Output**: The Messages interface loads, displaying any input fields for sending or viewing messages.

**Success Indicators**:
- Messages section is accessible
- Input field for messages is visible

### Step 3: Inject XSS Payload into Input Field
procedure: [[procedures/Inject-XSS-Payload-into-Messages-Input]]

**Objective**: Introduce malicious JavaScript payload into the unsanitized input field to test for reflection.

**Instructions**: Enter the XSS payload into the messages input field and submit it.

**Expected Output**: The payload is reflected back in the page without sanitization, visible in the browser.

**Success Indicators**:
- Payload appears in the page source or rendered content
- No error or sanitization blocks the input

### Step 4: Trigger Reflected Payload
procedure: [[procedures/Trigger-Reflected-XSS-Payload]]

**Objective**: Execute the reflected JavaScript to confirm arbitrary code execution.

**Instructions**: Interact with the reflected content (e.g., right-click) to trigger the payload event.

**Expected Output**: A JavaScript alert or popup executes, such as confirming the document domain.

**Success Indicators**:
- Popup or alert displays
- JavaScript executes in the context of the victim's browser

## Attack Chain Summary

### Key Achievements

1. Successful navigation and access to the vulnerable Messages section
2. Injection and reflection of XSS payload without sanitization
3. Demonstration of arbitrary JavaScript execution via user interaction
4. Potential for impacts like session hijacking or data exfiltration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
