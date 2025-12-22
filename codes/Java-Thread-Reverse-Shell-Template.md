---
type: code
language: Java
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - java
  - thread
  - reverse-shell
  - template
platforms:
  - Linux
  - Windows
  - macOS
validated: true
---

# Java-Thread-Reverse-Shell-Template

## Code

```java
Thread thread = new Thread(){
    public void run(){
        // Reverse shell here
    }
};
thread.start();
```

## Description

This code snippet provides a template for creating an anonymous Java thread to run reverse shell logic in the background. It allows the shell to execute concurrently with the main program, enhancing stealth by avoiding blocking operations. Place the actual socket connection and process execution code inside the run() method to establish the reverse connection.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a structural template; add variables like host IP and port inside run() | N/A |

## Usage

Embed this in a Java class (e.g., public static void main), replace the comment with reverse shell implementation (e.g., Socket and Runtime.exec), compile with javac, and run with java. Ideal for post-exploitation in Java environments like application servers. Start a listener (e.g., nc -lvnp 4444) before execution.

## Detection

- Monitor Java processes for unusual thread creation or Runtime.exec invocations via application logging or EDR tools.
- Network monitoring for outbound connections from java/javaw processes to non-standard IPs/ports.
- Code review or static analysis for anonymous Thread objects with network/process calls.
- Behavioral alerts on Java apps spawning shells or connecting externally.

## Related

- [[procedures/Establish-Java-Reverse-Shell-Using-Thread]]
