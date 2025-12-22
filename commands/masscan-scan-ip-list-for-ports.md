---
id: 3d7a67e1-d507-43f2-8bb2-3a73724cc7aa
type: command
executor: bash
data: >-
  masscan -iL $_IPS_FILE --rate $_RATE -p$_LOW_PORT-$_HIGH_PORT -oL
  $_OUTPUT_FILE
output: >-
  root@hacker:~/rs# masscan -iL ips-online.txt --rate 10000 -p80-80 -oL
  masscan.out

  Starting masscan 1.0.5 (http://bit.ly/14GZzcT) at 2020-06-30 18:00:38 GMT
   -- forced options: -sS -Pn -n --randomize-hosts -v --send-eth
  Initiating SYN Stealth Scan

  Scanning 3 hosts [1 port/host]



  root@hacker:~/rs# cat masscan.out 

  #masscan

  open tcp 80 104.XX.27.XX 1593540039

  open tcp 80 172.XX.10.XX 1593540039

  open tcp 80 104.XX.26.XX 1593540039

  # end
created_at: '2020-06-30T18:05:36.049153+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - port-scan
  - masscan
verified: true
validated: true
---

# masscan-scan-ip-list-for-ports

## Command

```bash
masscan -iL $_IPS_FILE --rate $_RATE -p$_LOW_PORT-$_HIGH_PORT -oL $_OUTPUT_FILE
```

## Description

This command scans a list of IP addresses for a specified range of ports using SYN packets at a configurable high rate. It is designed for rapid reconnaissance of open ports across multiple targets, leveraging masscan's asynchronous capabilities. Run with sudo for raw socket access. Use this during initial network enumeration to identify potential entry points.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -iL $_IPS_FILE | Path to the input file containing a list of IP addresses or hosts (one per line) | Yes |
| --rate $_RATE | Scanning rate in packets per second (e.g., 10000 for high speed) | Yes |
| -p$_LOW_PORT-$_HIGH_PORT | Port range to scan (e.g., 80-80 for port 80 only, or 1-65535 for all ports) | Yes |
| -oL $_OUTPUT_FILE | Path to the output file in list format (easily parseable for further processing) | Yes |

## Examples

### Basic Usage

Scan an IP list for port 80 at 1000 packets per second:
```bash
sudo masscan -iL ips.txt --rate 1000 -p80-80 -oL open_ports.list
```

### Advanced Usage

Scan for a broader port range with higher rate:
```bash
sudo masscan -iL targets.txt --rate 5000 -p22,80,443 -oL results.list
```

## Expected Output

The command outputs scan progress to the console, including the number of hosts scanned and rate. The output file contains lines indicating open ports in the format: "open tcp PORT IP TIMESTAMP". For example:

```
Starting masscan 1.0.5 at [TIMESTAMP]
 -- forced options: -sS -Pn -n --randomize-hosts -v --send-eth
Initiating SYN Stealth Scan
Scanning [N] hosts [[M] port/host]

#masscan
open tcp 80 104.XX.27.XX [TIMESTAMP]
open tcp 80 172.XX.10.XX [TIMESTAMP]
open tcp 80 104.XX.26.XX [TIMESTAMP]
# end
```

Success is indicated by the presence of "open" lines in the output file for discovered ports.

## Related

- [[tools/masscan]]
