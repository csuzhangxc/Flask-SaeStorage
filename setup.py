#!/usr/bin/env python

from setuptools import setup


setup(
    name='Flask-SaeStorage',
    version='0.9.0',
    url='https://github.com/csuzhangxc/Flask-SaeStorage',
    license='MIT',
    author='Zhang Xuecheng',
    author_email='csuzhangxc@gmail.com',
    description='SAE Storage for Flask',
    long_description='SAE Storage for Flask. Please visit: https://github.com/csuzhangxc/Flask-SaeStorage',
    py_modules=['flask_saestorage'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    keywords='sae storage for flask',
    package_data={'': ['LICENSE']},
    install_requires=[
        'setuptools',
        'Flask'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
