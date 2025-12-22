---
id: 98480aa7-0f74-4118-bd04-0518905151eb
name: 2FA-Bypass-via-Response-Manipulation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:53.929168+00:00'
updated_at: '2023-04-06T03:55:53.944949+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Multi-Factor-Authentication-Interception|T1621 - Multi-Factor
    Authentication]]
sub_techniques:
  - >-
    [[techniques/Multi-Factor-Authentication-Interception-Captured-Credentials|T1621.001
    - Captured Credentials]]
tags:
  - '[[tags/2FA Bypasses]]'
  - '[[tags/Account Takeover]]'
  - '[[tags/Response Manipulation]]'
commands:
  - '[[commands/curl-send-2fa-request]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# 2FA-Bypass-via-Response-Manipulation

## Summary

This procedure demonstrates how to bypass two-factor authentication (2FA) by intercepting and manipulating the server's JSON response during the authentication challenge. By modifying the response from indicating failure to success, an attacker can trick the client application into granting access without providing the correct 2FA code. This technique relies on man-in-the-middle (MITM) positioning and is commonly used against web applications with weak response validation.

## Description

In a typical 2FA flow, a user logs in with their username and password, triggering a 2FA challenge where they enter a time-based or app-generated code. The server validates the code and responds with a JSON object indicating success or failure, such as {"success": true} or {"success": false}. This procedure exploits vulnerabilities in the client-side handling of responses by intercepting the HTTP traffic (e.g., via a proxy) and altering the response to simulate a successful 2FA verification. This allows unauthorized access to the account, potentially leading to data theft or further compromise.

The target environment is web-based applications using HTTP/HTTPS for authentication, where the attacker has the ability to perform MITM (e.g., via ARP poisoning on the network or by controlling the proxy in a testing setup). Expected outcomes include session hijacking and full account takeover. This technique is realistic in scenarios like corporate networks or during red team engagements where traffic interception is feasible.

## Requirements

1. Network position for MITM interception (e.g., same LAN as target or configured proxy like Burp Suite).
2. Knowledge of the application's authentication endpoint URLs and JSON response structure.
3. Tools for traffic interception and modification, such as [[tools/Burp-Suite]].
4. Valid username/password for initial login to trigger the 2FA challenge.
5. Optional: SSL certificate installation on the target device to handle HTTPS traffic without warnings.

## Defense

Defensive measures and detection strategies:

- Implement certificate pinning or HSTS to prevent MITM attacks and proxy interception.
- Use end-to-end encryption for 2FA tokens and validate responses server-side with additional checks (e.g., session binding).
- Enable logging of authentication attempts and monitor for anomalous success patterns after failed 2FA submissions.
- Deploy Web Application Firewalls (WAFs) to detect response tampering attempts and enforce strict JSON validation.
- Encourage use of hardware-based 2FA (e.g., YubiKey) that cannot be easily intercepted.

## Objectives

1. Intercept the 2FA challenge response and modify it to indicate success.
2. Gain unauthorized access to the target account without the correct 2FA code.
3. Establish a persistent session for further actions like data exfiltration or privilege escalation.

## Instructions

### Step 1: Set Up Traffic Interception

**Context**: Configure a proxy tool to intercept HTTP/HTTPS traffic between the client and the authentication server. This allows inspection and modification of responses in real-time. Use [[tools/Burp-Suite]] for this purpose, as it provides a user-friendly interface for request/response manipulation.

**Instructions**: Launch Burp Suite, configure the browser proxy to 127.0.0.1:8080, and install the Burp CA certificate in the browser to handle HTTPS. Ensure the scope is set to the target application's domain.

> No specific command needed here; this is a GUI setup. Verify by browsing to the login page and confirming requests appear in Burp's Proxy history.

### Step 2: Initiate Authentication and Trigger 2FA

**Context**: Perform the initial login to reach the 2FA challenge stage. This generates the session and prompts the server to send a 2FA code (if applicable) or wait for user input.

**Command** ([[commands/curl-send-2fa-request]]):
```bash
curl -X POST https://target-app.com/api/2fa-verify \
  -H "Content-Type: application/json" \
  -H "Cookie: session_id=$_SESSION_ID" \
  -d '{"code": "$_2FA_CODE"}' \
  -k
```

> This command simulates sending an incorrect 2FA code to trigger a failure response. Replace $_SESSION_ID with the captured session cookie from the initial login, and $_2FA_CODE with a deliberately wrong code (e.g., "123456"). The -k flag ignores SSL warnings for testing. Expected output is a JSON response like {"success": false, "message": "Invalid code"}. In a real engagement, use the browser through the proxy instead of curl for interactive flow.

### Step 3: Intercept and Inspect the Failed Response

**Context**: With traffic intercepted, capture the server's response to the invalid 2FA submission. Identify the JSON field indicating failure, typically {"success": false}.

**Code** ([[codes/2FA-Failed-JSON-Response]]):

```json
{"success": false}
```

> Locate this response in Burp's Repeater or Proxy tab. Confirm the structure matches the application's format. If the response includes additional fields (e.g., error messages), note them for accurate modification.

### Step 4: Modify the Response to Simulate Success

**Context**: Alter the intercepted response to change the success indicator, tricking the client into proceeding as if 2FA was verified. This bypasses the need for the correct code.

**Code** ([[codes/2FA-Success-JSON-Response]]):

```json
{"success": true}
```

> In Burp Suite, right-click the response in the Proxy history, select "Send to Repeater," then edit the response body to replace the failure JSON with the success variant. Preserve other headers and fields (e.g., session tokens) to avoid detection. Forward the modified response to the client.

**Instructions**: Drop the original response, send the modified one, and observe the client behavior (e.g., redirect to dashboard).

### Step 5: Verify Access and Clean Up

**Context**: Confirm the bypass worked by checking if the application grants access. Monitor for any server-side validations that might invalidate the session.

**Instructions**: After forwarding the modified response, interact with the application to ensure full access (e.g., view sensitive data). If access is granted, the bypass succeeded. Clear proxy history and revert configurations to avoid leaving traces.

> Expected: Successful login without correct 2FA, with active session.
