from setuptools import find_packages, setup

setup(
    name="lifeguard-rabbitmq",
    version="0.0.1",
    url="https://github.com/LifeguardSystem/lifeguard-rabbitmq",
    author="Diego Rubin",
    author_email="contact@diegorubin.dev",
    license="GPL2",
    scripts=[],
    include_package_data=True,
    description="Lifeguard integration with RabbitMQ",
    install_requires=["lifeguard==0.0.15"],
    classifiers=["Development Status :: 3 - Alpha"],
    packages=find_packages(),
)