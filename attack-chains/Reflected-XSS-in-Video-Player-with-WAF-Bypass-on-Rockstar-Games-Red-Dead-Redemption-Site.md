---
tags:
  - xss
  - reflected-xss
  - waf-bypass
  - javascript-execution
  - session-hijacking
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
  - '[[procedures/Discover-Reflected-XSS-in-Video-Player]]'
  - '[[procedures/Demonstrate-XSS-with-WAF-Bypass-POC]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:23.288Z'
description: >-
  A multi-stage attack exploiting a reflected XSS vulnerability in the video
  player on www.rockstargames.com/reddeadredemption, including a WAF bypass to
  execute arbitrary JavaScript for potential session hijacking or data theft.
skill_level: intermediate
impact_level: medium
id: 67c44560-b71e-4f99-be91-0f65f51bf08e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174000
name: Reflected XSS in Video Player with WAF Bypass on Rockstar Games Red Dead Redemption Site
type: attack_chain
description: A multi-stage attack exploiting a reflected XSS vulnerability in the video player on www.rockstargames.com/reddeadredemption, including a WAF bypass to execute arbitrary JavaScript for potential session hijacking or data theft.
verified: false
submitted: false
step_count: 2
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: [[procedures/Discover-Reflected-XSS-in-Video-Player]], [[procedures/Demonstrate-XSS-with-WAF-Bypass-POC]]
techniques: [[Exploit Public-Facing Application]], [[JavaScript]]
tactics: [[Initial Access]], [[Execution]]
tags: xss, reflected-xss, waf-bypass, javascript-execution, session-hijacking
platforms: Web
tools: []
---

# Reflected XSS in Video Player with WAF Bypass on Rockstar Games Red Dead Redemption Site

Multi-stage attack chain demonstrating a complete attack workflow exploiting a reflected XSS in the video player feature, bypassing the WAF to enable JavaScript execution in victims' browsers.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of Reflected XSS] --> B[POC Demonstration with WAF Bypass]
    B --> C[JavaScript Execution and Impact]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser with developer tools (e.g., Chrome DevTools)
- Proxy tool like Burp Suite for payload testing (optional but recommended)

### Target Environment

- Web platform
- Access to www.rockstargames.com/reddeadredemption
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Public internet access to the target site
- No credentials required
- Researcher or ethical hacker positioning

## Detailed Attack Procedures

### Step 1: Discovery of Reflected XSS
procedure: [[procedures/Discover-Reflected-XSS-in-Video-Player]]

**Objective**: Identify the reflected XSS vulnerability in the video player where user input is echoed back without sanitization, allowing potential JavaScript injection.

**Instructions**: Navigate to the video player feature on www.rockstargames.com/reddeadredemption using a web browser. Use the developer tools to inspect how user-supplied parameters (e.g., video URL or query parameters) are handled and reflected in the page source. Test basic payloads like `<script>alert(1)</script>` in input fields related to video playback to check for unsanitized reflection.

**Expected Output**: The payload appears in the HTML source without encoding, and upon submission, it triggers a JavaScript alert or console log in the browser.

**Success Indicators**:
- User input reflected in page without HTML entity encoding
- Basic XSS payload executes in the browser context

### Step 2: POC Demonstration with WAF Bypass
procedure: [[procedures/Demonstrate-XSS-with-WAF-Bypass-POC]]

**Objective**: Craft and test a proof-of-concept payload that evades the WAF rules and successfully executes arbitrary JavaScript, demonstrating the vulnerability's exploitability.

**Instructions**: Using a proxy like Burp Suite, intercept requests to the video player endpoint. Modify parameters to include an obfuscated XSS payload, such as using case variations or encoding (e.g., `<ScRiPt>alert(document.cookie)</ScRiPt>`) to bypass WAF signature detection. Replay the request and observe the response for reflection and execution.

**Expected Output**: The WAF does not block the request, and the payload executes, potentially displaying cookies or enabling further actions like session theft simulation.

**Success Indicators**:
- Request passes through WAF without blocking
- JavaScript executes in the victim's browser context
- Potential for data exfiltration or phishing demonstrated

## Attack Chain Summary

### Key Achievements

1. Identified insufficient input sanitization in the video player leading to reflected XSS
2. Developed a WAF-bypassing POC to confirm exploitability
3. Highlighted medium-severity impact including session hijacking risks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
