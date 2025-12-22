---
id: proc-algolia-trigger-public-001
tags:
  - xss
  - stored-xss
  - algolia
  - execution
  - public-exploit
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:47.216Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-XSS-in-Public-UI-Demo

## Summary

This procedure generates and accesses a public UI demo for the affected Algolia index, executing the Stored XSS for any visitor.

## Description

Algolia's public UI Demo feature creates shareable realtime search pages that inherit index configurations, including faceting. Rendering the malicious attribute triggers JS execution publicly. This maximizes impact by bypassing authentication. Depends on all prior steps. Outcomes: Arbitrary execution on public URLs.

## Requirements

1. Index with malicious faceting configured
2. Permission to generate public demos
3. Public internet access for verification

## Defense

Defensive measures and detection strategies:

- Disable or sanitize public demos for untrusted indices
- Apply strict CSP to demo pages
- Scan generated demos for XSS before publishing

## Objectives

1. Execute in fully public context
2. Demonstrate broad impact
3. Enable visitor-targeted attacks

## Instructions

### Step 1: Generate and Access Public Demo

**Context**: Create and load the demo URL.

In index settings, select 'Create Public UI Demo' to get a URL like https://www.algolia.com/realtime-search-demo/your_index. Visit it anonymously.

> Payload executes on load, showing alert. Confirm no auth required and shareability.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[algolia]]
- [[public-exploit]]
