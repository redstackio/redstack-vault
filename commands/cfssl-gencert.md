---
id: cmd-12
data: >-
  cfssl gencert -ca=ca.pem -ca-key=ca.key -profile=kubernetes csr.json |
  cfssljson -bare user
tags:
  - cert
  - forge
type: command
output: user-*.pem files
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.522Z'
verified: false
validated: true
submitted: true
---
# cfssl-gencert

## Command

```bash
cfssl gencert -ca=ca.pem -ca-key=ca.key -profile=kubernetes csr.json | cfssljson -bare user
```

## Description

Generates and signs a certificate from CSR using CA, outputting PEM files via cfssljson.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-ca` | CA cert file | Yes |
| `-ca-key` | CA private key | Yes |
| `-profile` | CSR profile | Yes |
| `csr.json` | Input CSR | Yes |
| `cfssljson -bare user` | Output prefix | Yes |

## Examples

### Basic Usage

```bash
cfssl gencert -ca=ca.pem -ca-key=ca.key csr.json | cfssljson -bare client
```

### Advanced Usage

```bash
cfssl gencert --config config.json ...
```

## Expected Output

user.csr, user.pem, user-key.pem.

## Related

- [[commands/kubectl-config-set-credentials]]
