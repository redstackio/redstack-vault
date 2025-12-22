---
id: 2d099d09-8672-475c-844f-e817f7b5ed82
name: extract-hidden-file-from-image-with-steghide
type: procedure
verified: true
submitted: false
created_at: '2019-10-10T00:34:20.445224+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Collection|TA0009]]'
techniques:
  - '[[techniques/Archive Collected Data|T1560.001]]'
sub_techniques: []
tags:
  - steganography
  - cryptography
  - data-obfuscation
commands:
  - '[[commands/steghide-extract-hidden-file-in-image]]'
platforms:
  - Linux
tools:
  - '[[tools/Steghide]]'
validated: true
---

# extract-hidden-file-from-image-with-steghide

## Summary

This procedure extracts embedded files from images using steganography tools, often revealing hidden credentials or keys in CTF or real-world scenarios where attackers hide data in publicly accessible media.

## Description

Steganography conceals data within non-secret files like images. Steghide embeds/extracts using passwords, supporting JPEG/PNG. After discovering an image via directory brute-force, extraction requires the passphrase, yielding files like SSH keys for further access.

## Requirements

- Image file (cover file) downloaded from target
- Correct passphrase (brute-force if unknown)
- Steghide installed

## Defense

- Avoid embedding secrets in public files
- Scan uploads for steganography with tools like stegdetect
- Use content security policies to restrict image handling

## Objectives

- Recover hidden data from images
- Obtain credentials for CMS login
- Decrypt stego payloads

## Instructions

### Step 1: Download the Cover Image

**Context**: Retrieve the image from the web server, e.g., via wget after directory enumeration.

No command; use browser or wget http://$_TARGET_IP/path/to/image.jpg.

### Step 2: Extract Embedded File

**Context**: Run extraction, providing the passphrase to decrypt and output the hidden file.

**Command** ([[commands/steghide-extract-hidden-file-in-image]]):
```bash
steghide extract -sf $_IMAGE_FILE
```

> Prompts for passphrase; success extracts file like 'id_rsa.pub' to current directory.
