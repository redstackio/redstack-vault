---
tags:
  - xss
  - payload-craft
  - json
type: procedure
tools:
  - '[[tools/webpack]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:36.978Z'
sub_techniques: []
id: 27c40569-ec5e-41b6-8b54-04096aee86de
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Webpack-Stats-JSON

## Summary

This procedure crafts a webpack stats JSON file with malicious asset names designed to exploit the XSS vulnerability in webpack-bundle-analyzer by injecting script tags that break out of HTML contexts.

## Description

Webpack stats JSON contains compilation details, including asset names derived from third-party modules. An attacker crafts names like '</script><script>alert(1)</script>main.js' which are rendered unsanitized in the viewer.ejs template at line 14. This procedure manually creates such a poc.json file, simulating control over third-party module structure. The target is a local file system, and the outcome is a JSON input that, when analyzed, leads to JavaScript execution on page load.

## Requirements

1. Basic knowledge of JSON structure for webpack stats
2. Text editor to create the file
3. Understanding of XSS payloads for script injection

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all file/directory names in webpack configs
- Use secure third-party modules from trusted sources
- Employ static analysis on webpack stats before visualization

## Objectives

1. Embed XSS payload in asset names within stats JSON
2. Ensure JSON validity for analyzer parsing
3. Simulate malicious third-party module influence

## Instructions

### Step 1: Craft the JSON File

**Context**: Create poc.json with a webpack stats object containing malicious asset names.

**Command** (Manual file creation):
```bash
# Example content for poc.json:
{
  "assets": [
    {
      "name": "</script><script>alert(1)</script>main.js"
    }
  ]
}
```

> Save the above as poc.json. This embeds the payload in the asset name, which will be injected into the EJS template without escaping, triggering XSS on render.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/webpack]]

## Tags

- xss
- payload-craft
- json
