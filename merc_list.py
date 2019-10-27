class Mercs():

    def merc_num(merc_name):

        merc_choice = str.lower(merc_name)

        MERCS = {
            "alec" : str(177),
            "angelica" : str(179),
            "granhildr" : str(178),
            "celia" : str(156),
            "nartas" : str(180),
            "refithea" : str(185),
            "velfern" : str(291),
            "valze" : str(293),
            "mamonir" : str(292),
            "asmode" : str(290),
            "lucius" : str(288),
            "seto" : str(289),
            "levia" : str(295),
            "beliath" : str(294)}

        return(MERCS[merc_choice])