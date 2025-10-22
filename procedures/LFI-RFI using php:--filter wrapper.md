---
id: fffa0325-b216-4571-9e4a-7090ce21733e
name: LFI/RFI using php://filter wrapper
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.301791+00:00'
updated_at: '2023-04-10T20:22:14.199442+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[File Inclusion]]'
- '[[LFI / RFI using wrappers]]'
- '[[Wrapper php://filter]]'
---

# LFI/RFI using php://filter wrapper

## Summary

LFI/RFI using the php://filter wrapper is a technique used to bypass input validation filters and achieve remote code execution. This technique works by using the php://filter wrapper to apply filters to the input data. The wrapper can be used to apply filters like base64-encode, string.rot13 and z

## Description

# Description

LFI/RFI using the php://filter wrapper is a technique used to bypass input validation filters and achieve remote code execution. This technique works by using the php://filter wrapper to apply filters to the input data. The wrapper can be used to apply filters like base64-encode, string.rot13 and zlib.deflate, which can help to bypass input validation filters. Attackers can use this technique to read sensitive files, execute arbitrary code, or launch further attacks against the target system. This technique is commonly used in web application attacks.

## Requirements

1. Access to a vulnerable web application.

## Defense

1. Implement input validation filters to ensure that user-supplied input is safe.

1. Use a web application firewall (WAF) to detect and block attacks that use LFI/RFI.

1. Keep web servers and applications up to date with the latest security patches.

## Objectives

1. To bypass input validation filters and achieve remote code execution.

1. To read sensitive files, execute arbitrary code, or launch further attacks against the target system.

# Instructions

1. 

**Code**: [[php://filter]]

> The php://filter wrapper is used to apply filters to the input data. Filters can be used to modify or transform the data, which can help to bypass input validation filters.

2. 

**Code**: [[http://example.com/index.php?page=php://filter/con]]

> The "convert.base64-encode" filter is used to encode the input data in base64 format. This can help to bypass input validation filters that are looking for specific strings or characters.

3. 

**Code**: [[http://example.com/index.php?page=php://filter/zli]]

> Wrappers can be chained together to apply multiple filters to the input data. The zlib.deflate filter is used to compress the input data, which can help to bypass input validation filters that are looking for specific file signatures. This technique is particularly useful for large files.

4. 

**Code**: [[|]]

> The php://filter wrapper can be chained with other wrappers to apply multiple filters to the input data. Wrappers can be chained together using either "/" or "|".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[File Inclusion]]
- [[LFI / RFI using wrappers]]
- [[Wrapper php://filter]]
