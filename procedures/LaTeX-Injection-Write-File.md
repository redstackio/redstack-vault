---
id: e034c869-bfe3-4e7b-b49e-8fd280ea3fd5
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.773485+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
sub_techniques: []
tags:
  - '[[tags/LaTeX-Injection]]'
  - '[[tags/File-Write]]'
commands: []
platforms:
  - Linux
  - Windows
  - macOS
tools: []
validated: true
---

# LaTeX-Injection-Write-File

## Summary

This procedure demonstrates how to inject LaTeX code into a vulnerable document processing system to write an arbitrary file on the target system. By exploiting insufficient input sanitization in LaTeX parsers, an attacker can use built-in LaTeX commands to create and populate files, potentially enabling persistence, data staging for exfiltration, or further exploitation.

## Description

LaTeX injection occurs when user-supplied input is processed as LaTeX code without proper validation, allowing attackers to execute LaTeX primitives that interact with the file system. This specific technique focuses on file writing using commands like \newwrite, \openout, \write, and \closeout. In scenarios such as web-based LaTeX editors, PDF generators, or document collaboration tools (e.g., Overleaf-like services), this can lead to server-side file creation. The written file could contain scripts, configurations, or data dumps. Note that while this example writes a simple text file, extensions like \write18 (if enabled) could escalate to shell command execution, but this procedure sticks to pure file I/O. Success depends on the LaTeX engine's permissions and the injection point's context.

## Requirements

1. Access to an input field or endpoint that processes user-supplied LaTeX code (e.g., a web form for document rendering).
2. Knowledge of the target system's LaTeX environment and file system permissions.
3. A vulnerable LaTeX processor (e.g., pdfLaTeX, XeLaTeX) running with write access to the target directory.
4. Optional: Tools for testing injection like a browser or [[tools/Burp-Suite]] for intercepting requests.

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and validation to strip or escape LaTeX commands from user inputs.
- Use sandboxed LaTeX processing environments with restricted file system access (e.g., via TeX Live's shell-escape disablement).
- Employ allowlisting for permitted LaTeX commands, blocking file I/O primitives like \newwrite and \openout.
- Monitor LaTeX processing logs for unexpected file creations and audit document rendering endpoints for injection attempts.
- Run LaTeX engines under least-privilege accounts to limit writable directories.

## Objectives

1. Inject LaTeX code to create a new file on the target system.
2. Write specified content to the file for staging data or persistence.
3. Verify file creation without triggering alerts in restricted environments.

## Instructions

### Step 1: Identify Injection Point

**Context**: Locate a vulnerable input where LaTeX code is processed, such as a document editor or API endpoint that compiles user content into PDF or renders previews.

Test for injection by submitting basic LaTeX like \textbf{test} and observing if it's rendered. If successful, proceed to file write primitives.

### Step 2: Craft and Inject LaTeX Payload

**Context**: Use the LaTeX file write code snippet to specify the target filename and content. This step accomplishes file creation by defining a write handle, opening the output, writing lines, and closing it.

**Code** ([[codes/LaTeX-Write-File-Snippet]]):

```tex
\newwrite\outfile
\openout\outfile=cmd.tex
\write\outfile{Hello-world}
\write\outfile{Line 2}
\write\outfile{I like trains}
\closeout\outfile
```

> Inject this code into the vulnerable field. The \newwrite creates a file handle, \openout specifies the output file (e.g., cmd.tex in the current working directory of the LaTeX process), \write appends content line by line, and \closeout finalizes the file. Customize the filename after = in \openout and content in \write braces. Expected output during processing: No errors in LaTeX compilation logs, and the file appears in the target directory.

### Step 3: Trigger Processing and Verify

**Context**: Submit the input to force LaTeX compilation or rendering, then check for the written file.

If the system provides logs or a file browser, inspect the working directory (often /tmp or the app's data dir). Manually verify by accessing the server if possible, or look for side effects like error messages indicating file I/O.

> Expected output: A new file (e.g., cmd.tex) containing the written lines. If permissions are insufficient, LaTeX may error with "I can't write on file 'cmd.tex'".

### Step 4: Iterate for Complex Content

**Context**: For multi-line or binary content, chain multiple \write commands or encode data appropriately.

Adjust the payload to write scripts (e.g., a shell script) for further exploitation, ensuring LaTeX treats it as text.
