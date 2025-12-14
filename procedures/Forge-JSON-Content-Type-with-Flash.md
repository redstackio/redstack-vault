---
tags:
  - flash
  - header
  - bypass
  - web
type: procedure
tools:
  - '[[tools/Adobe-Flash]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:36.189Z'
sub_techniques: []
id: 36e02439-82af-4a21-8afa-e152ffa477ad
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Forge JSON Content-Type with Flash

## Summary

Use a Flash SWF file to set a custom Content-Type header (application/json;charset=UTF-8) in a cross-origin request, bypassing modern browser restrictions.

## Description

Browsers block custom headers in cross-site requests, but Flash (pre-deprecation) allowed this via URLRequest. Combined with the crossdomain policy, this forges the header needed for the endpoint's JSON validation.

## Requirements

1. Flash development environment
2. Hosted SWF file
3. Crossdomain policy in place

## Defense

Defensive measures and detection strategies:

- Deprecate and block Flash
- Enforce strict header validation
- Use SameSite cookies

## Objectives

1. Set required Content-Type
2. Enable JSON request acceptance
3. Bypass CSRF header checks

## Instructions

### Step 1: Develop SWF File

**Context**: Create Flash to send request.

Use ActionScript to load policy and send URLRequest to redirector with header.

Example AS3:

```actionscript
import flash.net.URLRequest;
import flash.net.URLRequestHeader;
var req:URLRequest = new URLRequest("https://testingsubdomain.000webhostapp.com/stripo.php?userid=123");
req.method = URLRequestMethod.POST;
req.data = JSON.stringify(payload);
req.requestHeaders.push(new URLRequestHeader("Content-Type", "application/json;charset=UTF-8"));
```

> Compile to SWF and host.

### Step 2: Trigger from Page

**Context**: Embed SWF in malicious page.

Direct victim to page with <object> embedding SWF.

> Expected: SWF executes, forges header.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Adobe-Flash]]

## Tags

- [[flash]]
- [[header]]
