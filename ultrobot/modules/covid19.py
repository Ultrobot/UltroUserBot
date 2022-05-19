

# ██████ LANGUAGE CONSTANTS ██████ #

from ultrobot.language import get_value
LANG = get_value("covid19")

# ████████████████████████████████ #

from ultrobot import CMD_HELP
from ultrobot.events import register
from requests import get
import pytz
import flag
from ultrobot.cmdhelp import CmdHelp

@register(outgoing=True, pattern="^.covid ?(.*)$")
async def covid(event):
    try:
        if event.pattern_match.group(1) == '':
            country = 'TR'
        else: 
            country = event.pattern_match.group(1)

        bayrak = flag.flag(country)
        worldData = get('https://coronavirus-19-api.herokuapp.com/all').json()
        countryData = get('https://coronavirus-19-api.herokuapp.com/countries/' + pytz.country_names[country]).json()
    except:
        await event.edit(LANG['SOME_ERRORS'])
        return

    sonuclar = (f"** {LANG['DATA']}**\n" +
                f"\n**{LANG['EARTH']}**\n" +
                f"**{LANG['CASE']}** `{worldData['cases']}`\n" +
                f"**{LANG['DEATH']}** `{worldData['deaths']}`\n" +
                f"**{LANG['HEAL']}** `{worldData['recovered']}`\n" +
                f"\n**{pytz.country_names[country]}**\n" +
                f"**{bayrak} {LANG['TR_ALL_CASES']}** `{countryData['cases']}`\n" +
                f"**{bayrak} {LANG['TR_CASES']}** `{countryData['todayCases']}`\n" +
                f"**{bayrak} {LANG['TR_CASE']}** `{countryData['active']}`\n" +
                f"**{bayrak} {LANG['TR_ALL_DEATHS']}** `{countryData['deaths']}`\n" +
                f"**{bayrak} {LANG['TR_DEATHS']}** `{countryData['todayDeaths']}`\n" +
                f"**{bayrak} {LANG['TR_HEAL']}** `{countryData['recovered']}`\n" +
                f"**{bayrak} Test Sayısı:** `{countryData['totalTests']}`"
                )
    await event.edit(sonuclar)

CmdHelp('covid19').add_command(
    'covid', LANG['COVİD1'], LANG['COVİD2'], LANG['COVİD3']
).add_warning(LANG['COVİD4']).add()
