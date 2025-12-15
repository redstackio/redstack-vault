---
data: './poc.sh [GitLab host] [Project URL] [target ID] [Repeat count of request]'
tags:
  - dos
  - script
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:55.983Z'
id: acf02c41-3f97-47b9-9335-c47733fc9104
verified: false
validated: true
submitted: true
---
# poc-sh-run-dos-script

## Command

```bash
./poc.sh [GitLab host] [Project URL] [target ID] [Repeat count of request]
```

## Description

Executes a shell script to perform server-side DoS on GitLab by looping large comment POST requests, exhausting CPU resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[GitLab host]` | Target hostname (e.g., gitlab.com) | Yes |
| `[Project URL]` | Full project path (e.g., /user/test01) | Yes |
| `[target ID]` | Issue ID (e.g., 1) | Yes |
| `[Repeat count]` | Number of concurrent requests (e.g., 100) | Yes |

## Examples

### Basic Usage

```bash
./poc.sh gitlab.com /user/test01 1 100
```

### Advanced Usage

With higher loop:
```bash
./poc.sh selfhosted.example.com /group/project 3 500
```

## Expected Output

Script runs silently, spawning background processes; server experiences CPU exhaustion and service denial.

## Related

- [[commands/curl-post-large-comment]]
- [[procedures/Execute-Server-Side-DoS-with-Script]]
