from setuptools import setup

setup(name='demo',
      version='1.0',
      description='OpenShift App',
      author='Miguel',
      author_email='miguel.angel.lopez@correounivalle.edu.co',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['Flask==0.10.1',
                        'WTForms==2.1',
                        'Flask-WTF==0.12'
                        'psycopg2==2.5.2'],
     )
