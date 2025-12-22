---
id: 123e4567-e89b-12d3-a456-426614174005
name: Intercept-and-Replay-Authentication-Flow-with-Stolen-Cookies
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.859Z'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
techniques:
  - '[[T1078.004]]'
  - '[[Pass the Hash]]'
sub_techniques: []
tags:
  - auth-bypass
  - cookie-replay
  - sso
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: advanced
impact_level: critical
detection_risk: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[T1078.004]]'
  - '[[Pass the Hash]]'
---

# Intercept-and-Replay-Authentication-Flow-with-Stolen-Cookies

## Summary

Using an intercepting proxy, this procedure modifies requests and responses in the SSO authentication flow by injecting stolen cookies, achieving session hijacking and full impersonation without victim credentials.

## Description

With captured _csid and state from the malicious page, the attacker navigates to the relayed URL in their browser, intercepts the request to auth.uber.com with a proxy, adds Cookie headers, forwards, then intercepts the response redirect to riders.uber.com, injects Set-Cookie headers, and completes login. This bypasses CSRF and scopes to .uber.com services. Targets web SSO; requires proxy setup. Outcomes: Attacker gains victim's access.

## Requirements

1. Captured cookies and state tokens
2. Intercepting proxy configured (e.g., Burp)
3. Attacker browser session

## Defense

Defensive measures and detection strategies:

- Enforce short-lived session tokens with invalidation on use
- Log and alert on cookie injections or unusual proxy-like traffic
- Use client-side fingerprinting to detect session anomalies

## Objectives

1. Replay stolen cookies in auth flow
2. Hijack session across subdomains
3. Achieve persistent impersonation

## Instructions

### Step 1: Initiate Replay in Browser

**Context**: Start the captured URL to trigger request to auth.uber.com.

**Command** (Browser):
```bash
# Navigate to: https://auth.uber.com/login?state=xyz789&redirect_uri=...
```

> Proxy intercepts outgoing request.

### Step 2: Modify Request with Stolen Cookies

**Context**: Add headers using proxy.

**Command** (Burp):
```bash
# In Proxy: Add Header - Cookie: _csid=abc123; state=xyz789
Forward
```

> Expected: Server accepts, proceeds to response.

### Step 3: Inject Cookies in Response

**Context**: Alter redirect to set cookies in attacker's browser.

**Command** (Burp):
```bash
# In Response: Add Header - Set-Cookie: _csid=abc123; domain=.uber.com
Set-Cookie: state=xyz789
Forward
```

> Browser receives cookies, redirects to victim's dashboard.

### Step 4: Verify Access

**Context**: Test impersonation.

**Command** (Browse):
```bash
# Access https://partners.uber.com
```

> Expected: Full access without re-auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

### Techniques

- [[T1078.004]] Valid Accounts: Cloud Accounts
- [[Pass the Hash]] Use Alternate Authentication Material: Pass the Ticket (adapted for cookies)

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[auth-bypass]]
- [[cookie-replay]]
