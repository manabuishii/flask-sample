# flask-sample
Flask sample

## Install flask

Install Flask

Tested version is following.

```text
Flask==2.1.1
```

### pip Install

```text
pip install -r requiments.text
```

## Very small sample

Very small sample at official site

* [Welcome | Flask (A Python Microframework)](http://flask.pocoo.org/)

## Flask 0.12 Document

* [Welcome to Flask — Flask Documentation (0.12)](http://flask.pocoo.org/docs/0.12/)

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
docker run --rm manabuishii/flask-sample:0.3.0
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

## Pattern 4 , Get parameter


```
$ curl http://localhost:15000/parametertest\?yourparameter\=MYPARAMETER
[MYPARAMETER] World!
```

* [The Request Context — Flask Documentation (0.12)](http://flask.pocoo.org/docs/0.12/reqcontext/)

## Pattern 5 , Create form

TODO

## Pattern 6 , File upload

TODO

## Pattern 7 , static file

Static file serving

```console
$ curl http://localhost:15000/static/staticfile.html
<html>
<head>
<meta charset="utf-8">
<title>Staticfile sample</title>
</head>
<body>
<h1>Staticfile</h1>
Sample
</body>
</html>
```

## Pattern 8 , just template

```console
$ curl http://localhost:15000/templatehelloworld\?yournameparameter\=rainbow
<html>
<head>
<meta charset="utf-8">
<title>Template sample</title>
</head>
<body>
<h1>Template samle</h1>
Hello rainbow !<br>
Welcome template world!<br>
</body>
</html>
```

## Publish to Internet

## Apache httpd reverse proxy

TODO
