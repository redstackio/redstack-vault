---
id: 64b23141-fd68-42ee-8375-1943f1a18cc0
name: Twig-Debug-Dump-Payload
type: code
language: twig
verified: true
created_at: '2023-04-06T03:56:40.276302+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - PHP
tags:
  - ssti
  - twig
  - payload
  - rce
validated: true
---

# Twig-Debug-Dump-Payload

## Code

```twig
{{7*7}}
{{7*'7'}} would result in 49
{{dump(app)}}
{{dump(_context)}}
{{app.request.server.all|join(',')}}
```

## Description

This Twig payload demonstrates basic arithmetic, string operations, variable dumping, and server variable extraction for Server-Side Template Injection (SSTI) when debug mode is enabled. It starts with simple tests to confirm injection and escalates to dumping application context and joining server arrays for reconnaissance.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| app | The Symfony/Twig app object (auto-available in debug mode) | N/A (contextual) |
| _context | Current template context variables | N/A (contextual) |
| app.request.server.all | Array of server superglobals (e.g., HTTP headers, paths) | N/A (contextual) |

No user-defined variables; placeholders are implicit in the injection point.

## Usage

Inject this payload into user-controlled inputs like form parameters, cookies, or headers in a Twig-rendered PHP application. Start with '{{7*7}}' to test, then progress to dumps. Deliver via HTTP requests (e.g., POST data or GET params). Use in red team engagements to confirm SSTI and gather intel for RCE chaining.

## Detection

- WAF rules blocking '{{' or 'dump(' patterns in requests.
- Application logs showing rendered template errors or unusual variable dumps.
- Response body containing debug output like object representations or joined server vars.
- Increased server load from complex template evaluations.

## Related

- [[procedures/Twig-Debugging-Injection-for-Arbitrary-Code-Execution]]
- [[Burp-Suite]]
