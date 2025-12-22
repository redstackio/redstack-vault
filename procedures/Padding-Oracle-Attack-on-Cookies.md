---
id: b88947f8-6d78-48e4-8de9-4dbeb4b03c2c
name: Padding-Oracle-Attack-on-Cookies
type: procedure
verified: true
submitted: true
created_at: '2019-10-24T00:47:43.960526+00:00'
updated_at: '2023-05-26T00:44:49.809719+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
platforms:
  - Web
tags:
  - '[[tags/Cryptography]]'
  - '[[tags/Web Applications]]'
commands:
  - '[[commands/padbuster-decrypt-cookie]]'
  - '[[commands/padbuster-encrypt-plaintext-to-cookie]]'
tools:
  - '[[tools/PadBuster]]'
  - '[[tools/Burp Suite]]'
validated: true
---

# Padding-Oracle-Attack-on-Cookies

## Summary

This procedure demonstrates how to exploit a padding oracle vulnerability in CBC-mode encrypted cookies to decrypt sensitive data like usernames and encrypt arbitrary plaintext to impersonate users. By leveraging the server's padding validation responses, an attacker can brute-force byte-by-byte decryption and encryption without knowing the encryption key, enabling credential access in web applications using vulnerable cryptography.

## Description

Padding oracle attacks target block cipher modes like CBC where the server acts as an "oracle" by revealing whether padding is valid through error messages or response differences (e.g., status codes, content lengths). In web applications, this often affects encrypted cookies used for session authentication. The attack involves modifying ciphertext blocks and observing server responses to deduce plaintext bytes iteratively. Once decryption succeeds, the same oracle can be used to encrypt new plaintext, allowing cookie forgery for account takeover. This procedure assumes a vulnerable endpoint that processes the cookie without additional authentication checks and uses PKCS#7 padding. It applies to scenarios where cookies encode user identities in 3DES or AES with block sizes of 8 or 16 bytes respectively.

## Requirements

1. Access to a vulnerable web application endpoint that processes encrypted cookies and leaks padding information via response variations (e.g., different content lengths or status codes).
2. The target cookie value, obtained via browser developer tools or a proxy like Burp Suite.
3. PadBuster tool installed on a Kali Linux or similar environment.
4. Knowledge of the cookie name (e.g., 'auth') and block size (8 for 3DES, 16 for AES).
5. Network access to the target URL; no privileged credentials needed beyond initial cookie acquisition.

## Defense

Defensive measures and detection strategies:

- Implement authenticated encryption modes like AES-GCM instead of CBC to prevent tampering detection without oracle leaks.
- Enforce strict padding validation and return identical error responses for all decryption failures to eliminate the oracle.
- Use secure session management with HMAC or signed tokens (e.g., JWT with proper signing) rather than encrypt-only cookies.
- Monitor for anomalous requests to authentication endpoints with modified cookies, using WAF rules to detect repeated padding probes.
- Enable logging of HTTP response lengths and status codes for encrypted endpoints to detect brute-force patterns.

## Objectives

1. Decrypt the current user's cookie to reveal plaintext data like usernames or roles.
2. Encrypt arbitrary plaintext (e.g., an admin username) into a valid ciphertext cookie.
3. Impersonate a target user by setting the forged cookie, achieving unauthorized access.
4. Validate the vulnerability and demonstrate full credential access via cookie manipulation.

## Instructions

### Step 1: Acquire the Target Cookie

**Context**: Obtain the encrypted cookie value from the legitimate user's session to serve as the starting point for the attack. This can be done via browser inspection or proxy interception without alerting the server.

Use browser developer tools or [[tools/Burp Suite]] to extract the cookie:

- In Firefox: Right-click > Inspect Element > Storage > Cookies.
- In Chrome: Right-click > Inspect > Application > Cookies.
- In Burp Suite: Proxy > HTTP History > Select request > View cookie in headers.

**Expected Output**: The full cookie value (e.g., 'vUTZknJSU7A%2BJ02NeAP2MingCdt8ctB2') and its name (e.g., 'auth').

### Step 2: Decrypt the Cookie Using Padding Oracle

**Context**: Use PadBuster to exploit the padding oracle by sending modified ciphertexts and analyzing server responses to decrypt the cookie block-by-block. This reveals the plaintext without the key, confirming the vulnerability.

**Command** ([[commands/padbuster-decrypt-cookie]]):
```bash
padbuster http://$_TARGET_URL $_COOKIE $_BLOCK_SIZE -cookies $_COOKIE_NAME=$_COOKIE -encoding 0
```

> Run this command interactively; PadBuster will analyze responses and prompt for the error condition ID (typically the shortest response). It performs byte-at-a-time decryption starting from the last block.

**Expected Output**: Decrypted plaintext in ASCII, HEX, and Base64 formats (e.g., 'user=dave'), along with intermediate block details.

### Step 3: Encrypt Arbitrary Plaintext into a Forged Cookie

**Context**: Once decryption succeeds, reuse the oracle to encrypt a new plaintext value (e.g., impersonating an admin user) by crafting intermediate bytes that produce valid padding when combined with the known IV or previous block.

**Command** ([[commands/padbuster-encrypt-plaintext-to-cookie]]):
```bash
padbuster http://$_TARGET_URL $_COOKIE $_BLOCK_SIZE -cookies $_COOKIE_NAME=$_COOKIE -encoding 0 -plaintext $_NEW_PLAINTEXT
```

> Specify the desired plaintext (e.g., 'user=admin'). PadBuster computes the necessary ciphertext modifications based on oracle feedback.

**Expected Output**: New encrypted cookie value (e.g., 'BAitGdYuupMjA3gl1aFoOwAAAAAAAAAA') ready for injection.

### Step 4: Inject the Forged Cookie and Verify Access

**Context**: Replace the original cookie with the encrypted forgery in the browser or proxy to impersonate the target user. This tests the attack's success by gaining unauthorized access.

Use Burp Suite Repeater or browser dev tools to set the cookie header:

- In Burp: Intercept request > Edit cookie value > Forward.
- In Browser: Application > Cookies > Edit and refresh.

**Expected Output**: Successful authentication as the impersonated user, with access to privileged resources (e.g., admin dashboard).

> If the server rejects the cookie, verify block size, encoding, or endpoint behavior; adjust and retry.
