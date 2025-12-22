---
tags:
  - xxe
  - dos
  - svg
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: advanced
impact_level: low
detection_risk: medium
sub_techniques: []
id: 0fc53d4c-bdb3-482b-bf87-a921be92bad2
created_at: '2025-12-14T03:46:14.356Z'
updated_at: '2025-12-14T03:46:14.356Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Test XXE and DoS in SVG Entities

## Summary

Probes the SVG parser for XML External Entity (XXE) processing or Denial of Service via entity expansion, confirming restrictions to static entities only.

## Description

Embeds DOCTYPE declarations in SVG to test entity resolution. The parser allows internal entities but blocks SYSTEM/external DTDs and recursive expansions like Billion Laughs, limiting to no exploitation.

## Requirements

1. Knowledge of XXE payloads
2. SVG editor for DOCTYPE insertion

## Defense

Defensive measures and detection strategies:

- Disable DTD processing in XML parsers (e.g., libexpat flags)
- Set entity expansion limits
- Scan uploads for DOCTYPE

## Objectives

1. Check entity support
2. Confirm no XXE/DoS
3. Scope attack surface

## Instructions

### Step 1: Embed Internal Entity

**Context**: Test basic resolution.

Add to SVG: <!DOCTYPE testingxxe [ <!ENTITY xml "eXtensible Markup Language"> ]> <text>&xml;</text>

> Upload and check if text renders (via oracle if possible).

### Step 2: Attempt External/DoS

**Context**: Probe advanced attacks.

Try <!ENTITY xxe SYSTEM "file:///etc/passwd"> or Billion Laughs; expect failure.

> No external fetch or crash.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploitation for Client Execution]] Configuration Inference

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xxe]]
- [[dos]]
