---
id: 43da8d05-61be-4e35-8bce-84f550626c7b
name: CSP Bypass using JSONP from Google
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.192763+00:00'
updated_at: '2023-04-10T20:21:42.276521+00:00'
tags:
- '[[Bypass CSP using JSONP from Google (Trick by [@apfeifer27](https://twitter.com/apfeifer27))]]'
- '[[Cross Site Scripting]]'
- '[[CSP Bypass]]'
---

# CSP Bypass using JSONP from Google

## Summary

This technique is a method to bypass Content Security Policy (CSP) using JSONP from Google. This technique abuses the fact that Google APIs are whitelisted by default in most CSP configurations. The attacker can use a JSONP request to a Google API to execute arbitrary JavaScript code that would oth

## Description

# Description

This technique is a method to bypass Content Security Policy (CSP) using JSONP from Google. This technique abuses the fact that Google APIs are whitelisted by default in most CSP configurations. The attacker can use a JSONP request to a Google API to execute arbitrary JavaScript code that would otherwise be blocked by the CSP. This technique allows the attacker to bypass the CSP and perform Cross-Site Scripting (XSS) attacks.

From a technical perspective, JSONP (JSON with Padding) is a technique for loading data from a different domain or subdomain by dynamically adding a script tag to the HTML page. The script tag includes a callback parameter that specifies the name of a function to be executed with the JSON data. By using JSONP, the attacker can load malicious JavaScript code from a different domain and execute it in the context of the victim's web page.

The business value of this technique is that it allows an attacker to bypass CSP protections and perform XSS attacks, which can lead to data theft, unauthorized access, and other malicious activities.

## Requirements

1. Access to a website with a vulnerable CSP configuration

1. Ability to send a JSONP request to a Google API

## Defense

1. Implement a strict CSP configuration that blocks all external scripts and only allows trusted sources

1. Use a web application firewall (WAF) that can detect and block JSONP requests to Google APIs

1. Regularly review and update the CSP configuration to ensure that it is effective against new attack techniques

## Objectives

1. Bypass Content Security Policy (CSP) protections

1. Execute arbitrary JavaScript code on a victim's web page

1. Perform Cross-Site Scripting (XSS) attacks

# Instructions

1. To execute this command, simply copy and paste the provided data into the browser console and press enter.

**Code**: [[<script/src=//google.com/complete/search?client=ch]]

> This command is used to check the Content Security Policy (CSP) of a website using Google's CSP Evaluator tool. The provided data is a script that can be used to test if the website's CSP is properly configured to prevent cross-site scripting (XSS) attacks. The command also provides a link to a blog post that explains how to use the tool to bypass CSP in case the website has not properly implemented it. The language of the script is JavaScript and it should be executed in the browser console. Please note that this command should only be used for testing purposes on websites that you have permission to test.

## Tags

- [[Bypass CSP using JSONP from Google (Trick by [@apfeifer27](https://twitter.com/apfeifer27))]]
- [[Cross Site Scripting]]
- [[CSP Bypass]]
