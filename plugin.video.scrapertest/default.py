import sys

import nanscrapers
import urlresolver9 as urlresolver
import xbmc
import xbmcgui
import xbmcaddon

addon_id = 'plugin.video.scrapertest'
ADDON = xbmcaddon.Addon(id=addon_id)


type = xbmcgui.Dialog().select("Choose type", ["movie", "tvshow", "music"])

if type == 0:
    if ADDON.getSetting('movie_choice')=='On':
        name = ADDON.getSetting('movie_title')
        year = ADDON.getSetting('movie_year')
        imdb = ADDON.getSetting('movie_imdb')
    else:
        name = xbmcgui.Dialog().input("Movie Name")
        year = xbmcgui.Dialog().input("Movie Year", type=xbmcgui.INPUT_NUMERIC)
        imdb = xbmcgui.Dialog().input("IMDB id")

    if name is not "" and year is not "":
        def sort_function(item):
            quality = item[1][0]["quality"]
            if quality == "1080": quality = "HDa"
            if quality == "720": quality = "HDb"
            if quality == "560": quality = "HDc"
            if quality == "HD": quality = "HDd"
            if quality == "480": quality = "SDa"
            if quality == "360": quality = "SDb"
            if quality == "SD": quality = "SDc"

            return quality


        link = nanscrapers.scrape_movie_with_dialog(name, year, imdb, timeout=600, sort_function=sort_function)
        if link is False:
            xbmcgui.Dialog().ok("Movie not found", "No Links Found for " + name + " (" + year + ")")
        else:
            if link:
                url = link['url']
                try:
                    xbmc.log("resolving " + url)
                    resolved_url = urlresolver.resolve(url)
                    xbmc.log("resolved")
                except:
                    xbmcgui.Dialog().notification("Scraper test", "unplayable stream")
                    sys.exit()
                if resolved_url:
                    url = resolved_url
                xbmc.Player().play(url, xbmcgui.ListItem(name))

if type == 1:
    if ADDON.getSetting('tv_choice')=='On':
        name = ADDON.getSetting('tv_title')
        show_year = ADDON.getSetting('tv_show_year')
        year = ADDON.getSetting('tv_year')
        season = ADDON.getSetting('tv_season')
        episode = ADDON.getSetting('tv_episode')
        imdb = ADDON.getSetting('tv_imdb')
    else:
        name = xbmcgui.Dialog().input("Show Name")
        show_year = xbmcgui.Dialog().input("Show Year", type=xbmcgui.INPUT_NUMERIC)
        year = xbmcgui.Dialog().input("Episode Year", type=xbmcgui.INPUT_NUMERIC)
        season = xbmcgui.Dialog().input("Season", type=xbmcgui.INPUT_NUMERIC)
        episode = xbmcgui.Dialog().input("Episode", type=xbmcgui.INPUT_NUMERIC)
        imdb = xbmcgui.Dialog().input("IMDB id")

    if name is not "" and year is not "" and season is not "" and episode is not "":
        link = nanscrapers.scrape_episode_with_dialog(name, show_year, year, season, episode, imdb, None)
        if link is False:
            xbmcgui.Dialog().ok("TV Show not found", "No Links Found for " + name + " (" + year + ")" + " - S" + season
                                + "E" + episode)
        else:
            if link:
                url = link['url']
                try:
                    resolved_url = urlresolver.resolve(url)
                except:
                    xbmcgui.Dialog().notification("Scraper test", "unplayable stream")
                    sys.exit()
                if resolved_url:
                    url = resolved_url
                xbmc.Player().play(url, xbmcgui.ListItem(name))

if type == 2:
    artist = xbmcgui.Dialog().input("Artist")
    title = xbmcgui.Dialog().input("Title")
    if title is not "" and artist is not "":
        link = nanscrapers.scrape_song_with_dialog(title, artist)
        if link is False:
            xbmcgui.Dialog().ok("Song not found", "No Links Found for " + artist + " - " + title)
        else:
            if link:
                url = link['url']
                try:
                    resolved_url = urlresolver.resolve(url)
                except:
                    xbmcgui.Dialog().notification("Scraper test", "unplayable stream")
                    sys.exit()
                if resolved_url:
                    url = resolved_url
                xbmc.Player().play(url, xbmcgui.ListItem(artist + "- " + title))
