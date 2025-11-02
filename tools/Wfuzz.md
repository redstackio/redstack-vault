---
id: 89a9dbe5-dc2a-46e2-91c1-68a3ec8a5e56
name: Wfuzz
type: tool
verified: false
created_at: '2019-08-28T21:17:17.782157+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
- '[[Wfuzz Brute Force DNS with the Host Parameter]]'
- '[[Wfuzz Directory Brute Force with Burp Proxy]]'
- '[[Wfuzz Directory Brute Force]]'
- '[[Wfuzz directory brute force with extensions]]'
- '[[Wfuzz recursive directory brute force]]'
- '[[wfuzz Brute Force a HTTP POST Form]]'
platforms:
- Web
tags:
- '[[Enumeration]]'
- '[[Web Applications]]'
---

# Wfuzz

## Overview

Wfuzz is a web application assessment tool, which sends crafted HTTP requests to enumerate various application components such as parameters, authentication, forms, directories, files, headers, and more. By supplying Wfuzz with a wordlist and specifying a parameter for fuzz with the "FUZZ" keyword,

## Description

# Description

Wfuzz is a web application assessment tool, which sends crafted HTTP requests to enumerate various application components such as parameters, authentication, forms, directories, files, headers, and more. By supplying Wfuzz with a wordlist and specifying a parameter for fuzz with the "FUZZ" keyword, Wfuzz will brute force the parameter, and display the results. 



Unlike other fuzzers, Wfuzz does not automatically hide status codes, leaving it up to the user to specify them. Users can choose which codes to suppress  such as 404, 403, 301, etc. Other handy filters can be applied, based on the size of the page returned, number of lines, or number of words.



# Example



{{EMBEDDED_COMMAND_d0ad3758-1ef3-4e3a-9f22-863e103d38a8}}



# Installation

## Install with pip





## Install from Source









## Platforms

- Web

## Services

- http
- http
- https
- https

## Commands (1)

- [[Wfuzz Directory Brute Force]]

## Tags

- [[Enumeration]]
- [[Web Applications]]


