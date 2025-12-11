---
id: 6104ab20-be8c-4c9e-b7fe-cbc8737d07e9
name: exampled-tx-group-create
type: command
executor: bash
data: >-
  exampled tx group create-group-with-policy
  cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0 "" "" members.json policy.json
  --gas auto --yes
output: null
created_at: '2025-12-11T03:47:56.365Z'
updated_at: '2025-12-11T03:47:56.365Z'
platforms:
  - Blockchain
tags:
  - cosmos-sdk
  - transaction
verified: false
validated: true
submitted: true
---

# exampled-tx-group-create

## Command

```bash
exampled tx group create-group-with-policy cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0 "" "" members.json policy.json --gas auto --yes
```

## Description

Creates a group with the specified policy and members in the Cosmos chain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `admin` | Admin address | Yes |
| `members` | Members JSON file | Yes |
| `policy` | Policy JSON file | Yes |
| `--gas` | Gas limit (auto) | No |
| `--yes` | Confirm without prompt | No |

## Examples

### Basic Usage

```bash
exampled tx group create-group-with-policy cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0 "" "" members.json policy.json --gas auto --yes
```

## Expected Output

Group created successfully.

## Related

- [[commands/exampled-q-group-policies]]
- [[procedures/Exploit-Cosmos-SDK-Groups-Module-with-Malicious-Weights]]
