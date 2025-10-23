---
id: f58059eb-0fec-4868-97ed-c7c5e1923a39
name: XSS in CSS with Malicious Background Image Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.157835+00:00'
updated_at: '2023-04-10T20:21:52.322995+00:00'
tags:
- '[[Cross Site Scripting]]'
- '[[XSS in CSS]]'
- '[[XSS in files]]'
---

# XSS in CSS with Malicious Background Image Injection

## Summary

XSS in CSS with Malicious Background Image Injection is a technique used by attackers to inject malicious code into a website's CSS files. This technique is executed by injecting malicious code into the background-image property of a CSS file. The malicious code can then be used to steal sensitive 

## Description

# Description

XSS in CSS with Malicious Background Image Injection is a technique used by attackers to inject malicious code into a website's CSS files. This technique is executed by injecting malicious code into the background-image property of a CSS file. The malicious code can then be used to steal sensitive information, such as user credentials or session tokens, or to execute arbitrary code on the victim's machine. This technique can be used to bypass security controls and evade detection.

 

## Requirements

1. Access to the website's CSS files

1. Knowledge of the website's CSS file structure

1. Malicious Background Image Injection tool

 

## Defense

1. Implement input validation to prevent malicious code injection

1. Implement Content Security Policy to restrict the sources of content that can be loaded on a web page

1. Regularly scan and monitor the website's CSS files for malicious code

 

## Objectives

1. Inject malicious code into a website's CSS files

1. Steal sensitive information from the victim

1. Execute arbitrary code on the victim's machine

 

# Instructions

1. This command injects a malicious background image into a webpage.

 



**Code**: [[<!DOCTYPE html>
<html>
<head>
<style>
div  {
    b]]



> It works by using a data URL to encode an SVG image that contains JavaScript code. When the image is loaded as a background image, the JavaScript code is executed, which in this case displays an alert message containing the domain of the current page. This technique can be used to perform various types of attacks, such as stealing cookies, redirecting users to malicious websites, or executing arbitrary code on the victim's machine.

## Tags

- [[Cross Site Scripting]]
- [[XSS in CSS]]
- [[XSS in files]]


