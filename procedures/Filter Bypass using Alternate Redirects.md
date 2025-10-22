---
id: 915c8f7b-a970-49de-a321-20d3fcc61494
name: Filter Bypass using Alternate Redirects
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.747739+00:00'
updated_at: '2023-04-10T20:21:29.889683+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
tags:
- '[[Bypass using an alternate way to redirect]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Filter Bypass using Alternate Redirects

## Summary

This attack uses a filter bypass technique to execute malicious code on a victim's browser. The attacker injects a script into the victim's browser, which can then be used to steal sensitive information or perform other malicious actions. In this case, the attacker is using an alternate way to redi

## Description

# Description

This attack uses a filter bypass technique to execute malicious code on a victim's browser. The attacker injects a script into the victim's browser, which can then be used to steal sensitive information or perform other malicious actions. In this case, the attacker is using an alternate way to redirect the victim to a malicious website. This technique can be used to bypass filters that are designed to prevent cross-site scripting attacks.

To execute this attack, the attacker must first find a vulnerability in the target website that allows them to inject code. Once the code is injected, it can be used to redirect the victim to a malicious website. This attack can be difficult to detect, as the victim may not realize they have been redirected to a malicious site.

## Requirements

1. Access to a vulnerable website

1. Ability to inject code into the website

## Defense

1. Ensure that all input is properly sanitized to prevent injection attacks

1. Use Content Security Policy (CSP) to prevent the execution of malicious scripts

1. Regularly scan websites for vulnerabilities and patch any issues that are found

## Objectives

1. Redirect the victim to a malicious website

1. Bypass filters designed to prevent cross-site scripting attacks

# Instructions

1. Use any of the following commands to redirect to Google:

**Code**: [[location="http://google.com"
document.location = "]]

> The 'location' object in JavaScript represents the current URL of the page. In this case, we are setting the value of the 'location' object to 'http://google.com' using different methods. 

The 'document.location' property is an alias for 'window.location'. The 'href' property of 'location' object specifies the URL of the page to be loaded. The 'assign()' method of the 'location' object loads a new document. We can also set the 'href' property using bracket notation, like 'window['location']['href']'.

All of these methods will redirect the user to the specified URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]

## Tags

- [[Bypass using an alternate way to redirect]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]
