---
id: b6ff4fc2-bcee-41a5-a65d-b7249c0193ca
type: code
language: Ruby
verified: true
created_at: '2023-04-06T03:56:40.181381+00:00'
updated_at: '2023-04-10T20:23:34.487395+00:00'
tags:
  - ssti
  - ruby
  - payload
  - file-read
platforms:
  - Web
  - Linux
validated: true
---

# Ruby-ERB-File-Read-Etc-Passwd

## Code

```ruby
<%= File.open('/etc/passwd').read %>
```

## Description

This Ruby ERB template payload exploits Server-Side Template Injection (SSTI) vulnerabilities in Ruby-based web applications to read the /etc/passwd file on a Linux server. When injected into a vulnerable parameter processed by the ERB engine, it executes during template rendering, outputting the file's contents which include user account information such as usernames, UIDs, home directories, and default shells.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| '/etc/passwd' | Path to the target file on the Linux system | '/etc/passwd' |

## Usage

Inject this payload into user-controlled inputs in Ruby applications using ERB templates, such as search fields or dynamic content sections in Ruby on Rails or Sinatra apps. Use tools like Burp Suite to send the payload via HTTP requests (e.g., GET or POST parameters). The payload executes server-side, displaying the file contents in the response body. Ideal for initial reconnaissance in web exploitation scenarios to enumerate system users.

## Detection

- Web application logs showing ERB evaluation errors or unexpected file access patterns.
- WAF alerts for '<%= %>' patterns or anomalous requests containing Ruby code.
- File integrity monitoring (FIM) tools detecting reads of sensitive files like /etc/passwd by the web process.
- Response analysis for leaked system information in HTTP bodies.

## Related

- [[procedures/Ruby-SSTI-to-Read-Etc-Passwd-File]]
