---
id: proc-uuid-1
tags:
  - authentication
  - graphql-capture
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:59.381Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-and-Capture-GraphQL-Request

## Summary

This procedure authenticates to the HackerOne platform and uses Burp Suite to intercept and capture a GraphQL POST request to a sensitive endpoint, such as bounty settings, for subsequent replay in session revocation testing.

## Description

In the context of testing session expiration vulnerabilities, this procedure establishes an authenticated session on HackerOne.com and captures a GraphQL query that fetches sensitive user data. The target environment is the web-based HackerOne platform using GraphQL over HTTPS. Prerequisites include valid user credentials and Burp Suite configured as a proxy. Expected outcomes include a captured request with session tokens that can be replayed post-revocation to demonstrate the flaw.

## Requirements

1. Valid HackerOne credentials (e.g., hacker or program owner account)
2. Burp Suite installed and running as an HTTP proxy (default port 8080)
3. Browser configured to proxy traffic through Burp Suite
4. Direct network access to https://hackerone.com

## Defense

Defensive measures and detection strategies:

- Implement comprehensive proxy detection and block unauthorized interception tools
- Enforce strict certificate pinning to prevent MITM via proxies like Burp Suite
- Monitor for unusual GraphQL query patterns or high-frequency requests from authenticated sessions

## Objectives

1. Establish authenticated access to HackerOne
2. Intercept a GraphQL request to sensitive data endpoints
3. Prepare captured request for replay testing

## Instructions

### Step 1: Configure Burp Suite Proxy

**Context**: Set up Burp Suite to intercept HTTPS traffic from the browser.

No specific command; configure Burp Suite GUI: Start Burp, go to Proxy tab, ensure Intercept is on, and set browser proxy to 127.0.0.1:8080. Install Burp's CA certificate in the browser for HTTPS interception.

> Expected output: Browser traffic routed through Burp; HTTPS sites load without certificate errors.

### Step 2: Login to HackerOne

**Context**: Authenticate using valid credentials to obtain a session.

Navigate to https://hackerone.com and login with username/password. Observe the login request in Burp Proxy history.

> Expected output: Successful redirection to dashboard; session cookie/token in request headers.

### Step 3: Navigate to Sensitive Page and Capture Request

**Context**: Access a page that triggers a GraphQL query for sensitive data and intercept it.

Go to https://hackerone.com/settings/bounties. In Burp Proxy, intercept the outgoing GraphQL POST request to https://hackerone.com/graphql.

**Technical Details**: The request body includes a query like {"query":"query User_bounty_settings_page($first_0:Int!,$currency_1:CurrencyCode!,$currency_2:CurrencyCode!) { me { id, ...Fg } } ..."} with variables {"first_0":100,"currency_1":"USD","currency_2":"XLA"}. Forward the request after inspection.

> Expected output: Captured POST request with Authorization header containing session token.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- authentication
- graphql-capture
- session-token
