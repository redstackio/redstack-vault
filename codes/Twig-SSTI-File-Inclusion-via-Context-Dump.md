---
type: code
language: twig
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - SSTI
  - Twig
  - file-inclusion
  - payload
platforms:
  - Web
  - PHP
validated: true
---

# Twig-SSTI-File-Inclusion-via-Context-Dump

## Code

```twig
FILENAME{% set var = dump(_context)[OFFSET:LENGTH] %} {{ include(var) }}
```

## Description

This payload dumps the Twig rendering context using 'dump(_context)', slices a portion with [OFFSET:LENGTH], stores it in a variable, and includes it as a file path via Twig's include() function. It enables arbitrary file reads by extracting paths from the context without quotes, bypassing filters on direct strings.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| FILENAME | Base file path to prepend or target | /etc/passwd |
| OFFSET | Starting index in the dumped context string | 0 |
| LENGTH | Length of substring to extract | 20 |

## Usage

Inject into a Twig input to dump and include internal files like config.php or /proc/self/environ. Adjust OFFSET and LENGTH based on dump output from initial tests. Used in SSTI chains for reconnaissance before full RCE, as in [[procedures/Exploit-Twig-SSTI-for-Remote-Code-Execution]].

## Detection

- Log Twig dump() calls or include() with dynamic paths.
- Monitor for access to sensitive files like /etc/passwd via web logs.
- Anomaly detection on context dumping in application traces.

## Related

- [[procedures/Exploit-Twig-SSTI-for-Remote-Code-Execution]]
