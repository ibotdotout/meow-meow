from mako.lookup import TemplateLookup

mako_lookup = TemplateLookup(directories=['meow_meow/templates'],
                             module_directory='/tmp/mako_modules',
                             input_encoding='utf-8')
