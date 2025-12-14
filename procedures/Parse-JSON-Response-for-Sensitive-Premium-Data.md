---
id: proc-parse-xvideos-json-sensitive
tags:
  - information-disclosure
  - json-parsing
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:29.233Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Parse JSON Response for Sensitive Premium Data

## Summary

This procedure involves inspecting and extracting key fields from the unauthenticated JSON responses of xvideos.red API endpoints to uncover premium video metadata, financial earnings, and engagement metrics.

## Description

Once the API endpoint is accessed, the returned JSON contains detailed premium content information that should be restricted. Fields like `pmp` reveal creator earnings (e.g., "$24.99"), while `videos` arrays provide titles, durations, and flags for private/premium status. This step focuses on manual parsing via browser tools in a web environment, leading to identification of exploitable data for paywall bypass. No advanced setup is required beyond dev tools.

## Requirements

1. Web browser with JSON viewer or dev tools enabled
2. Prior access to the API endpoint response
3. Knowledge of JSON structure for field identification

## Defense

Defensive measures and detection strategies:

- Encrypt or obfuscate sensitive fields in API responses (e.g., remove financial data from public payloads).
- Enforce HTTPS and content security policies to prevent easy inspection.
- Log and analyze JSON field access patterns for unauthorized parsing attempts.

## Objectives

1. Extract financial and metadata from premium JSON.
2. Identify premium-flagged videos for further access.
3. Gather engagement metrics for analysis.

## Instructions

### Step 1: Inspect JSON in Dev Tools

**Context**: Load the API response and view its structure to locate sensitive fields.

In the browser, press F12 to open dev tools, go to the Network tab, and reload the API URL. Click on the request to view the Response tab, which displays the raw JSON.

> Look for top-level fields like `id`, `status`, `is_private`, and the `videos` array. Successful parse shows structured data without errors.

### Step 2: Identify Key Sensitive Fields

**Context**: Manually scan for premium indicators and financial info.

Within the `videos` array, note fields: `u` (URL), `tf` (title), `d` (duration), `pmp` (price/earnings), `p` (producer), `pn` (producer name), `ch` (channel), `pm` (premium).

> Expected: Visibility of earnings like `pmp: "$24,99"` and `pm: true` for premium content.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[json-parsing]]
