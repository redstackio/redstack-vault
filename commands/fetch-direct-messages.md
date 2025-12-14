---
data: print api.direct_messages()
tags:
  - data-collection
  - direct-messages
type: command
output: List of Direct Messages
executor: python
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.490Z'
id: 3d59d9db-10e3-4197-ac9e-87effc9655d7
verified: false
validated: true
submitted: true
---
# fetch-direct-messages

## Command

```python
print api.direct_messages()
```

## Description

Fetches and prints all Direct Messages for the authenticated Twitter user using a Tweepy API instance. Demonstrates unauthorized access in privacy violation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| api | Authenticated Tweepy API object | Yes |

## Examples

### Basic Usage

```python
print api.direct_messages()
```

### Advanced Usage

Fetch and process:

```python
dms = api.direct_messages()
for dm in dms:
    print(dm.text, dm.sender.screen_name)
```

## Expected Output

[<tweepy.models.DirectMessage object at 0x...>, ...] with details like id, text, sender_id, etc.

## Related

- [[commands/create-authenticated-api]]
- [[procedures/Fetch-Direct-Messages-via-Authenticated-API]]
