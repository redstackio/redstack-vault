---
tags:
  - xss
  - phishing
  - credential-theft
  - web-exploit
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-XSS-in-Search-Functionality]]'
  - '[[procedures/Style-XSS-Payload-to-Mimic-UI-Elements]]'
  - '[[procedures/Exploit-Reflected-XSS-for-Phishing-Prompt]]'
  - '[[procedures/Exploit-Stored-XSS-in-Shop-Descriptions]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:28:28.187Z'
description: >-
  A multi-stage XSS attack exploiting unsanitized inputs in Reverb.com's search
  and shop description fields to inject phishing prompts that mimic locked
  account interfaces, leading to credential theft.
skill_level: intermediate
impact_level: high
id: a0ff875b-96ef-4e02-acc5-bdcab895bb06
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[T1566.002]]'
---
# Reflected and Stored XSS for Phishing Credential Theft on Reverb.com

Multi-stage attack chain demonstrating exploitation of cross-site scripting (XSS) vulnerabilities in Reverb.com's search functionality and shop descriptions to deliver persistent and reflected phishing attacks that impersonate locked account prompts, tricking users into submitting credentials to attacker-controlled sites.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of XSS in Search] --> B[Styling Payload to Mimic UI]
    B --> C[Reflected XSS Phishing Injection]
    C --> D[Stored XSS in Shop for Persistence]
    D --> E[Credential Theft via Phishing Links]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser with developer tools (e.g., Chrome DevTools for inspecting rendered HTML)

### Target Environment

- Web platform
- Access to Reverb.com marketplace
- No special services or ports required; operates over standard HTTPS

### Initial Access Requirements

- Public access to Reverb.com (no credentials needed for search testing)
- Ability to create a shop for stored XSS testing (requires free account)
- Network access to external phishing site (e.g., attacker-controlled domain)

## Detailed Attack Procedures

### Step 1: Discovery of XSS in Search Functionality
procedure: [[procedures/Discover-XSS-in-Search-Functionality]]

**Objective**: Identify that user input in the search query is not sanitized, allowing HTML tags to render directly.

**Instructions**: Navigate to the Reverb.com marketplace search page and append a query parameter with simple HTML tags to the URL, such as `/marketplace?query=<span>test</span>`. Observe the page source or rendered output to confirm the tag executes as HTML rather than escaped text.

**Expected Output**: The `<span>test</span>` renders as a styled element on the page, visible in the browser's DOM inspector.

**Success Indicators**:
- HTML tags appear in the page's rendered HTML without escaping
- No JavaScript errors or sanitization blocks the rendering

### Step 2: Styling XSS Payload to Mimic UI Elements
procedure: [[procedures/Style-XSS-Payload-to-Mimic-UI-Elements]]

**Objective**: Enhance the XSS payload by applying site-specific CSS classes to make injected elements blend with Reverb.com's legitimate UI.

**Instructions**: Modify the search query to include class attributes that match Reverb's button and alert styles, e.g., `/marketplace?query=<span class="btn button button--orange button--wide">Fake Button</span>`. Inspect the page to verify the styling applies correctly.

**Expected Output**: The injected element adopts Reverb.com's orange button styling, appearing as a native UI component.

**Success Indicators**:
- Injected elements use site CSS classes without override or rejection
- Visual inspection shows seamless integration with page design

### Step 3: Exploit Reflected XSS for Phishing Prompt
procedure: [[procedures/Exploit-Reflected-XSS-for-Phishing-Prompt]]

**Objective**: Inject a crafted phishing overlay that simulates a locked account login prompt to lure users into clicking malicious links.

**Instructions**: URL-encode a full HTML payload and inject it into the search query, e.g., `/marketplace?query=%3Cdiv%20class%3D%22fancybox-overlay%22%3E%3Cdiv%20class%3D%22fancybox-skin%22%3E%3Ch1%3EAccount%20Locked%3C/h1%3E%3Cp%3EDue%20to%20suspicious%20activity...%3C/p%3E%3Ca%20href%3D%22http%3A//badwebsite.com/login%22%3EUnlock%20Account%3C/a%3E%3C/div%3E%3C/div%3E`. Share the malicious URL via social engineering to trick victims into visiting it.

**Expected Output**: A modal-like overlay appears on the search results page with a fake login form linking to the attacker's phishing site.

**Success Indicators**:
- Payload renders as an interactive phishing interface
- Links to external phishing site are clickable and functional

### Step 4: Exploit Stored XSS in Shop Descriptions
procedure: [[procedures/Exploit-Stored-XSS-in-Shop-Descriptions]]

**Objective**: Persist the phishing payload in a shop description to affect all visitors to the shop page without needing direct URL sharing.

**Instructions**: Create or edit a shop on Reverb.com and insert the HTML payload into the description field, e.g., `<span class="bottom-alert videos-header"><strong>Log In to Reverb</strong><br><code>Due to multiple unsuccessful attempts...</code><br><a href="http://badwebsite.com"><span class="btn button button--orange button--wide">Unlock</span></a></span>`. Save and visit the shop page `/shop/this-is-bad-shop` to confirm persistence.

**Expected Output**: The phishing prompt renders on the shop page for any visitor, increasing exposure.

**Success Indicators**:
- Payload persists across page loads and sessions
- Multiple users encounter the phishing interface naturally

## Attack Chain Summary

### Key Achievements

1. Confirmed reflected XSS in search for immediate phishing delivery
2. Demonstrated UI mimicking via CSS classes for higher deception success
3. Created persistent stored XSS in shops for broad victim reach
4. Enabled credential theft through realistic locked-account impersonation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]] JavaScript (XSS execution in browser)
- [[T1566.002]] Spearphishing Link (phishing via injected links)

### MITRE ATT&CK Tactics

- [[Execution]] Execution (injecting and executing malicious scripts)
- [[Collection]] Collection (gathering credentials via phishing)

---
*Last updated: 2023-10-01T00:00:00Z*
