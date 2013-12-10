# ANSI escape sequences for several colors
class Colors:
  """"Model to encapsulate colors for use in messaging"""
  END           = '\033[0m'

  # Formatting options
  BOLD          = '\033[1m'
  ITALIC        = '\033[3m'
  UNDERLINE     = '\033[4m'

  # Text colors
  TEXTBLACK     = '\033[30m'
  TEXTRED       = '\033[31m'
  TEXTGREEN     = '\033[32m'
  TEXTYELLOW    = '\033[33m'
  TEXTBLUE      = '\033[34m'

  # Background colors
  BACKBLACK     = '\033[40m'
  BACKRED       = '\033[41m'
  BACKGREEN     = '\033[42m'
  BACKELLOW     = '\033[43m'
  BACKLUE       = '\033[44m'
  BACKYAN       = '\033[46m'
