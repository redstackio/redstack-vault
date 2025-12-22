---
id: 490cee8c-ae6e-4902-be83-c816cd450dfd
name: simple-buffer-overflow-crash-c
type: code
language: cpp
verified: true
created_at: '2023-04-06T03:56:17.158809+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - crash-program
  - core-dump
  - privilege-escalation
validated: true
---

# simple-buffer-overflow-crash-c

## Code

```cpp
int main(void) {
    char buf[1];
    for (int i = 0; i < 100; i++) {
        buf[i] = 1;
    }
    return 0;
}
```

## Description

This C program intentionally causes a buffer overflow by writing 100 bytes into a 1-byte array, triggering a segmentation fault. When compiled and executed in a Docker container with a modified core_pattern, it generates a core dump that can be used for privilege escalation by writing to root-owned locations.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No runtime parameters; static buffer size and loop count are hardcoded for simplicity. | N/A |

## Usage

Save as crash.c, compile with `gcc -o crash crash.c`, and run `./crash` in a privileged Docker container after setting core_pattern. This triggers the dump to the piped location, creating a root-owned file. Modify the buffer size or loop for different dump sizes if needed. Used in container escape scenarios to write payloads outside isolation.

## Detection

- Monitor for gcc compilations of small C programs or unexpected segfaults in containers.
- Audit core dump files in /var/lib/docker/overlay2 paths for unusual sizes or contents.
- Syscall tracing (e.g., via strace) for writes to /proc/sys/kernel/core_pattern followed by crashes.
- Container logs for 'Segmentation fault (core dumped)' events.

## Related

- [[procedures/Abuse-Core-Dumps-and-Core-Pattern-for-Privilege-Escalation-in-Docker]]
