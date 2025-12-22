---
id: 81d38402-834c-46d0-b696-7336b510bcc6
name: Network-Trace-Capture
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.114120+00:00'
updated_at: '2023-04-10T20:25:12.020303+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Sniffing|T1040 - Network Sniffing]]'
sub_techniques: []
tags:
  - '[[tags/Capture a network trace with builtin tools]]'
  - '[[tags/Network Pivoting Techniques]]'
  - network-sniffing
  - traffic-capture
commands:
  - '[[commands/tcpdump-capture-tcp-packets]]'
  - '[[commands/tcpdump-capture-port-22]]'
  - '[[commands/tcpdump-print-ascii]]'
  - '[[commands/tcpdump-write-to-file]]'
  - '[[commands/etl2pcapng-convert-trace]]'
  - '[[commands/apt-install-tcpdump]]'
  - '[[commands/netsh-trace-start-basic]]'
  - '[[commands/netsh-trace-start-with-filters]]'
  - '[[commands/netsh-trace-start-persistent]]'
  - '[[commands/netsh-trace-stop]]'
platforms:
  - Windows
  - Linux
tools: []
validated: true
---

# Network-Trace-Capture

## Summary

Network Trace Capture is a procedure for intercepting and recording network traffic using built-in operating system tools on Windows (netsh trace) and Linux (tcpdump). This technique enables security analysts or red team operators to monitor communications for sensitive data leakage, such as credentials or application data, in a controlled environment. It maps to MITRE ATT&CK technique T1040 (Network Sniffing) under Discovery and Credential Access tactics, allowing identification of unencrypted traffic or protocol weaknesses.

## Description

In offensive security operations, capturing network traces helps discover active services, extract credentials from cleartext protocols (e.g., HTTP, Telnet), or analyze lateral movement opportunities. On Windows, netsh trace captures packets in ETL format, which can be converted to PCAPNG for analysis in tools like Wireshark. On Linux, tcpdump provides flexible packet capture with filters for specific protocols or ports. This procedure requires administrative privileges and is typically performed on compromised hosts or network segments to avoid detection. Prerequisites include physical or remote access to the target system. Expected outcomes include raw packet data for offline analysis, revealing potential vulnerabilities like weak encryption or misconfigurations.

## Requirements

1. Administrative or root privileges on the target Windows or Linux system to initiate captures.
2. Network interface access (e.g., Ethernet or Wi-Fi adapter) with promiscuous mode support if needed for full visibility.
3. Sufficient disk space for trace files (e.g., ETL or PCAP files can grow large during extended captures).
4. For Windows ETL conversion, download etl2pcapng.exe from Microsoft or a trusted source.
5. Optional: Analysis tool like Wireshark for post-capture review.

## Defense

- Encrypt all sensitive traffic using TLS/SSL for protocols like HTTP to prevent credential exposure in traces.
- Implement network segmentation with firewalls to limit capture scope and monitor for unusual sniffing activity via endpoint detection tools.
- Enable host-based logging (e.g., Windows Event Logs for netsh usage) and anomaly detection in network traffic to identify unauthorized captures.
- Use application-layer security like mutual TLS to obscure data even if packets are intercepted.

## Objectives

1. Capture raw network packets to inspect for unencrypted credentials or sensitive data transmission.
2. Identify active network services, protocols, and communication patterns for further discovery or exploitation.
3. Generate analyzable trace files (PCAP/ETL) to support post-exploitation analysis or evidence collection in red team engagements.

## Instructions

### Windows: Start Basic Network Capture

**Context**: Begin capturing all network traffic on Windows using netsh trace, saving to an ETL file. This step initiates the trace without filters for comprehensive data collection. Run as administrator to ensure full interface access.

**Command** ([[commands/netsh-trace-start-basic]]):
```cmd
netsh trace start capture=yes report=disabled tracefile=c:\trace.etl maxsize=16384
```

> This command starts packet capture on all interfaces, disables reporting overhead, and limits the file to 16MB (adjust maxsize as needed). Expected output is a confirmation message like "Trace configuration started."

### Windows: Apply Filters to Capture

**Context**: Narrow the capture to specific traffic, such as IPv4 packets to/from a target IP, to focus on relevant data and reduce file size. Replace placeholders with actual values (e.g., target IP).

**Command** ([[commands/netsh-trace-start-with-filters]]):
```cmd
netsh trace start capture=yes report=disabled Ethernet.Type=IPv4 IPv4.Address=10.200.200.3 tracefile=c:\trace.etl maxsize=16384
```

> Filters like Ethernet.Type=IPv4 and IPv4.Address limit to IPv4 traffic involving the specified address. Success is indicated by the trace starting without errors; monitor file growth to confirm activity.

### Windows: Enable Persistent Capture

**Context**: Configure the trace to survive reboots, useful for long-term monitoring on persistent access scenarios. This ensures continuity if the system restarts during an operation.

**Command** ([[commands/netsh-trace-start-persistent]]):
```cmd
netsh trace start capture=yes report=disabled persistent=yes tracefile=c:\trace.etl maxsize=16384
```

> The 'persistent=yes' flag allows the trace to restart post-reboot. Expected output confirms persistence; verify by checking the trace status with 'netsh trace show status'.

### Windows: Stop the Capture

**Context**: End the trace session to finalize the ETL file for analysis. Always stop after collecting sufficient data to avoid excessive resource usage.

**Command** ([[commands/netsh-trace-stop]]):
```cmd
netsh trace stop
```

> This halts all tracing and closes the file. Output includes a summary of captured data; the ETL file is now ready for conversion.

### Windows: Convert ETL to PCAPNG

**Context**: Transform the Windows-specific ETL format to the standard PCAPNG for compatibility with analysis tools like Wireshark. Download etl2pcapng.exe from Microsoft's Sysinternals or GitHub repository.

**Command** ([[commands/etl2pcapng-convert-trace]]):
```cmd
etl2pcapng.exe c:\trace.etl c:\trace.pcapng
```

> Run from the directory containing the executable. Expected output is a progress indicator and a new PCAPNG file; errors occur if paths are invalid or ETL is corrupted.

### Linux: Install tcpdump

**Context**: Ensure tcpdump is available on the Linux target, as it may not be pre-installed on minimal systems. This step is prerequisite for all Linux captures.

**Command** ([[commands/apt-install-tcpdump]]):
```bash
sudo apt-get install tcpdump
```

> On Debian-based systems; use 'yum install tcpdump' for RPM-based. Success: Package installs without errors, verifiable with 'tcpdump --version'.

### Linux: Capture Packets to File

**Context**: Record all traffic on a specific interface to a PCAP file for offline analysis. Specify the interface (e.g., eth0) based on 'ip link show' output.

**Command** ([[commands/tcpdump-write-to-file]]):
```bash
tcpdump -w 0001.pcap -i eth0
```

> The '-w' writes to file without display; press Ctrl+C to stop. Expected: File created and growing; use 'ls -lh 0001.pcap' to check size.

### Linux: Print Packets in ASCII

**Context**: Display captured packets in human-readable ASCII format for real-time inspection, useful for quick credential spotting in cleartext.

**Command** ([[commands/tcpdump-print-ascii]]):
```bash
tcpdump -A -i eth0
```

> '-A' prints payload as ASCII; run until relevant traffic appears. Output streams packet contents; look for strings like passwords in HTTP requests.

### Linux: Capture TCP Packets Only

**Context**: Filter to TCP traffic to focus on connection-oriented protocols where data like credentials is often exchanged.

**Command** ([[commands/tcpdump-capture-tcp-packets]]):
```bash
tcpdump -i eth0 tcp
```

> Limits to TCP; expected output lists TCP headers and payloads in real-time. Verify with no non-TCP packets appearing.

### Linux: Capture Specific Port Traffic

**Context**: Target traffic on a port like 22 (SSH) to monitor specific services without overwhelming data volume.

**Command** ([[commands/tcpdump-capture-port-22]]):
```bash
tcpdump -i eth0 port 22
```

> Captures SSH traffic; output shows SYN/ACK handshakes and encrypted payloads. Success: Only port 22 packets displayed.
