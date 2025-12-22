---
id: cmd-python-raw-input-001
data: 'last_id = raw_input("Prompt: ") or default'
tags:
  - input
  - scripting
type: command
output: User-provided string ID
executor: python
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.085Z'
verified: false
validated: true
submitted: true
---
# python-raw-input

## Command

```python
last_id = raw_input("\nEnter the last report you know about [Ignore if before #159875]: ") or "159874"
```

## Description

Prompts the user for the starting report ID in a Python 2 script, defaulting to 159874 if input is empty, used to initialize scanning baseline.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| prompt | String message for user input | Yes |
| default | Fallback value if empty | No |

## Examples

### Basic Usage

```python
last_id = raw_input("Enter ID: ") or "159874"
print(last_id)
```

### Advanced Usage

```python
last_id = raw_input("\nEnter the last report you know about [Ignore if before #159875]: ") or "159874"
int(last_id)  # Convert to int for use
```

## Expected Output

User input as string, e.g., '159890' or defaults to '159874'.

## Related

- [[Related Procedure: Determine-Last-Known-Report-ID]]
