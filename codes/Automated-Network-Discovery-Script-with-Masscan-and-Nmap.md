---
id: 75e7033d-1529-444a-83ab-2c15eed1796f
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:22.199114Z'
updated_at: '2023-04-10T20:25:05.874180Z'
platforms:
  - Linux
tags:
  - script
  - automation
  - scanning
validated: true
---

# Automated-Network-Discovery-Script-with-Masscan-and-Nmap

## Code

```bash
masscan -iL ips-online.txt --rate 10000 -p1-65535 --only-open -oL masscan.out
masscan -e tun0 -p1-65535,U:1-65535 10.10.10.97 --rate 1000

# find machines on the network
sudo masscan --rate 500 --interface tap0 --router-ip $ROUTER_IP --top-ports 100 $NETWORK -oL masscan_machines.tmp
cat masscan_machines.tmp | grep open | cut -d " " -f4 | sort -u > masscan_machines.lst

# find open ports for one machine
sudo masscan --rate 1000 --interface tap0 --router-ip $ROUTER_IP -p1-65535,U:1-65535 $MACHINE_IP --banners -oL $MACHINE_IP/scans/masscan-ports.lst


# TCP grab banners and services information
TCP_PORTS=$(cat $MACHINE_IP/scans/masscan-ports.lst| grep open | grep tcp | cut -d " " -f3 | tr '\n' ',' | head -c -1)
[ "$TCP_PORTS" ] && sudo nmap -sT -sC -sV -v -Pn -n -T4 -p$TCP_PORTS --reason --version-intensity=5 -oA $MACHINE_IP/scans/nmap_tcp $MACHINE_IP

# UDP grab banners and services information
UDP_PORTS=$(cat $MACHINE_IP/scans/masscan-ports.lst| grep open | grep udp | cut -d " " -f3 | tr '\n' ',' | head -c -1)
[ "$UDP_PORTS" ] && sudo nmap -sU -sC -sV -v -Pn -n -T4 -p$UDP_PORTS --reason --version-intensity=5 -oA $MACHINE_IP/scans/nmap_udp $MACHINE_IP
```

## Description

This bash script automates network discovery using Masscan for fast host and port detection, followed by Nmap for detailed TCP/UDP service enumeration. It includes example invocations and the core logic for discovering machines, extracting IPs, scanning ports, and generating Nmap reports. Useful for batch processing multiple targets in red team operations or penetration tests.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $ROUTER_IP | IP of the router for interface routing | 10.10.14.1 |
| $NETWORK | Target network CIDR | 10.10.10.0/24 |
| $MACHINE_IP | Specific target IP for port scan | 10.10.10.97 |

## Usage

Save as a .sh file, set variables (e.g., export ROUTER_IP=10.10.14.1), ensure directories exist (mkdir -p $MACHINE_IP/scans), and run with sudo: `sudo bash script.sh`. It generates output files for manual review or integration into larger toolchains like Metasploit. Use in controlled environments to avoid disrupting production networks.

## Detection

- High-volume SYN packets from Masscan detectable by IDS/IPS (e.g., Snort rules for port scans).
- Nmap's script execution may trigger HIDS alerts on target hosts.
- Log anomalous outbound connections or process executions (masscan/nmap) on the attacker's pivot host.
- Network flow monitoring for scan patterns across ports/IPs.

## Related

- [[procedures/Network-Discovery-with-Masscan]]
- [[tools/masscan]]
- [[tools/Nmap]]
