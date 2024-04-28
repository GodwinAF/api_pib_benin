# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 19:57:13 2024

@author: Godwin AKATY
"""

from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class item(BaseModel):
    PIB_ANNEE : str
    valeur:float
    id:int

pib_benin = {1960 : item(PIB_ANNEE ="PIB1960",valeur =226195578.434497,id=1960),
1961 : item(PIB_ANNEE ="PIB1961",valeur =235668220.508202,id=1961),
1962 : item(PIB_ANNEE ="PIB1962",valeur =236434954.038578,id=1962),
1963 : item(PIB_ANNEE ="PIB1963",valeur =253927697.25805,id=1963),
1964 : item(PIB_ANNEE ="PIB1964",valeur =269819005.87814,id=1964),
1965 : item(PIB_ANNEE ="PIB1965",valeur =289908680.426395,id=1965),
1966 : item(PIB_ANNEE ="PIB1966",valeur =302925235.151997,id=1966),
1967 : item(PIB_ANNEE ="PIB1967",valeur =306221953.104911,id=1967),
1968 : item(PIB_ANNEE ="PIB1968",valeur =326323105.26476,id=1968),
1969 : item(PIB_ANNEE ="PIB1969",valeur =330748244.539574,id=1969),
1970 : item(PIB_ANNEE ="PIB1970",valeur =333627713.494438,id=1970),
1971 : item(PIB_ANNEE ="PIB1971",valeur =335073027.54117,id=1971),
1972 : item(PIB_ANNEE ="PIB1972",valeur =410331856.991218,id=1972),
1973 : item(PIB_ANNEE ="PIB1973",valeur =504376074.185709,id=1973),
1974 : item(PIB_ANNEE ="PIB1974",valeur =554654860.702577,id=1974),
1975 : item(PIB_ANNEE ="PIB1975",valeur =676870140.341529,id=1975),
1976 : item(PIB_ANNEE ="PIB1976",valeur =698408261.922237,id=1976),
1977 : item(PIB_ANNEE ="PIB1977",valeur =750049778.84069,id=1977),
1978 : item(PIB_ANNEE ="PIB1978",valeur =928843469.431727,id=1978),
1979 : item(PIB_ANNEE ="PIB1979",valeur =1186231019.82044,id=1979),
1980 : item(PIB_ANNEE ="PIB1980",valeur =1405251846.54048,id=1980),
1981 : item(PIB_ANNEE ="PIB1981",valeur =1291120188.43104,id=1981),
1982 : item(PIB_ANNEE ="PIB1982",valeur =1267778670.35902,id=1982),
1983 : item(PIB_ANNEE ="PIB1983",valeur =1095348199.43911,id=1983),
1984 : item(PIB_ANNEE ="PIB1984",valeur =1051134008.78979,id=1984),
1985 : item(PIB_ANNEE ="PIB1985",valeur =1045712789.14884,id=1985),
1986 : item(PIB_ANNEE ="PIB1986",valeur =1336102025.27763,id=1986),
1987 : item(PIB_ANNEE ="PIB1987",valeur =1562412227.90058,id=1987),
1988 : item(PIB_ANNEE ="PIB1988",valeur =1620246083.79478,id=1988),
1989 : item(PIB_ANNEE ="PIB1989",valeur =1502294416.17129,id=1989),
1990 : item(PIB_ANNEE ="PIB1990",valeur =1959965330.14765,id=1990),
1991 : item(PIB_ANNEE ="PIB1991",valeur =1986437796.53053,id=1991),
1992 : item(PIB_ANNEE ="PIB1992",valeur =1695315305.70308,id=1992),
1993 : item(PIB_ANNEE ="PIB1993",valeur =2274558082.76135,id=1993),
1994 : item(PIB_ANNEE ="PIB1994",valeur =1598075943.86774,id=1994),
1995 : item(PIB_ANNEE ="PIB1995",valeur =2169627137.9207,id=1995),
1996 : item(PIB_ANNEE ="PIB1996",valeur =2361116449.39308,id=1996),
1997 : item(PIB_ANNEE ="PIB1997",valeur =2268301646.46707,id=1997),
1998 : item(PIB_ANNEE ="PIB1998",valeur =2455092686.34712,id=1998),
1999 : item(PIB_ANNEE ="PIB1999",valeur =3677393998.74486,id=1999),
2000 : item(PIB_ANNEE ="PIB2000",valeur =3519991440.47913,id=2000),
2001 : item(PIB_ANNEE ="PIB2001",valeur =3666222635.13875,id=2001),
2002 : item(PIB_ANNEE ="PIB2002",valeur =4194342686.2178,id=2002),
2003 : item(PIB_ANNEE ="PIB2003",valeur =5349258094.48239,id=2003),
2004 : item(PIB_ANNEE ="PIB2004",valeur =6190270380.49856,id=2004),
2005 : item(PIB_ANNEE ="PIB2005",valeur =6567654954.38903,id=2005),
2006 : item(PIB_ANNEE ="PIB2006",valeur =7034111314.88812,id=2006),
2007 : item(PIB_ANNEE ="PIB2007",valeur =8169048382.83875,id=2007),
2008 : item(PIB_ANNEE ="PIB2008",valeur =9787734526.23965,id=2008),
2009 : item(PIB_ANNEE ="PIB2009",valeur =9738626517.00319,id=2009),
2010 : item(PIB_ANNEE ="PIB2010",valeur =9535345015.78355,id=2010),
2011 : item(PIB_ANNEE ="PIB2011",valeur =10693321363.6574,id=2011),
2012 : item(PIB_ANNEE ="PIB2012",valeur =11141358115.8991,id=2012),
2013 : item(PIB_ANNEE ="PIB2013",valeur =12517845123.9315,id=2013),
2014 : item(PIB_ANNEE ="PIB2014",valeur =13284527846.9081,id=2014),
2015 : item(PIB_ANNEE ="PIB2015",valeur =11388160997.1089,id=2015),
2016 : item(PIB_ANNEE ="PIB2016",valeur =11821065852.1271,id=2016),
2017 : item(PIB_ANNEE ="PIB2017",valeur =12701655845.9612,id=2017),
2018 : item(PIB_ANNEE ="PIB2018",valeur =14262408079.7014,id=2018),
2019 : item(PIB_ANNEE ="PIB2019",valeur =14390708756.988,id=2019),
2020 : item(PIB_ANNEE ="PIB2020",valeur =15686741893.5187,id=2020),
2021 : item(PIB_ANNEE ="PIB2021",valeur =17687623534.6665,id=2021),
2022 : item(PIB_ANNEE ="PIB2022",valeur =17396792699.5489,id=2022)}


@app.get("/")
def index() -> dict[str, dict[int,item]]:
    return {"pib_benin":pib_benin}


@app.get("/pib_benin/{item_id}")
def query_item_by_id(item_id: int)-> item:
    if item_id not in pib_benin:
        raise HTTPException(
            status_code = 404, detail=f"item with {item_id=} does not exist.")
    return pib_benin[item_id]








