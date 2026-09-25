"""Typed errors for dbt metadata dictionary processing."""


class DataDictionaryError(Exception):
    """Base error for dictionary generation failures."""


class InputPathError(DataDictionaryError):
    """Raised when the input manifest path is missing or unreadable."""


class ManifestValidationError(DataDictionaryError):
    """Raised when a manifest is structurally invalid for dictionary generation."""


class OutputWriteError(DataDictionaryError):
    """Raised when the requested output destination cannot be used."""
