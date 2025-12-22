---
id: 50c9b0a5-4bcd-40ea-a09b-e737486ba100
type: procedure
verified: true
submitted: false
created_at: '2019-10-10T00:28:44.147383+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Command and Control]]'
techniques:
  - '[[Software Packing]]'
sub_techniques: []
tags:
  - cryptography
  - data-obfuscation
  - steganography
commands:
  - '[[commands/steghide-embed-file-in-image]]'
platforms:
  - Linux
tools:
  - '[[tools/Steghide]]'
skill_level: beginner
impact_level: low
detection_risk: medium
validated: true
---

# Embed-File-in-Image-Using-Steghide

## Summary

This procedure uses the Steghide tool to embed a secret file, such as an SSH public key or sensitive data, into a cover image or audio file via steganography. The resulting file appears innocent while concealing the embedded content, which can be extracted later with the correct passphrase. This technique is useful for data exfiltration, covert communication, or bypassing basic file inspection in red team operations.

## Description

Steganography hides data within non-secret files like images (JPEG, BMP) or audio (WAV, AU) without visibly altering the carrier file. Steghide employs algorithms like JPEG-JSTEG or BMP-LSB to embed files securely, prompting for a passphrase during embedding and extraction. The primary changes are an increase in file size and potential minor quality degradation in the cover file. This procedure assumes a Linux environment with Steghide installed and focuses on embedding into an image. It maps to MITRE ATT&CK technique T1027.002 (Software Packing) under the obfuscation tactic, as it packs data into innocuous formats to evade detection.

## Requirements

1. Linux system (e.g., Kali or Ubuntu) with administrative access for installation if needed.
2. Steghide tool installed ([[tools/Steghide]]).
3. Cover file (e.g., innocent image like wallpaper.jpg) and embedded file (e.g., id_rsa.pub for SSH key).
4. Passphrase for encryption (chosen by operator, minimum 8 characters recommended).

## Defense

Defensive measures and detection strategies:

- File integrity monitoring: Use tools like Tripwire or OSSEC to detect unexpected file size changes or modifications in shared directories.
- Steganography detection: Employ tools like Stegdetect or StegExpose to analyze images for anomalies in LSB patterns or entropy.
- Network egress filtering: Block or inspect outbound transfers of large media files that may contain hidden payloads.
- Endpoint detection: Monitor for Steghide process execution via EDR tools like CrowdStrike or Sysmon logging unusual image/audio manipulations.

## Objectives

1. Successfully embed a file into a cover image without visible alterations.
2. Protect the embedded data with a passphrase to prevent unauthorized extraction.
3. Create a steganographic carrier suitable for covert transmission or storage.
4. Verify the embedding process through file size comparison and optional extraction test.

## Instructions

### Step 1: Prepare Files

**Context**: Select and verify the cover file (an innocent image) and the file to embed (e.g., sensitive data or key). Ensure the cover file is larger than the embedded file to minimize suspicion.

Place both files in the working directory. For example, use a wallpaper image as cover and an SSH public key as embedded.

### Step 2: Embed the File

**Context**: Use Steghide to embed the secret file into the cover, prompting for a passphrase to encrypt the data. This step performs the core steganographic operation.

**Command** ([[commands/steghide-embed-file-in-image]]):
```bash
steghide embed -ef $_EMBEDDED_FILE -cf $_COVER_FILE
```

When executed, the command will prompt for a passphrase twice. Enter a strong passphrase (e.g., 'secret'). The tool will embed the file and output a success message if completed.

### Step 3: Verify Embedding

**Context**: Confirm the operation by checking the output file size and optionally attempting extraction to ensure integrity.

Compare file sizes before and after using `ls -lh`. To test extraction without saving, run `steghide extract -sf output.jpg` and enter the passphrase; it should prompt to overwrite the original embedded file if successful.

**Expected Output**: After embedding, expect a message like "embedding \"$_EMBEDDED_FILE\" in \"$_COVER_FILE\"... done". The output file (e.g., wallpaper.jpg with embedded data) will have a slightly larger size.
