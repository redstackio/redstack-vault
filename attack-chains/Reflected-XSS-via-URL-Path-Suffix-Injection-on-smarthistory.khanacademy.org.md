---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - xss
  - reflected-xss
  - url-injection
  - khan-academy
  - web-vulnerability
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
  - '[[procedures/Identify-Vulnerable-URL-Path-on-smarthistory-khanacademy-org]]'
  - '[[procedures/Craft-Malicious-XSS-Payload-URL]]'
  - '[[procedures/Trigger-XSS-by-Accessing-Malicious-URL]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:06.115Z'
description: >-
  A multi-step attack chain exploiting a reflected XSS vulnerability in the URL
  path suffix of the smarthistory.khanacademy.org subdomain, allowing arbitrary
  JavaScript execution to steal user data.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reflected XSS via URL Path Suffix Injection on smarthistory.khanacademy.org

Multi-stage attack chain demonstrating a complete reflected XSS workflow on the smarthistory.khanacademy.org subdomain.

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
    A[Identify Vulnerable Path] --> B[Craft Payload URL]
    B --> C[Trigger Execution]
    C --> D[Data Theft]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)
- Optional: Proxy tool like Burp Suite for URL manipulation

### Target Environment

- Web platform
- Access to http://smarthistory.khanacademy.org/
- No specific ports or services beyond HTTP/HTTPS

### Initial Access Requirements

- Public internet access to the target subdomain
- No credentials required for initial identification and testing
- Victim must access the malicious URL (e.g., via phishing)

## Detailed Attack Procedures

### Step 1: Identify Vulnerable URL Path
procedure: [[procedures/Identify-Vulnerable-URL-Path-on-smarthistory-khanacademy-org]]

**Objective**: Discover the lack of sanitization in the URL path suffix, enabling injection points after legitimate paths.

**Instructions**: Navigate to legitimate pages on smarthistory.khanacademy.org, such as http://smarthistory.khanacademy.org/Campin, and inspect the URL structure. Test by appending special characters like ">" to observe if the site reflects unsanitized input in the response.

**Expected Output**: The page renders without proper encoding, showing potential breakout from HTML context.

**Success Indicators**:
- Unsanitized path suffix reflected in HTML output
- No error or redirection on malformed URLs

### Step 2: Craft Malicious XSS Payload URL
procedure: [[procedures/Craft-Malicious-XSS-Payload-URL]]

**Objective**: Construct a proof-of-concept URL that injects and executes JavaScript by breaking out of the expected path context.

**Instructions**: Build the payload by appending a closing quote, script tag, and alert to a legitimate path, e.g., http://smarthistory.khanacademy.org/Campin"><script>alert(/BigBear/)</script>.html. Use a text editor or browser URL bar to encode if needed, ensuring the payload evades basic filters.

**Expected Output**: A valid URL that, when parsed, injects the script tag into the HTML.

**Success Indicators**:
- Payload syntax breaks out of quotes or tags
- URL is accessible without 404 errors

### Step 3: Trigger XSS by Accessing Malicious URL
procedure: [[procedures/Trigger-XSS-by-Accessing-Malicious-URL]]

**Objective**: Execute the injected JavaScript in the victim's browser context to demonstrate code execution and potential data theft.

**Instructions**: Open the crafted URL in a web browser. Observe the alert popup confirming execution. In a real attack, replace alert with code to steal cookies, e.g., document.cookie.

**Expected Output**: JavaScript alert or console log executes, proving arbitrary code runs.

**Success Indicators**:
- Alert box or script output appears
- Browser console shows no errors; payload executes

## Attack Chain Summary

### Key Achievements

1. Identified unsanitized URL path suffix for injection
2. Crafted executable XSS payload without server-side validation
3. Demonstrated client-side JavaScript execution for data exfiltration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
