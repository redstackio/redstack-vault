---
id: e4d94e39-457c-4765-9c07-67b265e7eac1
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:23.096834+00:00'
updated_at: '2023-04-10T20:25:12.041396+00:00'
---

# Code Snippet e4d94e39

**Language**: ps1

```ps1
# start a capture use the netsh command.
netsh trace start capture=yes report=disabled tracefile=c:\trace.etl maxsize=16384

# stop the trace
netsh trace stop

# Event tracing can be also used across a reboots
netsh trace start capture=yes report=disabled persistent=yes tracefile=c:\trace.etl maxsize=16384

# To open the file in Wireshark you have to convert the etl file to the cap file format. Microsoft has written a convert for this task. Download the latest version.
etl2pcapng.exe c:\trace.etl c:\trace.pcapng

# Use filters
netsh trace start capture=yes report=disabled Ethernet.Type=IPv4 IPv4.Address=10.200.200.3 tracefile=c:\trace.etl maxsize=16384
```
