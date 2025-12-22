---
id: proc-uuid-1
tags:
  - recon
  - wordpress
  - swf
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-13T23:52:55.643Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Analyze WordPress flashmediaelement.swf File

## Summary

This procedure involves downloading and decompiling the flashmediaelement.swf file from a WordPress installation to analyze its ActionScript code, focusing on flashVars handling, GET parameter sanitization, character blacklisting, and ExternalInterface validations for identifying XSS bypass opportunities.

## Description

In the context of exploiting a reflected Flash XSS in WordPress's MediaElement library, this reconnaissance step examines the SWF at /wp-includes/js/mediaelement/flashmediaelement.swf. The file processes GET parameters into flashVars but includes protections: scrubbing dangerous params like 'jsinitfunction', blacklisting payload characters, and checking ExternalInterface.objectID. Analysis reveals bypasses via invalid URL escapes, ES6 backticks, and browser auto-embedding. Prerequisites include access to a vulnerable WordPress site and tools for SWF decompilation. Expected outcome: Detailed understanding of the vulnerability chain leading to arbitrary JS execution.

## Requirements

1. Public access to the target WordPress site's SWF file
2. SWF decompiler (e.g., JPEXS Free Flash Decompiler)
3. Basic knowledge of ActionScript and URL encoding

## Defense

Defensive measures and detection strategies:

- Disable direct SWF access via .htaccess or server config
- Monitor for unusual SWF requests in access logs
- Upgrade WordPress and MediaElement to patched versions

## Objectives

1. Identify protection mechanisms in SWF code
2. Map bypass techniques for subsequent exploitation
3. Confirm vulnerability presence without execution

## Instructions

### Step 1: Download the SWF File

**Context**: Retrieve the target SWF to enable local analysis.

Use browser or curl to download:

```bash
curl -O https://target.com/wp-includes/js/mediaelement/flashmediaelement.swf
```

> Downloads the binary SWF file for decompilation.

### Step 2: Decompile and Review Code

**Context**: Inspect ActionScript for parameter processing logic.

Open in decompiler and search for 'flashVars', 'jsinitfunction', ExternalInterface.call, and blacklist arrays.

**Expected Output**: Code snippets showing scrubbing (e.g., delete if name == 'jsinitfunction'), blacklist checks (e.g., for '(', '{'), and objectID validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[wordpress]]
