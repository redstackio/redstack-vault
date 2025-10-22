---
id: bb8a3378-891c-4d95-892c-dc91373cd132
name: XSS in SVG Triangle with JavaScript Alert
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.034627+00:00'
updated_at: '2023-04-10T20:21:35.666381+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Scripting|T1064 - Scripting]]'
- '[[User Execution|T1204 - User Execution]]'
tags:
- '[[Cross Site Scripting]]'
- '[[XSS in files]]'
- '[[XSS in SVG]]'
---

# XSS in SVG Triangle with JavaScript Alert

## Summary

XSS in SVG is a technique used to inject malicious code into an SVG file. The attacker can use various techniques to inject the code, such as embedding the code in a script tag or using a data URI. When the SVG file is opened in a web browser, the malicious code is executed, allowing the attacker t

## Description

# Description

XSS in SVG is a technique used to inject malicious code into an SVG file. The attacker can use various techniques to inject the code, such as embedding the code in a script tag or using a data URI. When the SVG file is opened in a web browser, the malicious code is executed, allowing the attacker to steal sensitive information or perform other malicious actions. In this specific example, the attacker is using an SVG triangle with a JavaScript alert to demonstrate the XSS vulnerability.

## Requirements

1. Access to a web server to host the SVG file

1. A web browser to open the SVG file

1. Knowledge of XSS techniques

## Defense

1. Input validation can help prevent XSS attacks by filtering out malicious code

1. Content Security Policy (CSP) can be used to restrict the types of content that can be loaded by a web page

1. Regularly updating web browsers and plugins can help prevent XSS attacks

## Objectives

1. Inject malicious code into an SVG file

1. Execute the code when the SVG file is opened in a web browser

1. Demonstrate the XSS vulnerability

# Instructions

1. Create an SVG triangle with a green fill and a dark green stroke. Add a JavaScript script tag to the SVG that creates an alert with the document's domain when the SVG is loaded.

**Code**: [[<?xml version="1.0" standalone="no"?>
<!DOCTYPE sv]]

> The SVG triangle is created using the polygon element with the id 'triangle' and the points '0,0 0,50 50,0'. The fill color is set to green (#009900) and the stroke color is set to dark green (#004400). The JavaScript script tag creates an alert with the document's domain when the SVG is loaded.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Scripting|T1064 - Scripting]]
- [[User Execution|T1204 - User Execution]]

## Tags

- [[Cross Site Scripting]]
- [[XSS in files]]
- [[XSS in SVG]]
