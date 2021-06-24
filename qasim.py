import requests
from bs4 import BeautifulSoup
import random
from time import sleep
import time
import telebot

bot = telebot.TeleBot("1634595282:AAEjNiHoPjV0uRfJi4Qbd_8TQBAz3zo6pV8")


@bot.message_handler(commands=['start'])
def welcome_help(message):
    bot.send_message(message.chat.id, 'admin @Qissm22')


@bot.message_handler(content_types=['text'])
def send_document(message):
    if message.chat.type == 'supergroup':
        if ('https://www.chegg.com/my/account') in message.text or ('https://www.chegg.com/search') in message.text:
            bot.send_message(message.chat.id, 'الرجاء قم بارسال رابط السؤال بصورة صحيحة',
                             reply_to_message_id=message.message_id)
        elif 'chapter' in message.text:
            bot.send_message(message.chat.id, 'اجابات المصادر غير موجودةSources not available',
                             reply_to_message_id=message.message_id)
        elif message.text.startswith("https://www.chegg.com/homework-help/questions-and-answers/") or message.text.startswith("https://www.chegg.com/homework-help/"):
            url = message.text
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'cookie': 'C=0; O=0; V=40284a92b7d730815a548f54d744590660989fc27589f2.18718116; usprivacy=1YNY; _pxvid=aa6c9a9e-b13a-11eb-9f58-0242ac120009; _omappvp=JJqCeJ9EuvA5F93I1JecvNvOez2tx5qeIZl2wcX0GAbJlixUzlLGiLI0vkY1IYHYnVnSPfcPOicslTZOOKNsC5CgrMMJczie; adobeujs-optin=%7B%22aam%22%3Atrue%2C%22adcloud%22%3Atrue%2C%22aa%22%3Atrue%2C%22campaign%22%3Atrue%2C%22ecid%22%3Atrue%2C%22livefyre%22%3Atrue%2C%22target%22%3Atrue%2C%22mediaaa%22%3Atrue%7D; s_ecid=MCMID%7C83597856594541360060557814214213396744; _ga=GA1.2.680442464.1620615110; _scid=a22a9fa3-9d1e-40a9-a101-73038ea415c8; _rdt_uuid=1620615110618.887e279e-3cff-46c5-aa74-49c921b910f7; _fbp=fb.1.1620615111105.79295125; _gcl_au=1.1.839235490.1620615111; optimizelyEndUserId=oeu1620615175475r0.1442633774958626; __gads=ID=01da3ec73d6ef144:T=1620615181:S=ALNI_MaR_e59_Aq4soxWqsI3kkS7OpOA5g; _cs_c=1; sbm_dma=0; sbm_country=IQ; _ym_uid=1621337530255138749; _ym_d=1621337530; _vid=CsGUfEs7h9JPk2P3MiqY; DFID=web|CsGUfEs7h9JPk2P3MiqY; sourceTracking=adobe; chgcsdmtoken=%7B%22user_uuid%22%3A%223e8ada61-f9de-428c-9e0f-ea20289f2307%22%2C%22created_date%22%3A%222021-05-22T11%3A07%3A48.053Z%22%2C%22account_sharing_device_management%22%3A1%7D; omSeen-tgjg3ieouzbhy6fc0ctw=1622367008723; _cs_id=b2fe01fd-4c69-adcc-e937-b690ab1b811c.1620615206.7.1622449309.1622449309.1.1654779206894.Lax.0; __CT_Data=gpv=15&ckp=tld&dm=chegg.com&apv_79_www33=15&cpv_79_www33=15; _gid=GA1.2.1076720400.1622568318; __ssid=1bac04c43bede1a0f4fa750af09354d; _sctr=1|1622581200000; _ym_isad=1; intlPaQExitIntentModal=hide; user_geo_location=%7B%22country_iso_code%22%3A%22IQ%22%2C%22country_name%22%3A%22Iraq%22%2C%22region%22%3A%22BG%22%2C%22region_full%22%3A%22Baghdad%22%2C%22city_name%22%3A%22Baghdad%22%2C%22locale%22%3A%7B%22localeCode%22%3A%5B%22ar-IQ%22%5D%7D%7D; AMCVS_3FE7CBC1556605A77F000101%40AdobeOrg=1; _gd1622651046268=1; al_cell=2021-6-2-wt-main-1-control; BIBSESSID=9b080df2-6565-4aa3-9391-a6336f3661c6; CVID=01d774a0-9199-416b-a2e3-925acaa9f9d4; mcid=83597856594541360060557814214213396744; CSID=1622651047107; schoolapi=null; PHPSESSID=ttjpqp6br6bfflsnpbaah445uq; CSessionID=ebdda520-5dce-4489-9215-877e009ad629; _gd1622651066328=1; forterToken=68c9cf61a25d42b9b490387536b85f5e_1622651065960__UDF43_13ck; _px3=7fc56524b43cd6d0fcf4f6770a68d328717d8655d4fa933cc4a0e30bc017e1ef:ruxaDd8mFrvHn9qaw0pOBMT0mV+NxnKdhWs8zNzrcCUtp6Jtklv/HnuE0QQVYJmnMPAt2w7Z8ED5QowCsPEmmg==:1000:b3TlUy31Q4LEkj9sOzoczopUB7XzOadDrTFmlwDAnGca/WWVE45BU6t8mW2Nk2W/38FNUuX+R72r1+1CmSU5T19DOHB/CnuHUqxzEKahNZokYxTFrhbfvKFOMYJKqWuZc+9mQucgZVK2Kyc97gcQ4ygY3M1jDn+dKClBnR/t3HRGVGM+4UBmqZ6XRROy53i8u8EpOc3NHHFxcSmr81uyiQ==; chgmfatoken=%5B%20%22account_sharing_mfa%22%20%3D%3E%201%2C%20%22user_uuid%22%20%3D%3E%20f56de97c-4625-4ee4-a177-a73b0c6f291c%2C%20%22created_date%22%20%3D%3E%202021-06-02T16%3A25%3A02.049Z%20%5D; id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJmNTZkZTk3Yy00NjI1LTRlZTQtYTE3Ny1hNzNiMGM2ZjI5MWMiLCJhdWQiOiJDSEdHIiwiaXNzIjoiaHViLmNoZWdnLmNvbSIsImV4cCI6MTYzODQyMTE0OCwiaWF0IjoxNjIyNjUxMTQ4LCJlbWFpbCI6InJhcW0yNTc1QGdtYWlsLmNvbSJ9.f_yZQ-czs2y2w_nT0e9Bs17JR8s944-ESwPnMRedkN_ZrzRfciOFBx82l8jSuj2DtYGsXeZ2fWwGzjW3KWFO-tBC7nHSOIOG2GfFN0u3ZCHltTDZ3qfyA0GcErNyKuaaYvPrZV-uaLcEdCyaxgPFuTkHljSOkZQ8L9EtzT1EyrbEilfwjdx-hBGp_PLeYR-w3pSEKaF1ySnBavHGGFEfrfJpj9jjDb_cCI03g9QOcE3BCoO-BtuYUa0RDImP7uFexrIaeuMvPHPChb3fyrMV7rum9IHnqtaZzzeW7rFKny59H8prFN-WhhXxnHkwal3taBKkIGQYD7FwSpYgQHec8w; access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhUTkU0cWwxNTRxekZieTBBakxDdSJ9.eyJodHRwczovL3Byb3h5LmNoZWdnLmNvbS9jbGFpbXMvYXBwSWQiOiJOc1lLd0kwbEx1WEFBZDB6cVMwcWVqTlRVcDBvWXVYNiIsImlzcyI6Imh0dHBzOi8vY2hlZ2ctcHJvZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8ZjU2ZGU5N2MtNDYyNS00ZWU0LWExNzctYTczYjBjNmYyOTFjIiwiYXVkIjpbImNoZWdnLW9pZGMiLCJodHRwczovL2NoZWdnLXByb2QudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMjY1MTE0OCwiZXhwIjoxNjIyNjUyNTg4LCJhenAiOiIzVFpiaGZzWndkZUhiaG9WTXhPdlpHYjM3TWN2YzBvOCIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgYWRkcmVzcyBwaG9uZSBvZmZsaW5lX2FjY2VzcyIsImd0eSI6InBhc3N3b3JkIn0.gM14_tYocXn7UlUM07dwNmaiEYelZMi7gclXwL_4SqD4Nyn-Ve2gEtyPORi2Iq6U_T1iHNHTJOaZPTXQXe0Tg1f8r8-bsJQUiUF--sBxhtO2JwuzAI9lk2bEUMlF5VrLZpQJ2NCxM-3enTKQN_FeYj9XgAId6vXhhBjE8y8lreEoYJiTyOGeYhCiZnopQkBz0lxRrL2ZimSGvI91-rYbj8DI3IM0R1TSPiA6Bi04klzyMJfmADPJ0QqTKxmy9bgtXJsYutXoOnSDDTaHFZpWff9XqfBC09JMNl54P-XmVnlMIQx9ETvrAzxXpJGPFxcQ7MtDaZ-fmcVSSoYHqsyufA; access_token_expires_at=1622652588; refresh_token=ext.a0.t00.v1.MfYp3eVlG_QI_WVT7aRExoQ8b1gMUsWVaCliCVFtYOeWITJA_ADsu8zXMU2zbHhDdyRXJqcFqelg6w0PC4RvJng; SU=d3_yaxOhLAPJURIStOeFXGKfxT6sDvOa8S5pE8_PpKEGFmkGh3Q2cj2ORUaECZ5f_WufG6mKzd-hAHj4DALUWnpqoXQfsmpkRxaCsqLVrDTtcsWxRip_VOW1Scaf5Efr; U=065661d4ccb0a8f368884de9866941e8; exp=A184A%7CA311C%7CA803B%7CC024A%7CA560B%7CA259B%7CA207B%7CA209A%7CA212A%7CA239A%7CA935B%7CA110B%7CA270C%7CA278C%7CA448A%7CA966G%7CA890H%7CA315B; expkey=F1A45BDFF230387297B59706D875D79C; _gd1622651148390=1; sbm_a_b_test=3-control; _sdsat_cheggUserUUID=f56de97c-4625-4ee4-a177-a73b0c6f291c; _sdsat_authState=Hard%20Logged%20In; tpudsa=tpudsa; userRole=mybibpro; AMCV_3FE7CBC1556605A77F000101%40AdobeOrg=-408604571%7CMCIDTS%7C18780%7CMCMID%7C83597856594541360060557814214213396744%7CMCAAMLH-1623256048%7C6%7CMCAAMB-1623256048%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1622658448s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18765%7CvVersion%7C4.6.0%7CMCCIDH%7C2042747136; OptanonConsent=isIABGlobal=false&datestamp=Wed+Jun+02+2021+19%3A27%3A28+GMT%2B0300+(%D8%A7%D9%84%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A+%D8%A7%D9%84%D8%B1%D8%B3%D9%85%D9%8A)&version=6.10.0&hosts=&consentId=e05d66d4-ca62-4f3f-81c8-d43179299e6e&interactionCount=1&landingPath=NotLandingPage&groups=snc%3A1%2Cfnc%3A1%2Cprf%3A1%2CSPD_BG%3A1%2Ctrg%3A1&AwaitingReconsent=false; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; s_pers=%20buFirstVisit%3Dcs%252Ccore%252Cothers%7C1778383769532%3B%20gpv_v6%3Dchegg%257Cweb%257Ccs%257Cqa%257Cquestion%2520page%7C1622653049049%3B; _px3=d2daff3deabb3047382aa08ff1dccea8e3fc5803e4c431fcb3ea95e12c7475aa:oJttIEAAybiGYK+SWWikgJX3lx5HjlJjYkB1mZPoMWrdrEKlnGqPIm1mM2QRAMR3L/Gzx4DELxFScnfueavMgw==:1000:ePJa0IPZcm5x6BYp9r0b8oxdqGMrWQ+I3qUmrrxj4sRkCybLipo0qA/aGBfKDA4qn05QakPmfmuYzYiQHBMTqWWz7e2VYU7kOtA15PfDZDMzp9csaqHJfpu3//LKotPZsaFej73RX5a9D/XkzwNGXCbPJZPZ5BaW/71RcdzDZyRR0omF/azIKsIButyHDXa4RhLlByj/az06dSHMYXInKQ==; _px=oJttIEAAybiGYK+SWWikgJX3lx5HjlJjYkB1mZPoMWrdrEKlnGqPIm1mM2QRAMR3L/Gzx4DELxFScnfueavMgw==:1000:VWMX8L9mhAaK0g1qoSeT6uVIA3N8Vg+piGA3ZuQJvsCPmtsFCszrlWE2WpFOxGdrZWIXMpcgnE0ofAX2TGyPxKG0eOkrel1xfSpIBfkgFTxG0X0SFIEgE4bOnp7QPSCfLKcgCk9wnJ1C244IYUwxPded2E0dFANHaQ78uCQekZQidCve08rHN6I3lEzRoyUHizBsbxHLZfoEyNajvhrgXoyD3aGtS2+ap+AZyFOq4bl+QSVRtyaYWfP+65y7h5L2MNy9pMor/VUIVLJb2SRk1w==; s_sess=%20s_sq%3Dcheggincriovalidation%253D%252526pid%25253Dchegg%2525257Cweb%2525257Ccore%2525257Chome%25252520page%252526pidt%25253D1%252526oid%25253Dhttps%2525253A%2525252F%2525252Fwww.chegg.com%2525252Fhomework-help%2525252Fquestions-and-answers%2525252F01-consider-following-table-given-economy-%252526ot%25253DA%3B%20intcid%3D%3B%20buVisited%3Dcore%252Ccs%3B%20cheggCTALink%3Dfalse%3B%20SDID%3D1E5FF7F1E7E28EBD-42BA26A50D9FBE11%3B%20s_ptc%3D0.01%255E%255E0.00%255E%255E0.00%255E%255E0.00%255E%255E1.10%255E%255E0.39%255E%255E4.96%255E%255E0.20%255E%255E6.36%3B; f56de97c-4625-4ee4-a177-a73b0c6f291c_TMXCookie=true; _sdsat_highestContentConfidence={%22course_uuid%22:%227ce71a9e-db20-4b5e-a74c-f658a003a48f%22%2C%22course_name%22:%22macroeconomic-theory%22%2C%22confidence%22:0.6792%2C%22year_in_school%22:%22college-year-2%22%2C%22subject%22:[{%22uuid%22:%22066d0438-21ad-43f0-85d9-0ce9b16f4505%22%2C%22name%22:%22economics%22}]}; _uetsid=57940850c2fe11eb9199b1e404140140; _uetvid=ab517ea0b13a11eb8f289de9ecf27314; wcs_bt=s_4544d378d9e5:1622651258; _gat=1',
                'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content, 'html.parser')
            x0 = soup.find('div', class_="answers-h2")
            if ("An expert answer will be posted here") in soup.text:
                bot.send_message(message.chat.id, 'لم يتم حل السؤال بعد Not resolved ',
                                 reply_to_message_id=message.message_id)
            else:
                url = message.text
                headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'cookie': 'C=0; O=0; V=40284a92b7d730815a548f54d744590660989fc27589f2.18718116; usprivacy=1YNY; _pxvid=aa6c9a9e-b13a-11eb-9f58-0242ac120009; _omappvp=JJqCeJ9EuvA5F93I1JecvNvOez2tx5qeIZl2wcX0GAbJlixUzlLGiLI0vkY1IYHYnVnSPfcPOicslTZOOKNsC5CgrMMJczie; adobeujs-optin=%7B%22aam%22%3Atrue%2C%22adcloud%22%3Atrue%2C%22aa%22%3Atrue%2C%22campaign%22%3Atrue%2C%22ecid%22%3Atrue%2C%22livefyre%22%3Atrue%2C%22target%22%3Atrue%2C%22mediaaa%22%3Atrue%7D; s_ecid=MCMID%7C83597856594541360060557814214213396744; _ga=GA1.2.680442464.1620615110; _scid=a22a9fa3-9d1e-40a9-a101-73038ea415c8; _rdt_uuid=1620615110618.887e279e-3cff-46c5-aa74-49c921b910f7; _fbp=fb.1.1620615111105.79295125; _gcl_au=1.1.839235490.1620615111; optimizelyEndUserId=oeu1620615175475r0.1442633774958626; __gads=ID=01da3ec73d6ef144:T=1620615181:S=ALNI_MaR_e59_Aq4soxWqsI3kkS7OpOA5g; _cs_c=1; sbm_dma=0; sbm_country=IQ; _ym_uid=1621337530255138749; _ym_d=1621337530; _vid=CsGUfEs7h9JPk2P3MiqY; DFID=web|CsGUfEs7h9JPk2P3MiqY; sourceTracking=adobe; chgcsdmtoken=%7B%22user_uuid%22%3A%223e8ada61-f9de-428c-9e0f-ea20289f2307%22%2C%22created_date%22%3A%222021-05-22T11%3A07%3A48.053Z%22%2C%22account_sharing_device_management%22%3A1%7D; omSeen-tgjg3ieouzbhy6fc0ctw=1622367008723; _cs_id=b2fe01fd-4c69-adcc-e937-b690ab1b811c.1620615206.7.1622449309.1622449309.1.1654779206894.Lax.0; __CT_Data=gpv=15&ckp=tld&dm=chegg.com&apv_79_www33=15&cpv_79_www33=15; _gid=GA1.2.1076720400.1622568318; __ssid=1bac04c43bede1a0f4fa750af09354d; _sctr=1|1622581200000; _ym_isad=1; intlPaQExitIntentModal=hide; user_geo_location=%7B%22country_iso_code%22%3A%22IQ%22%2C%22country_name%22%3A%22Iraq%22%2C%22region%22%3A%22BG%22%2C%22region_full%22%3A%22Baghdad%22%2C%22city_name%22%3A%22Baghdad%22%2C%22locale%22%3A%7B%22localeCode%22%3A%5B%22ar-IQ%22%5D%7D%7D; AMCVS_3FE7CBC1556605A77F000101%40AdobeOrg=1; _gd1622651046268=1; al_cell=2021-6-2-wt-main-1-control; BIBSESSID=9b080df2-6565-4aa3-9391-a6336f3661c6; CVID=01d774a0-9199-416b-a2e3-925acaa9f9d4; mcid=83597856594541360060557814214213396744; CSID=1622651047107; schoolapi=null; PHPSESSID=ttjpqp6br6bfflsnpbaah445uq; CSessionID=ebdda520-5dce-4489-9215-877e009ad629; _gd1622651066328=1; forterToken=68c9cf61a25d42b9b490387536b85f5e_1622651065960__UDF43_13ck; _px3=7fc56524b43cd6d0fcf4f6770a68d328717d8655d4fa933cc4a0e30bc017e1ef:ruxaDd8mFrvHn9qaw0pOBMT0mV+NxnKdhWs8zNzrcCUtp6Jtklv/HnuE0QQVYJmnMPAt2w7Z8ED5QowCsPEmmg==:1000:b3TlUy31Q4LEkj9sOzoczopUB7XzOadDrTFmlwDAnGca/WWVE45BU6t8mW2Nk2W/38FNUuX+R72r1+1CmSU5T19DOHB/CnuHUqxzEKahNZokYxTFrhbfvKFOMYJKqWuZc+9mQucgZVK2Kyc97gcQ4ygY3M1jDn+dKClBnR/t3HRGVGM+4UBmqZ6XRROy53i8u8EpOc3NHHFxcSmr81uyiQ==; chgmfatoken=%5B%20%22account_sharing_mfa%22%20%3D%3E%201%2C%20%22user_uuid%22%20%3D%3E%20f56de97c-4625-4ee4-a177-a73b0c6f291c%2C%20%22created_date%22%20%3D%3E%202021-06-02T16%3A25%3A02.049Z%20%5D; id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJmNTZkZTk3Yy00NjI1LTRlZTQtYTE3Ny1hNzNiMGM2ZjI5MWMiLCJhdWQiOiJDSEdHIiwiaXNzIjoiaHViLmNoZWdnLmNvbSIsImV4cCI6MTYzODQyMTE0OCwiaWF0IjoxNjIyNjUxMTQ4LCJlbWFpbCI6InJhcW0yNTc1QGdtYWlsLmNvbSJ9.f_yZQ-czs2y2w_nT0e9Bs17JR8s944-ESwPnMRedkN_ZrzRfciOFBx82l8jSuj2DtYGsXeZ2fWwGzjW3KWFO-tBC7nHSOIOG2GfFN0u3ZCHltTDZ3qfyA0GcErNyKuaaYvPrZV-uaLcEdCyaxgPFuTkHljSOkZQ8L9EtzT1EyrbEilfwjdx-hBGp_PLeYR-w3pSEKaF1ySnBavHGGFEfrfJpj9jjDb_cCI03g9QOcE3BCoO-BtuYUa0RDImP7uFexrIaeuMvPHPChb3fyrMV7rum9IHnqtaZzzeW7rFKny59H8prFN-WhhXxnHkwal3taBKkIGQYD7FwSpYgQHec8w; access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhUTkU0cWwxNTRxekZieTBBakxDdSJ9.eyJodHRwczovL3Byb3h5LmNoZWdnLmNvbS9jbGFpbXMvYXBwSWQiOiJOc1lLd0kwbEx1WEFBZDB6cVMwcWVqTlRVcDBvWXVYNiIsImlzcyI6Imh0dHBzOi8vY2hlZ2ctcHJvZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8ZjU2ZGU5N2MtNDYyNS00ZWU0LWExNzctYTczYjBjNmYyOTFjIiwiYXVkIjpbImNoZWdnLW9pZGMiLCJodHRwczovL2NoZWdnLXByb2QudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMjY1MTE0OCwiZXhwIjoxNjIyNjUyNTg4LCJhenAiOiIzVFpiaGZzWndkZUhiaG9WTXhPdlpHYjM3TWN2YzBvOCIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgYWRkcmVzcyBwaG9uZSBvZmZsaW5lX2FjY2VzcyIsImd0eSI6InBhc3N3b3JkIn0.gM14_tYocXn7UlUM07dwNmaiEYelZMi7gclXwL_4SqD4Nyn-Ve2gEtyPORi2Iq6U_T1iHNHTJOaZPTXQXe0Tg1f8r8-bsJQUiUF--sBxhtO2JwuzAI9lk2bEUMlF5VrLZpQJ2NCxM-3enTKQN_FeYj9XgAId6vXhhBjE8y8lreEoYJiTyOGeYhCiZnopQkBz0lxRrL2ZimSGvI91-rYbj8DI3IM0R1TSPiA6Bi04klzyMJfmADPJ0QqTKxmy9bgtXJsYutXoOnSDDTaHFZpWff9XqfBC09JMNl54P-XmVnlMIQx9ETvrAzxXpJGPFxcQ7MtDaZ-fmcVSSoYHqsyufA; access_token_expires_at=1622652588; refresh_token=ext.a0.t00.v1.MfYp3eVlG_QI_WVT7aRExoQ8b1gMUsWVaCliCVFtYOeWITJA_ADsu8zXMU2zbHhDdyRXJqcFqelg6w0PC4RvJng; SU=d3_yaxOhLAPJURIStOeFXGKfxT6sDvOa8S5pE8_PpKEGFmkGh3Q2cj2ORUaECZ5f_WufG6mKzd-hAHj4DALUWnpqoXQfsmpkRxaCsqLVrDTtcsWxRip_VOW1Scaf5Efr; U=065661d4ccb0a8f368884de9866941e8; exp=A184A%7CA311C%7CA803B%7CC024A%7CA560B%7CA259B%7CA207B%7CA209A%7CA212A%7CA239A%7CA935B%7CA110B%7CA270C%7CA278C%7CA448A%7CA966G%7CA890H%7CA315B; expkey=F1A45BDFF230387297B59706D875D79C; _gd1622651148390=1; sbm_a_b_test=3-control; _sdsat_cheggUserUUID=f56de97c-4625-4ee4-a177-a73b0c6f291c; _sdsat_authState=Hard%20Logged%20In; tpudsa=tpudsa; userRole=mybibpro; AMCV_3FE7CBC1556605A77F000101%40AdobeOrg=-408604571%7CMCIDTS%7C18780%7CMCMID%7C83597856594541360060557814214213396744%7CMCAAMLH-1623256048%7C6%7CMCAAMB-1623256048%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1622658448s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18765%7CvVersion%7C4.6.0%7CMCCIDH%7C2042747136; OptanonConsent=isIABGlobal=false&datestamp=Wed+Jun+02+2021+19%3A27%3A28+GMT%2B0300+(%D8%A7%D9%84%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A+%D8%A7%D9%84%D8%B1%D8%B3%D9%85%D9%8A)&version=6.10.0&hosts=&consentId=e05d66d4-ca62-4f3f-81c8-d43179299e6e&interactionCount=1&landingPath=NotLandingPage&groups=snc%3A1%2Cfnc%3A1%2Cprf%3A1%2CSPD_BG%3A1%2Ctrg%3A1&AwaitingReconsent=false; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; s_pers=%20buFirstVisit%3Dcs%252Ccore%252Cothers%7C1778383769532%3B%20gpv_v6%3Dchegg%257Cweb%257Ccs%257Cqa%257Cquestion%2520page%7C1622653049049%3B; _px3=d2daff3deabb3047382aa08ff1dccea8e3fc5803e4c431fcb3ea95e12c7475aa:oJttIEAAybiGYK+SWWikgJX3lx5HjlJjYkB1mZPoMWrdrEKlnGqPIm1mM2QRAMR3L/Gzx4DELxFScnfueavMgw==:1000:ePJa0IPZcm5x6BYp9r0b8oxdqGMrWQ+I3qUmrrxj4sRkCybLipo0qA/aGBfKDA4qn05QakPmfmuYzYiQHBMTqWWz7e2VYU7kOtA15PfDZDMzp9csaqHJfpu3//LKotPZsaFej73RX5a9D/XkzwNGXCbPJZPZ5BaW/71RcdzDZyRR0omF/azIKsIButyHDXa4RhLlByj/az06dSHMYXInKQ==; _px=oJttIEAAybiGYK+SWWikgJX3lx5HjlJjYkB1mZPoMWrdrEKlnGqPIm1mM2QRAMR3L/Gzx4DELxFScnfueavMgw==:1000:VWMX8L9mhAaK0g1qoSeT6uVIA3N8Vg+piGA3ZuQJvsCPmtsFCszrlWE2WpFOxGdrZWIXMpcgnE0ofAX2TGyPxKG0eOkrel1xfSpIBfkgFTxG0X0SFIEgE4bOnp7QPSCfLKcgCk9wnJ1C244IYUwxPded2E0dFANHaQ78uCQekZQidCve08rHN6I3lEzRoyUHizBsbxHLZfoEyNajvhrgXoyD3aGtS2+ap+AZyFOq4bl+QSVRtyaYWfP+65y7h5L2MNy9pMor/VUIVLJb2SRk1w==; s_sess=%20s_sq%3Dcheggincriovalidation%253D%252526pid%25253Dchegg%2525257Cweb%2525257Ccore%2525257Chome%25252520page%252526pidt%25253D1%252526oid%25253Dhttps%2525253A%2525252F%2525252Fwww.chegg.com%2525252Fhomework-help%2525252Fquestions-and-answers%2525252F01-consider-following-table-given-economy-%252526ot%25253DA%3B%20intcid%3D%3B%20buVisited%3Dcore%252Ccs%3B%20cheggCTALink%3Dfalse%3B%20SDID%3D1E5FF7F1E7E28EBD-42BA26A50D9FBE11%3B%20s_ptc%3D0.01%255E%255E0.00%255E%255E0.00%255E%255E0.00%255E%255E1.10%255E%255E0.39%255E%255E4.96%255E%255E0.20%255E%255E6.36%3B; f56de97c-4625-4ee4-a177-a73b0c6f291c_TMXCookie=true; _sdsat_highestContentConfidence={%22course_uuid%22:%227ce71a9e-db20-4b5e-a74c-f658a003a48f%22%2C%22course_name%22:%22macroeconomic-theory%22%2C%22confidence%22:0.6792%2C%22year_in_school%22:%22college-year-2%22%2C%22subject%22:[{%22uuid%22:%22066d0438-21ad-43f0-85d9-0ce9b16f4505%22%2C%22name%22:%22economics%22}]}; _uetsid=57940850c2fe11eb9199b1e404140140; _uetvid=ab517ea0b13a11eb8f289de9ecf27314; wcs_bt=s_4544d378d9e5:1622651258; _gat=1',
                    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                    'sec-ch-ua-mobile': '?0', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
                r = requests.get(url, headers=headers).content
                soup = BeautifulSoup(r, 'html.parser')
                x0 = soup.find('div', '</div>', class_="ugc-base question-body-text")
                x1 = soup.find('div', '</div>', class_="answer-given-body ugc-base")
                if x1 == None:
                    bot.reply_to(message, "عذرا عزيزي قم بفتح الرابط ثم قم بنسخه من اعلى المتصفح ومن ثم ارسالهOpen the link and copy from the top browser")
                else:
                    bot.reply_to(message, "♥ ♥  سيتم ارسال الاجابة في  غضون ثوانيwait seconds")
                    dds = sum([1 for i in x1.find_all('img') if '//d2vlcm61l7u1fs.cloudfront.net' in i['src']])
                    print(dds)
                    if dds==0:
                        rt = str(time.clock())
                        mma = rt.split(".")[0]
                        f = open("answer.html", "w", encoding='utf8')
                        mmes = """
                                                                                                                                                                <html>
                                                                                                                                                                <head>
                                                                                                                                                                <link href='http://fonts.googleapis.com/css?family=Droid+Sans' rel='stylesheet' type='text/css'>
                                                                                                                                                                <meta charset="utf-8"/>
                                                                                                                                                                <meta content="IE=11" http-equiv="X-UA-Compatible"/>
                                                                                                                                                                <meta content="width=device-width, initial-scale=1, maximum-scale=10" name="viewport"/>
                                                                                                                                                                </head>
                                                                                                                                                                <style> .hi{{background-color: #FFC133; width:800px; border-radius:6px;


                                                                                                                                                                }}
                                                                                                                                    .us{{background-color: #05ABD5;width:100%; width:800px; border-radius:6px;}}

                                                                                                                                    h3{{
                                                                                                                                        color: white;
                                                                                                                                        font-family: 'Droid Sans', arial, serif;;
                                                                                                                                        text-align: center;
                                                                                                                                        font-size:22px;
                                                                                                                                    }}
                                                                                                                                    h2{{
                                                                                                                                        color: #302F2D;
                                                                                                                                        font-family: 'Droid Sans', arial, serif;;
                                                                                                                                        text-align: center;
                                                                                                                                        font-size:22px;
                                                                                                                                    }}
                                                                                                                                    h4{{text-align:center; color:white; font-size:30px; font-family: 'Droid Sans', arial, serif;;}}
                                                                                                                                    .qa{{border:13px solid #FFC133; font-size:20px; width:800px;}}
                                                                                                                                    .q1{{background-color:#D50524; border-radius:6px; width:800px;}}
                                                                                                                                    .q2{{background-color:#05D52D; border-radius:6px; width:800px;}}
                                                                                                                                    </style>
                                                                                                                                        <body> <div class="hi">
                                                                                                                                        <h2>By Qasim Al-Salihi
 </h2>
                                                                                                                                        </div> <div class="us">
                                                                                                                                        <h3>Follow us on Telegram @Qissm22 and @Iraqi227_1</h3>
                                                                                                                                        </div><div class="q1"><h4>Question</h4></div><div class="qa" align="center">{Q}</div><div class="q2"><h4>Answer</h4></div><div class="qa" align="center">{A}</div></body>
                                                                                                                                                                </html>
                                                                                                                                                                """.format(
                            Q=x0, A=x1)

                        f.write(mmes)
                        f.close()
                        i = open('./answer.html', 'rb')
                        try:
                            bot.send_document(message.chat.id, i,
                                              caption="🌐 Answer\n\n🛡 Join Channel : @Iraqi227\n\n🛑 Contact : @Qissm22 \n\n ⏱ Time : " + str(
                                                  mma) + 's', parse_mode="Markdown",
                                              disable_notification=True, reply_to_message_id=message.message_id)
                        except:
                            pass

                    if dds == 1:
                        s = x1.findAll('img')[0]['src']
                        bbz = s.split("//")[1]
                        jj = f"https://{bbz}?x-oss-process=image/resize,w_560"
                        g = str(x1).replace(s, jj)
                        rt = str(time.clock())
                        mma = rt.split(".")[0]
                        f = open("answer.html", "w", encoding='utf8')
                        mmes = """
                                                                                                                                        <html>
                                                                                                                                        <head>
                                                                                                                                        <link href='http://fonts.googleapis.com/css?family=Droid+Sans' rel='stylesheet' type='text/css'>
                                                                                                                                        <meta charset="utf-8"/>
                                                                                                                                        <meta content="IE=11" http-equiv="X-UA-Compatible"/>
                                                                                                                                        <meta content="width=device-width, initial-scale=1, maximum-scale=10" name="viewport"/>
                                                                                                                                        </head>
                                                                                                                                        <style> .hi{{background-color: #FFC133; width:800px; border-radius:6px;


                                                                                                                                        }}
                                                                                                            .us{{background-color: #05ABD5;width:100%; width:800px; border-radius:6px;}}

                                                                                                            h3{{
                                                                                                                color: white;
                                                                                                                font-family: 'Droid Sans', arial, serif;;
                                                                                                                text-align: center;
                                                                                                                font-size:22px;
                                                                                                            }}
                                                                                                            h2{{
                                                                                                                color: #302F2D;
                                                                                                                font-family: 'Droid Sans', arial, serif;;
                                                                                                                text-align: center;
                                                                                                                font-size:22px;
                                                                                                            }}
                                                                                                            h4{{text-align:center; color:white; font-size:30px; font-family: 'Droid Sans', arial, serif;;}}
                                                                                                            .qa{{border:13px solid #FFC133; font-size:20px; width:800px;}}
                                                                                                            .q1{{background-color:#D50524; border-radius:6px; width:800px;}}
                                                                                                            .q2{{background-color:#05D52D; border-radius:6px; width:800px;}}
                                                                                                            </style>
                                                                                                                <body> <div class="hi">
                                                                                                                <h2>By Qasim Al-Salihi
 </h2>
                                                                                                                </div> <div class="us">
                                                                                                                <h3>Follow us on Telegram @Qissm22 and @Iraqi227</h3>
                                                                                                                </div><div class="q1"><h4>Question</h4></div><div class="qa" align="center">{Q}</div><div class="q2"><h4>Answer</h4></div><div class="qa" align="center">{A}</div></body>
                                                                                                                                        </html>
                                                                                                                                        """.format(
                            Q=x0, A=g)

                        f.write(mmes)
                        f.close()
                        i = open('./answer.html', 'rb')
                        try:
                            bot.send_document(message.chat.id, i,
                                              caption="🌐 Answer\n\n🛡 Join Channel : @Iraqi227\n\n🛑 Contact : @Qissm22 \n\n ⏱ Time : " + str(
                                                  mma) + 's', parse_mode="Markdown",
                                              disable_notification=True, reply_to_message_id=message.message_id)
                        except:
                            pass
                    elif dds == 2:
                        s = x1.findAll('img')[0]['src']
                        dd = x1.findAll('img')[1]['src']
                        bbz = s.split("//")[1]
                        kkm = dd.split("//")[1]
                        jj = f"https://{bbz}?x-oss-process=image/resize,w_560"
                        cc = f"https://{kkm}?x-oss-process=image/resize,w_560"
                        g = str(x1).replace(s, jj).replace(dd, cc)
                        rt = str(time.clock())
                        mma = rt.split(".")[0]
                        f = open("answer.html", "w", encoding='utf8')
                        mmes = """
                                                                                                                                                                    <html>
                                                                                                                                                                    <head>
                                                                                                                                                                    <link href='http://fonts.googleapis.com/css?family=Droid+Sans' rel='stylesheet' type='text/css'>
                                                                                                                                                                    <meta charset="utf-8"/>
                                                                                                                                                                    <meta content="IE=11" http-equiv="X-UA-Compatible"/>
                                                                                                                                                                    <meta content="width=device-width, initial-scale=1, maximum-scale=10" name="viewport"/>
                                                                                                                                                                    </head>
                                                                                                                                                                    <style> .hi{{background-color: #FFC133; width:800px; border-radius:6px;


                                                                                                                                                                    }}
                                                                                                                                        .us{{background-color: #05ABD5;width:100%; width:800px; border-radius:6px;}}

                                                                                                                                        h3{{
                                                                                                                                            color: white;
                                                                                                                                            font-family: 'Droid Sans', arial, serif;;
                                                                                                                                            text-align: center;
                                                                                                                                            font-size:22px;
                                                                                                                                        }}
                                                                                                                                        h2{{
                                                                                                                                            color: #302F2D;
                                                                                                                                            font-family: 'Droid Sans', arial, serif;;
                                                                                                                                            text-align: center;
                                                                                                                                            font-size:22px;
                                                                                                                                        }}
                                                                                                                                        h4{{text-align:center; color:white; font-size:30px; font-family: 'Droid Sans', arial, serif;;}}
                                                                                                                                        .qa{{border:13px solid #FFC133; font-size:20px; width:800px;}}
                                                                                                                                        .q1{{background-color:#D50524; border-radius:6px; width:800px;}}
                                                                                                                                        .q2{{background-color:#05D52D; border-radius:6px; width:800px;}}
                                                                                                                                        </style>
                                                                                                                                            <body> <div class="hi">
                                                                                                                                            <h2>By Eng Mahmoud Fadhil</h2>
                                                                                                                                            </div> <div class="us">
                                                                                                                                            <h3>Follow us on Telegram @eng2028 and @Chegg_1</h3>
                                                                                                                                            </div><div class="q1"><h4>Question</h4></div><div class="qa" align="center">{Q}</div><div class="q2"><h4>Answer</h4></div><div class="qa" align="center">{A}</div></body>
                                                                                                                                                                    </html>
                                                                                                                                                                    """.format(
                            Q=x0, A=g)

                        f.write(mmes)
                        f.close()
                        i = open('./answer.html', 'rb')
                        try:
                            bot.send_document(message.chat.id, i,
                                              caption="🌐 Answer\n\n🛡 Join Channel : @Iraqi227\n\n🛑 Contact : @Qissm22\n\n⏱ Time : " + str(
                                                  mma) + 's', parse_mode="Markdown",
                                              disable_notification=True, reply_to_message_id=message.message_id)
                        except:
                            pass
                    elif dds == 3:
                        s = x1.findAll('img')[0]['src']
                        dd = x1.findAll('img')[1]['src']
                        bn = x1.findAll('img')[2]['src']
                        bbz1 = s.split("//")[1]
                        bbz2 = dd.split("//")[1]
                        bbz3 = bn.split("//")[1]
                        jj = f"https://{bbz1}?x-oss-process=image/resize,w_560"
                        cc = f"https://{bbz2}?x-oss-process=image/resize,w_560"
                        ll = f"https://{bbz3}?x-oss-process=image/resize,w_560"
                        g = str(x1).replace(s, jj).replace(dd, cc).replace(bn, ll)
                        rt = str(time.clock())
                        mma = rt.split(".")[0]
                        f = open("answer.html", "w", encoding='utf8')
                        mmes = """
                                                                                                                                                                    <html>
                                                                                                                                                                    <head>
                                                                                                                                                                    <link href='http://fonts.googleapis.com/css?family=Droid+Sans' rel='stylesheet' type='text/css'>
                                                                                                                                                                    <meta charset="utf-8"/>
                                                                                                                                                                    <meta content="IE=11" http-equiv="X-UA-Compatible"/>
                                                                                                                                                                    <meta content="width=device-width, initial-scale=1, maximum-scale=10" name="viewport"/>
                                                                                                                                                                    </head>
                                                                                                                                                                    <style> .hi{{background-color: #FFC133; width:800px; border-radius:6px;


                                                                                                                                                                    }}
                                                                                                                                        .us{{background-color: #05ABD5;width:100%; width:800px; border-radius:6px;}}

                                                                                                                                        h3{{
                                                                                                                                            color: white;
                                                                                                                                            font-family: 'Droid Sans', arial, serif;;
                                                                                                                                            text-align: center;
                                                                                                                                            font-size:22px;
                                                                                                                                        }}
                                                                                                                                        h2{{
                                                                                                                                            color: #302F2D;
                                                                                                                                            font-family: 'Droid Sans', arial, serif;;
                                                                                                                                            text-align: center;
                                                                                                                                            font-size:22px;
                                                                                                                                        }}
                                                                                                                                        h4{{text-align:center; color:white; font-size:30px; font-family: 'Droid Sans', arial, serif;;}}
                                                                                                                                        .qa{{border:13px solid #FFC133; font-size:20px; width:800px;}}
                                                                                                                                        .q1{{background-color:#D50524; border-radius:6px; width:800px;}}
                                                                                                                                        .q2{{background-color:#05D52D; border-radius:6px; width:800px;}}
                                                                                                                                        </style>
                                                                                                                                            <body> <div class="hi">
                                                                                                                                            <h2>By Qasim Al-salihi</h2>
                                                                                                                                            </div> <div class="us">
                                                                                                                                            <h3>Follow us on Telegram @Qissm22 and @Iraqi227</h3>
                                                                                                                                            </div><div class="q1"><h4>Question</h4></div><div class="qa" align="center">{Q}</div><div class="q2"><h4>Answer</h4></div><div class="qa" align="center">{A}</div></body>
                                                                                                                                                                    </html>
                                                                                                                                                                    """.format(
                            Q=x0, A=g)

                        f.write(mmes)
                        f.close()
                        i = open('./answer.html', 'rb')
                        try:
                            bot.send_document(message.chat.id, i,
                                              caption="🌐 Answer\n\n🛡 Join Channel : @Iraqi227\n\n🛑 Contact : @Qissm22\n\n⏱ Time : " + str(
                                                  mma) + 's', parse_mode="Markdown",
                                              disable_notification=True, reply_to_message_id=message.message_id)
                        except:
                            pass
                    elif dds == 4:
                        s = x1.findAll('img')[0]['src']
                        dd = x1.findAll('img')[1]['src']
                        bn = x1.findAll('img')[2]['src']
                        bl = x1.findAll('img')[3]['src']
                        bbz1 = s.split("//")[1]
                        bbz2 = dd.split("//")[1]
                        bbz3 = bn.split("//")[1]
                        bbz4 = bl.split("//")[1]
                        jj = f"https://{bbz1}?x-oss-process=image/resize,w_560"
                        cc = f"https://{bbz2}?x-oss-process=image/resize,w_560"
                        ll = f"https://{bbz3}?x-oss-process=image/resize,w_560"
                        llx = f"https://{bbz4}?x-oss-process=image/resize,w_560"
                        g = str(x1).replace(s, jj).replace(dd, cc).replace(bn, ll).replace(bl, llx)
                        rt = str(time.clock())
                        mma = rt.split(".")[0]
                        f = open("answer.html", "w", encoding='utf8')
                        mmes = """
                                                                                                                                                                                                <html>
                                                                                                                                                                                                <head>
                                                                                                                                                                                                <link href='http://fonts.googleapis.com/css?family=Droid+Sans' rel='stylesheet' type='text/css'>
                                                                                                                                                                                                <meta charset="utf-8"/>
                                                                                                                                                                                                <meta content="IE=11" http-equiv="X-UA-Compatible"/>
                                                                                                                                                                                                <meta content="width=device-width, initial-scale=1, maximum-scale=10" name="viewport"/>
                                                                                                                                                                                                </head>
                                                                                                                                                                                                <style> .hi{{background-color: #FFC133; width:800px; border-radius:6px;


                                                                                                                                                                                                }}
                                                                                                                                                                    .us{{background-color: #05ABD5;width:100%; width:800px; border-radius:6px;}}

                                                                                                                                                                    h3{{
                                                                                                                                                                        color: white;
                                                                                                                                                                        font-family: 'Droid Sans', arial, serif;;
                                                                                                                                                                        text-align: center;
                                                                                                                                                                        font-size:22px;
                                                                                                                                                                    }}
                                                                                                                                                                    h2{{
                                                                                                                                                                        color: #302F2D;
                                                                                                                                                                        font-family: 'Droid Sans', arial, serif;;
                                                                                                                                                                        text-align: center;
                                                                                                                                                                        font-size:22px;
                                                                                                                                                                    }}
                                                                                                                                                                    h4{{text-align:center; color:white; font-size:30px; font-family: 'Droid Sans', arial, serif;;}}
                                                                                                                                                                    .qa{{border:13px solid #FFC133; font-size:20px; width:800px;}}
                                                                                                                                                                    .q1{{background-color:#D50524; border-radius:6px; width:800px;}}
                                                                                                                                                                    .q2{{background-color:#05D52D; border-radius:6px; width:800px;}}
                                                                                                                                                                    </style>
                                                                                                                                                                        <body> <div class="hi">
                                                                                                                                                                        <h2>By Eng Mahmoud Fadhil</h2>
                                                                                                                                                                        </div> <div class="us">
                                                                                                                                                                        <h3>Follow us on Telegram @eng2028 and @Chegg_1</h3>
                                                                                                                                                                        </div><div class="q1"><h4>Question</h4></div><div class="qa" align="center">{Q}</div><div class="q2"><h4>Answer</h4></div><div class="qa" align="center">{A}</div></body>
                                                                                                                                                                                                </html>
                                                                                                                                                                                                """.format(
                            Q=x0, A=g)

                        f.write(mmes)
                        f.close()
                        i = open('./answer.html', 'rb')
                        try:
                            bot.send_document(message.chat.id, i,
                                              caption="🌐 Answer\n\n🛡 Join Channel : @Iraqi227\n\n🛑 Contact : @Qissm22 \n\n ⏱ Time : " + str(
                                                  mma) + 's', parse_mode="Markdown",
                                              disable_notification=True, reply_to_message_id=message.message_id)
                        except:
                            pass
                    elif dds == 5:
                        s = x1.findAll('img')[0]['src']
                        dd = x1.findAll('img')[1]['src']
                        bn = x1.findAll('img')[2]['src']
                        bl = x1.findAll('img')[3]['src']
                        bx = x1.findAll('img')[4]['src']
                        bbz1 = s.split("//")[1]
                        bbz2 = dd.split("//")[1]
                        bbz3 = bn.split("//")[1]
                        bbz4 = bl.split("//")[1]
                        bbz5 = bx.split("//")[1]
                        jj = f"https://{bbz1}?x-oss-process=image/resize,w_560"
                        cc = f"https://{bbz2}?x-oss-process=image/resize,w_560"
                        ll = f"https://{bbz3}?x-oss-process=image/resize,w_560"
                        llx = f"https://{bbz4}?x-oss-process=image/resize,w_560"
                        llm = f"https://{bbz5}?x-oss-process=image/resize,w_560"
                        g = str(x1).replace(s, jj).replace(dd, cc).replace(bn, ll).replace(bl, llx).replace(bx, llm)
                        sleep(2)
                        rt = str(time.clock())
                        mma = rt.split(".")[0]
                        f = open("answer.html", "w", encoding='utf8')
                        mmes = """
                                                                                                                                                                                                <html>
                                                                                                                                                                                                <head>
                                                                                                                                                                                                <link href='http://fonts.googleapis.com/css?family=Droid+Sans' rel='stylesheet' type='text/css'>
                                                                                                                                                                                                <meta charset="utf-8"/>
                                                                                                                                                                                                <meta content="IE=11" http-equiv="X-UA-Compatible"/>
                                                                                                                                                                                                <meta content="width=device-width, initial-scale=1, maximum-scale=10" name="viewport"/>
                                                                                                                                                                                                </head>
                                                                                                                                                                                                <style> .hi{{background-color: #FFC133; width:800px; border-radius:6px;


                                                                                                                                                                                                }}
                                                                                                                                                                    .us{{background-color: #05ABD5;width:100%; width:800px; border-radius:6px;}}

                                                                                                                                                                    h3{{
                                                                                                                                                                        color: white;
                                                                                                                                                                        font-family: 'Droid Sans', arial, serif;;
                                                                                                                                                                        text-align: center;
                                                                                                                                                                        font-size:22px;
                                                                                                                                                                    }}
                                                                                                                                                                    h2{{
                                                                                                                                                                        color: #302F2D;
                                                                                                                                                                        font-family: 'Droid Sans', arial, serif;;
                                                                                                                                                                        text-align: center;
                                                                                                                                                                        font-size:22px;
                                                                                                                                                                    }}
                                                                                                                                                                    h4{{text-align:center; color:white; font-size:30px; font-family: 'Droid Sans', arial, serif;;}}
                                                                                                                                                                    .qa{{border:13px solid #FFC133; font-size:20px; width:800px;}}
                                                                                                                                                                    .q1{{background-color:#D50524; border-radius:6px; width:800px;}}
                                                                                                                                                                    .q2{{background-color:#05D52D; border-radius:6px; width:800px;}}
                                                                                                                                                                    </style>
                                                                                                                                                                        <body> <div class="hi">
                                                                                                                                                                        <h2>By Eng Mahmoud Fadhil</h2>
                                                                                                                                                                        </div> <div class="us">
                                                                                                                                                                        <h3>Follow us on Telegram @eng2028 and @Chegg_1</h3>
                                                                                                                                                                        </div><div class="q1"><h4>Question</h4></div><div class="qa" align="center">{Q}</div><div class="q2"><h4>Answer</h4></div><div class="qa" align="center">{A}</div></body>
                                                                                                                                                                                                </html>
                                                                                                                                                                                                """.format(
                            Q=x0, A=g)

                        f.write(mmes)
                        f.close()
                        i = open('./answer.html', 'rb')
                        try:
                            bot.send_document(message.chat.id, i,
                                              caption="🌐 Answer\n\n🛡 Join Channel : @Iraqi227\n\n🛑 Contact : @Qissm22 \n\n ⏱ Time : " + str(
                                                  mma) + 's', parse_mode="Markdown",
                                              disable_notification=True, reply_to_message_id=message.message_id)
                        except:
                            pass
        else:
            pass


bot.polling()
