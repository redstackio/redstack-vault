---
id: tool-bind
url: 'https://www.isc.org/bind/'
tags:
  - dns
  - server
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.596Z'
validated: true
submitted: true
---
# BIND

**Status**: Unverified

## Overview

BIND (Berkeley Internet Name Domain) is open-source DNS server software used to host domains and log queries for exfiltration verification in attacks.

## Description

Configures zones for controlled domains to capture DNS requests from exploited servers, confirming gadget execution.

## Features

- Feature 1: Authoritative DNS serving
- Feature 2: Query logging
- Feature 3: Zone management

## Installation

### Requirements

- Linux server

### Install Commands

```bash
# Ubuntu
apt install bind9
systemctl start named
```

## Basic Usage

```bash
named -v
```

### Common Options

| Option | Description |
|--------|-------------|
| -g | Run in foreground |
| -c config | Specify config |

## Examples

### Example 1: Basic Usage

```bash
named -c /etc/bind/named.conf
```

### Example 2: Advanced Usage

Configure /etc/bind/named.conf.local for zone logging.

## MITRE ATT&CK Mapping

### Techniques

- [[Exfiltration Over Command and Control Channel]]

### Tactics

- [[Collection]]

## Detection

- Detection method 1: DNS server logs
- Detection method 2: Anomalous query patterns

## Related Procedures

- [[procedures/Verify-Execution-with-DNS-Logs]]

## Related Tools

- [[tools/dnsmasq]]

## References

- Official: https://www.isc.org/bind/
