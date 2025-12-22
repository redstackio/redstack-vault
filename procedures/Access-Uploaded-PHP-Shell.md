---
id: proc-access-shell
tags:
  - rce
  - webshell
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T05:32:13.405Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Access-Uploaded-PHP-Shell

## Summary

This procedure constructs and accesses the URL of the uploaded .php file to trigger execution of the embedded PHP shell, confirming RCE.

## Description

Using the username and timestamp, the file path is predictable (/uploads/profile/[USERNAME][timestamp].php). Visiting this URL executes the metadata PHP, e.g., reading /etc/passwd, exploiting the lack of content checks.

## Requirements

1. Extracted timestamp and username
2. Network access to the forum
3. Browser or HTTP client

## Defense

Defensive measures and detection strategies:

- Serve uploads from a non-executable directory or with .htaccess restrictions
- Scan uploaded files for executable code
- Monitor direct access to upload paths

## Objectives

1. Trigger PHP execution on the shell file
2. Verify RCE with output
3. Access server resources

## Instructions

### Step 1: Construct URL

**Context**: Build the predictable path.

**Instructions**: Format as https://forum.getmonero.org/uploads/profile/[USERNAME][timestamp].php, e.g., https://forum.getmonero.org/uploads/profile/lNobodyl1527341299.php.

**Expected Output**: N/A (preparation).

### Step 2: Access the URL

**Context**: Execute the shell.

**Instructions**: Open the URL in a browser.

**Expected Output**: PHP output, e.g., /etc/passwd contents.

**Success Indicators**:
- Server files displayed
- No 404 error

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- url-access
- shell-execution
