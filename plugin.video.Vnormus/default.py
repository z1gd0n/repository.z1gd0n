# -*- coding: utf-8 -*-
import xbmcaddon,os,xbmc,xbmcgui,urllib,urllib2,re,xbmcplugin,sys,logging

__USERAGENT__ = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11'
links_israel=[('ONE HD','http://127.0.0.1:6878/ace/getstream?url=http://91.92.66.82/trash/ttv-list/acelive/as_cid_fa0adf.acelive&.mp4','https://www.dropbox.com/s/6a2on9lioid9414/ONE%20HD.JPG?dl=1'),
       ('SPORT 1HD','http://127.0.0.1:6878/ace/getstream?url=http://91.92.66.82/trash/ttv-list/acelive/as_cid_844b71.acelive&.mp4','https://www.dropbox.com/s/zh15eqcvff5hp5z/SPORT%201.jpg?dl=1'),
	   ('SPORT 2HD','http://127.0.0.1:6878/ace/getstream?url=http://91.92.66.82/trash/ttv-list/acelive/as_cid_b9bd7d.acelive&.mp4','https://www.dropbox.com/s/oobh6mksft33cp7/SPORT%202.jpg?dl=1'),
	   ('SPORT 5HD','http://127.0.0.1:6878/ace/getstream?url=http://91.92.66.82/trash/ttv-list/acelive/as_cid_7a6891.acelive&.mp4','https://www.dropbox.com/s/gtxx2nyo42ln2ks/SPORT%205HD.JPG?dl=1'),
	   ('SPORT 5+ LIVE HD','http://127.0.0.1:6878/ace/getstream?url=http://91.92.66.82/trash/ttv-list/acelive/as_cid_c41bd5.acelive&.mp4','https://www.dropbox.com/s/g0w54sz85wvpbab/5%20LIVE%20HD.jpg?dl=1'),
      
      ]
links_world=[('SKY SPORT 1HD','http://127.0.0.1:6878/ace/getstream?url=http://91.92.66.82/trash/ttv-list/acelive/as_cid_6f5dd9.acelive&.mp4','http://2.bp.blogspot.com/-DegSaay9Mtw/UlJcZzIfseI/AAAAAAAAGAc/2PIco6UBn14/s1600/sky_uk_sports1_in_pubs.png'),
       ('SKY SPORT 2HD','http://127.0.0.1:6878/ace/getstream?url=http://91.92.66.82/trash/ttv-list/acelive/as_cid_8f4f13.acelive&.mp4','https://vignette3.wikia.nocookie.net/logopedia/images/e/e1/Sky_Sports_2_logo_2003.svg/revision/latest?cb=20100402105638'),
	   ('SKY SPORT 3HD','http://127.0.0.1:6878/ace/getstream?url=http://91.92.66.82/trash/ttv-list/acelive/as_cid_9ebc38.acelive&.mp4','http://1.bp.blogspot.com/-YNFajVRPiFk/VJU4K9e53FI/AAAAAAAAASs/IfAhSgo2_bI/s1600/sky%2Bsports%2B3%2Blive%2Bmykora.png'),
	   ('SKY SPORT 4HD','http://127.0.0.1:6878/ace/getstream?url=http://91.92.66.82/trash/ttv-list/acelive/as_cid_ed6c07.acelive&.mp4','http://3.bp.blogspot.com/-VBBZAd1M9ho/VAW70LPtqCI/AAAAAAAAFVg/SdbUouoEhdM/s1600/sky%2Bsports%2B4%2Blive%2Bmykora.png'),
	   ('SKY SPORT 5HD','http://127.0.0.1:6878/ace/getstream?url=http://91.92.66.82/trash/ttv-list/acelive/as_cid_c9e68d.acelive&.mp4','http://www.skysports.com/core/img/channels/Sky-Sports-5-Logo.png'),
	   ('SKY SPORT Premier League HD','http://127.0.0.1:6878/ace/getstream?url=http://91.92.66.82/trash/ttv-list/acelive/as_cid_5c247a.acelive&.mp4','http://e0.365dm.com/16/08/1-1/40/pl-logo-blog-premier-league_3758341.jpg?20160805124844'),
	   ('SKY SPORT main event HD','http://127.0.0.1:6878/ace/getstream?url=http://91.92.66.82/trash/ttv-list/acelive/as_cid_ee0c0f&.mp4','http://web.static.nowtv.com/images/NOWTV_2017/02_TV_Passes/03_Sport/Sky_Sports_Rebrand/Sports_channels_Main_Event.png'),
      
      ]

def get_params():
        param=[]
        if len(sys.argv)>=2:
          paramstring=sys.argv[2]
          if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param     


###############################################################################################################        

def addDir3(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        
        return ok


def addLink( name, url,mode,isFolder, iconimage="DefaultFolder.png"):
 

          
         
         
          u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
          liz = xbmcgui.ListItem( name, iconImage=iconimage, thumbnailImage=iconimage)

          liz.setInfo(type="Video", infoLabels={ "Title": urllib.unquote( name)   })
          liz.setProperty( "Fanart_Image", iconimage )
          liz.setProperty("IsPlayable","true")
          
          xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz,isFolder=isFolder)


def read_site_html(url_link):

    req = urllib2.Request(url_link)
    req.add_header('User-agent',__USERAGENT__)# 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')
    html = urllib2.urlopen(req).read()
    return html

def main_menu():
    
    addDir3('ספורט ישראל','links_israel',2,'https://pbs.twimg.com/profile_images/316451557/IFA_CMYK_400x400.jpg','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_Udc25CdEMiDuuFYysQg66r2K2kCBzyBkifNvbutYzAyncLpv','ספורט ישראל')
    addDir3('ספורט עולמי','links_world',2,'http://www.limontasport.com/wp-content/uploads/2016/03/limonta-sport-box-referenze-600x456.jpg','https://blog.studocu.com/wp-content/uploads/2016/10/slide1-image-tablet.png','ספורט עולמי')

def get_links(url):
  if url=='links_israel':
    for name,link,image in links_israel:
      addLink( name, link,3,False,image)
  if url=='links_world':
    for name,link,image in links_world:
      addLink( name, link,3,False,image)
      
def play(url,name):
  logging.warning(url)
  listitem = xbmcgui.ListItem(path=url)
  listitem.setInfo( type="Video", infoLabels={ "Title": name } )
  listitem.setInfo( type="Music", infoLabels={ "Title": name } )
  xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)

params=get_params()

url=None
name=None
mode=None
iconimage=None
fanart=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
   


if mode==None or url==None or len(url)<1:
        main_menu()
elif mode==2:
     get_links(url)
elif mode==3:
      play(url,name)
      
xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
xbmc.executebuiltin("Container.SetViewMode(504)")

xbmcplugin.endOfDirectory(int(sys.argv[1]))

