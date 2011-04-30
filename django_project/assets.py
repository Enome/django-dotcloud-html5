from django_assets import Bundle, register

################
# STYLESHEETS #
##############

#libraries
nine_sixty =        Bundle('styles/libs/960.css')
handheld =          Bundle('styles/libs/handheld.css')
html5_boilerplate = Bundle('styles/libs/reset_defaults.css')

lib_combined = Bundle( nine_sixty, html5_boilerplate )

#Project
main = Bundle('styles/tags.sass',
              'styles/general.sass',
              filters='sass')

stylesheets = Bundle( lib_combined,
                      main,
                      filters='cssmin',
                      output='combined/styles/main.css')

register('stylesheets', stylesheets)

###############
# JAVASCRIPT #
#############

#Libraries

