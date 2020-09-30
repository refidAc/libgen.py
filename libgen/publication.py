from typing import Any, Dict, Optional

from utils import random_string


class Publication(object):
    """Publication is a class where the attributes of each
    of its objects are passed to the constructor."""

    def __init__(self, attrs: Dict[str, Any]) -> None:
        """Constructs a new Publication.

        :Example:

        attrs = {'author': 'Fernando Pessoa', 'title': 'O Livro do Desassossego"}
        Publication(**attrs)

        :param attrs: a Dict of attributes
        :rtype: None"""
        self.attrs = attrs

    @property
    def attributes(self):
        return self.attrs

    @property
    def fields(self):
        return self.attrs.keys()

    @property
    def values(self):
        """Returns a list containing the values of every field in the object."""
        return self.attrs.values()

    def __getattr__(self, attr) -> Optional[Any]:
        return self.attrs.get(attr)

    def filename(self) -> Optional[str]:
        ext = self.attrs.get('extension')  # required
        if ext is None:
            return None
        title = self.attrs.get('title')  # optional
        # if title is None, generate random filename
        if title is None:
            random_filename = random_string(15)
            return f'{random_filename}.{ext}'
        year = self.attrs.get('year')  # optional
        if year:
            authors = self.attrs.get('authors')  # optional
            if authors:
                return f'{title} ({year}) - {authors}.{ext}'
            else:
                return f'{title} ({year}).{ext}'
        return f'{title}.{ext}'

    def __repr__(self) -> str:
        attrs = ', '.join([f'{a!r}: {v}' for (a, v) in self.attrs.items()])
        return f'{self.__class__.__name__}({attrs})'

    def __len__(self) -> int:
        return len(self.attrs)
