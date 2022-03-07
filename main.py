import requests


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[ip]': response.get('query'),
            '[int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }
        return data
        # print(response)
    except requests.exceptions.ConnectionError:
        print('Please check your connection!')


def main():
    ip = input('Please inter a target ip:')
    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()

