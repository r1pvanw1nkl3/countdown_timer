# Countdown Timer

## Description
This is a terminal-based countdown timer designed to be used for Non Programming Talks at the Recurse Center.

## Installation
Requires the uv package manager.


## Usage
Defaults to a fifteen minute timer with a 5 minute "yellow" warning and a one minute "red" warning.

```bash
uv run timer #runs the default 15 min timer
uv run timer 10 3 .5 #runs a 10 minute timer, with a 3 minute "yellow" warning and a 30 second "red warning"
```

