---
id: 96ed686b-3be6-412e-bc3e-45f489b79ae8
name: Forge-Custom-JWT-Token-for-Auth-Bypass
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:00.494269+00:00'
updated_at: '2023-04-10T20:22:33.109807+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
tags:
  - '[[tags/JWT Format]]'
  - '[[tags/JWT - JSON Web Token]]'
  - '[[tags/Payload]]'
  - jwt
  - token-forgery
  - auth-bypass
commands:
  - '[[commands/python-encode-jwt-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# Forge-Custom-JWT-Token-for-Auth-Bypass

## Summary

This procedure demonstrates how to forge a custom JSON Web Token (JWT) by defining a payload with privileged attributes (e.g., admin flag) and encoding it using the PyJWT library in Python. It is useful in red team engagements for testing authentication bypasses, privilege escalation via valid-looking tokens, or simulating token manipulation attacks in web applications that rely on JWT for session management.

## Description

JWTs are compact, URL-safe tokens used for secure information transmission in web applications, consisting of a header, payload, and signature. In offensive security, attackers forge JWTs to impersonate users or escalate privileges by crafting payloads with elevated claims (e.g., setting 'admin' to true) and encoding them, often exploiting weak validation like the 'none' algorithm or known secrets. This procedure focuses on creating such a token in a controlled environment, assuming the target application uses HS256 signing or vulnerable configurations. The resulting token can be injected into requests to gain unauthorized access, mapping to MITRE ATT&CK techniques for using valid accounts while evading detection through obfuscation.

## Requirements

1. Python 3.x installed on the attacker's system
2. PyJWT library (install via pip if needed)
3. Knowledge of the target's JWT structure (e.g., expected claims like 'sub', 'exp')
4. Optional: Target application secret key or use 'none' algorithm for bypass testing

## Defense

- Use secure JWT libraries with strict algorithm enforcement (e.g., reject 'none')
- Encrypt sensitive claims and implement short expiration times
- Validate tokens server-side with signature verification and claim checks
- Monitor for anomalous token usage via logging and anomaly detection

## Objectives

1. Create a JWT token with a specified payload including privileged attributes
2. Authenticate as a high-privilege user or transmit manipulated information using the forged token
3. Test for token validation weaknesses in the target application

## Instructions

### Step 1: Prepare the Custom Payload

**Context**: Define the JWT payload as a JSON object with desired claims, such as user ID, name, expiration, and a privilege flag. This step sets the data that will be embedded in the token to simulate an admin user. Reference the sample payload structure in [[codes/JWT-Payload-Example-with-Admin-Flag]] for customization.

Embed the payload JSON directly in your encoding script or save it to a file (e.g., payload.json) for reuse.

> This payload includes an expiration timestamp (exp) to mimic legitimate tokens; adjust values to match the target's format to avoid immediate rejection.

### Step 2: Encode the Payload into a JWT Token

**Context**: Use Python's PyJWT library to encode the payload into a full JWT string. This step signs the token with a placeholder secret (or 'none' for testing bypasses), producing a base64-encoded token ready for use in HTTP requests.

**Command** ([[commands/python-encode-jwt-payload]]):
```python
python -c "import jwt; payload = {\"sub\":\"1234567890\", \"name\":\"Amazing Haxx0r\", \"exp\":1466270722, \"admin\":True}; print(jwt.encode(payload, '$_SECRET_KEY', algorithm='HS256'))"
```

> Run this command on your attacker machine, replacing $_SECRET_KEY with the target's signing secret if known (e.g., extracted via other means). For testing 'none' algorithm vulnerabilities, change to algorithm='none' and set the key to None. Expected output is a string like 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFtw6l6aW5nIEhheHhavyIsImV4cCI6MTQ2NjI3MDcyMiwiYWRtaW4iOnRydWV9.signature_here'. Verify by decoding the token online or with a decode command to ensure claims are intact.

### Step 3: Verify and Use the Forged Token

**Context**: Decode the generated token to confirm the payload is correctly embedded, then inject it into target application requests (e.g., via Authorization header) to test for successful privilege escalation or access grant.

Use a browser developer tools or proxy like Burp Suite to set the token in requests. For verification, run a simple decode:

```python
python -c "import jwt; token = '$_TOKEN'; print(jwt.decode(token, '$_SECRET_KEY', algorithms=['HS256']))"
```

> Replace $_TOKEN with your encoded JWT and $_SECRET_KEY as before. Expected output mirrors the original payload JSON. Success is indicated if the application accepts the token without signature errors and grants admin actions (e.g., accessing restricted endpoints).
