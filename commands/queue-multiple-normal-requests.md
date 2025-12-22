---
data: 'for i in range(14): engine.queue(target.req); time.sleep(0.05)'
tags:
  - scripting
  - turbo-intruder
type: command
executor: python
platforms:
  - Web
id: 83d08dd4-033f-4af9-8aa6-f73e57bc2f46
created_at: '2025-12-13T09:01:22.451Z'
updated_at: '2025-12-13T09:01:22.451Z'
verified: false
validated: true
submitted: true
---
# Queue Multiple Normal Requests

## Command

```python
for i in range(14): engine.queue(target.req); time.sleep(0.05)
```

## Description

Queues 14 normal requests with a delay to increase chances of poisoning a victim's request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `range(14)` | Loop 14 times | Yes |
| `time.sleep(0.05)` | Delay | Yes |

## Examples

### Basic Usage

```python
for i in range(14): engine.queue(target.req); time.sleep(0.05)
```

## Expected Output

Requests queued.

## Related

- [[procedures/Prepare-Turbo-Intruder-Desync-Script]]
