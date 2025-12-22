---
id: 2d4742ff-0514-4f96-acf9-ac072a689d61
type: tool
description: >-
  vgdb is the GDB server component of Valgrind, enabling remote debugging of
  instrumented programs for memory and threading analysis.
verified: true
created_at: '2019-08-28T21:17:32.327422+00:00'
updated_at: '2024-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - debugging
  - valgrind
  - gdb
  - binary-analysis
url: 'https://valgrind.org/docs/manual/manual-vgdb.html'
commands:
  - '[[commands/vgdb-basic-connection]]'
  - '[[commands/vgdb-wait-connection]]'
validated: true
---

# vgdb

**Status**: Unverified

## Overview

vgdb (Valgrind GDB) is a utility within the Valgrind toolkit that serves as a GDB server, allowing users to attach the GNU Debugger (GDB) to programs running under Valgrind instrumentation. It is primarily used for debugging Linux applications to detect memory leaks, threading bugs, and performance issues. In security contexts, vgdb aids reverse engineers and vulnerability researchers in analyzing binaries, exploits, and malware by providing detailed runtime inspection without significantly altering program behavior.

## Description

vgdb facilitates communication between GDB and Valgrind-monitored processes via named pipes or TCP. To use it, a program is executed with Valgrind options like --vgdb=yes to enable the server mode. vgdb then connects to this session, relaying commands and data. This setup supports tools like Memcheck (memory error detection), Helgrind (thread error detection), and Cachegrind (profiling). Security professionals leverage vgdb for tasks such as fuzzing analysis, exploit development, and identifying buffer overflows or use-after-free vulnerabilities in target software.

## Features

- Remote GDB attachment to Valgrind-instrumented processes
- Support for pipe-based or TCP-based communication
- Configurable timeouts and process identification for targeted connections
- Integration with Valgrind's suite for comprehensive debugging and profiling

## Installation

### Requirements

- Linux kernel (tested on 2.6+)
- GNU Debugger (GDB) version 7.0 or later
- Valgrind package (vgdb is bundled within it)

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update
sudo apt install valgrind gdb

# On Kali Linux (pre-installed in many cases)
sudo apt install valgrind gdb

# On Fedora/RHEL
sudo dnf install valgrind gdb

# From source (if needed)
# Download from https://valgrind.org/downloads/
# tar xzf Valgrind-3.21.0.tar.bz2
# cd Valgrind-3.21.0
# ./configure
# make
# sudo make install
```

## Basic Usage

```bash
vgdb --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help message and exit |
| `--wait=N` | Wait up to N seconds for a GDB connection |
| `--vgdb-prefix=PREFIX` | Specify the prefix for Valgrind-GDB communication pipes (default: vgdb-pipe) |
| `--pid=PID` | Connect to the Valgrind process with the given PID |
| `--port=PORT` | Use TCP port PORT for remote connections (experimental) |

## Examples

### Example 1: Basic Usage

First, run a program under Valgrind with vgdb enabled:

```bash
valgrind --tool=memcheck --vgdb=yes --vgdb-error=0 ./target_program
```

In a separate terminal, connect with vgdb:

```bash
vgdb
```

Then launch GDB and attach:

```bash
gdb ./target_program
(gdb) target remote \| vgdb
```

This establishes a debugging session where you can set breakpoints and inspect memory.

### Example 2: Advanced Usage

Wait for a connection with a custom timeout and prefix:

```bash
vgdb --wait=120 --vgdb-prefix=/tmp/mydebug-pipe
```

Use this when coordinating with a delayed GDB attachment or in scripted environments.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1057.001]] Process Discovery (via GDB inspection of running processes under Valgrind)
- [[Windows Service]] Create or Modify System Process (instrumenting processes for analysis in security research)

### Tactics

- [[Discovery]] Discovery (analyzing software behavior and vulnerabilities)

Note: vgdb is primarily a defensive and research tool used in red teaming for binary analysis and exploit development, rather than direct offensive operations.

## Detection

Indicators and methods for detecting this tool's usage:

- System processes named 'valgrind' or 'vgdb' visible via `ps aux | grep vgdb`
- Named pipes in /tmp/ like vgdb-pipe-* or custom prefixes
- Elevated CPU and memory usage from Valgrind instrumentation
- GDB sessions connected to local pipes (netstat or lsof for pipe monitoring)
- Log entries in /proc/<pid>/cmdline showing valgrind arguments

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/valgrind]]
- [[tools/gdb]]
- [[tools/gdbserver]]

## References

- Official vgdb documentation: https://valgrind.org/docs/manual/manual-vgdb.html
- Valgrind project homepage: https://valgrind.org/
- GDB integration guide: https://sourceware.org/gdb/onlinedocs/gdb/Remote-Debugging.html
