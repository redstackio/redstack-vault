---
type: command
executor: bash
data: pip install pyjwt==0.4.3
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - installation
  - python
  - jwt
verified: true
validated: true
---

# pip-install-pyjwt-0-4-3

## Command

```bash
pip install pyjwt==0.4.3
```

## Description

Installs the vulnerable version 0.4.3 of the PyJWT library, which permits signing HS256 tokens with mismatched key types like RSA public keys, enabling key confusion attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `==0.4.3` | Specifies the exact vulnerable version to install | Yes |

## Examples

### Basic Usage

```bash
pip install pyjwt==0.4.3
```

### In Virtual Environment

```bash
python -m venv jwt_env
source jwt_env/bin/activate
pip install pyjwt==0.4.3
```

## Expected Output

Collecting pyjwt==0.4.3
  Downloading PyJWT-0.4.3.tar.gz
  ...
Successfully installed PyJWT-0.4.3

## Related

- [[procedures/JWT-Key-Confusion-Attack-RS256-to-HS256]]
