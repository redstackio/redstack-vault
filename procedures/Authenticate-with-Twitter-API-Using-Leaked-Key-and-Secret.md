---
id: 0a72f708-1476-4dd7-b796-f8ef57a2fb42
name: Authenticate-with-Twitter-API-Using-Leaked-Key-and-Secret
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:52.355776+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Unsecured Credentials]]'
sub_techniques:
  - '[[Credentials in Files]]'
  - '[[Credentials in Registry]]'
  - '[[Bash History]]'
  - '[[Private Keys]]'
  - '[[Cloud Instance Metadata API]]'
tags:
  - api-key-leaks
  - exploit
  - twitter-api-secret
commands:
  - '[[commands/curl-twitter-api-bearer-token]]'
platforms:
  - Linux
  - macOS
  - Windows
tools: []
validated: true
---

# Authenticate-with-Twitter-API-Using-Leaked-Key-and-Secret

## Summary

This procedure outlines how to authenticate to the Twitter API using a leaked API key and secret to obtain a bearer token. The bearer token grants application-level access to Twitter's API endpoints, allowing actions such as posting tweets, reading timelines, or accessing user data without user-specific credentials. This is useful in scenarios where credentials are exposed via misconfigurations, like in public repositories or unsecured servers.

## Description

Leaked Twitter API keys and secrets often appear in public GitHub repositories, unsecured cloud storage, or application logs due to developer errors. Once obtained, an attacker can use these credentials to request a bearer token via OAuth 2.0 client credentials flow. This token enables read/write operations on behalf of the application, potentially leading to account compromise, data exfiltration, or spam propagation. The technique targets unsecured credentials storage and is applicable in web and API environments. Success depends on the key's validity and any rate limits imposed by Twitter.

## Requirements

1. Leaked Twitter API Key and API Secret (consumer key and consumer secret from a Twitter developer app).
2. curl tool installed on the attacker's machine (available on most Unix-like systems; use PowerShell Invoke-WebRequest on Windows if curl is unavailable).
3. Network connectivity to https://api.twitter.com (no proxy restrictions).
4. Basic understanding of HTTP requests and JSON parsing.

## Defense

Defensive measures and detection strategies:

- Store API keys and secrets in environment variables or secure vaults (e.g., AWS Secrets Manager, HashiCorp Vault) instead of code or config files.
- Regularly scan public repositories and code commits for exposed credentials using tools like TruffleHog or GitHub's secret scanning.
- Enable Twitter's application-only authentication limits and monitor API usage via the developer dashboard for anomalous activity.
- Implement API rate limiting and anomaly detection on the application side to flag unusual token requests.

## Objectives

1. Authenticate to the Twitter API using leaked credentials to obtain a bearer token.
2. Verify the token's validity by making a test API call.
3. Enable further API interactions, such as data collection or unauthorized actions on affected accounts.

## Instructions

### Step 1: Prepare API Credentials

**Context**: Gather and format the leaked API key and secret for use in the authentication request. This step ensures the credentials are correctly combined for HTTP Basic Authentication, preventing syntax errors in the subsequent request. Replace placeholders with actual leaked values obtained from sources like public repos or phishing.

No specific command is needed here; manually set variables in your shell or script:

```bash
export API_KEY="your_leaked_api_key_here"
export API_SECRET="your_leaked_api_secret_here"
```

> This sets environment variables for secure handling. Expected output: No output; verify with `echo $API_KEY` to confirm values are set without exposing them in command history.

### Step 2: Request Bearer Token

**Context**: Send a POST request to Twitter's OAuth 2.0 token endpoint using the prepared credentials. This step performs the core authentication, leveraging the client_credentials grant type for application-only access. The request uses Basic Auth with the key:secret format encoded in the Authorization header.

**Command** ([[commands/curl-twitter-api-bearer-token]]):

```bash
curl -u "$API_KEY:$API_SECRET" --data 'grant_type=client_credentials' 'https://api.twitter.com/oauth2/token'
```

> This command authenticates and requests the bearer token. If successful, it returns a JSON response with the access_token. Handle errors like 401 Unauthorized if credentials are invalid or revoked.

### Step 3: Extract and Verify Token

**Context**: Parse the JSON response to isolate the bearer token and test it with a simple API call. This verifies the token's functionality and confirms access to protected endpoints, such as retrieving public tweets. Use tools like jq for parsing if available.

**Command** (using jq for parsing; assume installed or use manual extraction):

```bash
echo '{"token_type":"bearer","access_token":"example_token"}' | jq -r '.access_token'
```

> Replace the echo with the actual curl output piped to jq. Expected output: The raw access_token string. To verify, make a test API call:

```bash
curl -H "Authorization: Bearer $ACCESS_TOKEN" 'https://api.twitter.com/1.1/statuses/home_timeline.json?count=1'
```

> This fetches the home timeline (limited to 1 tweet). Success indicates valid access; expect JSON with tweet data or a 401 if token is invalid.

## Expected Output

For Step 2, successful execution produces:

```json
{
  "token_type": "bearer",
  "access_token": "AAAAAAAAAAAAAAAAAAAA%2Fexample%3D%3Dtoken%3D%3D"
}
```

For Step 3, the extracted token is a long Base64-encoded string, and the verification call returns tweet JSON or an empty array if no recent activity.
