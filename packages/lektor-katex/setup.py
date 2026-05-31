from setuptools import setup

setup(
    name="lektor-katex",
    version="0.1.0",
    description="Build-time KaTeX rendering inside Lektor's Mistune markdown.",
    py_modules=["lektor_katex"],
    install_requires=["Lektor"],
    entry_points={
        "lektor.plugins": [
            "katex = lektor_katex:KatexPlugin",
        ],
    },
)
