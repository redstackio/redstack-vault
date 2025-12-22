---
id: 33f1ce51-1679-4c9b-bf36-8ca7edfa715d
name: pywhisker-remove-key-credential
type: command
executor: bash
data: >-
  python3 pywhisker.py -d "$_DOMAIN" -u "$_USERNAME" -p "$_PASSWORD" --target
  "$_TARGET_NAME" --action "remove" --device-id "$_DEVICE_ID"
output: null
created_at: '2023-04-06T03:56:06.261844+00:00'
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

# pywhisker-remove-key-credential

## Command

```bash
python3 pywhisker.py -d "$_DOMAIN" -u "$_USERNAME" -p "$_PASSWORD" --target "$_TARGET_NAME" --action "remove" --device-id "$_DEVICE_ID"
```

## Description

Removes a key credential by device ID using PyWhisker.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d $_DOMAIN | Domain | Yes |
| -u $_USERNAME | Username | Yes |
| -p $_PASSWORD | Password | Yes |
| --target $_TARGET_NAME | Target | Yes |
| --action "remove" | Action | Yes |
| --device-id $_DEVICE_ID | GUID to remove | Yes |

## Examples

### Basic Usage

```bash
python3 pywhisker.py -d "domain.local" -u "user1" -p "complexpassword" --target "user2" --action "remove" --device-id "a8ce856e-9b58-61f9-8fd3-b079689eb46e"
```

## Expected Output

Confirmation of removal.

## Related

- [[procedures/Shadow-Credentials-for-Windows-Hello]]
- [[tools/PyWhisker]]
