from setuptools import setup, find_packages

version = '0.0.17'

setup(
    name="alerta-dynatrace",
    version=version,
    description='Alerta webhook for Dynatrace',
    url='https://github.com/alerta/alerta-contrib',
    license='MIT',
    author='Sudhir Bhoga',
    author_email='sudhirbhoga@gmail.com',
    packages=find_packages(),
    py_modules=['alerta_dynatrace'],
    install_requires=[
    ],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.webhooks': [
            'dynatrace = alerta_dynatrace:DynatraceWebhook'
        ]
    }
)
