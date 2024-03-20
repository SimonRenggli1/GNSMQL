<div align="center">
<img src="![gnsmql](https://github.com/SimonRenggli1/GNSMQL/assets/96227533/c735f725-8e07-49d2-99ac-38a0a278d622)
" width=355 height=218>
<br/>
<h1>gnsmql: A Database for Sleepy People</h1>
<br/>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>
</div>

----------
## Table of Contents
- [Features](#Features)
- [Getting Started](#Getting-Started)
- [Quick Start](#Quick-Start)
- [Issues & bug reports](#Issues--bug-reports)
- [Show your support](#Show-your-support)
- [Credits](#Credits)

Welcome to gnsmql, the most straightforward database management system designed for developers who want to focus on their dreams as much as their data. gnsmql simplifies the complexities of data storage into a restful slumber of coding ease. Whether you're half-awake coding at 2 AM or just prefer a minimalist approach to database management, gnsmql is here to help.

## Features

- **Easy Setup**: Get your database running with just a few lines of code. Perfect for late-night coding sessions.
- **Minimalist Design**: Only the features you need, nothing you don't. No complicated configurations or setups.
- **JSON-Based Storage**: Readable and straightforward data storage using JSON files.
- **Custom Path Support**: Store your databases exactly where you want them, whether it's a local folder or a mounted drive in the clouds.
- **Pythonic Interface**: A clean, Pythonic API makes working with databases as comforting as counting sheep.
## Getting Started
### Prerequisites
- Python 3.6 or higher

### Installation
```pip install gnsmql```

## Quick Start
Create a Database Instance
```
import gnsmql

# Initialize with default path
gnsmql = gnsmql.gnsmqlConnector()

# Or specify a custom path for your database
# gnsmql = gnsmql.gnsmqlConnector('/path/to/your/custom/db')
```

Create a Database
```
gnsmql.execute("CREATE DATABASE dreamy;")
```
Create a Table
```
gnsmql.execute("CREATE TABLE dreamy.nightmares;")
```
Insert Data into Table
```
gnsmql.execute("INSERT INTO dreamy.nightmares VALUES ({'id': 1, 'nightmare': 'forgot to wear pants to work'});")
```
Query Data
```
gnsmql.execute("SELECT * FROM dreamy.nightmares;")
```

## Issues & bug reports
Just fill an issue and describe it. We'll check it ASAP!

- Please complete the issue template

## Show your support
### Star this repo
Give a ⭐️ if this project helped you!

## Credits
- Credits to [endoplasmatischesretikulum](https://github.com/endoplasmatischesretikulum) for being awesome 
