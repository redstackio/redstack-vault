---
data: end.pack(daiAmount);
tags:
  - blockchain
  - exploit
type: command
executor: solidity
platforms:
  - Ethereum
id: 8e674e1a-d4e3-4496-8a8d-2ebcfe00d10c
created_at: '2025-12-11T06:10:22.228Z'
updated_at: '2025-12-11T06:10:22.228Z'
verified: false
validated: true
submitted: true
---
# end-pack-prepare-collateral

## Command

```solidity
end.pack(daiAmount);
```

## Description

Prepares the specified DAI amount for conversion to collateral in the end contract.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `daiAmount` | Amount of DAI to pack | Yes |

## Examples

### Basic Usage

```solidity
end.pack(1000000000000000000000000);
```

## Expected Output

Prepares for cashing out collateral.

## Related

- [[procedures/Convert-DAI-to-Collateral-via-End.Pack-and-End.Cash]]
- [[commands/end-cash-transfer-collateral]]
