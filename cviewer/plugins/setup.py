def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('plugins', parent_package, top_path)

    config.add_subpackage('bindings')
    config.add_subpackage('cff2')
    config.add_subpackage('codeoracle')
    config.add_subpackage('text_editor')
    config.add_subpackage('ui')
    config.add_subpackage('nbs')
    config.add_subpackage('cmp')

    config.add_data_files('ui/preferences.ini')

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
