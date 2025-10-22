---
id: b72cc282-56aa-4dd2-bae7-380d9318ea3e
name: Unicode Filter Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.005450+00:00'
updated_at: '2023-04-10T20:21:30.213979+00:00'
tags:
- '[[Bypass using Unicode]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
commands:
- '[[Unicode character transformation]]'
---

# Unicode Filter Bypass

## Summary

Unicode filter bypass is a type of cross-site scripting (XSS) attack that uses Unicode characters to bypass input validation filters. This technique is commonly used to inject malicious code into web pages, allowing attackers to steal sensitive information or take control of the victim's browser. B

## Description

# Description

Unicode filter bypass is a type of cross-site scripting (XSS) attack that uses Unicode characters to bypass input validation filters. This technique is commonly used to inject malicious code into web pages, allowing attackers to steal sensitive information or take control of the victim's browser. By using Unicode characters that look similar to normal ASCII characters, attackers can circumvent filters that are designed to block certain types of input. This can allow them to bypass security measures and execute malicious code on the victim's machine.

From a technical perspective, this attack works by using Unicode character transformation to encode malicious code in a way that bypasses input validation filters. The attacker can then use the encoded payload to execute arbitrary code on the victim's machine. This attack can be particularly effective against web applications that are not properly secured or that do not have adequate input validation filters in place.

From a business perspective, this attack can be used to steal sensitive information such as login credentials, credit card numbers, and other personal data. It can also be used to take control of the victim's browser, allowing the attacker to perform actions on their behalf.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of Unicode character transformation techniques

## Defense

1. Implement input validation filters that are designed to detect and block Unicode character transformations

1. Use a web application firewall (WAF) to detect and block malicious input

1. Regularly update and patch web applications to prevent known vulnerabilities

## Objectives

1. Inject malicious code into web pages

1. Steal sensitive information

1. Take control of the victim's browser

# Instructions

1. This command transforms Unicode characters into their corresponding characters, encoded in UTF-8 format. The transformed characters are shown in the 'data' field.

**Code**: [[Unicode character U+FF1C FULLWIDTH LESS­THAN SIGN ]]

> The 'data' field shows the list of Unicode characters that were transformed along with their corresponding characters. This command is useful when dealing with encoded text or URLs, where certain characters may be encoded in Unicode format. By using this command, the encoded characters can be transformed into their corresponding characters, making it easier to read and understand the text or URL. The 'E.g' field provides an example of how the command can be used to transform encoded characters in a URL.

**Command** ([[Unicode character transformation]]):

```bash
Unicode character U+FF1C FULLWIDTH LESS­THAN SIGN (encoded as %EF%BC%9C) was transformed into U+003C LESS­THAN SIGN (<)

Unicode character U+02BA MODIFIER LETTER DOUBLE PRIME (encoded as %CA%BA) was transformed into U+0022 QUOTATION MARK (\")

Unicode character U+02B9 MODIFIER LETTER PRIME (encoded as %CA%B9) was transformed into U+0027 APOSTROPHE (\')

E.g : http://www.example.net/something%CA%BA%EF%BC%9E%EF%BC%9Csvg%20onload=alert%28/XSS/%29%EF%BC%9E/
%EF%BC%9E becomes >
%EF%BC%9C becomes <
```

2. To use this Unicode Uppercase Bypass, you can convert the Unicode characters to uppercase or lowercase to bypass certain security restrictions. The specific characters that can be used to bypass security restrictions are provided in the 'data' field of this command.

**Code**: [[İ (%c4%b0).toLowerCase() => i
ı (%c4%b1).toUpperCa]]

> The 'data' field provides a list of Unicode characters that can be used to bypass security restrictions. By converting these characters to uppercase or lowercase, you can bypass certain security restrictions that may be in place. This technique can be used in various contexts, such as in HTML tags or in JavaScript code.

## Commands Used

- [[Unicode character transformation]]

## Tags

- [[Bypass using Unicode]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]
