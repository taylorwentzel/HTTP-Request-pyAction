import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    payload = {'name':'Kit Plummer', 'username': 'kitplummer'}
    r = requests.post('https://ghatracker.herokuapp.com/', json=payload)


if __name__ == "__main__":
    main()
