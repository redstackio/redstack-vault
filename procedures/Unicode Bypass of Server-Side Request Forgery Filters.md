---
id: 0df9438a-5856-479e-b2c6-e147cc5e3ff7
name: Unicode Bypass of Server-Side Request Forgery Filters
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.587906+00:00'
updated_at: '2023-04-10T20:23:58.327662+00:00'
tags:
- '[[Bypassing filters]]'
- '[[Bypass using unicode]]'
- '[[Server-Side Request Forgery]]'
commands:
- '[[String of Digits]]'
---

# Unicode Bypass of Server-Side Request Forgery Filters

## Summary

This technique involves using unicode encoding to bypass filters that are designed to prevent Server-Side Request Forgery attacks. By encoding the input data in unicode, it is possible to evade filters that are looking for specific keywords or patterns. This can allow an attacker to send requests t

## Description

# Description

This technique involves using unicode encoding to bypass filters that are designed to prevent Server-Side Request Forgery attacks. By encoding the input data in unicode, it is possible to evade filters that are looking for specific keywords or patterns. This can allow an attacker to send requests to internal systems that are not intended to be accessible from the internet, potentially leading to further compromise of the target network.

Technical Explanation: By using unicode encoding, the attacker can represent characters in a way that bypasses filters that are looking for specific patterns. For example, the attacker can use the unicode representation of a period (U+002E) instead of the standard ASCII period (.) to bypass a filter that is looking for URLs containing periods.

Business Value: This technique can allow an attacker to gain access to internal systems that are not intended to be accessible from the internet, potentially leading to the compromise of sensitive data or systems.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of unicode encoding

1. Ability to craft HTTP requests

## Defense

1. Implement input validation to prevent unicode-encoded input

1. Use a web application firewall to detect and block unicode-encoded requests

1. Regularly review logs for suspicious activity related to Server-Side Request Forgery

## Objectives

1. Bypass filters that are designed to prevent Server-Side Request Forgery attacks

1. Send requests to internal systems that are not intended to be accessible from the internet

1. Compromise sensitive data or systems

# Instructions

1. The '\d' pattern matches any Unicode digit character.

**Code**: [[\d]]

> Unicode digits include decimal digits and digits that need special handling, such as the compatibility superscript digits. This pattern can be used to match any digit character in any language that uses digits.

2. The includes() method determines whether a string contains the characters of a specified string. This method returns true if the string contains the characters, and false if not.

**Code**: [[0123456789]]

> The includes() method takes one argument which is the string to be searched. The method returns a boolean value indicating whether the search string was found or not. If the search string is found in the original string, the method returns true. Otherwise, it returns false.

**Command** ([[String of Digits]]):

```bash
0123456789
```

3. CONVERT command

**Code**: [[๐๑๒๓๔๕๖๗๘๙]]

> The CONVERT command can be used to convert numeric data from one format to another. The argument for this command is the numeric data that needs to be converted. In this case, the numeric data is provided in Thai numerals. The CONVERT command can be used to convert these Thai numerals to standard Arabic numerals. The output of this command will be the numeric data in standard Arabic numerals.

## Commands Used

- [[String of Digits]]

## Tags

- [[Bypassing filters]]
- [[Bypass using unicode]]
- [[Server-Side Request Forgery]]
