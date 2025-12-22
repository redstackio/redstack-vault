---
id: 073ba3f1-2b76-40e1-acd7-4f51eacfbfff
name: pywhisker-add-key-credential
type: command
executor: bash
data: >-
  python3 pywhisker.py -d "$_FQDN_DOMAIN" -u "$_USERNAME" -p "$_CERT_PASSWORD"
  --target "$_TARGET_SAMNAME" --action "add"
output: null
created_at: '2023-04-06T03:56:06.261767+00:00'
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

# pywhisker-add-key-credential

## Command

```bash
python3 pywhisker.py -d "$_FQDN_DOMAIN" -u "$_USERNAME" -p "$_CERT_PASSWORD" --target "$_TARGET_SAMNAME" --action "add"
```

## Description

Adds a new key credential using PyWhisker. The password parameter here is for the certificate if provided.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d $_FQDN_DOMAIN | FQDN of domain | Yes |
| -u $_USERNAME | Auth username | Yes |
| -p $_CERT_PASSWORD | Certificate password | Yes |
| --target $_TARGET_SAMNAME | Target SAM | Yes |
| --action "add" | Action | Yes |

## Examples

### Basic Usage

```bash
python3 pywhisker.py -d "contoso.local" -u "admin" -p "certpass" --target "targetuser" --action "add"
```

## Expected Output

Success message confirming addition.

## Related

- [[procedures/Shadow-Credentials-for-Windows-Hello]]
- [[tools/PyWhisker]]
