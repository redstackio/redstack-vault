---
id: d86bb418-6f54-49c7-b394-079db9bb93ec
name: exampled-tx-group-vote
type: command
executor: bash
data: >-
  exampled tx group vote 1 cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0
  VOTE_OPTION_YES "" --gas auto --yes
output: null
created_at: '2025-12-11T03:47:56.335Z'
updated_at: '2025-12-11T03:47:56.335Z'
platforms:
  - Blockchain
tags:
  - cosmos-sdk
  - transaction
verified: false
validated: true
submitted: true
---

# exampled-tx-group-vote

## Command

```bash
exampled tx group vote 1 cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0 VOTE_OPTION_YES "" --gas auto --yes
```

## Description

Votes on a group proposal.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `proposal_id` | Proposal ID (e.g., 1) | Yes |
| `voter` | Voter address | Yes |
| `option` | Vote option (e.g., VOTE_OPTION_YES) | Yes |
| `metadata` | Metadata (empty string) | No |
| `--gas` | Gas limit (auto) | No |
| `--yes` | Confirm without prompt | No |

## Examples

### Basic Usage

```bash
exampled tx group vote 1 cosmos14xzyhnr8w098awcf8l6t57qw3qlhcwsntytvm0 VOTE_OPTION_YES "" --gas auto --yes
```

## Expected Output

Vote submitted, but may trigger chain halt on tally.

## Related

- [[commands/exampled-tx-group-submit-proposal]]
- [[procedures/Exploit-Cosmos-SDK-Groups-Module-with-Malicious-Weights]]
