---
data: 'python3 post_auth_nosqli.py -u attacker -p attacker ''http://localhost:3000'''
tags:
  - exploit
  - rce
type: command
output: 'Auth successful. Leaking data... Admin taken over. Shell: >'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.407Z'
id: 47ec7fe3-8cd1-443e-b66c-d35944dada5d
verified: false
validated: true
submitted: true
---
# python3-post-auth-nosqli-py

## Command

```bash
python3 post_auth_nosqli.py -u attacker -p attacker 'http://localhost:3000'
```

## Description

Executes the full exploit chain: auth, injection, leakage, takeover, webhook creation, and RCE shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u attacker | Username | Yes |
| -p attacker | Password | Yes |
| http://localhost:3000 | Target URL | Yes |

## Examples

### Basic Usage

```bash
python3 post_auth_nosqli.py -u attacker -p attacker 'http://localhost:3000'
```

## Expected Output

Leaks data, compromises admin, drops interactive shell.

## Related

- [[commands/pip3-install-requests-bcrypt]]
