---
id: proc-execute-shell-commands
tags:
  - rce
  - command-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/base64-encode-cmd]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
  - '[[PowerShell]]'
updated_at: '2025-12-14T05:32:13.402Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
  - '[[PowerShell]]'
---
# Execute-Commands-via-Shell

## Summary

This procedure uses the uploaded PHP shell to run arbitrary commands by appending base64-encoded payloads to the URL, demonstrating full server compromise.

## Description

The shell supports a ?do=base64exec parameter for command execution. Encode commands in base64 to bypass simple filters, allowing actions like pwd, ls, or more destructive operations on the Laravel/PHP backend.

## Requirements

1. Accessible shell URL from previous step
2. Base64 encoding capability (built-in tools)
3. Target commands for execution

## Defense

Defensive measures and detection strategies:

- Disable or sandbox PHP execution in upload directories
- Implement WAF rules to block base64 command patterns
- Monitor server logs for anomalous PHP executions from uploads

## Objectives

1. Run system commands via the webshell
2. Exfiltrate data or escalate access
3. Confirm persistent RCE

## Instructions

### Step 1: Encode Command

**Context**: Prepare the command in base64 to send via URL.

**Command** ([[commands/base64-encode-cmd]]):
```bash
echo -n 'pwd' | base64
```

> Outputs base64 string, e.g., "cHdk". Use for sensitive commands to avoid URL encoding issues.

### Step 2: Execute via URL

**Context**: Append to shell URL for RCE.

**Instructions**: Visit [shell-url]?do=base64exec&cmd=[base64], e.g., ?do=base64exec&cmd=cHdk.

**Expected Output**: Command result, e.g., "/var/www/html".

**Success Indicators**:
- Command output displayed
- Arbitrary execution possible

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]
- [[PowerShell]]

### Sub-Techniques


## Commands Used

- [[commands/base64-encode-cmd]]

## Tools Used


## Tags

- base64-exec
- webshell-command
