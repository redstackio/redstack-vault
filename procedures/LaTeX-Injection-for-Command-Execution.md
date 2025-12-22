---
id: ce883307-75e6-4051-b3b1-4f2fdbd7e5d4
name: LaTeX-Injection-for-Command-Execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.801562+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/XSL Script Processing|T1220 - XSL Script Processing]]'
sub_techniques: []
tags:
  - '[[tags/Command execution]]'
  - '[[tags/LaTex Injection]]'
commands: []
platforms:
  - Linux
tools: []
validated: true
---

# LaTeX-Injection-for-Command-Execution

## Summary

This procedure demonstrates how to exploit LaTeX's shell escape feature to execute arbitrary system commands on a target system processing LaTeX documents. By injecting malicious LaTeX code that leverages the \write18 primitive, attackers can run shell commands, redirect output to files, and retrieve results within the generated document, enabling remote code execution in environments where LaTeX rendering is allowed, such as document collaboration platforms or typesetting services.

## Description

LaTeX is a powerful typesetting system widely used for creating technical documents. When the shell_escape option is enabled (via --shell-escape flag in pdflatex or similar), LaTeX allows execution of external shell commands through primitives like \immediate\write18{command}. This feature, intended for including dynamic content, can be abused for command injection if user-supplied input is processed without sanitization. Attackers inject such code into LaTeX sources, PDFs, or web forms that compile LaTeX, leading to command execution on the server or client rendering the document. This technique is particularly effective against academic, publishing, or collaborative editing systems. Success depends on the LaTeX engine (e.g., pdfLaTeX, XeLaTeX) having shell escape enabled and the target having write permissions in the working directory.

## Requirements

1. Access to inject LaTeX code into a document processed by a LaTeX compiler on the target system (e.g., via file upload, web form, or shared document).
2. The LaTeX installation must have shell_escape enabled (default in some distributions but configurable).
3. Target system must be Unix-like (Linux/macOS) with common shell commands available (e.g., id, env, ls).
4. Write permissions in the LaTeX working directory to create output files.

## Defense

- Disable shell_escape in LaTeX configurations (e.g., run pdflatex without --shell-escape) and use sandboxed environments like TeX Live's restricted modes.
- Sanitize user inputs in LaTeX-processing applications by stripping or escaping dangerous primitives like \write18.
- Monitor LaTeX compilation logs and system process creation for unexpected shell invocations (e.g., via auditd or Sysmon).
- Implement application whitelisting to restrict LaTeX to read-only operations and containerize rendering processes.

## Objectives

1. Inject LaTeX code to execute arbitrary shell commands on the target system.
2. Redirect and retrieve command output within the LaTeX document for exfiltration or verification.
3. Encode output (e.g., via base64) to bypass simple filters or facilitate data extraction.

## Instructions

### Step 1: Execute Command and Redirect Output to File

**Context**: Use the \write18 primitive to run a shell command and save its output to a file, then include the file in the LaTeX document to display the results. This allows verification of execution and potential data retrieval.

**Code** ([[codes/LaTeX-Write18-Command-Redirect-to-File]]):

```tex
\immediate\write18{id > output}
\input{output}
```

> Replace 'id' with the desired command (e.g., 'whoami' or 'ls /etc'). Compile the LaTeX document (e.g., pdflatex --shell-escape document.tex). The command executes during compilation, creating 'output' file, which is then input into the document.

### Step 2: Execute Command and Save Base64-Encoded Output

**Context**: Pipe command output to base64 encoding and save to a file for obfuscated retrieval. This helps evade detection by non-printable characters or binary data in the document. Note: Ensure the input file reference matches the output file name to avoid errors.

**Code** ([[codes/LaTeX-Write18-Base64-Encode-Output]]):

```tex
\immediate\write18{env | base64 > test.tex}
\input{text.tex}
```

> Customize the command (e.g., 'id | base64 > output.b64'). After compilation, decode the included content with base64 -d to retrieve original output. The slight filename mismatch in the original (text.tex vs test.tex) may cause inclusion failure; adjust as needed in practice.
