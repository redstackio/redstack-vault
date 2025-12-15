---
tags:
  - malicious-script
  - upload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Remote File Copy]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 4356568e-ad72-4cb0-8611-e0bba7ca50db
created_at: '2025-12-14T17:23:24.997Z'
updated_at: '2025-12-14T17:23:24.997Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Create Malicious Script in jsreport

## Summary

This procedure uploads a malicious JavaScript file via the jsreport interface, which will be executed later through the unintended require vulnerability.

## Description

jsreport allows unauthenticated script creation, storing files on the filesystem. The payload demonstrates RCE by logging and listing directory contents using Node.js fs module.

## Requirements

1. Access to jsreport web interface
2. Discovered script-manager port (from prior step)

## Defense

Defensive measures and detection strategies:

- Require authentication for script uploads
- Validate script content for malicious requires
- Scan uploaded files for dangerous Node.js APIs like fs

## Objectives

1. Create and save 'pwn.js'
2. Ensure storage on accessible filesystem path
3. Prepare for path traversal exploitation

## Instructions

### Step 1: Create Script in Interface

**Context**: Add the payload to a new script entry.

**Command** (Browser Action):
No CLI; in jsreport, go to 'Scripts' > 'New Script', name 'pwn.js', content:

```javascript
console.log('PWNED');
var ls = require('fs').readdirSync('./');
console.log(ls);
```

Save.

> File stored as /jsreport/data/pwn.js/content.js.

### Step 2: Verify Creation

**Context**: Check if the script is listed and accessible.

**Command** (Browser):
Refresh scripts list.

> 'pwn.js' appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- malicious-script
- upload
