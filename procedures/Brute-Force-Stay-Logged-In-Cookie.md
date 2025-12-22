---
id: 3eb43c75-dfcc-423c-882f-c4ae8625bdde
name: Brute-Force-Stay-Logged-In-Cookie
type: procedure
verified: true
submitted: true
created_at: '2020-09-03T18:13:33.631001+00:00'
updated_at: '2023-05-26T18:50:37.090970+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Brute Force]]'
sub_techniques: []
tags:
  - broken-authentication
  - web-applications
commands:
  - '[[commands/hashcat-crack-md5]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Brute-Force-Stay-Logged-In-Cookie

## Summary

This procedure demonstrates how to brute-force a vulnerable stay-logged-in cookie mechanism in a web application. The cookie stores the username concatenated with an MD5 hash of the password, base64-encoded, allowing an attacker to crack the hash for their own account and then brute-force other users' passwords using a wordlist to achieve account takeover.

## Description

Many web applications implement a 'stay-logged-in' feature to keep users authenticated across browser sessions, often using a persistent cookie. In vulnerable implementations, this cookie may insecurely store credentials like username:MD5(password) in base64 format without proper validation or rate limiting. An attacker with initial access to one account can decode their own cookie, crack the MD5 hash to recover the plaintext password, and then use automated tools to generate and test cookie payloads for target usernames (e.g., 'carlos') against a password list. Success is indicated by responses revealing account-specific content, leading to unauthorized access without direct credential submission. This targets broken authentication mechanisms and is commonly seen in legacy or poorly designed login systems.

## Requirements

1. Burp Suite Professional (for proxying and Intruder functionality)
2. Valid credentials for an initial user account (e.g., 'wiener')
3. A wordlist of potential passwords (e.g., rockyou.txt)
4. Network access to the target web application
5. Basic knowledge of Burp Suite navigation and payload processing rules

## Defense

Defensive measures and detection strategies:

- Implement secure session management with HTTPOnly, Secure, and SameSite cookies to prevent client-side access and manipulation.
- Use strong hashing algorithms like bcrypt or Argon2 for any stored credentials; avoid MD5.
- Enforce rate limiting on login and cookie validation endpoints to detect brute-force attempts.
- Monitor for anomalous cookie modifications and unusual response patterns (e.g., grep for account-specific strings in logs).
- Validate cookie integrity with HMAC signatures to prevent tampering.

## Objectives

1. Analyze and crack the MD5 hash in the attacker's stay-logged-in cookie to recover the plaintext password.
2. Generate and test brute-force cookie payloads for a target user account using a password wordlist.
3. Achieve account takeover by identifying a valid cookie that grants access without credentials.
4. Expected outcome: Unauthorized access to the target account, demonstrated by loading protected pages.

## Instructions

### Step 1: Login and Capture the Stay-Logged-In Cookie

**Context**: Proxy traffic through Burp Suite to intercept the login request and identify the stay-logged-in cookie set upon successful authentication. This cookie will be the starting point for analysis.

**Instructions**: Configure your browser to use Burp as a proxy. Navigate to the login page, enter credentials for a known user (e.g., wiener:peter), and submit. In the Burp Proxy history, locate the response setting the stay-logged-in cookie.

**Expected Output**: A Set-Cookie header like `stay-logged-in=base64_encoded_value` in the login response.

### Step 2: Decode and Analyze the Cookie

**Context**: Use Burp's Decoder to reveal the cookie's structure, confirming it contains username:MD5(password) format. This step verifies the vulnerability before proceeding to cracking.

**Instructions**: In Burp's Proxy or Repeater, right-click the cookie value and select 'Send to Decoder'. In the Decoder tab, apply 'Base64 - Decode' to reveal the inner content, which should appear as `username:md5hash` (e.g., `wiener:51dc30ddc473d43a6011e9ebba6ca770`).

**Expected Output**: Decoded string showing username followed by a 32-character MD5 hash.

### Step 3: Crack the MD5 Hash to Recover Password

**Context**: Extract the MD5 hash from the decoded cookie and use an offline cracking tool to recover the plaintext password. This confirms the weakness of MD5 and provides the known password for payload generation.

**Command** ([[commands/hashcat-crack-md5]]):

Use Hashcat to crack the MD5 hash against a wordlist.

```bash
hashcat -m 0 -a 0 hash.txt wordlist.txt
```

> This command attempts dictionary attacks on the MD5 hash file. Replace `hash.txt` with a file containing the extracted hash (e.g., `51dc30ddc473d43a6011e9ebba6ca770`). Expected output includes the cracked password if it matches the wordlist (e.g., 'peter').

**Expected Output**: Cracked password displayed, such as `peter:51dc30ddc473d43a6011e9ebba6ca770`.

### Step 4: Prepare Intruder for Cookie Brute-Force

**Context**: Logout and capture the GET request to the root path (/), then configure Burp Intruder to brute-force the cookie by marking the stay-logged-in value as a payload position. This sets up automated testing of modified cookies.

**Instructions**: After logging out, intercept the GET / request in Burp Proxy and send it to Intruder. In the Positions tab, highlight the stay-logged-in cookie value (e.g., §base64_value§) and click 'Add §' to mark it as the payload position.

**Expected Output**: Intruder request template with the cookie value highlighted as §stay-logged-in§.

### Step 5: Configure Payload Processing for Valid Cookie Generation

**Context**: Set up payload processing rules to transform input payloads (passwords) into valid cookie formats: MD5 hash the password, prefix with username, and base64-encode. Test with the known password first to validate the setup.

**Instructions**: In the Payloads tab, set Payload type to 'Simple list' and add the known password (e.g., 'peter'). Under Payload Processing, add rules in sequence: 'Hash: MD5', then 'Add prefix: wiener:', then 'Encode: Base64-encode'. In Options, add a Grep - Match rule for 'My account' to identify successful logins. Start the attack.

**Expected Output**: Quick attack completion with one response containing 'My account', confirming the processed payload reconstructs a valid cookie.

### Step 6: Execute Brute-Force Attack on Target User

**Context**: Modify the prefix to the target username (e.g., 'carlos') and use a full password wordlist to generate and test cookies. Monitor for responses indicating successful authentication.

**Instructions**: Reset the attack. Change the 'Add prefix' rule to 'carlos:'. Set Payload type to 'Simple list from file' and load a password wordlist (e.g., rockyou.txt). Retain the MD5 hash and Base64-encode rules. Add the same Grep - Match for 'My account'. Start the attack and review results.

**Expected Output**: Multiple responses processed; one or more containing 'My account' if a password match is found.

### Step 7: Validate Account Takeover

**Context**: Identify the successful payload, reconstruct the valid cookie, and test it in the browser to confirm unauthorized access to the target account.

**Instructions**: Right-click the successful response (with 'My account'), select 'Copy URL', and paste it into your browser (ensuring Burp proxy is active). Alternatively, manually set the stay-logged-in cookie in the browser's developer tools using the successful payload.

**Expected Output**: Browser loads the page as the target user (e.g., 'carlos'), showing account-specific content without prompting for credentials.

**Success Indicators**:
- Valid cookie generates a response with account dashboard content.
- Browser access confirms session hijacking.
