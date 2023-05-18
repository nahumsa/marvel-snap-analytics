from setuptools import find_packages, setup

setup(
    name="marvel_snap_analytics",
    packages=find_packages(exclude=["marvel_snap_analytics_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
