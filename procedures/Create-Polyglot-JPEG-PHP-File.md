---
id: proc-uuid-polyglot-create-001
tags:
  - polyglot-file
  - php-embed
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
  - Windows
  - macOS
submitted: true
created_at: '2024-10-05T12:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:10.160Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Create-Polyglot-JPEG-PHP-File

## Summary

This procedure creates or obtains a polyglot file that is a valid JPEG image containing embedded PHP code, allowing it to pass image validation checks while hiding executable content for potential code execution.

## Description

In the context of exploiting file upload vulnerabilities like in Nextcloud, a polyglot file combines image data with script code in a way that the file parses correctly as an image but can execute as PHP if served appropriately. The file must start with JPEG headers (e.g., FF D8 FF) followed by image data, then append PHP code after the image footer (FF D9), ensuring no corruption. This bypasses MIME and structural validations that do not scan for embedded scripts.

## Requirements

1. Access to a hex editor or text editor capable of binary manipulation (e.g., HxD, Vim)
2. Basic knowledge of JPEG structure and PHP syntax
3. Internet access to download example polyglots if not creating manually

## Defense

Defensive measures and detection strategies:

- Implement deep content scanning for uploads beyond MIME types (e.g., using ClamAV or custom scripts to detect embedded code)
- Enforce strict file extension whitelisting and rename uploads to non-executable formats
- Log and monitor upload attempts for anomalous file sizes or types

## Objectives

1. Produce a file that validates as image/jpeg
2. Embed functional PHP code (e.g., phpinfo() for testing)
3. Ensure compatibility with target upload systems

## Instructions

### Step 1: Obtain Base JPEG

**Context**: Start with a valid, small JPEG image to minimize size and ensure clean structure.

Download or create a simple JPEG file, such as a 1x1 pixel image.

### Step 2: Embed PHP Code

**Context**: Append PHP code after the JPEG end marker without invalidating the image.

Open the JPEG in a hex editor. Locate the end of image marker (FF D9). After it, insert PHP opening tag and code, e.g., `<?php phpinfo(); ?>`. Save as binary to preserve structure.

Alternatively, download pre-made examples from http://91.121.108.101/image1.jpg, which already embeds such code.

**Expected Output**: File named `image1.jpg` that displays as an image but contains PHP when opened in text editor.

### Step 3: Validate Polyglot

**Context**: Confirm the file passes image validation tools.

Test with an image viewer to ensure it renders, and use `file` command or online MIME checker to confirm image/jpeg detection.

**Expected Output**: No errors in rendering; MIME type reported as image/jpeg.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- polyglot-file
- php-embed
- file-creation
