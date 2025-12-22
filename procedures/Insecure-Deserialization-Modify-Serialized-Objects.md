---
id: 4f3bea07-9f6f-4e14-8bd7-8d98c276be69
name: Insecure Deserialization (Modify Serialised Objects)
type: procedure
verified: true
submitted: true
created_at: '2020-08-17T17:54:49.504695+00:00'
updated_at: '2023-05-26T18:29:26.857567+00:00'
platforms:
  - Web
tags:
  - '[[tags/Insecure Deserialization]]'
  - '[[tags/Web Applications]]'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
commands: []
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Insecure Deserialization (Modify Serialized Objects)

## Summary

This procedure exploits insecure deserialization in web applications by modifying serialized session objects, such as PHP serialized cookies, to alter attributes like user privileges. Without server-side validation during deserialization, an attacker can change boolean flags (e.g., from non-admin to admin) to gain unauthorized access to restricted resources.

## Description

Insecure deserialization vulnerabilities occur when applications unserialize user-supplied data without proper validation, allowing attackers to manipulate object attributes. In this scenario, a session cookie contains a Base64-encoded, URL-encoded serialized PHP object. By decoding it, modifying the 'admin' attribute from 'b:0' (false) to 'b:1' (true), and re-encoding, the attacker can impersonate an admin user upon resubmission. This targets web applications using PHP or similar serialization formats vulnerable to tampering. The technique assumes the application trusts the deserialized object for access control decisions.

## Requirements

1. Valid user credentials for initial login to obtain a session cookie.
2. Access to a proxy tool like [[tools/Burp-Suite]] for intercepting and modifying HTTP requests.
3. Knowledge of the serialization format (e.g., PHP serialize).
4. Target web application with insecure deserialization in session handling.

## Defense

Defensive measures and detection strategies:

- Implement strict validation and signing of serialized objects (e.g., using HMAC) to prevent tampering.
- Avoid deserializing untrusted data; use safer alternatives like JSON with type checking.
- Enable web application firewall (WAF) rules to detect anomalous cookie modifications or deserialization attempts.
- Log and monitor deserialization events, alerting on unexpected object attributes.
- Use secure session management libraries that handle serialization securely.

## Objectives

1. Obtain and decode a legitimate session cookie containing serialized data.
2. Modify sensitive attributes in the serialized object to elevate privileges.
3. Re-encode and resubmit the tampered cookie to gain unauthorized access.
4. Verify access to restricted areas, such as admin interfaces.

## Instructions

### Step 1: Login and Capture Session Cookie

**Context**: Authenticate to the application to generate a session cookie, then capture it for analysis. This establishes a baseline legitimate session.

Use [[tools/Burp-Suite]] with intercept turned off to browse normally after login. Identify the session cookie in the POST-login GET request to the root path (/).

The cookie value will appear URL-encoded and Base64-encoded. Send the request to Burp Repeater for further inspection.

**Expected Output**: HTTP response with Set-Cookie header containing the serialized session data, e.g., a cookie named 'PHPSESSID' or similar with a long encoded string.

### Step 2: Decode the Serialized Cookie

**Context**: Reveal the underlying serialized PHP object to identify modifiable attributes, such as user roles or privileges.

In Burp Decoder, first decode the cookie value as URL, then as Base64. The decoded content will show a PHP serialized string, e.g., 'O:8:"stdClass":1:{s:5:"admin";b:0;}' where 'b:0' indicates non-admin status.

Locate the 'admin' attribute and change 'b:0' to 'b:1' to set it to true.

**Expected Output**: Decoded serialized object displaying object structure, e.g., confirming the admin flag is false before modification.

### Step 3: Re-encode the Modified Object

**Context**: Prepare the tampered serialized data for resubmission by reversing the encoding process to match the original format.

After editing the serialized string, encode it as Base64, then as URL. Copy the fully re-encoded value to replace the original cookie.

**Expected Output**: New cookie value, e.g., a URL-encoded Base64 string like 'JTQ2OE...%3D' that represents the modified object.

### Step 4: Submit Tampered Cookie and Verify Access

**Context**: Test the modified session by sending the request with the new cookie to bypass authorization checks.

In Burp Repeater, replace the session cookie with the modified value and forward the request to the server.

**Expected Output**: Successful HTTP 200 response granting access to admin-only pages or interfaces, such as an admin dashboard, instead of a 403 Forbidden or redirect.

### Step 5: Validate Privilege Escalation

**Context**: Confirm the deserialization flaw allows persistent elevated access and explore restricted functionality.

Interact with the application using the tampered session to perform admin actions, such as viewing sensitive data or modifying user settings.

**Expected Output**: Access to admin features without additional authentication, e.g., navigation to /admin panel succeeding.
