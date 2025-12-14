---
id: proc-uuid-5678
tags:
  - xss
  - stored-xss
  - web
  - duckduckgo
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/access-duckduckgo-vulnerable-search-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.812Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-DuckDuckGo-Stored-XSS-via-Search-Query

## Summary

This procedure exploits a stored XSS vulnerability in DuckDuckGo's search results by using a crafted query that pulls in unsanitized HTML from Urban Dictionary, allowing arbitrary JavaScript execution on the search page.

## Description

The vulnerability arises from DuckDuckGo's integration of external content from sites like urbandictionary.com without proper HTML escaping. A pre-existing malicious payload on Urban Dictionary, such as an img tag with onerror JavaScript, is rendered directly in the search results iframe or content area. This leads to stored XSS, where the payload executes for any user searching the vulnerable term. The attack enables data theft, session hijacking, or phishing on the trusted duckduckgo.com domain. Prerequisites include a web browser and internet access; no authentication is needed. Expected outcomes include JS alerts or console logs confirming execution, with potential for more severe impacts like cookie exfiltration.

## Requirements

1. Web browser with developer tools enabled for inspection
2. Access to DuckDuckGo search engine
3. Knowledge of the vulnerable query pattern involving Urban Dictionary

## Defense

Defensive measures and detection strategies:

- Implement strict Content Security Policy (CSP) to block inline scripts and unsafe eval
- Sanitize all external HTML content using libraries like DOMPurify before rendering
- Monitor for anomalous JS execution in search result logs and use WAF rules to detect common XSS payloads

## Objectives

1. Execute arbitrary JavaScript in the context of duckduckgo.com
2. Demonstrate potential for user data collection or session manipulation
3. Validate the vulnerability for reporting and remediation

## Instructions

### Step 1: Craft and Submit Vulnerable Search Query

**Context**: Use a search query that triggers the integration of vulnerable Urban Dictionary content, embedding the stored payload.

**Command** ([[commands/access-duckduckgo-vulnerable-search-url]]):
```bash
# Browser-based: Navigate to https://duckduckgo.com/ and search for 'urban dictionary "><img src=x<'
# Or via curl for initial fetch
curl "https://duckduckgo.com/?q=urban%20dictionary%20%5C%22%3E%3Cimg%20src%3Dx%3C" -o search_results.html
```

> This command fetches the search results containing the unsanitized payload. Open the HTML in a browser to trigger rendering. Expected output: Page source shows injected <img> tag from Urban Dictionary.

### Step 2: Inspect and Confirm Payload Execution

**Context**: Load the results and observe the XSS firing, such as through an alert or network requests initiated by the payload.

**Command** ([[commands/access-duckduckgo-vulnerable-search-url]]):
```bash
# Direct URL access for reproduction
curl "https://duckduckgo.com/?q=urban+dictionary+%22%3E%3Cimg+src%3Dx%3C&t=ffab&atb=v1-1&ia=web" --user-agent "Mozilla/5.0" -o vulnerable_page.html
# Inspect vulnerable_page.html for <img src=x onerror=alert(1)> or similar
```

> The payload executes on load, potentially showing an alert('XSS') if the stored script is alert-based. Expected output: JavaScript execution in browser console or visible effects like popups.

### Step 3: Validate Impact with Custom Payload Test

**Context**: If possible, test exfiltration by modifying observation for data theft simulation.

No specific command; use browser dev tools to simulate JS like document.cookie in console post-execution.

> Confirm domain context (duckduckgo.com) allows access to user session data. Expected output: Ability to read cookies or perform fetches.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/access-duckduckgo-vulnerable-search-url]]

## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[web]]
- [[duckduckgo]]
