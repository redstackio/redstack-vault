---
id: df05dc11-83a2-4119-b065-4b0c1592f89d
name: Cloudflare XSS Bypass using SVG and Video Injection Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.307711+00:00'
updated_at: '2023-04-10T20:21:48.520105+00:00'
tags:
- '[[25st January 2021]]'
- '[[Cloudflare XSS Bypasses by [@Bohdan Korzhynskyi](https://twitter.com/bohdansec)]]'
- '[[Common WAF Bypass]]'
- '[[Cross Site Scripting]]'
---

# Cloudflare XSS Bypass using SVG and Video Injection Attack

## Summary

This attack technique involves injecting malicious SVG or video files into a vulnerable web application to bypass Cloudflare's XSS protection. The attacker can then execute arbitrary code on the victim's browser, steal sensitive information, or perform other malicious actions. The attack works by e

## Description

# Description

This attack technique involves injecting malicious SVG or video files into a vulnerable web application to bypass Cloudflare's XSS protection. The attacker can then execute arbitrary code on the victim's browser, steal sensitive information, or perform other malicious actions. The attack works by exploiting a vulnerability in the way Cloudflare's WAF filters out malicious code. By injecting the payload into an SVG or video file, the attacker can bypass the filter and execute the payload on the victim's browser.

From a technical standpoint, this attack technique involves crafting a malicious SVG or video file that contains the payload. The attacker then uploads the file to the vulnerable web application, which serves it to the victim's browser. When the victim's browser renders the file, the payload is executed, allowing the attacker to take control of the victim's session.

The business value of this attack lies in its ability to compromise the confidentiality, integrity, and availability of the target system. By stealing sensitive information or taking control of the victim's session, the attacker can cause significant damage to the target organization.

 

## Requirements

1. Access to a vulnerable web application that uses Cloudflare's WAF

1. Ability to craft malicious SVG or video files

 

## Defense

1. Implement strict input validation and sanitization to prevent injection attacks

1. Use Content Security Policy (CSP) to restrict the sources of executable code

1. Regularly update and patch the web application and its dependencies to address known vulnerabilities

 

## Objectives

1. To bypass Cloudflare's XSS protection and execute arbitrary code on the victim's browser

1. To steal sensitive information or perform other malicious actions on the victim's browser

 

# Instructions

1. This command demonstrates an attack where an SVG and a video element are injected with malicious code. The code executes when the SVG is loaded and when the mouse hovers over the video element.

 



**Code**: [[<svg/onrandom=random onload=confirm(1)>
<video onn]]



> The code injected in the SVG and video elements can execute any arbitrary code on the user's machine, potentially leading to data theft or other malicious activities. It is important to sanitize user input and validate any data that is being rendered on a page to prevent such attacks.

## Tags

- [[25st January 2021]]
- [[Cloudflare XSS Bypasses by [@Bohdan Korzhynskyi](https://twitter.com/bohdansec)]]
- [[Common WAF Bypass]]
- [[Cross Site Scripting]]


