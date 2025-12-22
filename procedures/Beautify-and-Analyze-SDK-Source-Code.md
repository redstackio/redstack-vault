---
tags:
  - code-analysis
  - shopify
type: procedure
tools:
  - '[[tools/Code-Beautifier]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[User Execution]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: ab45b744-5074-407d-bf9a-94b08d512e86
created_at: '2025-12-13T23:56:03.999Z'
updated_at: '2025-12-13T23:56:03.999Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[User Execution]]'
---
# Beautify and Analyze SDK Source Code

## Summary

This procedure beautifies the Shopify Embedded App SDK source code to identify interesting events and DOM XSS sinks, such as Shopify.API.setWindowLocation, which navigates without protocol validation.

## Description

In this procedure, the minified SDK code from https://cdn.shopify.com/s/assets/external/app.js is beautified to facilitate analysis. The goal is to find functions that can be exploited for DOM-based XSS by allowing navigation to javascript: URLs. This is a reconnaissance step for vulnerability discovery in web applications. Prerequisites include access to the SDK URL and a code beautifier tool.

## Requirements

1. Access to the SDK source URL
2. Code beautifier tool
3. JavaScript knowledge

## Defense

Defensive measures and detection strategies:

- Obfuscate critical code paths
- Regularly audit SDK for sinks like setWindowLocation

## Objectives

1. Beautify minified code
2. Identify XSS sinks
3. Document vulnerable functions

## Instructions

### Step 1: Download SDK Code

**Context**: Fetch the minified JavaScript from the CDN.

> Use a browser or curl to download app.js.

### Step 2: Beautify Code

**Context**: Apply code beautifier to make the code readable.

> Run the beautifier on the downloaded file.

### Step 3: Analyze for Sinks

**Context**: Search for navigation functions without protocol checks.

> Look for Shopify.API.setWindowLocation and confirm lack of validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[User Execution]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Code-Beautifier]]

## Tags

- code-analysis
- shopify
