import requests


def craw():
    url = 'https://urs.earthdata.nasa.gov/profile'
    data={'username':'A05599',
          'password':'mywind@A05599',
          'authenticity_token': 'mTVJWMswya1GgShM6uEuk4z/eXl8X5bC+hhvJpb9ySJziNz0l4hg89MV1AuVay2MlcwUHhIuFdiA9AHFnwzPYQ=='}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'urs.earthdata.nasa.gov',
        'Referer': 'https://urs.earthdata.nasa.gov/',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Mobile Safari/537.36',
        # 'Origin': 'https: // urs.earthdata.nasa.gov',
        # 'Sec-Fetch-Mode': 'navigate',
        # 'Sec-Fetch-Site': 'same-origin',
        # 'Sec-Fetch-User': '?1',
        # 'Upgrade-Insecure-Requests': '1'
        'cookie': '_ga=GA1.2.965509429.1574246811; _gid=GA1.2.621293350.1574246811; nasa_gesdisc_data_archive=fIE3xQ+RQWKF24HpOkj3BOVaMYf8DQcvreN0mAQUinWkpruX00Vywizf2cmh2+jOYi4fMEFfXuaxQD5dntR3gRsfbOIwXuvYZYUyVESBphcgV4LdCRSS0uYKVochqJex; _ga=GA1.4.965509429.1574246811; _gid=GA1.4.621293350.1574246811; _gat_UA-62340125-2=1; _urs-gui_session=b07a11b7f96ea0ea469f9a5ed2fcf715; _gat_GSA_ENOR0=1; urs_user_already_logged=yes'
    }
    s = requests.session()
    # r = s.post(url, data=data, headers=headers)
    r = s.get(url, headers=headers)
    print(r.status_code)
    # with open('x.html','w')as f:f.write(r.text)
    urls = read_file()
    # st = s.get(urls[0])
    # print(st.status_code)
    # print(st.text)
    for item in urls:
        name = item.split('&')[3].split('=')[-1]
        req = s.get(item)
        if req.status_code == 200:
            with open(name,'w')as f:
                f.write(req.text)
        print(f'{name} write ok!')


def read_file():
    urls = []
    with open('mydat.txt') as f:
        for i in f.readlines():
            urls.append(i.strip('\n'))
        return urls


if __name__ == '__main__':
    craw()