# -*- coding: utf-8 -*-
# @Author: A05599
# @Date:   2019-11-20 16:50:39
# @Last Modified by:   A05599
# @Last Modified time: 2019-11-20 17:34:59
"""
功能：下载指定文件内的所有的http file
"""
# https://goldsmr5.gesdisc.eosdis.nasa.gov/cgi-bin/OTF/HTTP_DpFileDownloadMERRA2.pl?DATASET=MERRA_DP&FCP_DIR=/ftp/private/tmp/&APPLICATION=SUBSET_MERRA2&FILTER=SUBSET_MERRA2&SUB_LONMIN=113.6907&SUB_LONMAX=113.7604&SUB_LATMAX=22.1747&SUB_LATMIN=22.0858&OUTPUT_FORMAT=nc4&LOOKUPID_List=M2I3NPASM&STARTYR=2019&STARTMON=10&STARTDAY=14&ENDYR=2019&ENDMON=11&ENDDAY=31&PREGRID=NONE
import requests

def read_file():
	urls = []
	with open('mydat.txt') as f:
		for i in f.readlines():
			urls.append(i.strip('\n'))
		return urls


def craw():
	urls = read_file()
	# print(urls)
	headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'Accept-Encoding': 'gzip, deflate, br',
	'Connection': 'keep-alive',
	'Host': 'goldsmr5.gesdisc.eosdis.nasa.gov',
	'Referer': 'https://disc.gsfc.nasa.gov/daac-bin/FTPSubset2.pl'
	}
	data = {
	'username': '',
	'password': ''
	}
	session = requests.session()
	req = session.post(url=urls[0], data=data, headers=headers)
	print(req.status_code)


if __name__ == '__main__':
	craw()

# class SessionWithHeaderRedirection(requests.Session):
 
#     AUTH_HOST = 'urs.earthdata.nasa.gov'
 
#     def __init__(self, username, password):
 
#         super().__init__()
 
#         self.auth = (username, password)
 
  
 
#    # Overrides from the library to keep headers when redirected to or from
 
#    # the NASA auth host.
 
#     def rebuild_auth(self, prepared_request, response):
 
#         headers = prepared_request.headers
 
#         url = prepared_request.url
 
  
 
#         if 'Authorization' in headers:
 
#             original_parsed = requests.utils.urlparse(response.request.url)
 
#             redirect_parsed = requests.utils.urlparse(url)
 
  
 
#             if (original_parsed.hostname != redirect_parsed.hostname) and \
 
#                     redirect_parsed.hostname != self.AUTH_HOST and \
 
#                     original_parsed.hostname != self.AUTH_HOST:
 
#                 del headers['Authorization']
 
  
 
#         return
 
  
 
# # create session with the user credentials that will be used to authenticate access to the data
 
# username = ""
 
# password= ""
 
# session = SessionWithHeaderRedirection(username, password)
 
  
 
# # the url of the file we wish to retrieve
 
# url = "https://goldsmr5.gesdisc.eosdis.nasa.gov/daac-bin/OTF/HTTP_services.cgi?FILENAME=%2Fdata%2FMERRA2%2FM2I3NPASM.5.12.4%2F2018%2F06%2FMERRA2_400.inst3_3d_asm_Np.20180601.nc4&FORMAT=nc4%2F&BBOX=22.0858%2C113.6907%2C22.1747%2C113.7604&LABEL=MERRA2_400.inst3_3d_asm_Np.20180601.SUB.nc&SHORTNAME=M2I3NPASM&SERVICE=SUBSET_MERRA2&VERSION=1.02&LAYERS=&VARIABLES="
 
  
 
# # extract the filename from the url to be used when saving the file
 
# filename = url.split('&')[3].split('=')[-1]
 
  
 
# try:
 
#     # submit the request using the session
 
#     response = session.get(url, stream=True)
 
#     print(response.status_code)
 
  
 
#     # raise an exception in case of http errors
 
#     response.raise_for_status()  
 
  
 
#     # save the file
 
#     with open(filename, 'wb') as fd:
#         for chunk in response.iter_content(chunk_size=1024*1024):
#             fd.write(chunk)
 
  
 
# except requests.exceptions.HTTPError as e:
 
#     # handle any errors here
 
#     print(e)
