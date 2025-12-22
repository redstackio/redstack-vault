---
tags:
  - ssrf
  - ghost-cms
  - source-analysis
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T03:53:38.712Z'
skill_level: advanced
impact_level: low
detection_risk: low
sub_techniques: []
id: 9fff52f2-cf04-4264-9a79-ee4eea4379bf
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Analyze-Ghost-Source-Code-for-SSRF-Bypass

## Summary

This procedure examines the Ghost CMS source code to uncover the SSRF bypass via oEmbed link extraction, revealing unvalidated fetches in the backend.

## Description

The file core/server/api/canary/oembed.js contains fetchOembedData, which fetches the user-provided URL, and getOembedUrlFromHTML, which uses cheerio to parse the HTML and extract <link rel="alternate" type="application/json+oembed" href="..."/> without validating the href URL. This allows a secondary fetch to arbitrary internal resources.

## Requirements

1. Access to Ghost CMS source code (open-source or decompiled)
2. Code editor or browser for static analysis
3. Knowledge of Node.js and cheerio library

## Defense

Defensive measures and detection strategies:

- Perform static code analysis for URL validation gaps
- Audit third-party modules like cheerio for parsing risks
- Implement code signing or integrity checks

## Objectives

1. Identify the extraction logic flaw
2. Confirm lack of URL scheme/IP validation
3. Plan HTML-based bypass

## Instructions

### Step 1: Locate Relevant File

**Context**: Find the oEmbed handling code.

Open core/server/api/canary/oembed.js in a code editor.

> File contains the vulnerable functions.

### Step 2: Review Functions

**Context**: Analyze fetchOembedData and getOembedUrlFromHTML.

Examine how fetchOembedData retrieves content and passes it to getOembedUrlFromHTML, noting no checks on extracted hrefs before refetching.

> Discovery of unvalidated secondary request confirms bypass viability.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- ghost-cms
- source-analysis
