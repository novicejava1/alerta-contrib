from setuptools import setup, find_packages

version = '0.0.8'

setup(
    name="alerta-chronograf",
    version=version,
    description='Alerta webhook for Chronograf',
    url='https://github.com/alerta/alerta-contrib',
    license='MIT',
    author='Sudhir Bhoga',
    author_email='sudhirbhoga@gmail.com',
    packages=find_packages(),
    py_modules=['alerta_chronograf'],
    install_requires=[
    ],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.webhooks': [
            'chronograf = alerta_chronograf:ChronografWebhook'
        ]
    }
)
