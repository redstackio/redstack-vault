---
tags:
  - response-analysis
  - rendering
  - disclosure
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:25:18.300Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: bdb726e2-8def-482f-b55c-151cce644b2a
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Analyze-Response-for-Server-Information-Exfiltration

## Summary

This procedure renders the response from the exploited Sentry endpoint in Burp Suite to visualize and extract sensitive server information, such as debug details and internals.

## Description

The POST response from a misconfigured Sentry store often includes HTML/JS that, when rendered, displays UI elements with exposed data. This step uses Burp's rendering feature to interpret the response, revealing information like server configurations and potential attack vectors. Assumes prior request modification; outcomes include actionable intelligence for further attacks.

## Requirements

1. Raw response from modified POST request in Burp Repeater
2. Burp Suite with rendering enabled (default in Professional)
3. Ability to screenshot or export disclosed data

## Defense

Defensive measures and detection strategies:

- Strip sensitive data from error responses in Sentry config
- Enable response encryption or obfuscation
- Monitor for unusual response rendering attempts via logs

## Objectives

1. Render raw response to UI view
2. Identify and document disclosed server details
3. Assess impact for chained attacks

## Instructions

### Step 1: Access Response Tab

**Context**: Locate the response after sending the modified request.

In Burp Repeater, switch to the Response tab post-send.

> Raw HTML/JS visible; may appear garbled without rendering.

### Step 2: Render the Response

**Context**: Use Burp's built-in renderer to process dynamic content.

Click the [Render] button in the response viewer.

> UI loads, showing Sentry dashboard or error details with sensitive info.

### Step 3: Extract and Document

**Context**: Review for high-value disclosures.

Scan rendered page for server paths, versions, [█████] details, and stack traces. Screenshot and note elements aiding further attacks.

> Extracted data includes server internals, confirming high impact.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[analysis]]
- [[Exfiltration]]
- [[ui-render]]
