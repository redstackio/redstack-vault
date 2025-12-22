---
id: cmd-python-time-sleep-001
data: |-
  import time
  time.sleep(30)
tags:
  - delay
  - polling
type: command
output: 'No output, pauses execution'
executor: python
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.070Z'
verified: false
validated: true
submitted: true
---
# python-time-sleep

## Command

```python
import time
time.sleep(30)
```

## Description

Pauses script execution for 30 seconds to implement delays in polling loops, reducing request frequency and detection risk during scans for non-existent report IDs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| seconds | Duration in seconds (e.g., 30) | Yes |

## Examples

### Basic Usage

```python
import time
time.sleep(30)
print("Resumed after 30s")
```

### Advanced Usage

```python
import time
if len(response.text) == 36:
    time.sleep(30)  # Retry delay
```

## Expected Output

No output; execution resumes after specified delay.

## Related

- [[Related Procedure: Poll-for-New-Report-Submissions]]
