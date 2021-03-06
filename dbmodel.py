from google.appengine.ext import db
import datetime

class AuthToken(db.Model):
    """Representation of a stored authid"""
    user_id = db.StringProperty(required=True)
    blob = db.TextProperty(required=True)
    expires = db.DateTimeProperty(required=True)
    service = db.StringProperty(required=True)

class FetchToken(db.Model):
    """Representation of a stored fetch token"""
    authid = db.StringProperty(required=False)
    token = db.StringProperty(required=True)
    expires = db.DateTimeProperty(required=True)
    fetched = db.BooleanProperty(required=True)

class StateToken(db.Model):
    """Representation of a stored state token"""
    service = db.StringProperty(required=True)
    expires = db.DateTimeProperty(required=True)
    fetchtoken = db.StringProperty(required=False)


@db.transactional(xg=True)
def create_fetch_token(fetchtoken):
    # A fetch token stays active for 30 minutes
    if fetchtoken != None and fetchtoken != '':
        e = FetchToken.get_by_key_name(fetchtoken)
        if e == None:
            FetchToken(key_name=fetchtoken, token=fetchtoken, fetched=False, expires=datetime.datetime.utcnow() + datetime.timedelta(minutes=5)).put()

@db.transactional(xg=True)
def update_fetch_token(fetchtoken, authid):
    if fetchtoken != None and fetchtoken != '':
        e = FetchToken.get_by_key_name(fetchtoken)
        if e != None:
            e.expires = datetime.datetime.utcnow() + datetime.timedelta(seconds=30)
            e.authid = authid
            e.fetched = False
            e.put()

@db.transactional
def insert_new_authtoken(keyid, user_id, blob, expires, service):
    entry = AuthToken.get_by_key_name(keyid)
    if entry == None:
        
        entry = AuthToken(key_name=keyid, user_id=user_id, blob=blob, expires=expires, service=service)
        entry.put()

        return entry
    else:
        return None

@db.transactional(xg=True)
def insert_new_statetoken(token, service, fetchtoken):
    entry = StateToken.get_by_key_name(token)
    if entry == None:
        
        entry = StateToken(key_name=token, service=service, fetchtoken=fetchtoken, expires=datetime.datetime.utcnow() + datetime.timedelta(minutes=5))
        entry.put()

        return entry
    else:
        return None

