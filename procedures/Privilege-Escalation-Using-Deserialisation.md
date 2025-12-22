---
id: e7a14678-b2cd-491d-82a9-80acea43ae3c
name: Privilege-Escalation-Using-Deserialisation
type: procedure
verified: true
submitted: true
created_at: '2020-07-27T17:52:47.569921+00:00'
updated_at: '2023-05-26T18:37:47.238971+00:00'
tactics:
  - '[[Privilege-Escalation-via-Direct-URL-Access]]'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
sub_techniques: []
tags:
  - insecure-deserialization
  - owasp
  - owasp-top-10
  - web-applications
commands:
  - '[[commands/base64-decode-string]]'
  - '[[commands/base64-encode-string]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Privilege-Escalation-Using-Deserialisation

## Summary

This procedure exploits insecure deserialization in web applications that store user privileges in base64-encoded serialized cookies. By decoding the cookie, modifying the privilege flag (e.g., changing a non-admin indicator to admin), and re-encoding it, an attacker can impersonate an admin user to gain elevated access and perform restricted actions.

## Description

Web applications often serialize user session data, including roles and privileges, into cookies for stateless authentication. If the serialization lacks integrity checks (e.g., no signing or encryption), attackers can tamper with the data. This technique targets applications using formats like PHP serialize or simple key-value strings, where a flag like 's:0' denotes non-admin and 's:1' denotes admin. The exploit assumes the application deserializes the cookie blindly on the server side. It is commonly seen in legacy PHP or Java apps vulnerable to OWASP A8: Insecure Deserialization. Success grants unauthorized admin functionality, such as accessing sensitive admin panels or modifying user data.

## Requirements

- Active low-privilege user session in the target web application
- Burp Suite (or equivalent proxy like ZAP) configured to intercept HTTP traffic
- Browser with developer tools for cookie manipulation (alternative to Burp)
- Understanding of the application's serialization format (e.g., via error messages or source code leaks)
- Network access to the application (no special ports beyond standard HTTP/HTTPS)

## Defense

- Avoid serializing sensitive data in client-side cookies; use server-side sessions instead
- Implement cookie signing (e.g., HMAC) or encryption to prevent tampering
- Validate and sanitize deserialized data server-side, rejecting unexpected formats
- Use secure serialization libraries (e.g., JSON with validation over PHP serialize)
- Enable web application firewall (WAF) rules to detect anomalous cookie modifications
- Log and monitor deserialization attempts for anomalies like privilege changes

## Objectives

1. Capture and decode the serialized user cookie to inspect privilege data
2. Modify the privilege indicator to elevate user role
3. Re-encode and inject the tampered cookie to achieve admin access
4. Verify escalation by accessing admin-only features

## Instructions

### Step 1: Capture the User Cookie

**Context**: Log in as a non-admin user to establish a session. Intercept traffic to identify the _user cookie, which contains the base64-encoded serialized user object. This step ensures you have the exact cookie value before tampering.

**Tool** ([[tools/Burp-Suite]]):

Use Burp Proxy to intercept requests. Configure your browser to route through Burp (default: 127.0.0.1:8080). Navigate to a protected page and capture the Cookie or Set-Cookie header.

> Expected output: Cookie value like "dXNlcjp7InMiOjB9Cg==" (base64-encoded serialized data). If no cookie is set, check for other session mechanisms like JWTs.

### Step 2: Decode the Base64-Encoded Cookie

**Context**: The cookie is base64-encoded to obscure the serialized payload. Decoding reveals the underlying structure, allowing identification of the privilege field (e.g., 's' flag set to 0 for non-admin).

**Command** ([[commands/base64-decode-string]]):
```bash
echo "$_COOKIE_VALUE" | base64 --decode
```

> Replace $_COOKIE_VALUE with the captured cookie string. This step is performed to understand the format; use Burp Decoder for GUI alternative. Expected output: Decoded string like "user:{'s':0}", confirming non-admin status. If decoding fails, verify base64 validity.

### Step 3: Modify the Privilege Field in Serialized Data

**Context**: Edit the decoded serialized string to flip the privilege indicator. This impersonates an admin by altering the data the server will deserialize. Ensure modifications preserve the format to avoid deserialization errors.

> For example, change "s:0;" to "s:1;" in a PHP-like serialized string. Test in a text editor or Burp Repeater. If the format is complex (e.g., Java objects), use ysoserial or similar for gadget chains, but here assume simple tampering.

### Step 4: Re-Encode the Tampered Serialized Data

**Context**: Convert the modified string back to base64 to create a valid cookie. This prepares the payload for injection into the HTTP request.

**Command** ([[commands/base64-encode-string]]):
```bash
echo -n "$_MODIFIED_SERIALIZED_STRING" | base64
```

> Replace $_MODIFIED_SERIALIZED_STRING with the edited decoded content (e.g., "user:{'s':1}"). The -n flag prevents newline addition. Expected output: New base64 string like "dXNlcjp7InMiOjF9Cg==". Compare length to original to ensure no truncation.

### Step 5: Inject the Tampered Cookie and Verify Escalation

**Context**: Replace the original cookie with the new one and resubmit the request. The server deserializes the tampered data, granting admin privileges if vulnerable.

**Tool** ([[tools/Burp-Suite]]):

In Burp Repeater, update the Cookie header with the new value (e.g., _user=new_base64_value) and forward the request. Alternatively, use browser dev tools: Edit cookie in Application tab, set _user to new value, and refresh.

> Expected output: Server response grants access to admin features, such as a dashboard showing "Admin User" or new menu options. If errors occur (e.g., 500 Internal Server Error), the format may be invalid—revert and debug.
