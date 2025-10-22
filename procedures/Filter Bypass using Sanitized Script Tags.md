---
id: aee23567-9d9f-4b9b-b9c4-1e7e761ef2a5
name: Filter Bypass using Sanitized Script Tags
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.725566+00:00'
updated_at: '2023-04-10T20:21:45.694422+00:00'
tags:
- '[[Bypass using javascript inside a string]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Filter Bypass using Sanitized Script Tags

## Summary

Cross Site Scripting (XSS) is a type of injection attack that allows attackers to inject malicious code into web pages viewed by other users. Filter Bypass using Sanitized Script Tags is a technique used to bypass filters that are designed to block specific script tags. By using sanitized script ta

## Description

# Description

Cross Site Scripting (XSS) is a type of injection attack that allows attackers to inject malicious code into web pages viewed by other users. Filter Bypass using Sanitized Script Tags is a technique used to bypass filters that are designed to block specific script tags. By using sanitized script tags, attackers can inject malicious code into web pages without triggering the filters. This technique involves inserting a script tag into a string and then using a function to sanitize the tag so that it is not blocked by the filter.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of the specific filter being used

## Defense

1. Implement input validation techniques to prevent the injection of malicious code

1. Use a Content Security Policy (CSP) to restrict the types of content that can be loaded on a web page

1. Regularly monitor web applications for suspicious activity and unexpected changes

## Objectives

1. Inject malicious code into a web page

1. Bypass filters that block specific script tags

# Instructions

1. To sanitize script tags, use a regular expression to remove any opening and closing script tags and their contents. This will prevent any potential malicious code from being executed.

**Code**: [[<script>
foo="text </script><script>alert(1)</scri]]

> The 'data' field contains a string with potentially harmful script tags. The 'name' field should be filled in with a descriptive name for this command. The 'lang' field indicates the programming language being used. The 'text' field is not used in this command. The 'instruction' field provides guidance on how to sanitize script tags. The 'explain' field should explain why it's important to sanitize script tags and how to do it.

## Tags

- [[Bypass using javascript inside a string]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]
