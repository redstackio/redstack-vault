---
id: proc-algolia-xss-injection
tags:
  - xss
  - stored-xss
  - parameter-injection
  - cloudflare-bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.717Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Algolia-Explorer

## Summary

This procedure exploits a stored XSS vulnerability in Algolia's UI demo generation feature by modifying the 'name' attribute of form input elements to inject JavaScript payloads. The injection bypasses CloudFlare protections by embedding the payload in the parameter name, leading to arbitrary code execution when victims view the shared demo page.

## Description

In Algolia's explorer at https://www.algolia.com/explorer, the UI demo generation process renders user-provided attribute values directly into JavaScript code on the output demo page without proper escaping. By inspecting and altering the HTML 'name' attribute of inputs (e.g., primary_attribute), an attacker can inject payloads like '+document.write`${unescape`%3cimg%20src%3dx%20onerror%3dalert%28document.domain%29%3e`}`+' which evades value-based filtering. Once generated and shared, the demo URL triggers the XSS in any viewer's browser, enabling actions like session theft or data exfiltration. This affects all users accessing the link, making it a persistent cross-user attack.

## Requirements

1. Authenticated Algolia account with access to the explorer
2. Modern web browser with developer tools (e.g., Chrome, Firefox)
3. Direct internet access to https://www.algolia.com

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and escaping for all form attributes, including 'name' fields, when rendering to JavaScript
- Use Content Security Policy (CSP) to restrict inline script execution and eval-like functions on demo pages
- Monitor for anomalous JavaScript in backend-stored demo configurations and alert on suspicious patterns like unescaped HTML entities
- Employ WAF rules that inspect parameter names for JS payloads, beyond just values

## Objectives

1. Inject and store a JavaScript payload in the demo configuration
2. Bypass CloudFlare by using parameter name injection
3. Achieve arbitrary code execution in victim browsers via shared links

## Instructions

### Step 1: Access and Initiate Demo Generation

**Context**: Authenticate and start the vulnerable workflow to reach editable form fields.

Log in to Algolia and navigate to https://www.algolia.com/explorer. Click "GENERATE A UI DEMO" at the bottom right, enter a title, and click "NEXT" to reach the attribute fields.

### Step 2: Inspect and Modify Input Element

**Context**: Use dev tools to alter the input's name attribute for payload injection.

Right-click the Primary attribute field, select "Inspect Element", and change the name to: `engine[primary_attribute]['+document.write`${unescape`%3cimg%20src%3dx%20onerror%3dalert%28document.domain%29%3e`}`+']`.

> This payload decodes to an <img> tag with an onerror handler that alerts the domain, demonstrating execution. The unescape and template literal obscure it from basic filters.

### Step 3: Submit and Generate Demo

**Context**: Store the payload server-side and create the malicious demo.

Click "NEXT" to submit, then "GENERATE UI & SHARE". Copy the resulting URL (e.g., https://www.algolia.com/realtime-search-demo/some-title).

### Step 4: Verify and Exploit

**Context**: Test execution and share for victim impact.

Load the demo URL to see the alert. Share with another session to confirm cross-user execution.

> Expected: Alert fires on load, proving stored XSS success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss
- algolia
- javascript
