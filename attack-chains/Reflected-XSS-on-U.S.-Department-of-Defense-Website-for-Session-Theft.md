---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Reflected XSS on U.S. Department of Defense Website for Session Theft
tags:
  - xss
  - reflected-xss
  - web-vulnerability
  - session-theft
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Exploit-Reflected-XSS-via-Crafted-URL]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.092Z'
description: >-
  A single-stage attack exploiting a reflected XSS vulnerability on a DoD
  website to inject and execute malicious JavaScript via a crafted URL, enabling
  session hijacking or content manipulation.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Reflected XSS on U.S. Department of Defense Website for Session Theft

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Crafted URL] --> B[Execution of Malicious Script]
    B --> C[Session Theft or Content Modification]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser with developer tools (e.g., Chrome DevTools)
- Optional: Proxy tool like Burp Suite for URL crafting

### Target Environment

- Target: Public-facing DoD website
- Required services/ports: HTTP/HTTPS on port 80/443
- Network access requirements: Internet access to the target URL

### Initial Access Requirements

- No credentials required (public site)
- Victim must click the crafted link
- No prior access needed

## Detailed Attack Procedures

### Step 1: Craft and Deliver Malicious URL
procedure: [[procedures/Exploit-Reflected-XSS-via-Crafted-URL]]

**Objective**: Inject malicious JavaScript into the site's response by appending a payload to a vulnerable URL parameter, tricking the victim into executing it in their browser.

**Instructions**: Identify a vulnerable parameter (e.g., search query) on the DoD website. Append a reflected XSS payload such as `<script>alert('XSS')</script>` to the URL. For testing, use a browser to visit the crafted URL. To simulate delivery, share the link via email or social engineering.

Use [[commands/curl-xss-test]] to verify the payload reflection:

```bash
curl "https://example-dod-site.gov/search?q=<script>alert('XSS')</script>" -v
```

Then, open the URL in a browser to execute the script.

**Expected Output**: The browser executes the script, e.g., an alert box pops up, confirming XSS. In a real attack, the script could exfiltrate cookies via `document.cookie`.

**Success Indicators**:
- Payload reflected unsanitized in the page source
- JavaScript executes (e.g., alert triggers)
- Session cookies accessible via script

## Attack Chain Summary

### Key Achievements

1. Successful injection and execution of malicious JavaScript on a high-security DoD site
2. Potential for session theft, enabling unauthorized access
3. Demonstration of impact through content modification or data exfiltration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T12:00:00Z*
