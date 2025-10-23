---
id: 0a6aed58-cd85-427f-b9e3-27ebdb0d44bc
name: Base64 encoded HTML data WAF Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.503188+00:00'
updated_at: '2023-04-10T20:21:42.962880+00:00'
tags:
- '[[Common WAF Bypass]]'
- '[[Cross Site Scripting]]'
- '[[Incapsula WAF Bypass by [@c0d3G33k](https://twitter.com/c0d3G33k) - 11th September
  2018]]'
---

# Base64 encoded HTML data WAF Bypass

## Summary

The Base64 encoded HTML data WAF Bypass is a technique used to bypass Web Application Firewalls (WAFs) that are configured to block malicious HTML content. This technique involves encoding the malicious HTML data using Base64 encoding, which is then sent to the target web application. When the WAF 

## Description

# Description

The Base64 encoded HTML data WAF Bypass is a technique used to bypass Web Application Firewalls (WAFs) that are configured to block malicious HTML content. This technique involves encoding the malicious HTML data using Base64 encoding, which is then sent to the target web application. When the WAF inspects the data, it is unable to detect the malicious content as it is encoded. Once the data reaches the web application, it is decoded and the malicious content is executed, allowing the attacker to perform a Cross Site Scripting (XSS) attack.

This technique is effective against WAFs that only inspect plain text data and do not decode encoded content. The attacker can use this technique to bypass security controls and gain access to sensitive data, such as user credentials or other sensitive information.

Business value: This technique can be used by attackers to gain unauthorized access to sensitive data and compromise the security of web applications. By bypassing WAFs, attackers can gain access to valuable information, which can be used for financial gain or other malicious purposes.

 

## Requirements

1. Access to a web application with a WAF configured to block malicious HTML content

1. Knowledge of Base64 encoding

 

## Defense

1. Implement regular expression rules in the WAF to detect and block Base64 encoded content

1. Use a Content Security Policy (CSP) to restrict the execution of scripts and other types of content

1. Regularly update the WAF to ensure it is capable of detecting new attack techniques and patterns

 

## Objectives

1. Bypass WAFs to execute malicious HTML content

1. Perform a Cross Site Scripting (XSS) attack

 

# Instructions

1. Use the 'data' attribute of the 'object' tag to display base64 encoded HTML data.

 



**Code**: [[<object data='data:text/html;;;;;base64,PHNjcmlwdD]]



> The 'data' attribute of the 'object' tag can be used to display any type of data that can be represented as a URL. In this case, we are using a base64 encoded HTML string. The 'object' tag is a versatile HTML tag that can be used to display various types of content, including images, videos, and audio files, as well as HTML content.

## Tags

- [[Common WAF Bypass]]
- [[Cross Site Scripting]]
- [[Incapsula WAF Bypass by [@c0d3G33k](https://twitter.com/c0d3G33k) - 11th September 2018]]


