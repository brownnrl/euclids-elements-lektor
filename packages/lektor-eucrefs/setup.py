from setuptools import setup

setup(
    name="lektor-eucrefs",
    version="0.1.0",
    description="Mistune extension: @I.5 inline citations and [!just …] margin blocks resolved to Euclid's Elements URLs.",
    py_modules=["lektor_eucrefs"],
    install_requires=["Lektor"],
    entry_points={
        "lektor.plugins": [
            "eucrefs = lektor_eucrefs:EucrefsPlugin",
        ],
    },
)
