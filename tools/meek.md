---
id: 9c786727-c42f-4a36-b620-c441135ab47d
name: meek
type: tool
verified: true
created_at: '2019-08-28T21:17:29.218448+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - evasion
  - tor
  - pluggable-transport
  - censorship-bypass
url: 'https://tb-manual.torproject.org/pluggable-transports/#meek'
commands:
  - '[[commands/meek-client-azureedge-connect]]'
  - '[[commands/meek-client-amazon-connect]]'
validated: true
---

# meek

**Status**: Unverified

## Overview

Meek is a blocking-resistant pluggable transport (PT) for the Tor network. It disguises Tor traffic as innocent-looking HTTPS requests to popular cloud services like Azure or Amazon, making it difficult for censors to block without disrupting legitimate web access. In security testing, meek is useful for maintaining command-and-control (C2) channels or exfiltrating data in censored or monitored environments.

## Description

Meek operates by multiplexing Tor's data stream over multiple HTTPS connections to a bridge server, which relays it to the Tor network. It uses domain fronting, where traffic appears to go to a front domain (e.g., a CDN) while actually routing to the hidden bridge URL. This tool is particularly effective against deep packet inspection (DPI) and helps red teams simulate operations in hostile networks. Supported fronts include Azure Edge and AWS S3.

## Features

- **Domain Fronting**: Masks Tor traffic behind major cloud providers to evade blocking.
- **Multiplexing**: Splits data across multiple HTTPS streams for reliability.
- **Circuit Padding**: Adds noise to traffic patterns to avoid statistical detection.
- **Integration with Tor**: Seamless as a PT, configurable via torrc.

## Installation

### Requirements

- Go 1.11 or later (for building from source)
- Tor 0.2.7 or higher
- Git for cloning the repository

### Install Commands

```bash
# Clone and build on Ubuntu/Kali
sudo apt update
sudo apt install golang git build-essential
mkdir -p ~/src && cd ~/src
git clone https://git.torproject.org/pluggable-transports/meek.git
cd meek/meek-client
~/go/bin/go build
sudo cp meek-client /usr/local/bin/

# For Tor integration on Kali (Tor is pre-installed)
sudo apt install tor
```

On macOS: Use Homebrew to install Go and Tor, then build similarly.
On Windows: Use pre-built binaries from the Tor Project or build with MinGW.

## Basic Usage

```bash
meek-client --help
```

Configure Tor to use meek by editing /etc/tor/torrc:

```
UseBridges 1
ClientTransportPlugin meek exec /usr/local/bin/meek-client
Bridge meek 0.0.2.0:2 url=https://meek.azureedge.net/ front=ajax.aspnetcdn.com
```

Then restart Tor: `sudo systemctl restart tor`

### Common Options

| Option | Description |
|--------|-------------|
| --state-dir | Directory for persistent state files |
| --torrc | Path to Tor configuration |
| --url | Bridge server URL |
| --front | Front domain for domain fronting |
| --log | Enable logging (via Tor) |

## Examples

### Example 1: Basic Usage

Use the Azure Edge front:

```bash
meek-client --state-dir /var/lib/tor/pt_state --torrc /etc/tor/torrc --url https://meek.azureedge.net/ --front ajax.aspnetcdn.com
```

### Example 2: Advanced Usage

For Amazon front, update torrc with the Amazon bridge line and run:

```bash
meek-client --state-dir /var/lib/tor/pt_state --torrc /etc/tor/torrc --url https://meek.amazonws.com/ --front s3.amazonaws.com
```

Monitor connection via `tail -f /var/log/tor/notices.log`.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Encrypted Channel]] Encrypted Channel: Uses HTTPS to obfuscate C2 or data exfiltration.
- [[Connection Proxy]] Proxy: Leverages Tor bridges for pivoting in restricted networks.

### Tactics

- [[Command and Control]] Command and Control
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual HTTPS traffic patterns to CDNs like azureedge.net or s3.amazonaws.com from Tor processes.
- Presence of meek-client binary or PT state directories (e.g., /var/lib/tor/pt_state).
- Tor logs showing meek bridge connections; monitor for pluggable transport executions.
- Network anomalies: High volume of small HTTPS POST/GET to front domains without corresponding legitimate app traffic.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/tor]]
- [[tools/obfs4]]

## References

- Official Tor Project Documentation: https://tb-manual.torproject.org/pluggable-transports/#meek
- Git Repository: https://git.torproject.org/pluggable-transports/meek.git
- Blog on Domain Fronting: https://blog.torproject.org/domain-fronting-actually-works/

## Related Commands

- [[commands/meek-client-azureedge-connect]]
- [[commands/meek-client-amazon-connect]]
