---
id: proc-load-crossdomain-policy-flash
tags:
  - crossdomain-bypass
  - flash-policy
  - xml-policy
type: procedure
tools:
  - '[[tools/Adobe-Flash-SWF]]'
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
updated_at: '2025-12-14T17:29:56.776Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Load-Permissive-Crossdomain-Policy-via-Flash-SWF

## Summary

This procedure uses an Adobe Flash SWF file to load Vimeo's permissive crossdomain.xml policy, enabling arbitrary domain access to the OAuth endpoints and bypassing subdirectory restrictions.

## Description

Vimeo's crossdomain.xml at /oauth/ allows access from any domain (*), which the SWF loads explicitly via Security.loadPolicyFile. This overrides stricter policies (e.g., at /authorize/crossdomain.xml), allowing cross-domain requests. Prerequisites include the SWF embedded in a webpage and victim interaction. Outcome: Flash security sandbox is relaxed for api.vimeo.com.

## Requirements

1. Compiled SWF file with ActionScript capabilities
2. Access to Flash development tools (e.g., Adobe Flash Professional)
3. Victim's browser with Flash enabled and Vimeo session active
4. Network connectivity to api.vimeo.com

## Defense

Defensive measures and detection strategies:

- Remove or restrict crossdomain.xml to specific domains
- Disable Flash support or use sandboxing
- Monitor Flash policy file requests in server logs
- Enforce same-origin policy strictly for sensitive endpoints

## Objectives

1. Load the permissive policy to enable cross-domain access
2. Bypass Flash security restrictions for OAuth endpoints
3. Prepare for token extraction without user approval

## Instructions

### Step 1: Develop SWF ActionScript

**Context**: Write code to load the policy file.

In ActionScript 3.0:

```actionscript
import flash.system.Security;
Security.loadPolicyFile('https://api.vimeo.com/oauth/crossdomain.xml');
trace('Policy loaded');
```

> Compile to SWF using Flash compiler. This fetches and applies the * policy.

### Step 2: Embed and Test SWF

**Context**: Integrate into webpage and verify policy load.

Embed as in Step 1 of attack chain. Use Flash debugger to check for policy application.

> Expected: No security errors; policy allows * access.

### Step 3: Confirm Override

**Context**: Ensure subdirectory policies are bypassed.

Attempt a test cross-domain load post-policy; log success.

> Success if subsequent requests to /authorize succeed from arbitrary domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Adobe-Flash-SWF]]

## Tags

- crossdomain-bypass
- flash-policy
- xml-policy
