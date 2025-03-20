from setuptools import setup, find_packages

setup(
    name='shopify_app_store_scraper',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'shopify_app_store': ['app_urls.txt'],
    },
)