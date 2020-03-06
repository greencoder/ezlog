# ezlogs

A (very) simple wrapper around Python's logger

## Background

I got tired of the lengthy boilerplate code required to set up logging to both the console and the filesystem. This wrapper simplifies that.

## Installation

```
$ pip install ezlogs
```

## Usage

Setting up EZLogs is very simple:

```
import ezlogs

logger = ezlogs.Logger(file_name='log.txt', console_level='debug', file_level='info')

logger.info('This is an informational message')
logger.debug('This is a debugging message')
```

_Note: The console level defaults to `debug`, the file level defaults to `info`._

If you don't want file-level logging, simply pass `None` to the constructor and you will only get console-level logging:
```
logger = ezlogs.Logger(file_name=None, console_level='debug')
```

## Contributing

Pull requests are welcome so long as they do not add complexity to the end-user.
