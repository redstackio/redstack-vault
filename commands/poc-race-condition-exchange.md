---
id: 123e4567-e89b-12d3-a456-426614174008
name: poc-race-condition-exchange
type: command
executor: bash
data: ./accessTokenRaceConditionPOC.sh
output: Multiple valid access tokens generated from single code (probabilistic)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.888Z'
platforms:
  - Web
tags:
  - oauth2
  - race-condition
verified: false
validated: true
submitted: true
---

# poc-race-condition-exchange

## Command

```bash
./accessTokenRaceConditionPOC.sh
```

## Description

Executes a POC script to demonstrate a race condition in Vimeo's code-to-token exchange, potentially generating multiple tokens from one code via concurrent requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Runs with predefined code | No |

## Examples

### Basic Usage

```bash
./accessTokenRaceConditionPOC.sh
```

### Advanced Usage

```bash
# Modify script for specific code if needed
./accessTokenRaceConditionPOC.sh
```

## Expected Output

Output showing multiple successful token responses from parallel exchanges.

## Related

- [[commands/exchange-oauth-code-for-token]]
