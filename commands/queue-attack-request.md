---
data: engine.queue(attack)
tags:
  - scripting
  - turbo-intruder
type: command
executor: python
platforms:
  - Web
id: 49571e58-59b9-4a28-bc65-7ffc02818b04
created_at: '2025-12-13T09:01:22.453Z'
updated_at: '2025-12-13T09:01:22.453Z'
verified: false
validated: true
submitted: true
---
# Queue Attack Request

## Command

```python
engine.queue(attack)
```

## Description

Queues the modified attack request in Turbo Intruder for sending.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `attack` | The modified request | Yes |

## Examples

### Basic Usage

```python
engine.queue(attack)
```

## Expected Output

Request queued.

## Related

- [[procedures/Prepare-Turbo-Intruder-Desync-Script]]
