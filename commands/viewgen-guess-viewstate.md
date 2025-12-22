---
id: 8d976236-7fe9-4814-a212-6681e835bde2
name: viewgen-guess-viewstate
type: command
executor: bash
data: viewgen --guess "$_VIEWSTATE_DATA"
output: null
created_at: '2023-04-06T03:55:53.378545+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - viewstate
  - asp-net
  - decryption
verified: true
validated: true
---

# viewgen-guess-viewstate

## Command

```bash
viewgen --guess "$_VIEWSTATE_DATA"
```

## Description

This command uses ViewGen to analyze a base64-encoded ASP.NET ViewState string and guess its encryption status, signature algorithm, and potential machine key requirements. It is useful for initial reconnaissance of .NET application cryptography during exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VIEWSTATE_DATA | Base64-encoded __VIEWSTATE value from intercepted HTTP request | Yes |
| --guess | Flag to perform algorithm guessing on the provided data | Yes |

## Examples

### Basic Usage

```bash
viewgen --guess "/wEPDwUKMTYyODkyNTEzMw9kFgICAw8WAh4HZW5jdHlwZQUTbXVsdGlwYXJ0L2Zvcm0tZGF0YWRkuVmqYhhtcnJl6Nfet5ERqNHMADI="
```

### Advanced Usage

For encrypted ViewState with modifier:
```bash
viewgen --guess "encrypted_viewstate" --modifier "viewstategenerator_value"
```

## Expected Output

```
[+] ViewState is not encrypted
[+] Signature algorithm: SHA1
```
If encrypted, it may output key hints or errors indicating needed machine keys.

## Related

- [[Related Procedure]]: [[procedures/Exploit-IIS-Machine-Key-via-API-Key-Leaks]]
- [[Related Tool]]: [[tools/viewgen]]
