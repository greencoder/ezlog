# ezlog

A (very) simple wrapper around Python's logger

## Background

I got tired of the lengthy boilerplate code required to set up logging to both the console and the filesystem. This wrapper simplifies that.

## Usage

Setting up EZLog is very simple:

```
import ezlog

logger = ezlog.Logger(file_name='<filename>', console_level='debug|info|warn|error', file_level='debug|info|warn|error')

logger.info('This is an informational message')
logger.debug('This is a debugging message')
```

_Note: The console level defaults to `debug`, the file level defaults to `info`._

If you don't want file-level logging, simply pass `None` to the constructor and you will only get console-level logging:
```
logger = ezlog.Logger(file_name=None, console_level='debug|info|warn|error', file_level='debug|info|warn|error')
```

## Contributing

Pull requests are welcome so long as they do not add complexity to the end-user.
