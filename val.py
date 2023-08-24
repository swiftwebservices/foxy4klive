import uuid

TRIAL_KEY_: str = f'{uuid.uuid4()}'


class Val:
    DB_URI: str = "mysql+pymysql://bpsocksapp:appasp.net787912@45.79.227.90:3306/cid"
    HUB_URL: str = 'http://198.20.177.47:8000/'
    TRIAL_KEY: str = TRIAL_KEY_
