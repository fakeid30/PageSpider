# PageSpider - A scrapper of website

# Tutorial

There are two ways to run a python script. 
One requires the script to have executable permission by the executing user.
The other one doesn't.
We are going to look at the second method first.

## Using python interpreter

Assuming the python executable is named `python3` and the executable is in path, then it can be run by,

```bash
$ python3 page_spider.py -db tst.db -i input.txt
```

The output should look like,

```bash
we are going work with tst.db
we are going scan input.txt
reading https://en.wikipedia.org/wiki/Python_%28programming_language%29

reading https://en.wikipedia.org/wiki/Guido_van_Rossum

reading https://en.wikipedia.org/wiki/Benevolent_dictator_for_life
```

## Using shebang in the called script

For this one, one has to make the script executable first.
This can be done by issuing the following command,

```bash
chmod u+x page_spider.py
```

Here we have assumed the user is already in the cloned directory.

Now there are two ways to do this.
One is a primitive one, another is an elegant one.

### Primitive one

If the `python3` executable is residing in location `/usr/bin/python3`,
the following line needs to be added at the top of the file `page_spider.py`

```bash
#!/usr/bin/python3
```

Now doing this should work,
```bash
$ ./page_spider.py -db tst.db -i input.txt
```

### Elegant one

The elegant solution is to add the following at the very top of the file `page_spider.py`.

```bash
#!/usr/bin/env python3
```

Now, why is this an elegant one? Because if wrote like this, then `#!/usr/bin/env` ensures that the interpreter will use the first installed version on users environment's `$PATH`.