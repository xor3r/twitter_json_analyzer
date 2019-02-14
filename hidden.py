def oauth():
    f = open('KEYS.txt', 'r', encoding='utf-8', errors='ignore')
    keys = [line.strip() for line in f.readlines()]
    consumer_key, consumer_secret, token_key, token_secret = keys[:]

    return {"consumer_key": consumer_key,
            "consumer_secret": consumer_secret,
            "token_key": token_key,
            "token_secret": token_secret}

oauth()