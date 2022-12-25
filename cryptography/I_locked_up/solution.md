# Basically i locked up

## Write-Up

When we check the encryption, we can see that the encryption is basically a rotation after a xor with the given passowrd. and as the decryption function is given, we can directly decrypt the message if we have a password or a part of the message before the encryption (as says one of the properties of the xor)

and as luck we are, we have a part of the plaintext as an assertion in the function of the encryption :

```python
...
  assert(len(password) == 8)
  assert(b"HiDeteXT" in plaintext)
...
```

So we can use it as our password to decrypt the message.

## Flag

NITE{BrUT3fORceD_y0uR_wAy_iN}
