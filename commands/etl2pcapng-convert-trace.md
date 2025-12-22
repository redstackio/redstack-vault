---
id: 04e8a72c-efe6-496e-ab6b-1b673bf82508
name: etl2pcapng-convert-trace
type: command
executor: cmd
data: etl2pcapng.exe $_INPUT_ETL $_OUTPUT_PCAPNG
output: null
created_at: '2023-04-06T03:56:23.097191+00:00'
updated_at: '2023-04-10T20:25:12.038720+00:00'
platforms:
  - Windows
tags:
  - etl-conversion
  - pcapng
verified: true
validated: true
---

# etl2pcapng-convert-trace

## Command

```cmd
etl2pcapng.exe $_INPUT_ETL $_OUTPUT_PCAPNG
```

## Description

Converts Windows ETL trace files to PCAPNG format for use in Wireshark or other analyzers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INPUT_ETL | Path to input ETL file (e.g., c:\trace.etl) | Yes |
| $_OUTPUT_PCAPNG | Path for output PCAPNG file | Yes |

## Examples

### Basic Usage

```cmd
etl2pcapng.exe c:\trace.etl c:\trace.pcapng
```

### With Full Paths

```cmd
etl2pcapng.exe "C:\Traces\trace.etl" "C:\Output\trace.pcapng"
```

## Expected Output

Conversion progress and success message; new PCAPNG file created.

## Related

- [[procedures/Network-Trace-Capture]]
- [[commands/netsh-trace-stop]]
