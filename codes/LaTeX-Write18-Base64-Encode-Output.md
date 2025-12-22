---
id: 87a4c792-dae4-4ab3-aa83-df99148dd8ec
type: code
name: LaTeX-Write18-Base64-Encode-Output
language: tex
verified: true
created_at: '2023-04-06T03:56:01.799125+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - latex-injection
  - command-execution
  - base64
platforms:
  - Linux
validated: true
---

# LaTeX-Write18-Base64-Encode-Output

## Code

```tex
\immediate\write18{env | base64 > test.tex}
\input{text.tex}
```

## Description

This LaTeX code uses \write18 to execute a shell command that pipes environment variables to base64 encoding and saves the result to 'test.tex', then attempts to include 'text.tex' (note: potential filename mismatch). It facilitates obfuscated data exfiltration in LaTeX injection scenarios by encoding output for safe inclusion in documents.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| command | The shell command, including pipe to base64 | `env | base64` |
| output_file | File to save encoded output | `test.tex` |
| input_file | File to include (should match output_file) | `text.tex` |

## Usage

Inject into a LaTeX document processed on a vulnerable system. Compile with shell_escape to run the command and encode output. Decode the included base64 content post-compilation to retrieve data like environment variables.

## Detection

- Inspect LaTeX inputs for base64 pipes in \write18 commands.
- Monitor for base64-encoded files created during LaTeX processing.
- Enable logging of external command executions in LaTeX engines.

## Related

- [[procedures/LaTeX-Injection-for-Command-Execution]]
