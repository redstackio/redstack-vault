---
id: f45682c6-aa82-4dba-8b41-e94feb63f2ba
type: code
language: Bash
verified: true
created_at: '2020-03-17T03:51:54.037114+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - Obfuscation
  - Filename-Hiding
validated: true
---

# Create-File-With-Zero-Width-Space-Bash

## Code

```bash
touch i[CTRL + SHIFT + U]200b[ENTER]ndex.html
```

## Description

This bash code snippet demonstrates creating a file with an embedded zero-width space (Unicode U+200B) in the filename using the terminal's Unicode input method. It produces a file that appears visually identical to "index.html" but is actually distinct, useful for obfuscating malicious files in Linux environments to evade detection during reconnaissance or cleanup.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Filename parts | The base filename with insertion point for zero-width space | `i` and `ndex.html` |
| Unicode sequence | Ctrl+Shift+U followed by '200b' and Enter to insert U+200B | N/A |

## Usage

Execute this in a Linux terminal to create the obfuscated file. Ideal for post-exploitation to hide payloads, logs, or scripts in user directories or web roots. Combine with procedures like [[procedures/Creating-Files-with-Zero-Width-Spaces]] for full obfuscation workflows. Start with `touch` for files; adapt to `mkdir` for directories by replacing `touch` with `mkdir`.

## Detection

- Use `ls -b` to escape non-printable characters in listings.
- Scan with `find . -name '*[\xE2\x80\x8B]*' -print` or hex viewers to detect U+200B (bytes e2 80 8b).
- Monitor file creation via inotify or Auditd for unusual Unicode in names.
- Forensic tools like `strings` or `grep -P '\x{200b}'` on directory dumps.
