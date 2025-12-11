---
id: 3cc86303-710e-4de6-af8f-e8985ac3273a
name: exampled-tx-bank-send
type: command
executor: bash
data: >-
  exampled tx bank send cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0
  cosmos17pmq7hp4upvmmveqexzuhzu64v36re3w3447n7dt46uwp594wtpsqv4fn5 100stake
  --gas auto --yes
output: null
created_at: '2025-12-11T03:47:56.351Z'
updated_at: '2025-12-11T03:47:56.351Z'
platforms:
  - Blockchain
tags:
  - cosmos-sdk
  - transaction
verified: false
validated: true
submitted: true
---

# exampled-tx-bank-send

## Command

```bash
exampled tx bank send cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0 cosmos17pmq7hp4upvmmveqexzuhzu64v36re3w3447n7dt46uwp594wtpsqv4fn5 100stake --gas auto --yes
```

## Description

Sends tokens to a specified address in the Cosmos chain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `from` | Sender address | Yes |
| `to` | Recipient address | Yes |
| `amount` | Amount to send (e.g., 100stake) | Yes |
| `--gas` | Gas limit (auto) | No |
| `--yes` | Confirm without prompt | No |

## Examples

### Basic Usage

```bash
exampled tx bank send cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0 cosmos17pmq7hp4upvmmveqexzuhzu64v36re3w3447n7dt46uwp594wtpsqv4fn5 100stake --gas auto --yes
```

## Expected Output

Transaction successful.

## Related

- [[commands/exampled-tx-group-create]]
- [[procedures/Exploit-Cosmos-SDK-Groups-Module-with-Malicious-Weights]]
