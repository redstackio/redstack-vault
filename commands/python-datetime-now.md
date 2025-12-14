---
id: cmd-python-datetime-now-001
data: |-
  from datetime import datetime
  timestamp = datetime.now()
tags:
  - timestamp
  - logging
type: command
output: Current datetime object
executor: python
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.059Z'
verified: false
validated: true
submitted: true
---
# python-datetime-now

## Command

```python
from datetime import datetime
timestamp = datetime.now()
print(timestamp)
```

## Description

Captures the current date and time as a datetime object, used to timestamp detections of new report submissions in monitoring scripts for activity analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses system clock | N/A |

## Examples

### Basic Usage

```python
from datetime import datetime
print(datetime.now())
```

### Advanced Usage

```python
from datetime import datetime
if len(response.text) == 0:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Submission at {timestamp}")
```

## Expected Output

Datetime string or object, e.g., '2023-10-01 12:00:00'.

## Related

- [[Related Procedure: Log-and-Monitor-Submission-Activity]]
