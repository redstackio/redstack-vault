---
id: d93c59c0-019f-4449-9602-8a3831b43ca1
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:40.304378+00:00'
updated_at: '2023-04-10T20:23:51.950524+00:00'
---

# Code Snippet d93c59c0

**Language**: Python

```python
$output = $twig->render(
  'Dear' . $_GET['custom_greeting'],
  array("first_name" => $user.first_name)
);

$output = $twig->render(
  "Dear {first_name}",
  array("first_name" => $user.first_name)
);
```


