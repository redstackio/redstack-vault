---
id: 0acf16f7-8af5-46d3-b2f4-453402aed841
name: turbo-intruder-handle-response
type: command
executor: python
data: |-
  def handleResponse(req, interesting):
      # Add request to table
      table.add(req)
output: null
created_at: '2023-04-06T03:56:31.880512+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - race-condition
  - turbo-intruder
verified: true
validated: true
---

# turbo-intruder-handle-response

## Command

```python
def handleResponse(req, interesting):
    # Add request to table
    table.add(req)
```

## Description

This Python function processes responses in Turbo Intruder attacks, adding each request-response pair to the results table for analysis. It can be extended to flag interesting responses based on content, such as success indicators from a race condition exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| req | The request-response object from Turbo Intruder | Yes |
| interesting | List to append flagged responses (optional extension) | No |

## Examples

### Basic Usage

Paste into Turbo Intruder's handleResponse function editor.

### Advanced Usage

Add filtering logic:

```python
if 'unauthorized' not in req.response.lower():
    table.add(req)
    if 'success' in req.response:
        interesting.append(req)
```

## Expected Output

Results table in Turbo Intruder populates with columns for request, response, length, etc. Successful races show inconsistent or leaked data in response bodies.

## Related

- [[procedures/Exploit-Race-Condition-with-Turbo-Intruder]]
- [[commands/turbo-intruder-queue-requests]]
