---
id: proc-craft-pingback-payload
tags:
  - payload
  - xml
  - pingback
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:46.013Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Pingback-Ping-Payload

## Summary

This procedure constructs an XML-RPC payload for the pingback.ping method in WordPress xmlrpc.php, embedding an attacker-controlled URL to trigger SSRF.

## Description

The pingback.ping method in WordPress XML-RPC fetches the source URL to verify links, allowing SSRF if unvalidated. This crafts a methodCall XML with the attacker's OOB URL as the source and target site as the target, exploiting lack of URL sanitization. Used in unauthenticated scenarios on PHP/WordPress platforms.

## Requirements

1. Unique OOB URL from listener setup
2. Target site URL
3. XML knowledge for payload structure

## Defense

Defensive measures and detection strategies:

- Validate and whitelist URLs in pingback.ping
- Disable XML-RPC pingbacks via WordPress config
- Parse and log XML payloads for malicious patterns

## Objectives

1. Create valid XML to invoke pingback.ping
2. Inject external URL for SSRF trigger
3. Ensure payload evades basic filters

## Instructions

### Step 1: Build XML Structure in Burp

**Context**: Set POST body to XML methodCall.

No command; in Burp Repeater, paste XML.

> Use structure: methodName 'pingback.ping', params with <string> for attacker URL and target URL.

### Step 2: Set Headers

**Context**: Ensure proper content type.

No command; Add Content-Type: application/xml or text/xml.

> Test payload locally if possible to validate XML.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xml]]
- [[ssrf]]
