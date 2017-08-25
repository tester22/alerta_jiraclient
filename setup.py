
from setuptools import setup, find_packages

version = '0.0.3'

setup(
    name="alerta-jiraclient",
    version=version,
    description='Alerta plugin to escalate to Jira',
    url='https://github.com/alerta/alerta-contrib',
    license='MIT',
    author='Anton Delitsch',
    author_email='anton@trugen.net',
    packages=find_packages(),
    py_modules=['alerta_jiraclient'],
    install_requires=[
        #"jira==1.0.10"
    ],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.plugins': [
            'jiraclient = alerta_jiraclient:jiraClientEscalate',
        ]
    }
)
