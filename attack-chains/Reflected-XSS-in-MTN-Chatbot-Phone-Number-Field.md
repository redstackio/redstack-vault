---
tags:
  - xss
  - reflected-xss
  - web-vulnerability
  - chatbot
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
  - '[[procedures/Exploit-Reflected-XSS-in-Chatbot-Input]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:31.317Z'
description: >-
  A multi-step attack exploiting a reflected XSS vulnerability in the MTN Ghana
  website's chatbot phone number input field to execute arbitrary JavaScript.
skill_level: beginner
impact_level: high
id: c3aa51eb-ccf3-4371-83e8-0eb72f3f9a5c
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Reflected XSS in MTN Chatbot Phone Number Field

Multi-stage attack chain demonstrating a complete attack workflow exploiting a reflected cross-site scripting vulnerability in the MTN Ghana website's chatbot.

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
    A[Navigate to Website] --> B[Interact with Chatbot]
    B --> C[Inject XSS Payload]
    C --> D[Execute and Observe]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web platform
- Access to https://mtn.com.gh/
- No special services or ports required beyond standard HTTP/HTTPS

### Initial Access Requirements

- Public internet access
- No credentials needed
- Direct navigation to the target site

## Detailed Attack Procedures

### Step 1: Navigate to the Target Website
procedure: [[procedures/Exploit-Reflected-XSS-in-Chatbot-Input]]

**Objective**: Access the vulnerable MTN Ghana website to begin the interaction.

**Instructions**: Open a web browser and navigate to the target URL.

**Expected Output**: The homepage of https://mtn.com.gh/ loads successfully.

**Success Indicators**:
- Website homepage is accessible
- No access restrictions encountered

### Step 2: Interact with the MTN Chatbot
procedure: [[procedures/Exploit-Reflected-XSS-in-Chatbot-Input]]

**Objective**: Locate and open the chatbot feature to access the vulnerable input field.

**Instructions**: On the homepage, locate and click the MTN chat feature icon, then find the phone number input field within the chatbot interface.

**Expected Output**: Chatbot window opens with a phone number entry field visible.

**Success Indicators**:
- Chatbot interface is active
- Phone number field is present and interactive

### Step 3: Enter XSS Payload in the Phone Number Field
procedure: [[procedures/Exploit-Reflected-XSS-in-Chatbot-Input]]

**Objective**: Inject a malicious payload into the unsanitized input field to test for reflection.

**Instructions**: In the phone number field, enter the XSS payload `<button onClick="alert('xss')">Submit</button>` and submit the form.

**Expected Output**: The payload is submitted and reflected back into the page without sanitization.

**Success Indicators**:
- Payload is accepted without validation errors
- Form submission proceeds

### Step 4: Observe Execution of the Payload
procedure: [[procedures/Exploit-Reflected-XSS-in-Chatbot-Input]]

**Objective**: Confirm the vulnerability by verifying JavaScript execution in the victim's browser context.

**Instructions**: Upon submission, interact with the reflected element (e.g., click the button if rendered) to trigger the script.

**Expected Output**: An alert box displays with the message 'xss', indicating successful JavaScript execution.

**Success Indicators**:
- Alert box pops up
- Arbitrary code execution is confirmed

## Attack Chain Summary

### Key Achievements

1. Successful navigation and interaction with the vulnerable chatbot
2. Injection and reflection of XSS payload without sanitization
3. Execution of arbitrary JavaScript, demonstrating potential for session hijacking or data theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
