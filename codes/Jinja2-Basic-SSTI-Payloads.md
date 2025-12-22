---
id: 1387b80a-c435-4f07-93bc-6d71f447128a
name: Jinja2-Basic-SSTI-Payloads
type: code
language: Python
verified: true
created_at: '2023-04-06T03:56:39.560000+00:00'
updated_at: '2023-04-10T20:23:44.334338+00:00'
platforms:
  - Web
  - Python
tags:
  - ssti
  - jinja2
  - detection
  - payload
validated: true
---

# Jinja2-Basic-SSTI-Payloads

## Code

```python
16[[5*5]]
7777777
[('name', 'Jinja'), ('version', '2.11.3'), ('packages', {'jinja': '2.11.3', 'markupsafe': '1.1.1'})]
```

## Description

This code snippet contains sample Jinja2 template expressions and their expected rendered outputs for detecting basic Server-Side Template Injection (SSTI) vulnerabilities. The first line shows arithmetic evaluation (e.g., 4*4=16), the second uses bracketed expressions for math (5*5=25), the third demonstrates string repetition (7*'7'='7777777'), and the last accesses the config object to reveal environment details like version and packages. These are injected into vulnerable parameters to confirm template evaluation on the server.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | These are static payloads; substitute directly into HTTP parameters without variables. | N/A |

## Usage

Inject these payloads into user-controlled inputs in a Jinja2-powered web app, such as a search query: `q= {{7*'7'}}`. Observe if the response renders the evaluated result (e.g., '7777777') rather than the literal text. Use in conjunction with tools like curl or Burp Suite during web vulnerability testing. Once confirmed, chain to more advanced payloads for RCE.

## Detection

- Web logs showing template syntax like {{ }} or arithmetic expressions in inputs.
- Anomalous responses with evaluated code outputs or config dumps.
- Increased CPU usage from template rendering or error logs with 'TemplateSyntaxError'.
- WAF alerts on payloads containing '*', '{{', or 'config'.

## Related

- [[procedures/Basic-Jinja2-Server-Side-Template-Injection]]
- [[Python]]
