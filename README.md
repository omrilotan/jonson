# jonson [![](https://img.shields.io/pypi/v/jonson?style=flat-square)](https://pypi.org/project/jonson/) [![](https://img.shields.io/static/v1?label=github&message=jonson&labelColor=black&color=3572a5&style=flat-square&logo=github)](https://github.com/omrilotan/jonson)

## out-of-the-box, ready-to-use JSON logger


```py
from jonson import logger

logger.info("Something going as expected", { "host": socket.gethostname() })
logger.warn("Something must have gone terribly wrong")

except Exception as e:
    logger.error(e, { description: "something descriptive" })
```

### Log level
Create logger instance with a minimal log level

```py
from jonson import Logger

logger = Logger("warn")

logger.info("Something going as expected", { "host": socket.gethostname() }) # ignored
logger.warn("Something must have gone terribly wrong") # sent
```

#### Log levels hirarchy

A few synonyms are available for convenience

1. `trace`, `verbose`
1. `debug`
1. `info`, `log`
1. `warn`
1. `error`
1. `critical`, `fatal`, `panic`

For example, a logger with log level "warn" will only print logs with level "warn", "error", or "critical".

### Arguments
**Create**: Logger class accepts one or two arguments:

1. `{string}` Case insensitive name of **minimal** log level. defaults to `"info"`
1. `{dictionary}` {'Key':'Value'} pairs, optional. Persistent enrichment fields for all log records

```py
logger = Logger(os.environ["LOG_LEVEL"], { "host": socket.gethostname() })
```

**Send**: Logger functions accept one or two arguments:

1. `{any}` Record's "message" field. Traditionally this would be a string or an exception.
1. `{dictionary}` {'Key':'Value'} pairs, optional. Values should be JSON serializable

```py
logger.info("something, something", { dark: "side" })
```
