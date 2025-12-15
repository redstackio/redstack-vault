---
id: proc-hover-xss-execute
tags:
  - payload-execution
  - js-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/insecure-url-breadcrumb]]'
  - '[[commands/insecure-coveo-url-breadcrumb]]'
  - '[[commands/insecure-static-coveo-url-breadcrumb]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:20.718Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Hover-to-Execute-XSS-Payload

## Summary

This procedure triggers the execution of the injected JavaScript payload by hovering over the vulnerable 'Search Results' breadcrumb link, demonstrating arbitrary code execution like alerts or data theft.

## Description

With the malicious href injected (e.g., '//search.informatica.com/onmouseover=alert(document.domain)'), hovering activates the onmouseover event, running the payload in the browser context. This can lead to session hijacking, cookie theft, or DOM manipulation. Similar vulnerabilities exist in constructions using document.URL, varCoveoSearchResultPageURL, and varStaticCoveoSearchResultPageURL.

## Requirements

1. Breadcrumb link already injected from prior step.
2. Mouse interaction capability in the browser.
3. Payload designed for onmouseover or similar event.

## Defense

Defensive measures and detection strategies:

- Use Content Security Policy (CSP) to block inline event handlers.
- Audit JavaScript for unescaped dynamic HTML insertion and add output encoding.

## Objectives

1. Activate the event handler in the injected href.
2. Execute arbitrary JavaScript for proof-of-concept or exploitation.
3. Validate impact through observable effects like alerts.

## Instructions

### Step 1: Locate the Breadcrumb Link

**Context**: Identify the injected 'Search Results' link in #DynamicBreadcrumb.

**Command** (Inspect DOM):
```javascript
// Browser console: document.getElementById('DynamicBreadcrumb').innerHTML
```

> View the appended <a> element. Expected output: href with payload visible.

### Step 2: Trigger on Hover

**Context**: Mouse over the link to fire onmouseover.

**Command** (Payload execution):
```javascript
// Automatic on hover: alert(document.domain)
```

> No manual command; interaction triggers it. Expected output: Alert dialog with domain.

### Step 3: Extend for Data Theft

**Context**: Replace alert with exfiltration, e.g., send cookies to attacker server.

**Command** ([[commands/insecure-url-breadcrumb]]):
```javascript
strChild = '<a href="' + document.URL + '" style="color:#fff !important;font-size:10px">Search Results</a>';
```

> Demonstrates similar vuln in URL usage. Expected output: Injectable via hover if payload in URL.

### Step 4: Test Coveo URL Variants

**Context**: Check other insecure assignments.

**Command** ([[commands/insecure-coveo-url-breadcrumb]]):
```javascript
strChild = '<a href="' + varCoveoSearchResultPageURL + '" style="color:#999 !important;" >Search Results</a>';
```

> Vulnerable if varCoveoSearchResultPageURL controlled. Expected output: Payload execution on hover.

### Step 5: Test Static Coveo Variant

**Context**: Additional case for completeness.

**Command** ([[commands/insecure-static-coveo-url-breadcrumb]]):
```javascript
strChild = '<a href="' + varStaticCoveoSearchResultPageURL + '" style="color:#999 !important;" >Search Results</a>';
```

> Similar injection point. Expected output: Confirm execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/insecure-url-breadcrumb]]
- [[commands/insecure-coveo-url-breadcrumb]]
- [[commands/insecure-static-coveo-url-breadcrumb]]

## Tools Used


## Tags

- payload-execution
- js-theft
