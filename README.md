# GNSMQL: A Database for Sleepy People

Welcome to GNSMQL, the most straightforward database management system designed for developers who want to focus on their dreams as much as their data. GNSMQL simplifies the complexities of data storage into a restful slumber of coding ease. Whether you're half-awake coding at 2 AM or just prefer a minimalist approach to database management, GNSMQL is here to help.

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
```pip install GNSMQL```

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