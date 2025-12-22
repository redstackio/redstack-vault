---
tags:
  - ssrf
  - avatar-upload
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ccf9f634-87bc-4136-9165-a4158226cb0e
created_at: '2025-12-14T03:46:14.345Z'
updated_at: '2025-12-14T03:46:14.345Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SSRF via Profile Avatar Upload

## Summary

Exploits the same SVG disguise in profile avatar uploads to trigger SSRF, mirroring product image behavior.

## Description

Profile image upload shares validation flaws, processing SVG before checks, allowing external requests via xlink:href.

## Requirements

1. Authenticated user session
2. Profile edit access

## Defense

- Unified validation across upload endpoints
- Parser configuration for no externals

## Objectives

1. Trigger SSRF in user context
2. Expand attack surface

## Instructions

### Step 1: Prepare Avatar Payload

**Context**: Same as product, disguise SVG.

Create payload.png with SVG content.

### Step 2: Upload to Profile

**Context**: Submit via profile form or API.

POST to avatar endpoint with multipart image.

> Observe external fetch.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
