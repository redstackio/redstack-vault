---
id: 4e857791-a19e-42ae-83bc-b35d24ab662c
type: code
language: Ruby
verified: true
created_at: '2023-04-06T03:56:40.226221+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - SSTI
  - RCE
  - Ruby
  - Slim
  - Enumeration
validated: true
---

# Ruby-Slim-SSTI-Environment-Variables

## Code

```ruby
#{ %x|env| }
```

## Description

This Ruby code snippet exploits Server-Side Template Injection (SSTI) using the Slim template engine to execute the 'env' system command and output all environment variables from the server. The '#{}' interpolation in Slim allows embedding Ruby expressions, and '%x|env|' is a safe navigation syntax for command execution, returning the output as a string. This can expose sensitive configuration data like database credentials or API keys stored in the environment.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | Hardcoded to 'env'; replace 'env' with other commands (e.g., '%x|id|') for different reconnaissance. No variables needed. | N/A |

## Usage

Inject into a Slim-rendered input field in a Ruby application (confirm vulnerability with '#{7*7}' outputting '49'). Submit via HTTP request, and the response will include the environment dump. Use this after initial SSTI confirmation to gather config secrets for lateral movement or privilege escalation in red team engagements.

## Detection

- Application logs showing Slim interpolation of suspicious Ruby code like '%x' or command keywords.
- WAF signatures for Slim-specific patterns such as '#{' or '%x' in user inputs.
- Anomaly detection in server responses containing environment variable listings (e.g., grep for 'PATH=' or 'DB_PASSWORD' in logs).
- Endpoint protection monitoring for unexpected 'env' command spawns from web processes.

## Related

- [[procedures/Ruby-Server-Side-Template-Injection-for-Code-Execution]]
