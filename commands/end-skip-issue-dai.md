---
data: end.skip(auctionId);
tags:
  - blockchain
  - exploit
type: command
executor: solidity
platforms:
  - Ethereum
id: d63f5fe8-fb76-4647-9d39-88763d42506c
created_at: '2025-12-11T06:10:22.242Z'
updated_at: '2025-12-11T06:10:22.242Z'
verified: false
validated: true
submitted: true
---
# end-skip-issue-dai

## Command

```solidity
end.skip(auctionId);
```

## Description

Processes the specified auction in the end contract, issuing free DAI based on the fake bid value.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `auctionId` | ID of the fake auction | Yes |

## Examples

### Basic Usage

```solidity
end.skip(123);
```

## Expected Output

Issuance of free DAI to the attacker equal to the fake bid amount.

## Related

- [[procedures/Issue-Free-DAI-via-End.Skip]]
- [[commands/flip-kick-fake-auction]]
