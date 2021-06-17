from setuptools import setup, find_packages

version = '0.0.7'

setup(
    name="alerta-kibana",
    version=version,
    description='Alerta webhook for kibana',
    url='https://github.com/alerta/alerta-contrib',
    license='MIT',
    author='Sudhir Bhoga',
    author_email='sudhirbhoga@gmail.com',
    packages=find_packages(),
    py_modules=['alerta_kibana'],
    install_requires=[
    ],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.webhooks': [
            'kibana = alerta_kibana:kibanaWebhook'
        ]
    }
)
