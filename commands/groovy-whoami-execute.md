---
id: cmd-groovy-whoami
data: println "whoami".execute().text
tags:
  - rce
  - discovery
type: command
output: null
executor: groovy
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.531Z'
verified: false
validated: true
submitted: true
---
# groovy-whoami-execute

## Command

```groovy
println "whoami".execute().text
```

## Description

This Groovy command runs the 'whoami' shell command to identify the current user executing the Jenkins process, confirming RCE and privilege context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `"whoami"` | The shell command string to display the current user | Yes |
| `.execute()` | Spawns the command as a process | Yes |
| `.text` | Captures the process output as a string | Yes |
| `println` | Outputs the result to the console | Yes |

## Examples

### Basic Usage

```groovy
println "whoami".execute().text
```

### Advanced Usage

```groovy
println "id".execute().text
```

## Expected Output

The username under which the Jenkins process runs, e.g., "jenkins" or "root".

## Related

- [[commands/groovy-ls-execute]]
- [[procedures/Execute-OS-Commands-via-Groovy]]
