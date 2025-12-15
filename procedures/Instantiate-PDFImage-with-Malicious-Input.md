---
tags:
  - rce
  - injection
  - node.js
type: procedure
tools:
  - '[[tools/pdf-image-exploit-script]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:32.578Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: b0cc37fb-9788-4bbf-ae39-49726e6e55eb
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Instantiate-PDFImage-with-Malicious-Input

## Summary

This procedure creates a PDFImage object using a malicious filename payload that includes shell metacharacters, exploiting the lack of input sanitization to prepare for command injection.

## Description

The PDFImage constructor in pdf-image passes the filename directly to ImageMagick shell commands without escaping, allowing attackers to inject arbitrary commands if the filename is user-controlled (e.g., from file uploads or API parameters). This step demonstrates breakout from quoted strings using payloads like '"; sleep 500 #', which closes the quote and injects a command. Expected outcome: Instance created, ready for execution trigger.

## Requirements

1. pdf-image module required and loaded
2. Node.js script environment
3. User-controlled input simulation (e.g., hardcoded payload for testing)

## Defense

Defensive measures and detection strategies:

- Sanitize all filenames with whitelisting (e.g., alphanumeric only)
- Use safe libraries like pdf-poppler instead of shell-dependent ones
- Log and validate all inputs to PDF processing functions

## Objectives

1. Inject shell metacharacters via filename parameter
2. Bypass command quoting in underlying exec calls
3. Set up for RCE without immediate execution

## Instructions

### Step 1: Craft Payload

**Context**: Prepare a filename string that escapes the shell command context.

**Command** (Payload definition):
```javascript
const maliciousFilename = '"; sleep 500 #';
```

> This payload closes a double quote, injects 'sleep 500', and comments out the rest with #. Expected output: String variable set.

### Step 2: Instantiate Object

**Context**: Pass the payload to the constructor to taint the internal command.

**Command** (PDFImage new):
```javascript
const pdfImage = new PDFImage(maliciousFilename);
console.log("Instance created with payload");
```

> Run in Node.js. Expected output: "Instance created with payload"; no errors, but command will execute on method call.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/pdf-image-exploit-script]]

## Tags

- rce
- injection
