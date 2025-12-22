---
id: 1b7fbc2b-f18e-4e54-8930-590c6dcfb95c
type: code
name: LaTeX-Write18-Command-Redirect-to-File
language: tex
verified: true
created_at: '2023-04-06T03:56:01.798992+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - latex-injection
  - command-execution
platforms:
  - Linux
validated: true
---

# LaTeX-Write18-Command-Redirect-to-File

## Code

```tex
\immediate\write18{id > output}
\input{output}
```

## Description

This LaTeX code snippet exploits the shell_escape feature to execute a shell command (here, 'id') and redirect its output to a file named 'output', which is then included in the LaTeX document for display. It is used in LaTeX injection attacks to run system commands and embed results in the rendered output.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| command | The shell command to execute within \write18 | `id` or `ls -la /home` |
| output_file | Name of the file to redirect output to | `output` |

## Usage

Embed this code in a LaTeX document submitted to a vulnerable typesetting service or compiler with --shell-escape enabled. During compilation, the command runs, and the output file is included, allowing attackers to verify execution and extract information like user ID.

## Detection

- Monitor LaTeX compilation processes for --shell-escape flag usage.
- Scan LaTeX sources for \write18 or \immediate primitives in user inputs.
- Log file creations in LaTeX working directories and anomalous shell executions (e.g., via procmon or audit logs).

## Related

- [[procedures/LaTeX-Injection-for-Command-Execution]]
