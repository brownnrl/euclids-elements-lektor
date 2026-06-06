from setuptools import setup

setup(
    name="lektor-roman-slug-mimetypes",
    version="0.1.0",
    description="Register text/html for the numeric and Roman-numeral extensions our dotted slugs produce (defX.I, defX.II.1, …) so Lektor's dev server doesn't serve them as application/octet-stream.",
    py_modules=["lektor_roman_slug_mimetypes"],
    install_requires=["Lektor"],
    entry_points={
        "lektor.plugins": [
            "roman-slug-mimetypes = lektor_roman_slug_mimetypes:RomanSlugMimetypesPlugin",
        ],
    },
)
