---
id: 3d2cf63a-1e31-4349-82d2-6a2d6302f573
name: Debug-Facebook-Access-Token
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:53.114842+00:00'
updated_at: '2023-04-06T03:55:53.128187+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
  - >-
    [[sub-techniques/Credentials in Registry|T1552.002 - Credentials in
    Registry]]
  - '[[sub-techniques/Private Keys|T1552.004 - Private Keys]]'
tags:
  - '[[tags/API Key Leaks]]'
  - '[[tags/Exploit]]'
  - '[[tags/Facebook Access Token]]'
commands:
  - '[[commands/curl-facebook-access-token-debug]]'
platforms:
  - Web
tools: []
validated: true
---

# Debug-Facebook-Access-Token

## Summary

This procedure demonstrates how to inspect a Facebook Access Token using Facebook's official debug tool to retrieve details such as the associated user ID, expiration time, scopes, and validity status. It is useful after obtaining a potentially leaked token through other means, allowing an attacker to assess its value for further exploitation like unauthorized API access or data retrieval on behalf of the token's owner.

## Description

Facebook Access Tokens serve as authentication mechanisms for accessing the Facebook Graph API, enabling actions on behalf of users or applications. If a token is leaked—via application vulnerabilities, user error, or unsecured storage—an attacker can debug it to understand its permissions and lifespan without needing additional credentials. This technique falls under unsecured credentials as it leverages exposed tokens to gather intelligence for credential access. The target environment is any system with internet access and a command-line tool like curl. Expected outcomes include token metadata that can inform subsequent attacks, such as querying user data or performing authorized actions. Note that Facebook may revoke suspicious tokens, so rapid assessment is key.

## Requirements

1. A valid or suspected Facebook Access Token (obtained via leakage, phishing, or exploitation).
2. Internet connectivity to reach Facebook's developer tools.
3. curl installed on the attacker's machine (standard on Linux/macOS; available via package managers on Windows).
4. Basic knowledge of HTTP requests and JSON parsing.

## Defense

Defensive measures and detection strategies:

- Enforce short token expiration times and use refresh tokens with secure storage.
- Implement token introspection endpoints with rate limiting and logging to detect unauthorized debugging attempts.
- Monitor application logs for unusual API calls using leaked tokens and enable multi-factor authentication (MFA) for developer accounts.
- Use secure coding practices to prevent token exposure in client-side code, logs, or error messages.

## Objectives

1. Retrieve detailed metadata about the Access Token, including user ID and scopes.
2. Validate the token's usability for API interactions.
3. Identify potential for further compromise, such as accessing user data or performing actions on the victim's behalf.

## Instructions

### Step 1: Prepare the Access Token

**Context**: Ensure you have a leaked or obtained Facebook Access Token ready for inspection. This step involves verifying the token format (typically a long alphanumeric string) and preparing your environment to avoid exposure.

No specific command is needed here, but confirm the token does not contain sensitive prefixes or suffixes that might indicate invalidity.

> This preparatory step ensures the token is in a usable state before querying Facebook's API, preventing errors from malformed input.

### Step 2: Execute the Debug Request

**Context**: Use curl to send a GET request to Facebook's Access Token Debug tool, substituting the token placeholder. This retrieves JSON-formatted details about the token's properties, helping determine its scope and validity.

**Command** ([[commands/curl-facebook-access-token-debug]]):
```bash
curl "https://developers.facebook.com/tools/debug/accesstoken/?access_token=$_ACCESS_TOKEN&version=v3.2"
```

> This command queries the Facebook Graph API debug endpoint. Replace $_ACCESS_TOKEN with the actual token string. The response will include fields like app_id, type (e.g., "user"), data.access_token (the token itself), expires_at (Unix timestamp), is_valid (boolean), issued_at, scopes (array of permissions), and user_id. If the token is invalid or expired, is_valid will be false. Parse the JSON output using tools like jq for easier reading: `curl ... | jq .`.

### Step 3: Analyze the Response

**Context**: Review the output to assess the token's value. Look for high-privilege scopes (e.g., "user_posts", "email") that enable data exfiltration or account manipulation.

No command needed, but if jq is available:
```bash
curl "https://developers.facebook.com/tools/debug/accesstoken/?access_token=$_ACCESS_TOKEN&version=v3.2" | jq '.data | {user_id, scopes, is_valid, expires_at}'
```

> Extract key indicators: A valid token with broad scopes indicates success. If expires_at is in the future, the token is active. Decision point: If is_valid is true and scopes include sensitive permissions, proceed to API exploitation (e.g., Graph API calls for user data); otherwise, discard and seek another token source.
