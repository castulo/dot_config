"""Default configuration values used when generating a new config file

Variables that are between %(option)s are interpolated automatically by the
ConfigParser (with the caveat that they have to be in the same section).

Variables that are between ${section:option} will be interpolated with the
value from the appropriate section (similar to the way configparser from
Python3 works).
"""


def load_defaults(config):
    """All config default values are defined here"""

    # General Section
    config.add_section('general')
    config.set('general', 'log_path', '/home/user/log')

    # Section Example
    config.add_section('section_1')
    config.set('section_1', 'log_path', '${general:log_path}/section_1')
    config.set('section_1', 'log_level', 'debug')
    config.set('section_1', 'endpoint', 'http://{ip}:4040/endpoint')

    # Another Example
    config.add_section('section_2')
    config.set('section_2', 'server', '1.2.3.4')
    config.set('section_2', 'port', '8080')
    config.set('section_2', 'endpoint', 'http://%(server)s:%(port)s/section2')

    # <Add sections here!>

    return config
