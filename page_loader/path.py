"""Module converting URL into readable string or filename."""
from urllib.parse import urlparse
import re


def replace_chars(s):
    """Replace chars to hyphens.

    Args:
        s ([str]): string containing some chars, like:
                   "https://python.org/3/library/exceptions.html"

    Returns:
        [str]: string with chars replaced to hyphens, like:
               "https-python-org-3-library-exceptions-html"
    """
    # Replace all chars to hyphens
    s = re.sub(r"[^A-Za-z0-9]", '-', s)

    # Replace multiple hyphens in string
    s = re.sub(r"\-{2,}", '-', s)

    # Remove unneccessary hyphen from the start & end of the string
    s = re.sub(r"(^\-)|(\-$)", '', s)

    return s


def remove_url_ext(s: str) -> str:
    """Remove unnecessary extension from the end of line.

    Args:
        s ([str]): some string that may contain extension in the end of line,
                   like: "https://yastatic.net/pcode/adfox/header-bidding.js"

    Returns:
        [str]: string without extension in the end of line, like:
               "https://yastatic.net/pcode/adfox/header-bidding"
    """
    if re.search(r"\.[^.\/]*$", s):
        return re.sub(r'\.[^.\/]*$', '', s)
    else:
        return s


def get_ext(s: str) -> str:
    """Get extension from URL without unwanted elements.

    Args:
        s (str): some url, like 'www.example.com/test.php?id=12"

    Returns:
        [type]: url extension, like 'php'
    """
    path = parse_url(url=s)['path']
    # Get full extension from URL
    if re.search(r"(\.[^.\/]*)$", path):
        ext = re.search(r"\.([^.\/]*)$", path)[1]

        # Remove unwanted elements from extension ('js?2708' -> 'js')
        if '?' in ext:
            ext = ext.split('?')[0]
        return ext

    # Return 'html' if URL does not have extension
    else:
        return 'html'


def parse_url(url: str) -> dict:
    """Parse URL and split it to parameters.

    Args:
        url (str): input url

    Returns:
        dict: url parameters
    """
    p = urlparse(url)
    return {
        'scheme': p.scheme,
        'netloc': p.netloc,
        'path': p.path,
        'params': p.params,
        'query': p.query,
        'fragment': p.fragment
    }


def url_to_string(url: str) -> str:
    """Convert URL into readable string without unnescessary chars & elements.

    Args:
        url ([str]): url, like "https://python.org/3/library/exceptions.html"

    Returns:
        [type]: string containing URL netloc and path without any chars,
                like: "python-org-3-library-exceptions"
    """

    output = []

    # Parse url into elements (scheme, netloc, path, params, query, fragment)
    # and generare string containing netlock & path only
    p = parse_url(url)
    if p['netloc']:
        output.append(p['netloc'])
    if p['path']:
        output.append(remove_url_ext(p['path']))

    output = ''.join(output)

    return replace_chars(output)


def get_filename(url: str, ext: str):
    """Convert URL into filename name which may be saved on disk.

    Args:
        url (str): url, like "https://python.org/3/library/exceptions.html"
        ext (str):  extension, like 'html', 'css', 'png'

    Raises:
        ValueError: error

    Returns:
        [type]: filename, like: "python-org-3-library-exceptions.html"
    """
    if ext is None or ext == '':
        raise ValueError('Invalid asset value - may not be None or empty')
    return str(url_to_string(url) + '.' + ext)


def get_foldername(url: str):
    """Convert URL into foldername to save URL's files.

    Args:
        url (str): url, like "https://python.org/3/library/exceptions.html"

    Returns:
        [type]: foldername, like: "python-org-3-library-exceptions_files"
    """
    return str(url_to_string(url) + '_files')
