from http.cookies import SimpleCookie

URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-87.065294625%2C%22east%22%3A-73.530138375%2C%22south%22%3A23.075306866050514%2C%22north%22%3A28.319490494874934%7D%2C%22mapZoom%22%3A6%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%2C%22sortSelection%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat1%22:[%22mapResults%22]}&requestId=2'


def cookie_parser():
    cookie_string = 'zguid=23|$22559c46-cabc-4274-bf06-7ff067b30965; _ga=GA1.2.143118225.1646304807; _gid=GA1.2.522645553.1646304807; zjs_user_id=null; zg_anonymous_id="0c4b5bbe-198f-44e2-a359-1eb5fad3be06"; zjs_anonymous_id="22559c46-cabc-4274-bf06-7ff067b30965"; _pxvid=28af3bad-9ae0-11ec-bd20-6e487a4d5452; _gcl_au=1.1.1975185807.1646304809; KruxPixel=true; __pdst=86e74f01e4734b4780a3c51d522a2e79; _cs_c=0; _clck=1ou0r2q|1|ezg|0; KruxAddition=true; utag_main=v_id:017f4f69defe004662825eabe93805073001706b0086e$_sn:1$_se:1$_ss:1$_st:1646306612803$ses_id:1646304812803;exp-session$_pn:1;exp-session$dcsyncran:1;exp-session$tdsyncran:1;exp-session$dc_visit:1$dc_event:1;exp-session$dc_region:ap-northeast-1;exp-session$ttd_uuid:374381e3-5b69-492a-ace6-f6c8eee9b986;exp-session; g_state={"i_p":1646312178368,"i_l":1}; zgsession=1|548f2a5b-26f5-4585-ad23-04b19845d5b4; DoubleClickSession=true; _pin_unauth=dWlkPU1XTTBNMkUwTnprdFlUazNaaTAwTkdKaExXSmhNVFV0T0dOaFpXRTBaV1l3TmpFNA; _cs_id=fa2d7034-87c0-a9db-a9bc-7c08ebbabc47.1646304819.2.1646314997.1646314997.1.1680468819455; JSESSIONID=ADA572D7E7AEA16AB97881D9D31516B8; _cs_s=1.5.0.1646316798992; search=6|1648907035550|rect=25.89937666795752%2C-80.08622968359376%2C25.552970176936043%2C-80.50920331640626&rid=12700&disp=map&mdm=auto&p=1&z=1&lt=fsba%2Cfore%2Cnew%2Ccmsn&fs=1&fr=0&mmm=0&rs=0&ah=0&singlestory=0&housing-connector=0&abo=0&garage=0&pool=0&ac=0&waterfront=0&finished=0&unfinished=0&cityview=0&mountainview=0&parkview=0&waterview=0&hoadata=1&zillow-owned=0&3dhome=0&featuredMultiFamilyBuilding=0		12700						; _uetsid=2bbe0e909ae011eca6e385950ff40a2f; _uetvid=2bbe5fc09ae011eca3c1d3676cc5a8a1; AWSALB=1kdt28WW1XJi97mPOpWm5u5Ry7ZM2OgmF8RrU1MrdcKrnnEJwe6BZwyxrAHviR7j7EPH38KVIuvEOd1AO0id49W7Kv/YB/0garn/jn+rBbOg6vslNW+dNN22CwTd; AWSALBCORS=1kdt28WW1XJi97mPOpWm5u5Ry7ZM2OgmF8RrU1MrdcKrnnEJwe6BZwyxrAHviR7j7EPH38KVIuvEOd1AO0id49W7Kv/YB/0garn/jn+rBbOg6vslNW+dNN22CwTd; _px3=757cbf41227db3a053e03227aa018ac914d713b3b578935ab459e48616efd12c:L5i2IDkipp2NP8SEDCy00V3Aiw01Wrwyv/EgFlD/y1jm6FUNEZGDcKycHmNWOU53kemPjfCKR0vG37HW29hgVA==:1000:JH1sjf1gW7RZc/cdK0zDX4rmLdISMdCGBf6NcGlVEu/7obDAFSN/IHmfBFQyGb/N1UhPxzDexMjy46Fy3jQ/xNF5y7AQCPaFwqL6ykb/Kq03ywi3fEArfDS2e9Isuf7kg4bPxCfapaAVylJ/ey/4lLrn9WzmASF8RLE65KM+uPnC6yJ7A3Mu7HwsBMx/g9MJLzhsRsxThUeqyU8cUeEqyA==; _clsk=10z89tk|1646315977983|9|0|i.clarity.ms/collect'
    cookies = {}
    for cookie in cookie_string.split(';'):
        try:
            key = cookie.split('=', 1)[0]
            val = cookie.split('=', 1)[1]
            cookies[key] = val

        except:
            pass
    return cookies



