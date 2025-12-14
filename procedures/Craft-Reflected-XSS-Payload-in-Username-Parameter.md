---
id: proc-uuid-2
tags:
  - xss
  - payload-craft
  - html-injection
type: procedure
tools: []
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
updated_at: '2025-12-13T23:52:33.824Z'
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
# Craft Reflected XSS Payload in Username Parameter

## Summary

This procedure crafts a URL-encoded HTML payload for the username parameter on Snapchat's add page, confirming reflection in multiple unsanitized contexts like meta and header tags.

## Description

The username parameter in https://www.snapchat.com/add/<username> is reflected without HTML escaping in mobile-rendered elements, including Open Graph and Twitter meta tags, a snapcode object tag, and an h2 username tag. URL-encoding the payload (e.g., ">%3C/h1%3EXSS%3C/h1%3E) allows injection, breaking out of attributes for HTML insertion.

## Requirements

1. Mobile User-Agent enabled
2. URL encoding knowledge (e.g., via browser or online tool)
3. Target URL access

## Defense

Defensive measures and detection strategies:

- Sanitize/escape URL path parameters for HTML contexts
- Validate input against expected username format
- Monitor for encoded payloads in access logs

## Objectives

1. Inject and reflect HTML payload
2. Verify injection points
3. Assess reflection scope

## Instructions

### Step 1: Encode Basic Payload

**Context**: Create a simple breakout payload to test reflection.

Encode ">%3C/h1%3EXSS%3C/h1%3E using URL encoder.

> Expected: Payload ready for insertion.

### Step 2: Inject into URL and Load

**Context**: Access the modified URL with mobile User-Agent.

Navigate to https://www.snapchat.com/add/%22%3E%3Ch1%3EXSS%3C%2Fh1%3E.

> Expected: "XSS" injected into 6 elements: 4 meta tags (twitter:title, twitter:image, og:title, og:image), 1 object (snapcode), 1 h2 (username).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-craft]]
