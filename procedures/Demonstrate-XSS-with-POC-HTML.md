---
tags:
  - xss
  - poc
  - html
type: procedure
tools:
  - '[[tools/Firefox]]'
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
updated_at: '2025-12-14T03:16:37.193Z'
sub_techniques: []
id: 17fd58a7-dab3-4799-b7a7-d2fe1a9fdac2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Demonstrate-XSS-with-POC-HTML

## Summary

This procedure creates and executes a proof-of-concept HTML file to trigger the reflected XSS in ajax-quote.php, demonstrating JavaScript execution in the victim's browser.

## Description

A simple HTML file (testpost.html) is crafted to send an AJAX request to the vulnerable endpoint with a malicious payload in the 'quote' parameter, such as a script tag. When an authenticated user visits the file (e.g., via a phishing link), the payload reflects and executes, allowing actions like alerting or manipulating the DOM. Firefox is used due to its leniency with basic payloads, potentially bypassing XSS auditors in other browsers with crafted variants. This simulates real-world exploitation where the attacker tricks users into loading the POC.

## Requirements

1. Local file system to save and open HTML POC
2. Authenticated access to support.wordcamp.org
3. Firefox browser for execution
4. Basic HTML/JavaScript knowledge

## Defense

Defensive measures and detection strategies:

- Sanitize all AJAX inputs server-side with PHP functions like esc_js
- Deploy Web Application Firewall (WAF) rules to block script payloads
- Educate users on phishing links and verify URLs
- Log and alert on suspicious AJAX requests with script content

## Objectives

1. Trigger XSS via crafted HTML file
2. Execute arbitrary JavaScript in user context
3. Demonstrate limitations like HTTPOnly cookie protection

## Instructions

### Step 1: Create POC HTML File

**Context**: Build the HTML to send the malicious request.

Create a file named testpost.html with content:

```html
<!DOCTYPE html>
<html>
<body>
<script>
// Malicious payload
fetch('https://support.wordcamp.org/wp-admin/admin-ajax.php?action=quote&quote=<script>alert('XSS');</script>');
</script>
</body>
</html>
```

Save it locally.

**Expected Output**: Valid HTML file ready for loading.

### Step 2: Execute in Browser

**Context**: Load the file to trigger the request and XSS.

Open testpost.html in [[tools/Firefox]] while authenticated on support.wordcamp.org. The script sends the request, reflecting the payload.

**Expected Output**: Alert 'XSS' appears, confirming execution; check console for errors.

### Step 3: Test Payload Variations

**Context**: Adapt payload to bypass potential filters.

Modify the script tag to use event handlers or encoded variants, e.g., `onerror=alert(1)` in an img tag, and reload.

**Expected Output**: Successful execution without auditor blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- xss
- poc
- html
- firefox
