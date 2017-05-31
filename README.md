# flask-sample
Flask sample

# Install flask

Install Flask (0.12)

# Run

```
python flasksample.py
```

it works well

```
$ python flasksample.py
 * Running on http://0.0.0.0:15000/ (Press CTRL+C to quit)
```

## docker run

```
docker run --rm manabuishii/flask-sample:0.2.0
```

# Test


## Pattern 1

```
$ curl http://localhost:15000
Hello World!
```

## Pattern 2

```
$ curl http://localhost:15000/testaccess
Test Access complete.
```

## Pattern 3 , execute command

This sample execute `date` command

```
$ curl http://localhost:15000/datecmd
Wed May 31 08:26:23 UTC 2017
```
