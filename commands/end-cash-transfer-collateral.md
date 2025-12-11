---
data: end.cash();
tags:
  - blockchain
  - exploit
type: command
executor: solidity
platforms:
  - Ethereum
id: fcfc9246-9c1b-4f91-b0cd-ff809ebb7eb6
created_at: '2025-12-11T06:10:22.213Z'
updated_at: '2025-12-11T06:10:22.213Z'
verified: false
validated: true
submitted: true
---
# end-cash-transfer-collateral

## Command

```solidity
end.cash();
```

## Description

Completes the conversion of packed DAI to collateral, transferring it to the attacker.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | N/A |

## Examples

### Basic Usage

```solidity
end.cash();
```

## Expected Output

Transfers all collateral to the attacker if DAI amount matches total supply.

## Related

- [[procedures/Convert-DAI-to-Collateral-via-End.Pack-and-End.Cash]]
- [[commands/end-pack-prepare-collateral]]
