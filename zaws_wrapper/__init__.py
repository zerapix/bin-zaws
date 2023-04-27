from zsetup import setup_with_pkg_name

__version__ = '1.0.0'


setup_with_pkg_name(__name__, 'zaws')


def wrapper_main():
    from zaws import main
    main()
