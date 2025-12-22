---
type: tool
verified: true
created_at: '2019-08-28T21:17:43.046817+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - web-server
  - payload-delivery
  - nginx
  - lua
  - red-team
url: 'https://openresty.org/'
validated: true
---

# Serving-Random-Payloads

**Status**: Unverified

## Overview

Serving Random Payloads is a configuration setup using OpenResty (an enhanced NGINX with Lua scripting) to randomly select and serve files from a designated payload directory. This tool is commonly used in red teaming and penetration testing to deliver varying payloads (e.g., executables, scripts, or documents) via HTTP, helping to evade static signature-based detection by varying the delivered content on each request.

## Description

The setup involves installing OpenResty, creating a payloads directory, and configuring a Lua script within NGINX to iterate over files in the directory, select one at random using Lua's math.random, and redirect/serve it. This allows attackers to host a single endpoint (e.g., /random-payload) that dynamically serves different files, simulating polymorphic delivery. It's particularly useful for command-and-control (C2) payload staging or phishing campaign testing. The configuration also includes a static directory listing for direct access to payloads if needed.

## Features

- Random file selection using Lua scripting for true server-side randomness.
- Support for various file types (executables, archives, scripts) in the payload directory.
- Autoindexing for browsing payloads directly.
- Lightweight and performant, leveraging NGINX's efficiency.
- Customizable directory and server name in the config.

## Installation

### Requirements

- Ubuntu 18.04+ or Debian-based Linux distribution.
- Root or sudo access.
- Internet connection for package downloads.
- Optional: lua-resty-filesystem for advanced directory handling (install via opm: `opm get lobbes/lua-resty-filesystem`).

### Install Commands

Use [[commands/install-openresty-ubuntu]] to install OpenResty.

After installation, verify with `openresty -v`.

## Basic Usage

```bash
openresty -t
```

This tests the configuration. For full setup:
1. Run [[commands/create-payloads-directory]] to prepare the storage.
2. Run [[commands/configure-openresty-random-payloads]] to create the site config.
3. Run [[commands/enable-openresty-site-random-payloads]] to activate it.
4. Run [[commands/test-and-restart-openresty]] to apply changes.
5. Place payload files in /var/www/payloads/ (e.g., `sudo cp payload1.exe /var/www/payloads/`).
6. Access http://your-server/random-payload to receive a random file.

### Common Options

| Option | Description |
|--------|-------------|
| `-t` | Test configuration syntax |
| `-s reload` | Gracefully reload after config changes |
| `-s stop` | Stop the server |

## Examples

### Example 1: Basic Usage

After setup, curl the endpoint:

```bash
curl -O http://localhost/random-payload
```

This downloads a random payload file.

### Example 2: Advanced Usage

List available payloads:

```bash
curl http://localhost/payloads/
```

Modify the Lua block in the config to filter file types (e.g., only .exe) by adding `if string.match(file, "%.exe$") then` before inserting to files table.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[Encrypted Channel]] Encrypted Channel (if payloads are encrypted)

### Tactics

- [[Execution]] Execution
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of OpenResty or NGINX configs with Lua blocks referencing random file selection.
- Web server logs showing repeated accesses to /random-payload or similar endpoints.
- Unusual HTTP responses serving varying executables from the same path.
- File system anomalies: www-data owned directories with suspicious binaries in /var/www/.
- Network traffic: HTTP GETs to non-standard paths delivering malware.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[NGINX]] (core web server without Lua)
- [[OpenResty]] (enhanced NGINX used here)

## References

- Official OpenResty Documentation: https://openresty.org/en/
- NGINX Lua Module: https://github.com/openresty/lua-nginx-module
- Example Lua Random Selection: Adapted from community scripts for dynamic content serving.
