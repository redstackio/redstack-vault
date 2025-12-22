---
id: 722829de-0957-4960-8bc1-4388bda68ba5
name: pywhisker-list-key-credentials
type: command
executor: bash
data: >-
  python3 pywhisker.py -d "$_DOMAIN" -u "$_USERNAME" -p "$_PASSWORD" --target
  "$_TARGET_NAME" --action "list"
output: null
created_at: '2023-04-06T03:56:06.261674+00:00'
updated_at: '2023-04-10T20:26:09.591812+00:00'
platforms:
  - Linux
  - Windows
tags:
  - active-directory
  - key-credentials
verified: true
validated: true
---

# pywhisker-list-key-credentials

## Command

```bash
python3 pywhisker.py -d "$_DOMAIN" -u "$_USERNAME" -p "$_PASSWORD" --target "$_TARGET_NAME" --action "list"
```

## Description

Lists key credentials for a target using PyWhisker, authenticating with provided credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d $_DOMAIN | Domain name (e.g., domain.local) | Yes |
| -u $_USERNAME | Username for auth | Yes |
| -p $_PASSWORD | Password for auth | Yes |
| --target $_TARGET_NAME | Target user/computer | Yes |
| --action "list" | Action to perform | Yes |

## Examples

### Basic Usage

```bash
python3 pywhisker.py -d "domain.local" -u "user1" -p "complexpassword" --target "user2" --action "list"
```

## Expected Output

JSON or formatted list of credentials with GUIDs and keys.

## Related

- [[procedures/Shadow-Credentials-for-Windows-Hello]]
- [[tools/PyWhisker]]
