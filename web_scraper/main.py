import requests
import time
import json
import datetime

def extract(date_tuple):
	start_date = date_tuple[0]
	end_date = date_tuple[1]
	start_date = str(int(time.mktime(datetime.datetime.strptime(start_date, "%m/%d/%Y").timetuple()))) + "000"
	end_date = str(int(time.mktime(datetime.datetime.strptime(end_date, "%m/%d/%Y").timetuple()))) + "000"
	print("Start Date {}".format(start_date))
	print("End Date {}".format(end_date))

	url = "http://communitycrimemap.com/Protected/RAIDS/Data/DataGrid.serv"

	payload = "start=0&limit=500&sort=view62&dir=DESC&dataView=%7B%22modes%22%3A%5B%7B%22id%22%3A1%7D%5D%2C%22endDate%22%3A{}%2C%22centerLon%22%3A-73.69178509999999%2C%22pageSize%22%3Anull%2C%22limitBy%22%3A500%2C%22analytics%22%3A%5B%7B%22width%22%3A0%2C%22id%22%3A3%2C%22position%22%3A1%2C%22height%22%3A0%7D%2C%7B%22width%22%3A0%2C%22id%22%3A50%2C%22position%22%3A2%2C%22height%22%3A0%7D%2C%7B%22width%22%3A0%2C%22id%22%3A59%2C%22position%22%3A3%2C%22height%22%3A0%7D%2C%7B%22width%22%3A0%2C%22id%22%3A74%2C%22position%22%3A4%2C%22height%22%3A0%7D%5D%2C%22dataRelation%22%3A%22Primary%22%2C%22gridStatStamp%22%3Anull%2C%22pageStart%22%3Anull%2C%22keywordOption%22%3A%22notes%22%2C%22zoom%22%3A14%2C%22filters%22%3A%5B%5D%2C%22viewAttributeVersion%22%3A0%2C%22viewIteration%22%3A10%2C%22polygon%22%3A%7B%22valid%22%3Atrue%2C%22minLon%22%3A-73.71616101552735%2C%22maxLat%22%3A42.74458175118046%2C%22centroid%22%3A%7B%22x%22%3A-73.6917851%2C%22y%22%3A42.728409591806056%2C%22class%22%3A%22com.bairinc.raids.model.dataview.polygon.RaidsPolygon%24Point%22%7D%2C%22minLat%22%3A42.71223743243165%2C%22centerLon%22%3A-73.6917851%2C%22maxLon%22%3A-73.66740918447266%2C%22alias%22%3A%22box%22%2C%22centerLat%22%3A42.728409591806056%2C%22draw%22%3Afalse%7D%2C%22sortingClause%22%3A%5B%7B%22pos%22%3A0%2C%22attribute%22%3A%7B%22mode%22%3A%7B%22timeComparisonSupported%22%3Atrue%2C%22classificationGroupName%22%3Anull%2C%22display%22%3A%22Event%22%2C%22relational%22%3Afalse%2C%22id%22%3A1%2C%22customClassificationProcessor%22%3Afalse%7D%2C%22viewId%22%3A%22view62%22%2C%22displayName%22%3A%22Date%22%2C%22dataViewName%22%3A%22Date%22%2C%22id%22%3A62%2C%22hpccWildCardSupport%22%3Afalse%2C%22derived%22%3Afalse%7D%2C%22order%22%3Afalse%7D%5D%2C%22dataViewName%22%3A%22grid%22%2C%22singleMode%22%3Anull%2C%22centerLat%22%3A42.7284117%2C%22page%22%3A%5B%7B%22mode%22%3A%7B%22classificationGroupName%22%3Anull%2C%22customClassificationProcessor%22%3Afalse%2C%22display%22%3A%22Event%22%2C%22id%22%3A1%2C%22relational%22%3Afalse%2C%22timeComparisonSupported%22%3Atrue%7D%2C%22page%22%3A0%2C%22pageCount%22%3A0%2C%22pageSize%22%3A20%2C%22recordCount%22%3A0%7D%2C%7B%22mode%22%3A%7B%22classificationGroupName%22%3Anull%2C%22customClassificationProcessor%22%3Afalse%2C%22display%22%3A%22Offenders%22%2C%22id%22%3A3%2C%22relational%22%3Afalse%2C%22timeComparisonSupported%22%3Atrue%7D%2C%22page%22%3A0%2C%22pageCount%22%3A0%2C%22pageSize%22%3A1%2C%22recordCount%22%3A0%7D%5D%2C%22user%22%3A%7B%22firstName%22%3Anull%2C%22lastName%22%3Anull%2C%22roles%22%3A%5B%7B%22productId%22%3Anull%2C%22name%22%3A%22user%22%7D%5D%2C%22dataProviderId%22%3A-1%2C%22userID%22%3A-1%2C%22email%22%3A%22public%40communitycrimemap.com%22%2C%22singleSignOnEntityId%22%3Anull%7D%2C%22filterIterator%22%3A%7B%7D%2C%22startDate%22%3A{}%2C%22classfications%22%3A%5B%7B%22mode%22%3A%7B%22id%22%3A1%7D%2C%22id%22%3A8%7D%2C%7B%22mode%22%3A%7B%22id%22%3A1%7D%2C%22id%22%3A18%7D%2C%7B%22mode%22%3A%7B%22id%22%3A1%7D%2C%22id%22%3A10%7D%2C%7B%22mode%22%3A%7B%22id%22%3A1%7D%2C%22id%22%3A11%7D%2C%7B%22mode%22%3A%7B%22id%22%3A1%7D%2C%22id%22%3A1%7D%2C%7B%22mode%22%3A%7B%22id%22%3A1%7D%2C%22id%22%3A16%7D%2C%7B%22mode%22%3A%7B%22id%22%3A1%7D%2C%22id%22%3A6%7D%2C%7B%22mode%22%3A%7B%22id%22%3A1%7D%2C%22id%22%3A7%7D%2C%7B%22mode%22%3A%7B%22id%22%3A1%7D%2C%22id%22%3A4%7D%2C%7B%22mode%22%3A%7B%22id%22%3A1%7D%2C%22id%22%3A12%7D%5D%2C%22primary%22%3Atrue%7D&searchOptions=notes&searchTerms=&mode=1".format(end_date,start_date)
	headers = {
		'Accept': "*/*",
		'Accept-Encoding': "gzip, deflate, br",
		'Accept-Language': "en-US,en;q=0.9",
		'Connection': "keep-alive",
		'Content-Length': "3451",
		'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
		'Cookie': "ys-announcement=b%3A1; ys-terms=b%3A1; __utmc=153880490; JSESSIONID=E2839C24C8CD9DF2DF3F1CFC944C86C8.APP102; __utma=153880490.53914170.1569206734.1569532178.1569553252.12; __utmz=153880490.1569553252.12.6.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=153880490.8.8.1569553287048, ys-announcement=b%3A1; ys-terms=b%3A1; __utmc=153880490; JSESSIONID=E2839C24C8CD9DF2DF3F1CFC944C86C8.APP102; __utma=153880490.53914170.1569206734.1569532178.1569553252.12; __utmz=153880490.1569553252.12.6.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=153880490.8.8.1569553287048; JSESSIONID=6EE2CDFFE6792B9D65FACCBA18534C29.APP102",
		'Host': "communitycrimemap.com",
		'nonce': "-2311282226219886181",
		'Origin': "https://communitycrimemap.com",
		'Referer': "https://communitycrimemap.com/",
		'Sec-Fetch-Mode': "cors",
		'Sec-Fetch-Site': "same-origin",
		'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
		'X-Requested-With': "XMLHttpRequest",
		'Cache-Control': "no-cache",
		'Postman-Token': "68a34902-9667-492a-9501-4cd78291c368,89621dc0-d887-4f41-b87c-02e27cb036ac",
		'cache-control': "no-cache"
		}

	response = requests.request("POST", url, data=payload, headers=headers)
	with open('../crime_data/data_{}_{}.json'.format(start_date,end_date), 'w') as f:
		json.dump(response.text, f)
	print(response.text)

def main():
	dates = [
			('01/01/2013','03/31/2013'), #2013
			('04/01/2013','06/30/2013'),
			('07/01/2013','09/30/2013'),
			('10/01/2013','12/31/2013'),
			('01/01/2014','03/31/2014'), #2014
			('04/01/2014','06/30/2014'),
			('07/01/2014','09/30/2014'),
			('10/01/2014','12/31/2014'),
			('01/01/2015','03/31/2015'), #2015
			('04/01/2015','06/30/2015'),
			('07/01/2015','09/30/2015'),
			('10/01/2015','12/31/2015'),
			('01/01/2016','03/31/2016'), #2016
			('04/01/2016','06/30/2016'),
			('07/01/2016','09/30/2016'),
			('10/01/2016','12/31/2016'),
			('01/01/2017','03/31/2017'), #2017
			('04/01/2017','06/30/2017'),
			('07/01/2017','09/30/2017'),
			('10/01/2017','12/31/2017'),
			('01/01/2018','03/31/2018'), #2018
			('04/01/2018','06/30/2018'),
			('07/01/2018','09/30/2018'),
			('10/01/2018','12/31/2018'),
			]
	for date_tuple in dates:
		extract(date_tuple)

if __name__ == '__main__':
	main()