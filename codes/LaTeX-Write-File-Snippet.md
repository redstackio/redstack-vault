---
id: 6bfcce1a-cf79-4709-8a20-287c80263390
type: code
language: tex
verified: true
created_at: '2023-04-06T03:56:01.772177+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - latex-injection
  - file-write
platforms:
  - Linux
  - Windows
  - macOS
validated: true
---

# LaTeX-Write-File-Snippet

## Code

```tex
\newwrite\outfile
\openout\outfile=cmd.tex
\write\outfile{Hello-world}
\write\outfile{Line 2}
\write\outfile{I like trains}
\closeout\outfile
```

## Description

This LaTeX code snippet creates a new file named 'cmd.tex' and writes three lines of text to it using LaTeX's file I/O primitives. It is designed for injection into vulnerable LaTeX processing contexts to perform unauthorized file creation, which can be used for data staging, persistence, or preparing payloads for further attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| outfile | File handle name (arbitrary) | outfile |
| cmd.tex | Target filename (after = in \openout) | data.txt or script.sh |
| {Hello-world} etc. | Content lines to write (in \write braces) | Custom text or encoded data |

## Usage

Inject this snippet into a user-controlled LaTeX input field in applications like web-based document editors or PDF generators. Trigger compilation to execute the file write. Customize the filename and content for specific needs, such as writing a reverse shell script. Used in red team operations to establish persistence in document processing pipelines.

## Detection

- Monitor LaTeX compilation logs for \newwrite, \openout, or \write commands in processed inputs.
- Audit file system for unexpected files in LaTeX working directories (e.g., /tmp, app data folders).
- Implement runtime analysis of LaTeX inputs to flag file I/O primitives.
- Use intrusion detection on document processing services for anomalous file creations.

## Related

- [[procedures/LaTeX-Injection-Write-File]]
