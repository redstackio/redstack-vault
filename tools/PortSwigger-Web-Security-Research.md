---
id: t1b2c3d4-e5f6-7890-abcd-ef1234567896
url: 'http://blog.portswigger.net/2016/01/xss-without-html-client-side-template.html'
tags:
  - research
  - xss
  - template-injection
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:47:12.706Z'
validated: true
submitted: true
---
# PortSwigger-Web-Security-Research

**Status**: Unverified

## Overview

PortSwigger's Web Security blog provides research articles on vulnerabilities like client-side template injection leading to XSS, serving as a reference for crafting AngularJS bypass payloads in web applications.

## Description

This resource details techniques for exploiting template engines without HTML context, focusing on AngularJS sandbox escapes. It's used in offensive security to inspire payloads for stored XSS in dynamic fields, such as address inputs in e-commerce plugins.

## Features

- In-depth analysis of AngularJS expression evaluation
- Example payloads for JS execution via templates
- Guidance on detection and exploitation chains

## Installation

### Requirements

- Web browser for reading
- No installation needed; online access

### Install Commands

N/A (web-based resource)

## Basic Usage

Visit the URL and review the article for payload ideas.

### Common Options

N/A

## Examples

### Example 1: Basic Usage

Read the blog post to understand template injection vectors.

### Example 2: Advanced Usage

Adapt provided payloads for specific frameworks like AngularJS in WordPress.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- N/A (informational resource)
- Monitor for payload patterns from known researches

## Related Procedures


## Related Tools


## References

- Official PortSwigger Blog
- Related XSS research articles
