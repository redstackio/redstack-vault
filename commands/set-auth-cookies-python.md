---
data: 'cookies = {''appSession'': ''<dummy_account_session>''}'
tags:
  - auth
  - cookies
type: command
output: null
executor: python
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.404Z'
id: 9e6182d0-56dd-4086-addd-ff7dd432c987
verified: false
validated: true
submitted: true
---
# set-auth-cookies-python

## Command

```python
cookies = {'appSession': '<dummy_account_session>'}
```

## Description

Sets a dictionary with the appSession cookie for authenticating API requests as the dummy account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| appSession | Session token value | Yes |

## Examples

### Basic Usage

```python
cookies = {'appSession': 'your_session_token_here'}
```

## Expected Output

No output; creates cookies dict.

## Related

- [[commands/post-upload-metadata-python]]
