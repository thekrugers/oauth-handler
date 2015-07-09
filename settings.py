
#############################################
#                                           #
#     DO NOT CHANGE THIS FILE !!!!!!        #
#                                           #
# You must copy the file config-template.py #
# to config.py and edit that instead        #
#                                           #
#############################################


TESTING = False

APP_DOMAIN='change-me-in-config-py.appspot.com'
APP_NAME = 'CHANGE-ME-IN-CONFIG.PY'
SERVICE_DISPLAYNAME = APP_NAME + ' OAuth Handler'
WL_CLIENT_ID='XXXXXXXXXXXXXXXXXXXX'
WL_CLIENT_SECRET='XXXXXXXXXXXXXXXXXXXX'
GD_CLIENT_ID='XXXXXXXXXXXXXXXXXXXX'
GD_CLIENT_SECRET='XXXXXXXXXXXXXXXXXXXX'
HC_CLIENT_ID='XXXXXXXXXXXXXXXXXXXX'
HC_CLIENT_SECRET='XXXXXXXXXXXXXXXXXXXX'


try:
    from config import WL_CLIENT_ID
    from config import WL_CLIENT_SECRET
except ImportError:
    pass

try:
    from config import GD_CLIENT_ID
    from config import GD_CLIENT_SECRET
except ImportError:
    pass

try:
    from config import HC_CLIENT_ID
    from config import HC_CLIENT_SECRET
except ImportError:
    pass

try:
    from config import APP_DOMAIN
except ImportError:
    pass

try:
    from config import APP_NAME
except ImportError:
    pass

try:
    from config import SERVICE_DISPLAYNAME
except ImportError:
    pass

try:
    from config import TESTING
except ImportError:
    pass

OAUTH_CALLBACK_URI = 'https://' + APP_DOMAIN + '/logged-in'

try:
    from config import OAUTH_CALLBACK_URI
except ImportError:
    pass


WL_REDIRECT_URI=OAUTH_CALLBACK_URI
WL_AUTH_URL='https://login.live.com/oauth20_token.srf'
WL_LOGIN_URL='https://login.live.com/oauth20_authorize.srf'

GD_REDIRECT_URI=OAUTH_CALLBACK_URI
GD_AUTH_URL='https://www.googleapis.com/oauth2/v3/token'
GD_LOGIN_URL='https://accounts.google.com/o/oauth2/auth'

HC_REDIRECT_URI=OAUTH_CALLBACK_URI
HC_AUTH_URL='https://api.hubic.com/oauth/token/'
HC_LOGIN_URL='https://api.hubic.com/oauth/auth/'




LOOKUP = {
    'wl' : {
        'display': 'Windows Live',
        'client-id': WL_CLIENT_ID,
        'client-secret': WL_CLIENT_SECRET,
        'redirect-uri': WL_REDIRECT_URI,
        'auth-url': WL_AUTH_URL,
        'login-url': WL_LOGIN_URL
    },

    'gd' : {
        'display': 'Google',
        'client-id': GD_CLIENT_ID,
        'client-secret': GD_CLIENT_SECRET,
        'redirect-uri': GD_REDIRECT_URI,
        'auth-url': GD_AUTH_URL,
        'login-url': GD_LOGIN_URL
    },

    'hc' : {
        'display': 'HubiC',
        'client-id': HC_CLIENT_ID,
        'client-secret': HC_CLIENT_SECRET,
        'redirect-uri': HC_REDIRECT_URI,
        'auth-url': HC_AUTH_URL,
        'login-url': HC_LOGIN_URL
    }
}

SERVICES = [
    {
        'display': 'Microsoft OneDrive',
        'type': 'wl',
        'id': 'onedrive',
        'scope': 'wl.offline_access wl.skydrive_update wl.skydrive',
        'servicelink': 'https://onedrive.live.com',
        'notes': '<p style="font-size: small">By using the OAuth login service for OneDrive you agree to the <a href="http://explore.live.com/microsoft-service-agreement" target="_blank">Microsoft Service Agreement</a> and <a href="http://privacy.microsoft.com/en-us/fullnotice.mspx" target="_blank">Microsoft Online Privacy Statement</a></p>'
    },
    {
        'display': 'Google Drive',
        'type': 'gd',
        'id': 'googledrive',
        'scope': 'https://www.googleapis.com/auth/drive.file',
        'extraurl': 'access_type=offline&approval_prompt=force',
        'servicelink': 'https://drive.google.com'
    },
    {
        'display': 'Google Docs',
        'type': 'gd',
        'id': 'googledocs',
        'scope': 'https://www.googleapis.com/auth/drive',
        'extraurl': 'access_type=offline&approval_prompt=force',
        'servicelink': 'https://drive.google.com'
    },
    {
        'display': 'Google Cloud Storage',
        'type': 'gd',
        'id': 'gcs',
        'scope': 'https://www.googleapis.com/auth/devstorage.read_write',
        'extraurl': 'access_type=offline&approval_prompt=force',
        'servicelink': 'https://cloud.google.com/storage/'
    },
    {
        'display': 'HubiC',
        'type': 'hc',
        'id': 'hubic',
        'scope': 'credentials.r',
        'servicelink': 'https://hubic.com'
    }
]


