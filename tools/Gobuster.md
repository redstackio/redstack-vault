---
id: 3eb05ebf-280e-40e1-8d9d-e8a6e09e4ba4
name: Gobuster
type: tool
verified: false
created_at: '2019-08-28T21:17:36.051053+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
- '[[Gobuster Command to Find Existent Directories]]'
- '[[Gobuster Directory Brute Force with Burp proxy]]'
- '[[Gobuster Directory Brute Force with Extensions]]'
- '[[Gobuster Directory Brute Force]]'
platforms:
- Web
tags:
- '[[Brute Force]]'
- '[[Web Applications]]'
---

# Gobuster

## Overview

Gobuster is a web application directory, vhost, and DNS server brute forcing tool, which uses wordlists to enumerate services. Gobuster contains three modules: dir: this module performs traditional web application brute force attacks to enumerate files and folders. vhost: this module uses the "Host

## Description

# Description

Gobuster is a web application directory, vhost, and DNS server brute forcing tool, which uses wordlists to enumerate services. Gobuster contains three modules:



- dir: this module performs traditional web application brute force attacks to enumerate files and folders.

- vhost: this module uses the "Host" value in the HTTP header to enumerate websites in cases where a web application uses virtual hosts to serve different sites.

- dns: this module enumerates DNS subdomains by directly querying DNS servers, unlike the vhosts module which uses the HTTP headers. All requests are sent to the host system's configured DNS server, so system settings should be updated if the requests must be sent to a specific server (common when enumerating non-public domain servers).

# Example



{{EMBEDDED_COMMAND_21cc125b-0be7-4d96-9228-eb144900a21f}}



# Installation

## Install on Debian/Ubuntu









## Platforms

- Web

## Services

- http
- http
- https
- https

## Commands (1)

- [[Gobuster Directory Brute Force]]

## Tags

- [[Brute Force]]
- [[Web Applications]]


