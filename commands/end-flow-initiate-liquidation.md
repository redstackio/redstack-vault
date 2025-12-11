---
data: end.flow();
tags:
  - blockchain
  - exploit
type: command
executor: solidity
platforms:
  - Ethereum
id: c09dfb1a-34c7-498b-a523-fecb95f34c33
created_at: '2025-12-11T06:10:22.210Z'
updated_at: '2025-12-11T06:10:22.210Z'
verified: false
validated: true
submitted: true
---
# end-flow-initiate-liquidation

## Command

```solidity
end.flow();
```

## Description

Fixes the exchange rate for redeeming collateral, initiating the liquidation phase.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | N/A |

## Examples

### Basic Usage

```solidity
end.flow();
```

## Expected Output

System enters liquidation phase.

## Related

- [[procedures/Create-Fake-Auction-via-Flip.Kick]]
- [[commands/flip-kick-fake-auction]]
