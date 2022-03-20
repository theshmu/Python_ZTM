import requests
import hashlib
import sys


def request_api_data(query_char):
    """
    If working properly, res.status_code should return a value of 200, otherwise the first 5 characters of the hash
    aren't being sent properly. res returns a file where each line contains one of the matching hashes and the amount
    of times they were pwned separated by ':'.
    """
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    """
    each line in the text file hashes contains a matching hash tail and number of times it was pwned separated by a ':'
    """
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    hashed_pass = hashlib.sha1(password.encode('utf-8'))
    str_hashed_pass = hashed_pass.hexdigest().upper()
    first5_char, tail = str_hashed_pass[0:5], str_hashed_pass[5:]
    response = request_api_data(first5_char)

    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times, you should probably change it.')
        else:
            print(f'{password} was NOT found. NICE!')
    return '-------------- Check complete! --------------'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
