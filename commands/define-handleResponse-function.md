---
data: 'def handleResponse(req, interesting): table.add(req)'
tags:
  - scripting
  - turbo-intruder
type: command
executor: python
platforms:
  - Web
id: 498690c6-4cbb-45d3-93c7-adce719484d4
created_at: '2025-12-13T09:01:22.448Z'
updated_at: '2025-12-13T09:01:22.448Z'
verified: false
validated: true
submitted: true
---
# Define handleResponse Function

## Command

```python
def handleResponse(req, interesting): table.add(req)
```

## Description

Defines a function to handle responses by adding them to a table in Turbo Intruder.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `req` | Response object | Yes |
| `interesting` | Flag (unused) | No |

## Examples

### Basic Usage

```python
def handleResponse(req, interesting): table.add(req)
```

## Expected Output

Function defined.

## Related

- [[procedures/Prepare-Turbo-Intruder-Desync-Script]]
