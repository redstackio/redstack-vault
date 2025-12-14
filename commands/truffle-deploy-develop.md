---
data: truffle deploy --network develop
tags:
  - deployment
  - smart-contracts
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2024-10-01T12:00:00Z'
updated_at: '2025-12-14T17:26:12.540Z'
id: 7792bab1-1b1b-42a7-9026-69321a3ba633
verified: false
validated: true
submitted: true
---
# truffle-deploy-develop

## Command

```bash
truffle deploy --network develop
```

## Description

This command deploys smart contracts using the Truffle framework to a local development network, generating the necessary build/contracts/ directory with JSON artifacts required for scripts like saveContracts.js.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--network` | Specifies the deployment network (e.g., develop for local) | Yes |

## Examples

### Basic Usage

```bash
truffle deploy --network develop
```

### Advanced Usage

```bash
truffle deploy --network develop --reset
```

## Expected Output

Compilation and deployment logs, followed by creation of build/contracts/ with files like MyContract.json containing ABI and bytecode.

## Related

- [[Related Procedure]]
