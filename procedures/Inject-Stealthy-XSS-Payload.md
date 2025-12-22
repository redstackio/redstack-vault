---
tags:
  - xss
  - stealth
  - bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
id: 337dc00e-a438-4bd9-a9aa-3baea09ce0e5
created_at: '2025-12-14T03:47:12.593Z'
updated_at: '2025-12-14T03:47:12.593Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stealthy-XSS-Payload

## Summary

This procedure injects a non-disruptive XSS payload using double-encoded newlines, displaying a benign domain in the URL bar while executing JS silently, as found in the Semrush redirect bypass.

## Description

The technique uses payloads like javascript://www.semrush.com/%250aalert(document.domain) to execute without alerts, avoiding victim suspicion. Applies to web apps with partial URL validation. Prerequisites: Basic XSS working. Expected: Undetected data exfiltration.

## Requirements

1. Target domain knowledge (e.g., semrush.com)
2. Double-encoding capability
3. Silent execution testing environment

## Defense

Defensive measures and detection strategies:

- Normalize and decode URLs fully before processing
- Inspect for hidden JS in benign-looking URLs
- Log URL bar manipulations and JS events

## Objectives

1. Execute JS without visual cues
2. Maintain stealth for prolonged access
3. Exfiltrate data covertly

## Instructions

### Step 1: Design Stealth Payload

**Context**: Embed legitimate domain with encoded breakout.

Payload: javascript://www.semrush.com/%250aalert(document.domain).

> Expected: URL appears normal; JS ready to run.

### Step 2: Test Injection

**Context**: Deliver via redirect and confirm silence.

URL: https://www.semrush.com/redirect?url=javascript://www.semrush.com/%250aalert(document.domain). Visit.

> Expected: Domain in URL bar; alert fires without popup disruption.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[stealth-xss]]
- [[url-bypass]]
