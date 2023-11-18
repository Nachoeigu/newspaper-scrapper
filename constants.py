import json

HEADERS_TN = {
    'authority': 'tn.com.ar',
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.6',
    'cache-control': 'max-age=0',
    'if-modified-since': '1700317380698',
    'referer': 'https://tn.com.ar/ultimas-noticias',
    'sec-ch-ua': '"Brave";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

PARAMS_TN = {
    'query': '{"feed_offset":0,"feed_query":"subtype:article+AND+source.source_type:staff","imageSizes":["small"],"page":N_PAGE,"size":20}',
    'filter': '{content_elements{credits{by{_id,name,type}},description{basic},display_date,headlines{basic,mobile},promo_items{basic{caption,content_elements{caption,resized_urls{small}},embed{config{created,is_live_content,resized_urls{small}},id},resized_urls{small},subtype,type}},subheadlines{basic},taxonomy{tags{text}},type,website_url},count,next}',
    'd': '446',
    '_website': 'tn',
}
TN_ENDPOINT = 'https://tn.com.ar/pf/api/v3/content/fetch/content-feed'
TN_URL = 'https://tn.com.ar'

HEADERS_INFOBAE = {
    'authority': 'www.infobae.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-GB,en;q=0.8',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Sat, 18 Nov 2023 15:15:46 GMT',
    'if-none-match': 'W/"1c935a-gyVCEq2DM+t3oIEF1KzDnwU4D4k"',
    'sec-ch-ua': '"Brave";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}
INFOBAE_ENDPOINT = 'https://www.infobae.com/ultimas-noticias/'
INFOBAE_URL = 'https://www.infobae.com'

HEADERS_LANACION = {
    'authority': 'www.lanacion.com.ar',
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.6',
    'referer': 'https://www.lanacion.com.ar/ultimas-noticias/',
    'sec-ch-ua': '"Brave";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

PARAMS_LANACION = {
    'query': json.dumps({
            "authorId": None,
            "excludePreload": False,
            "excludeSectionId": False,
            "hasCollectionApertura": False,
            "imageConfig": "boxArticles",
            "page": 'N_PAGE',
            "promoItemsOnly": False,
            "sectionId": None,
            "sectionsIds": "(\"/economia\",\"/sociedad\",\"/deportes\",\"/politica\",\"/espectaculos\",\"/el-mundo\",\"/tecnologia\",\"/propiedades\",\"/dolar-hoy\",\"/buenos-aires\",\"/seguridad\",\"/educacion\",\"/cultura\",\"/salud\",\"/ciencia\",\"\")",
            "shouldNotFilter": False,
            "size": 30,
            "sourceOrigin": "composer",
            "type": "",
            "website": "la-nacion-ar"
        }),
    'filter': json.dumps({
        "_id": 1,
        "content_elements": {
            "_id": 1,
            "content_elements": {"content": 1, "type": 1},
            "content_restrictions": {"content_code": 1},
            "credits": {"by": {"_id": 1, "additional_properties": {"original": {"image": 1}}, "image": {"resized_urls": {"height": 1, "option": {"class": 1, "configPixelRatio": {"forScreenWidth": 1, "xDescriptor": 1}, "height": 1, "maxScreenWidth": 1, "media": 1, "media_preload": 1, "minScreenWidth": 1, "proportion": 1, "type": 1, "width": 1}, "resizedUrl": 1, "width": 1}, "url": 1}, "name": 1, "slug": 1, "type": 1}},
        "display_date": 1,
        "headlines": {"basic": 1, "mobile": 1},
        "label": {"chapita": {"display": 1, "text": 1}, "enviar_a_apps": {"text": 1}, "recomendar": {"text": 1}, "volanta": {"display": 1, "text": 1}},
        "marquesina": 1,
        "owner": {"sponsored": 1},
        "promo_items": {"basic": {"height": 1, "resized_urls": {"height": 1, "option": {"class": 1, "configPixelRatio": {"forScreenWidth": 1, "xDescriptor": 1}, "height": 1, "maxScreenWidth": 1, "media": 1, "media_preload": 1, "minScreenWidth": 1, "proportion": 1, "type": 1, "width": 1}, "resizedUrl": 1, "width": 1}, "subtitle": 1, "type": 1, "url": 1, "width": 1}},
        "publish_date": 1,
        "related_content": {"basic": {"_id": 1, "referent": {"type": 1}, "type": 1}},
        "subheadlines": {"basic": 1},
        "subtype": 1,
        "taxonomy": {"primary_section": {"_id": 1, "additional_properties": {"original": {"style": {"section_style_name": 1}}}, "name": 1, "path": 1}, "tags": {"slug": 1, "text": 1}},
        "website_url": 1
    }}),
    'd': '1381',
    '_website': 'la-nacion-ar'
}

LANACION_ENDPOINT = 'https://www.lanacion.com.ar/pf/api/v3/content/fetch/acuArticlesSource'
LANACION_URL = 'https://www.lanacion.com.ar'



