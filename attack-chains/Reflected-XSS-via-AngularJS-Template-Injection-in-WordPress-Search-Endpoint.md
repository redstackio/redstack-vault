---
tags:
  - xss
  - angularjs
  - wordpress
  - reflected-xss
  - template-injection
type: attack_chain
tools:
  - '[[tools/Web-Browser]]'
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
  - '[[procedures/Discover-AngularJS-Template-Injection-Vulnerability]]'
  - '[[procedures/Exploit-Reflected-XSS-with-AngularJS-Payload]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:25.548Z'
description: >-
  A multi-stage attack exploiting AngularJS template injection in the search
  functionality of mercantile.wordpress.org to achieve reflected XSS and execute
  arbitrary JavaScript.
skill_level: intermediate
impact_level: high
id: 5dae2495-2297-408b-bc40-bc40d948dc18
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Reflected XSS via AngularJS Template Injection in WordPress Search Endpoint

Multi-stage attack chain demonstrating a complete attack workflow exploiting unsanitized user input in the search endpoint of mercantile.wordpress.org to inject and evaluate AngularJS templates, leading to reflected XSS.

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
    A[Discovery of Template Injection] --> B[Payload Injection and Execution]
    B --> C[Arbitrary JavaScript Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Web-Browser]]

### Target Environment

- Web platform with WordPress and AngularJS integration
- Access to the search endpoint (/search/)
- Vulnerable browsers like Firefox or Safari

### Initial Access Requirements

- Public network access to mercantile.wordpress.org
- No credentials required
- Direct URL manipulation capability

## Detailed Attack Procedures

### Step 1: Discovery of AngularJS Template Injection
procedure: [[procedures/Discover-AngularJS-Template-Injection-Vulnerability]]

**Objective**: Identify if the search endpoint evaluates AngularJS expressions without sanitization by testing a simple mathematical payload.

**Instructions**: Navigate to the search endpoint and submit a test query using the browser's address bar or search form. Enter the payload `{{2*2}}` as the search term in the URL: `https://mercantile.wordpress.org/search/{{2*2}}`. Observe the page title in the browser.

**Expected Output**: The page title renders the evaluated result `4` instead of the literal string `{{2*2}}`, confirming AngularJS template processing.

**Success Indicators**:
- Page title shows `4`
- No errors in console; expression is silently evaluated

### Step 2: Exploit Reflected XSS with Payload
procedure: [[procedures/Exploit-Reflected-XSS-with-AngularJS-Payload]]

**Objective**: Inject a malicious AngularJS payload to execute arbitrary JavaScript, such as an alert displaying the document domain, demonstrating XSS.

**Instructions**: Modify the search URL to include the exploit payload: `https://mercantile.wordpress.org/search/{{constructor.constructor('alert(document.domain)')()}}`. Load the page in a vulnerable browser like Firefox or Safari.

**Expected Output**: An alert box pops up displaying the document domain (e.g., `mercantile.wordpress.org`), confirming JavaScript execution.

**Success Indicators**:
- Alert executes on page load
- Document domain is revealed
- Potential for further payloads to steal cookies or perform other actions

## Attack Chain Summary

### Key Achievements

1. Confirmed AngularJS template injection in the search endpoint's page title rendering.
2. Achieved reflected XSS by executing arbitrary JavaScript via constructor injection.
3. Demonstrated potential for session hijacking or client-side attacks in vulnerable browsers.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
