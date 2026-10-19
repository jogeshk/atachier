from ._version import __version__
from .io import load
from .backends.selection import select_geometry_backend

_backend = select_geometry_backend("auto")

def configure(*, backend: str = "auto") -> None:
    """Configure Atachier's geometry backend."""
    global _backend
    _backend = select_geometry_backend(backend)

def get_backend_name() -> str:
    """Return the active geometry backend name."""
    return _backend.name

def get_geometry_backend():
    """Return the active geometry backend instance."""
    return _backend

__all__ =[
    "__version__",
    "load",
    "configure",
    "get_backend_name",
    "get_geometry_backend",
]
