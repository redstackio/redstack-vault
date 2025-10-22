---
id: b88947f8-6d78-48e4-8de9-4dbeb4b03c2c
name: Padding Oracle Attack Against Cookies
type: procedure
verified: true
submitted: true
created_at: '2019-10-24T00:47:43.960526+00:00'
updated_at: '2023-05-26T00:44:49.809719+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
platforms:
- Web
tags:
- '[[Cryptography]]'
- '[[Web Applications]]'
commands:
- '[[PadBuster Decrypting a Cookie into Plaintext]]'
- '[[PadBuster Encrypting Plaintext into a Cookie]]'
---

# Padding Oracle Attack Against Cookies

**Status**: ✓ Verified

## Summary

Padding Oracle Attacks focus on a vulnerability in cipher block chaining (CBC), allowing attackers to extract plaintext from ciphertext, and encode plaintext as valid ciphertext. By sending crafted packets to the server and analyzing the results, attackers can learn information about encrypted valu

## Description

# Description

Padding Oracle Attacks focus on a vulnerability in cipher block chaining (CBC), allowing attackers to extract plaintext from ciphertext, and encode plaintext as valid ciphertext. By sending crafted packets to the server and analyzing the results, attackers can learn information about encrypted values, eventually identifying  the plaintext. If an attacker is able to decrypt ciphertext, they can can also encrypt plaintext, which allows them to impersonate other users when the ciphertext is used as a token, as can be the case when dealing with cookies.

# Instructions

1. Get the current user's cookie.

## Firefox

- Right click in the browser window > Inspect Element > Storage > Cookies

## Chrome/Chromium

- Right click in the browser window > Inspect > Application > Cookies

## Burp Suite

- Proxy > HTTP History > Select a request

2. Run PadBuster with the cookie from Step 1 to attempt to decode it, and determine if the server is vulnerable to POODLE attacks.

**Command** ([[PadBuster Decrypting a Cookie into Plaintext]]):

```bash
padbuster http://$TARGET_IP $COOKIE 8 -cookies $COOKIE_NAME=$COOKIE -encoding 0
```

Note: the pad size is specified as 8, which coincides with 3DES. If AES is used for encryption, this value should be 16.

If the attack is successful, a decoded value is revealed.

3. Assuming Step 2 is successful, attempt to encode a cookie with the plaintext username of an account which the attacker wishes to impersonate.

**Command** ([[PadBuster Decrypting a Cookie into Plaintext]]):

```bash
padbuster http://$TARGET_IP $COOKIE 8 -cookies $COOKIE_NAME=$COOKIE -encoding 0
```

4. Modify the user's cookie in the browser or Burp to the 'Encrypted value' returned by Step 3. If successful, user will be now logged in as the impersonated user.

## Platforms

- Web

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[PadBuster Decrypting a Cookie into Plaintext]]
- [[PadBuster Encrypting Plaintext into a Cookie]]

## Tags

- [[Cryptography]]
- [[Web Applications]]
