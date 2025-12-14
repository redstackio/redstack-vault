---
tags:
  - xss
  - reflected-xss
  - browser-specific
  - ie
  - edge
  - svg-payload
type: attack_chain
tools:
  - '[[tools/blackfan-ru-redirector]]'
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
  - '[[procedures/Exploit-Reflected-XSS-in-404-Error-Page]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:15:31.390Z'
description: >-
  A multi-stage attack exploiting a reflected XSS vulnerability in the 404 error
  page of forum.owncloud.org, where the Request-URI is echoed without HTML
  escaping, allowing JavaScript execution in Internet Explorer and Edge browsers
  via an SVG payload.
skill_level: intermediate
impact_level: high
id: 23a86c45-3a80-4cd6-b0a7-9df7fb06b788
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Reflected XSS via Unescaped Request-URI in 404 Error Page on forum.owncloud.org

Multi-stage attack chain demonstrating a complete attack workflow exploiting a reflected Cross-Site Scripting (XSS) vulnerability in the forum.owncloud.org website's 404 error page.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Craft Malicious URL] --> B[Trigger 404 and Execute Payload]
    B --> C[JavaScript Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/blackfan-ru-redirector]]

### Target Environment

- Web platform
- Target: forum.owncloud.org
- Browsers: Internet Explorer or Edge (due to SVG parsing in error contexts)
- No specific ports or services beyond HTTP/HTTPS access

### Initial Access Requirements

- Public network access to forum.owncloud.org
- Victim must click or access the crafted URL in IE or Edge
- No credentials required

## Detailed Attack Procedures

### Step 1: Craft Malicious URL
procedure: [[procedures/Exploit-Reflected-XSS-in-404-Error-Page]]

**Objective**: Create a URL that injects an SVG payload into the Request-URI to trigger a 404 error and reflect the payload unescaped in the HTML response.

**Instructions**: Use the [[tools/blackfan-ru-redirector]] to construct the malicious URL. The payload is an SVG tag with an onload JavaScript alert: `<svg/onload=alert(document.domain)>`. Append it to the path and use double-encoded `..` (`%252e%252e`) to ensure a 404 without navigating away.

The full URL format: `https://blackfan.ru/x?r=https://forum.owncloud.org/<svg/onload=alert(document.domain)>/%252e%252e`

**Expected Output**: A redirector URL ready to be shared with the victim.

**Success Indicators**:
- URL crafted without syntax errors
- Redirector loads the target URL upon access

### Step 2: Trigger Exploitation
procedure: [[procedures/Exploit-Reflected-XSS-in-404-Error-Page]]

**Objective**: Access the crafted URL in a vulnerable browser to execute the injected JavaScript via the reflected payload in the 404 page.

**Instructions**: Open the crafted URL in Internet Explorer or Edge. The server will return a 404 error page that echoes the Request-URI in a `<p>` tag without HTML escaping, such as: `No route found for "GET /<svg/onload=alert(document.domain)>/%2e%2e"`. Due to browser-specific parsing, the SVG tag executes the onload alert showing the document domain.

**Expected Output**: An alert box pops up displaying `forum.owncloud.org`.

**Success Indicators**:
- 404 page loads with reflected payload
- JavaScript alert executes confirming XSS

## Attack Chain Summary

### Key Achievements

1. Successful injection of executable SVG payload via Request-URI
2. Arbitrary JavaScript execution in victim's browser context
3. Demonstration of browser-specific exploitation in IE and Edge

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
