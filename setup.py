from pathlib import Path

from setuptools import setup, find_packages  # noqa: H301

with open('requirements.txt', 'r') as f:
    requires = [x.strip() for x in f if x.strip()]

with open('README.md', 'r') as f:
    readme = f.read()


NAME = "pinform"

meta = {}
with open(Path(__file__).parent / 'pinform' / '__init__.py') as f:
    exec('\n'.join(l for l in f if l.startswith('__')), meta)

setup(
    name=NAME,
    version=meta.get('__version__'),
    description="Pinform with a minor edit.",
    long_description=readme,
    url="https://github.com/iDrwish/pinform",
    keywords=["InfluxDB", "InfluxDB Python Client"],
    install_requires=requires,
    packages=find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
    data_files=['requirements.txt'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ])
