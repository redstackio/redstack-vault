---
id: 832c3ded-d107-49c3-ae3a-8c101c9b6aab
name: Filter Bypass using Katakana Library
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.898148+00:00'
updated_at: '2023-04-10T20:21:53.742255+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Data Encoding|T1132 - Data Encoding]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Bypass using Katana]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Filter Bypass using Katakana Library

## Summary

The Katakana library is a tool that can be used to bypass input filters and perform cross-site scripting attacks. The library provides a set of functions that can be used to encode and decode data in a variety of formats, including Unicode, HTML, and JavaScript. The library can be used to bypass in

## Description

# Description

The Katakana library is a tool that can be used to bypass input filters and perform cross-site scripting attacks. The library provides a set of functions that can be used to encode and decode data in a variety of formats, including Unicode, HTML, and JavaScript. The library can be used to bypass input filters that are designed to block certain characters or character sequences that are commonly used in attacks. By encoding the input data using the Katakana library, an attacker can bypass these filters and inject malicious code into the application.

From a technical perspective, the Katakana library works by converting input data into a different format that is not blocked by the input filter. For example, if an input filter is designed to block the '<' character, an attacker can use the Katakana library to encode the '<' character in a way that the filter will not recognize. The encoded data is then decoded by the application and executed as JavaScript, allowing the attacker to perform a cross-site scripting attack.

The business value of using the Katakana library is that it allows an attacker to bypass input filters that are designed to prevent attacks. This can be used to steal sensitive information, such as user credentials or financial data, or to perform other malicious actions on the application.

## Requirements

1. Access to the application's input fields

1. Knowledge of the input filters being used by the application

1. Ability to encode and decode data using the Katakana library

## Defense

1. Implement input validation and filtering to prevent malicious data from being injected into the application

1. Use a Content Security Policy (CSP) to restrict the types of content that can be loaded by the application

1. Regularly update and patch the application to address any known vulnerabilities

## Objectives

1. Bypass input filters to inject malicious code into the application

1. Perform cross-site scripting attacks to steal sensitive data or perform other malicious actions

# Instructions

1. To use the Katakana library in your JavaScript code, follow these steps:

**Code**: [[javascript:([,ウ,,,,ア]=[]+{},[ネ,ホ,ヌ,セ,,ミ,ハ,ヘ,,,ナ]=[]]

> 1. Download the Katakana library from https://github.com/aemkei/katakana.js 
2. Include the library in your HTML file using the script tag.
3. In your JavaScript code, call the Katakana function using the following syntax:

Katakana('your_text_here')

This will convert your text into Katakana characters. The converted text will be returned as a string.

Arguments: 
- your_text_here: This argument should be a string containing the text you want to convert into Katakana characters. 

Example usage: 

var katakanaText = Katakana('Hello, world!');
console.log(katakanaText); // Outputs 'ヘッロー、ヲールド！'

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Data Encoding|T1132 - Data Encoding]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Tags

- [[Bypass using Katana]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]
