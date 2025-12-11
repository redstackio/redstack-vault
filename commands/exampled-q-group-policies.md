---
id: 76beafae-106f-440e-8b1f-5ecb6a95063d
name: exampled-q-group-policies
type: command
executor: bash
data: >-
  exampled q group group-policies-by-admin
  cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0
output: null
created_at: '2025-12-11T03:47:56.360Z'
updated_at: '2025-12-11T03:47:56.360Z'
platforms:
  - Blockchain
tags:
  - cosmos-sdk
  - query
verified: false
validated: true
submitted: true
---

# exampled-q-group-policies

## Command

```bash
exampled q group group-policies-by-admin cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0
```

## Description

Queries group policies by admin address.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `admin` | Admin address | Yes |

## Examples

### Basic Usage

```bash
exampled q group group-policies-by-admin cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0
```

## Expected Output

List of group policies.

## Related

- [[commands/exampled-tx-group-create]]
- [[procedures/Exploit-Cosmos-SDK-Groups-Module-with-Malicious-Weights]]
