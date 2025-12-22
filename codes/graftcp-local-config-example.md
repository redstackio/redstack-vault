---
id: 18d7a6c9-f414-4994-a464-41a8009171b1
name: graftcp-local-config-example
type: code
language: ini
verified: true
created_at: '2023-04-06T03:56:22.550279+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - config
  - proxy
  - socks5
validated: true
---

# graftcp-local-config-example

## Code

```ini
# https://github.com/hmgle/graftcp/blob/master/local/example-graftcp-local.conf
## Listen address (default ":2233")
listen = :2233
loglevel = 1

## SOCKS5 address (default "127.0.0.1:1080")
socks5 = 127.0.0.1:1080
# socks5_username = SOCKS5USERNAME
# socks5_password = SOCKS5PASSWORD

## Set the mode for select a proxy (default "auto")
select_proxy_mode = auto
```

## Description

This INI-style configuration file for graftcp-local defines the listening port, logging, SOCKS5 proxy details, and proxy selection mode. Save as a .conf file and pass via -config flag if not using CLI args.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| listen | Listen address:port | :2233 |
| loglevel | Logging verbosity (1-6) | 1 |
| socks5 | SOCKS5 proxy host:port | 127.0.0.1:1080 |
| socks5_username | Optional SOCKS5 auth username | myuser |
| socks5_password | Optional SOCKS5 auth password | mypass |
| select_proxy_mode | Proxy selection (auto, random, round-robin) | auto |

## Usage

Create file e.g., graftcp.conf with this content, then run `graftcp-local -config graftcp.conf`. Useful for persistent setups or multiple proxies; overrides CLI defaults.

## Detection

- File system monitoring for .conf files with proxy configs in temp dirs.
- Process args scanning for -config flags pointing to suspicious files.
- Config content analysis for internal IPs in SOCKS5 fields.

## Related

- [[procedures/Proxify-Go-Application-with-Graftcp]]
- [[tools/Graftcp]]
