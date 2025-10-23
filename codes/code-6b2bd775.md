---
id: 6b2bd775-7fcc-48cc-99ec-6c501d42f1aa
type: code
language: HTML
verified: false
created_at: '2023-04-06T03:56:40.435571+00:00'
updated_at: '2023-04-10T20:23:38.205236+00:00'
---

# Code Snippet 6b2bd775

**Language**: HTML

```html
<html>
 <head><title>{PAGE_TITLE}</title></head>
 <body>
  <table>
   <caption>Authors</caption>
   <thead>
    <tr><th>Name</th><th>Email</th></tr>
   </thead>
   <tfoot>
    <tr><td colspan="2">{NUM_AUTHORS}</td></tr>
   </tfoot>
   <tbody>
<!-- BEGIN authorline -->
    <tr><td>{AUTHOR_NAME}</td><td>{AUTHOR_EMAIL}</td></tr>
<!-- END authorline -->
   </tbody>
  </table>
 </body>
</html>
```


