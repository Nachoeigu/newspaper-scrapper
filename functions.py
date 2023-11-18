import requests
import json
from datetime import datetime, timezone
import re
import pandas as pd
from constants import TN_ENDPOINT, TN_URL, INFOBAE_ENDPOINT, INFOBAE_URL, LANACION_ENDPOINT, LANACION_URL

def get_notes(session, media):
    if media == 'tn':
        url = TN_ENDPOINT
        final_url = TN_URL
    elif media == 'infobae':
        url = INFOBAE_ENDPOINT
        final_url = INFOBAE_URL
    elif media == 'lanacion':
        url = LANACION_ENDPOINT
        final_url = LANACION_URL
    
    response = session.get(url)
    if media in ['tn','lanacion']:
        notes = json.loads(response.content)['content_elements']
    else:
        data = response.content.decode('utf-8')
        notes = json.loads(data.split(',"feed-list":{')[-1].split('most-read-d23')[0].split('content_elements')[1].split('expires')[0][2:-3]) 

    rows = []
    old_news = 0
    for note in notes:
        if media in ['tn', 'lanacion']:
            date = note['display_date']
            subheadline = note['subheadlines']['basic']
            
        elif media == 'infobae':
            date = note['last_updated_date']
            subheadline = note['description']['basic']
            
        if is_from_today(date) == False:
            old_news = 1
            break
            
        row = {
                'title': note['headlines']['basic'],
                'subheadline': subheadline,
                'published': date,
                'url':  final_url + note['website_url']
        }
        rows.append(row)
      
    df = pd.DataFrame(rows)
    
    if old_news == 0:
        return (df, True)
    else:
        return (df, False)
    
    
def is_from_today(date_str):
    date_obj = datetime.fromisoformat(date_str.replace("Z", "+00:00"))

    now = datetime.now(timezone.utc)

    return date_obj.date() == now.date()