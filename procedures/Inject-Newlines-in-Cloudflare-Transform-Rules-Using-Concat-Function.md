---
tags:
  - http-smuggling
  - cloudflare
  - injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Cloud
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 64970890-9444-4538-b7c7-4a792dc9bbb1
created_at: '2025-12-13T09:01:26.061Z'
updated_at: '2025-12-13T09:01:26.061Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject Newlines in Cloudflare Transform Rules Using Concat Function

## Summary

This procedure exploits a vulnerability in Cloudflare's Transform Rules by using the concat() function to inject hexadecimal escape sequences like \x0d\x0a, enabling newline injection into request headers without proper sanitation.

## Description

The attack targets the Ruleset Engine in Cloudflare, where the concat() function processes hex escapes directly, allowing attackers to inject newlines and additional headers. This sets up for HTTP request smuggling, potentially bypassing security measures and accessing internal resources. It requires access to the Cloudflare dashboard to create rules.

## Requirements

1. Access to Cloudflare dashboard with permissions to create Transform Rules
2. Target domain configured in Cloudflare
3. Knowledge of the vulnerable concat() function behavior

## Defense

Defensive measures and detection strategies:

- Monitor Cloudflare rule changes for suspicious concat() usage
- Enable output sanitation in Transform Rules and update to patched versions

## Objectives

1. Inject newlines into HTTP headers
2. Modify headers like Transfer-Encoding
3. Prepare for request smuggling

## Instructions

### Step 1: Access Transform Rules Dashboard

**Context**: Navigate to the Cloudflare dashboard to create a new rule.

Log in to Cloudflare and go to the Rules > Transform Rules section for the target zone.

> This sets up the environment for rule creation.

### Step 2: Create Dynamic Header Rewrite Rule

**Context**: Define the rule using concat() to inject the newline and header.

Create a new HTTP Request Header Modification rule with the expression concat("-", "\x0d\x0aTransfer-Encoding: chunked") applied to a dynamic header.

> This injects \r\nTransfer-Encoding: chunked into the header value.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[http-smuggling]]
- [[cloudflare]]
