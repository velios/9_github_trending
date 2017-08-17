# Github Trends
The program prints the 20 most popular repositories from [GitHub](https://github.com/) for a week and highlights the most stable ones

### How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

### How to use
```bash
#Run
$ python3 github_trending.py
#Output
Program prints 20 most popular repositories since 2017-08-10
 1 https://github.com/paulgb/BarbBlock                486 stars  4 issues
 2 https://github.com/c-bata/go-prompt                378 stars  4 issues
 3 https://github.com/def-/time.gif                   361 stars  3 issues
...
20 https://github.com/baidu/Elasticsearch Try it!     93 stars  0 issues
```
Try it tag means repository have 0 issues and recommend to inspection 

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

### Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
