USER_AGENT = {
    'firefox': ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'],
    'chrome': ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'],
}


def select_random_usr_agent():
    import random
    browser = random.choice(list(USER_AGENT.keys()))
    return random.choice(USER_AGENT[browser])
