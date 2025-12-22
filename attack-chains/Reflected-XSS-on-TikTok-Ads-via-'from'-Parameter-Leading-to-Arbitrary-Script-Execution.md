---
tags:
  - xss
  - reflected-xss
  - tiktok
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-xss-test]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Exploiting-Reflected-XSS-in-TikTok-Ads-from-Parameter]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
description: >-
  A single-stage attack exploiting a reflected XSS vulnerability in the TikTok
  ads endpoint to execute arbitrary JavaScript in victims' browsers, enabling
  session hijacking or data theft.
skill_level: beginner
impact_level: high
id: d6aa65e7-c1a5-4105-a627-135a2ef2af54
created_at: '2025-12-13T23:55:38.464Z'
updated_at: '2025-12-13T23:55:38.464Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Reflected XSS on TikTok Ads via 'from' Parameter Leading to Arbitrary Script Execution

## Overview

This attack chain demonstrates a reflected cross-site scripting (XSS) vulnerability in the TikTok ads endpoint on ads.tiktok.com. The 'from' parameter in the URL is not properly sanitized, allowing attackers to inject and execute arbitrary JavaScript code in the victim's browser when they visit a maliciously crafted link. Discovered by @imran_nisar and reported via HackerOne (Report #1452375), this vulnerability could lead to session hijacking, credential theft, or phishing attacks. The chain focuses on crafting and delivering the payload for exploitation.

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
    A[Payload Delivery] --> B[Script Execution]
    B --> C[Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools)
- Optional: [[commands/curl-xss-test]] for testing

### Target Environment

- Platform: Web application
- Services: TikTok Ads endpoint (ads.tiktok.com)
- Network access: Public internet access to the domain

### Initial Access Requirements

- No credentials required
- Victim must click a malicious link (e.g., via phishing email or social engineering)
- Attacker needs ability to host or send the malicious URL

## Detailed Attack Procedures

### Step 1: Payload Delivery and Execution
procedure: [[procedures/Exploiting-Reflected-XSS-in-TikTok-Ads-from-Parameter]]

**Objective**: Inject a malicious JavaScript payload into the 'from' parameter to execute arbitrary code in the victim's browser upon visiting the crafted URL.

**Instructions**: Construct a URL targeting the vulnerable endpoint, such as `https://ads.tiktok.com/some-endpoint?from=<script>alert('XSS')</script>`. Test the payload locally or in a controlled environment using [[commands/curl-xss-test]] to verify reflection:

```bash
curl -G "https://ads.tiktok.com/vulnerable-endpoint" --data-urlencode "from=<script>alert('XSS')</script>"
```

Deliver the URL to the victim via email, social media, or shortened link. Once clicked, the payload executes in the browser context.

**Expected Output**: The response reflects the unsanitized input, and in a browser, it triggers the script (e.g., alert popup).

**Success Indicators**:
- Payload reflected in response without encoding
- JavaScript executes (e.g., alert fires or custom payload like stealing cookies via `document.cookie`)
- Victim's session data accessible if exfiltration payload used

## Attack Chain Summary

### Key Achievements

1. Successful injection and reflection of XSS payload via 'from' parameter
2. Arbitrary JavaScript execution in victim browser
3. Potential for session hijacking or data theft from TikTok ads platform

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01*
