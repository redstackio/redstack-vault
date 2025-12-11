---
id: a97f7ef8-2637-4255-9e71-40c206f9c221
name: exampled-tx-group-submit-proposal
type: command
executor: bash
data: exampled tx group submit-proposal proposal.json --gas auto --yes
output: null
created_at: '2025-12-11T03:47:56.340Z'
updated_at: '2025-12-11T03:47:56.340Z'
platforms:
  - Blockchain
tags:
  - cosmos-sdk
  - transaction
verified: false
validated: true
submitted: true
---

# exampled-tx-group-submit-proposal

## Command

```bash
exampled tx group submit-proposal proposal.json --gas auto --yes
```

## Description

Submits a group proposal from a JSON file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `proposal` | Proposal JSON file | Yes |
| `--gas` | Gas limit (auto) | No |
| `--yes` | Confirm without prompt | No |

## Examples

### Basic Usage

```bash
exampled tx group submit-proposal proposal.json --gas auto --yes
```

## Expected Output

Proposal submitted.

## Related

- [[commands/exampled-tx-group-vote]]
- [[procedures/Exploit-Cosmos-SDK-Groups-Module-with-Malicious-Weights]]
