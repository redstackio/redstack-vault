---
tags:
  - csp-bypass
  - polyglot
  - javascript
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
detection_risk: high
sub_techniques: []
id: ffebe281-6f00-4615-ab00-7a2adf250994
created_at: '2025-12-14T03:46:14.339Z'
updated_at: '2025-12-14T03:46:14.339Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# CSP Bypass via Polyglot GIF+JS Upload

## Summary

Uploads a polyglot GIF+JavaScript file to Shopify's CDN (CSP whitelisted), allowing JS execution bypassing policy.

## Description

GraphicsMagick preserves dual validity; uploaded as GIF, served from cdn.shopify.com, evading CSP restrictions on scripts.

## Requirements

1. Polyglot file generator

## Defense

- Validate file signatures strictly
- Exclude CDNs from CSP whitelists for scripts

## Objectives

1. Execute JS client-side

## Instructions

### Step 1: Create Polyglot

**Context**: GIF header + JS body.

Use tool or hex edit for valid GIF89a + JS.

### Step 2: Upload to CDN

**Context**: Submit as image.

Upload; access URL from cdn.shopify.com to execute.

> Bypasses CSP.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csp]]
