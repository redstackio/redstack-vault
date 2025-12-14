---
id: uuid5
tags:
  - live-reproduction
  - dos-confirmation
type: procedure
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:49.033Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Reproduce-on-Live-Reddit

## Summary

This procedure tests the Snudown vulnerabilities on live Reddit by sending a private message with colliding references, confirming persistence of hash flaws and incorrect resolutions.

## Description

Using Bug 3, send markdown with colliding names (e.g., '37qpypz' and 'uvhisfu' hashing to 7150400) each with unique URLs; observe HTML rendering using last URL for all. Targets production web apps; outcomes confirm real-world DoS potential.

## Requirements

1. Reddit account for private messaging
2. Generated colliding strings
3. Browser to view rendered output

## Defense

Defensive measures and detection strategies:

- Patch parser to use secure hashes
- Sanitize inputs for duplicate refs
- Log and alert on slow parsing events

## Objectives

1. Deliver malicious markdown via PM
2. Observe rendered HTML for wrong resolutions
3. Validate SDBM and flaws in production

## Instructions

### Step 1: Prepare Message

**Context**: Craft PM with colliding defs.

No specific command; write [37qpypz]: url1 [uvhisfu]: url2 then [37qpypz] links.

> Creates test input; expected output is formatted message.

### Step 2: Send and Render

**Context**: Submit PM on Reddit.

No specific command; use Reddit UI to send private message.

> Triggers parsing; expected output is viewed page.

### Step 3: Verify Output

**Context**: Check HTML for URL usage.

No specific command; inspect rendered links.

> All use last URL, confirming hash equality issue; expected output is proof of live vuln.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[live-reproduction]]
- [[dos-confirmation]]
