import pytest
from jonson import Logger, logger


def test_ignore(capfd):
    # Should not print anything when the record level is lower than the logger level
    logger = Logger("warn")
    logger.info("Something going as expected", {"key": "Balue"})
    out, err = capfd.readouterr()
    assert not out


def test_print(capfd):
    # Should print the record
    logger = Logger("debug")
    logger.info("Something going as expected")
    out, err = capfd.readouterr()
    assert out.find("Something going as expected") != -1


def test_level(capfd):
    # Should print the record with the correct level field
    logger = Logger("warn")
    logger.warn("Something ominous")
    out, err = capfd.readouterr()
    assert out.find("\"level\": \"warn\"") != -1


def test_enrichment(capfd):
    # Should print the record with additional fields
    logger = Logger("debug")
    logger.error("Something must have gone terribly wrong", {"additional": "details"})
    out, err = capfd.readouterr()
    assert out.find("\"additional\": \"details\"") != -1


def test_synonym_fatal(capfd):
    # Should print the record with the synonymous level field
    logger = Logger("debug")
    logger.fatal("Something must have gone terribly wrong")
    out, err = capfd.readouterr()
    assert out.find("\"level\": \"critical\"") != -1


def test_synonym_panic(capfd):
    # Should print the record with the synonymous level field
    logger = Logger("debug")
    logger.panic("Something must have gone terribly wrong")
    out, err = capfd.readouterr()
    assert out.find("\"level\": \"critical\"") != -1


def test_exception(capfd):
    # Should parse the exception and print the record with the exception message
    logger = Logger("warn")
    e = Exception("Something must have gone horribly wrong")
    logger.error(e)
    out, err = capfd.readouterr()
    assert out.find("\"message\": \"Something must have gone horribly wrong\"") != -1
    assert out.find("\"trace\":") != -1


def test_unserializable(capfd):
    # Should omit the unserializable enrichment
    logger = Logger("debug")
    e = Exception("Something must have gone horribly wrong")
    logger.info("Attaching this exception", {'error': e})
    out, err = capfd.readouterr()
    assert out.find("Attaching this exception") != -1
    assert out.find("error") == -1
    assert out.find("Something must have gone horribly wrong") == -1


def test_persistent(capfd):
    # Should print all records with the persistent enrichment
    logger = Logger("debug", {'host': 'Welcome to my party'})
    logger.info("Something going as expected", {"key": "Balue"})
    out, err = capfd.readouterr()
    assert out.find("\"host\": \"Welcome to my party\"") != -1


def test_persistent_error(capfd):
    # Should raise an error when the persistent enrichment is not JSON serializable
    with pytest.raises(TypeError) as excinfo:
        def func():
            return
        logger = Logger("debug", {'func': func})
    assert "Persistent enrichment dictionary must be JSON serializable" in str(excinfo.value)


def test_instance_export(capfd):
    # Should work out-of-the-box with the default logger instance
    logger.debug("Something going as expected")
    out, err = capfd.readouterr()
    assert out.find("Something going as expected") != -1
    assert out.find("\"level\": \"debug\"") != -1
