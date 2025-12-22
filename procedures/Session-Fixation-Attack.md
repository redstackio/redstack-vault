---
id: 76f1cd51-8b65-4328-8ee3-882ad61e94f1
name: Session-Fixation-Attack
type: procedure
verified: true
submitted: true
created_at: '2020-08-06T14:09:37.643261+00:00'
updated_at: '2023-05-26T18:37:59.803174+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Steal Web Session Cookie]]'
sub_techniques: []
tags:
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Session Fixation]]'
  - '[[tags/Session Management]]'
  - '[[tags/Web Applications]]'
  - session-hijacking
  - authentication-bypass
commands:
  - '[[commands/curl-initial-app-access]]'
  - '[[commands/curl-fixed-session-url]]'
  - '[[commands/curl-login-with-fixed-session]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Session-Fixation-Attack

## Summary

This procedure demonstrates how to perform a session fixation attack on a web application by crafting a URL with a predefined session identifier, tricking the application into reusing it post-authentication, allowing an attacker to hijack the authenticated session without stealing credentials directly.

## Description

Session fixation exploits poor session management in web applications where the session ID is set via a URL parameter (e.g., ?PHPSESSID=attacker_id) before login and remains unchanged after authentication. This allows an attacker to fix the victim's session to one they control. The attack targets applications that do not regenerate session IDs upon login, violating secure session handling practices like those in OWASP guidelines. It is effective against public-facing web apps with URL-based session passing, leading to unauthorized access to user accounts. Prerequisites include identifying a vulnerable endpoint that accepts session IDs via GET parameters and the ability to direct a victim to the crafted URL, such as via phishing.

## Requirements

1. Access to a vulnerable web application that sets session IDs via URL parameters (e.g., PHPSESSID, JSESSIONID).
2. Attacker-controlled session ID (generate one by accessing the app anonymously).
3. Tools for intercepting and modifying HTTP requests, such as a proxy (e.g., [[tools/Burp-Suite]]).
4. Victim's email or credentials for login simulation; in real attacks, lure the victim to the fixed URL.
5. Network access to the target application (no special privileges needed beyond public access).

## Defense

Defensive measures and detection strategies:

- Regenerate session IDs on every authentication event using secure random generation.
- Avoid passing session IDs in URLs; use secure cookies with HttpOnly, Secure, and SameSite=Strict flags.
- Implement server-side checks for session ID changes post-login and log anomalies.
- Use web application firewalls (WAFs) to detect and block URL-based session parameters.
- Monitor for multiple logins from the same session ID across different IP addresses.

## Objectives

1. Fix the victim's session to an attacker-controlled ID before authentication.
2. Confirm the session ID persists after login, enabling hijacking.
3. Gain unauthorized access to the authenticated user's session data and actions.

## Instructions

### Step 1: Access the Application and Capture Initial Session

**Context**: Begin by accessing the login or home page of the target application to establish an initial session and observe that no cookies are set initially, confirming URL-based session handling.

**Command** ([[commands/curl-initial-app-access]]):
```bash
curl -v "http://target-app.com/login.php" -c cookies.txt
```

> This command fetches the initial page and saves any cookies (expected to be none for vulnerable apps). Use verbose output (-v) to inspect headers. If using a proxy like Burp Suite, route traffic through it to intercept requests.

### Step 2: Craft URL with Fixed Session Identifier

**Context**: Generate or capture an attacker-controlled session ID, then craft a URL that includes it as a parameter to fix the session in the victim's browser upon access.

**Command** ([[commands/curl-fixed-session-url]]):
```bash
curl -v "http://target-app.com/login.php?PHPSESSID=$_ATTACKER_SESSION_ID" -b cookies.txt -c cookies.txt
```

> Replace $_ATTACKER_SESSION_ID with your controlled ID (e.g., from a prior anonymous access). This simulates directing the victim to the URL. Expected: The app accepts the fixed ID without setting a new one. In a browser, send this URL to the victim via email or link.

### Step 3: Authenticate and Verify Session Persistence

**Context**: Have the victim (or simulate) log in using the fixed session URL, then confirm the session ID remains unchanged, allowing the attacker to reuse it.

**Command** ([[commands/curl-login-with-fixed-session]]):
```bash
curl -v -X POST "http://target-app.com/login.php" -d "username=$_USERNAME&password=$_PASSWORD&PHPSESSID=$_ATTACKER_SESSION_ID" -b cookies.txt -c cookies.txt
```

> Submit login credentials with the fixed session ID. Expected: Successful authentication response without session regeneration (e.g., 200 OK with user dashboard). Now, the attacker can access the same URL with the fixed ID to hijack the session. Decision point: If login fails or ID changes, the app is not vulnerable—abort and report as secure.
