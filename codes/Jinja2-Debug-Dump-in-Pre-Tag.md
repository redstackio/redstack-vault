---
type: code
language: html
verified: true
tags:
  - ssti
  - jinja2
  - debug
  - template-injection
platforms:
  - Web
validated: true
---

# Jinja2-Debug-Dump-in-Pre-Tag

## Code

```html
<pre>{% debug %}</pre>
```

## Description

This HTML-wrapped Jinja2 snippet uses a <pre> tag to inject the debug statement, ensuring the output is displayed with preserved formatting in HTML contexts. It dumps template variables for SSTI reconnaissance, useful when basic injection is escaped or poorly rendered.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Static payload; adapt to the injection point (e.g., wrap in quotes for attributes). | N/A |

## Usage

Inject into vulnerable HTML-rendered inputs, such as error messages or dynamic content sections (e.g., <div>{vulnerable}</div> becomes <pre>{% debug %}</pre>). View the response in a browser or proxy tool to read the formatted variable dump.

## Detection

- Scan responses for <pre> tags containing debug output or variable lists.
- Input validation to strip HTML tags combined with template syntax.
- Behavioral monitoring for anomalous response sizes due to debug dumps.
- Server-side logging of rendered templates with user inputs.

## Related

- [[procedures/Exploit-Jinja2-Debug-Statement-for-SSTI]]
