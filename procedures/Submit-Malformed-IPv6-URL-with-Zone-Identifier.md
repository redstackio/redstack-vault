---
id: proc-submit-url
tags:
  - ssrf
  - url-injection
  - ipv6
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:36.078Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Malformed-IPv6-URL-with-Zone-Identifier

## Summary

This procedure involves injecting a crafted IPv6 URL with a percent-encoded zone identifier into a libcurl-dependent application to trigger inconsistent parsing and enable exploitation.

## Description

Target web applications that accept user-supplied URLs for fetching. The malformed URL `http://[fe80::1%25eth0]/` uses `%25` to encode `%eth0`, intending to route to the eth0 interface per RFC 6874. If libcurl strips the zone ID, it allows SSRF by connecting via default interface. No special tools needed beyond the app's interface.

## Requirements

1. Access to user input field for URLs in the target app
2. Knowledge of target's internal IPv6 link-local addresses
3. Application using libcurl without additional URL validation

## Defense

Defensive measures and detection strategies:

- Sanitize and decode URLs before parsing, rejecting percent-encoded zone IDs
- Use allowlists for permitted hostnames and interfaces
- Log all user-supplied URLs and monitor for IPv6 literals with zones

## Objectives

1. Deliver the malformed URL to the application
2. Initiate parsing without immediate rejection
3. Set up for zone ID omission during connection

## Instructions

### Step 1: Craft and Submit URL

**Context**: Prepare the URL to target a specific interface but rely on parsing flaw.

**Command** (No direct command; via app input):
Submit via application form or API: `http://[fe80::1%25eth0]/`

> The app processes this as a valid HTTP request to a link-local IPv6 address.

### Step 2: Verify Submission

**Context**: Confirm the URL is accepted and queued for fetching.

Check application logs for URL receipt without parsing errors.

> Expected: No validation failure; request proceeds to libcurl.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- ssrf
- url-injection
- ipv6
