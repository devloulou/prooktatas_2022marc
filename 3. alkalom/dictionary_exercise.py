# dictionary: kulcs - érték párokat tartalmazó objektum

from hashlib import sha3_224


my_dict = {
    "kulcs": "érték"
}

print(my_dict)


my_dict = {
    1: "azonosító",
    "name": "Ricsi",
    "age": 32,
    "munkahelyei": [
        "Munka1", "Munka2", "Munka3"
    ],
    "age": 10
}

# meglévő információk lekérése
# kulcs az mindig egyedi -> nem lehet 2 ugyan olyan nevű kulcshoz értéket rendelni

print(my_dict["name"])
print(my_dict["age"])
print(my_dict[1])
print(my_dict["munkahelyei"][1])

print(my_dict.get("name"))
print(my_dict.get("gyerekei_száma", "Nincs gyereke"))

my_value = None
#############################################################################
# elem hozzáadás és módosítása

# hozzá tudunk adni elemet: 
# update metódus , ha nincs még a kulcs a dictionarybe,
# akkor létrehozza
# ha létezik, akkor felülírja az értékét
# módosítani tudunk meglévő elemet

my_dict.update({"szemszín": "barna"})
my_dict.update({"name": "Ricsi"})

my_dict["munkakör"] = "fejlesztő"

#####################################################

# törölni tudunk elemet
print("#################################################")
my_dict.pop("name")
print(my_dict)
my_dict.popitem()

del my_dict["age"]

my_list = [1,2,3,4]

del my_list[1]

# del miért tud így működni

my_dict = {

    print: "ez egy kulcs",
    "autok": [
        {
            "auto_type": "benzin",
            "color": "green",
            "brand": "BMW"
        },
        {
            "auto_type": "benzin",
            "color": "yellow",
            "brand": "Merci"
        },
        {
            "auto_type": "diesel",
            "color": "green",
            "brand": "VW"
        },
        {
            "auto_type": "benzin",
            "color": "red",
            "brand": "Volvo"
        },
        {
            "auto_type": "electromos",
            "color": "white",
            "brand": "Tesla"
        }
    ],

    "sportok": {
        "lamba_srort": [
            {
                "sport": "foci"
            },
            {
                "sport": "röplabda"
            }
        ],
        "motorsportok": 
        [
            {
                "sport": "motogp"
            },
            {
                "sport": "f1"
            }
        ]

    },

    "kontinensek":
    {
        "azsia": {
            "orszagok": [
                {"orszagok": [
                    {"orszagok": [
                        {"orszagok": [
                            {"orszagok": [
                                {"orszagok": [
                                    {"orszagok": [
                {},
                {},
                {},
                {}
            ]},
                {},
                {},
                {}
            ]},
                {},
                {},
                {}
            ]},
                {},
                {},
                {}
            ]},
                {},
                {},
                {}
            ]},
                {},
                {},
                {}
            ]},
                {},
                {},
                {}
            ]
        },
        "europa": {"orszagok": [
                {},
                {},
                {},
                {}
            ]},
        "ameriak": {"orszagok": [
                {},
                {},
                {},
                {}
            ]}
    }


}

# debug hibaüzenet nem jelenik meg futási időben
# set  - duplikáció mentes, iterálható objektum

my_set = {1, 2, 3, 4}

my_set2 = {1, 2, 3}

difference = my_set.difference(my_set2)

is_sub_set = my_set2.issubset(my_set)

my_list = [1,2,2,2,2,2,3,4,5,6,7,7,8,8,8]

dedup_list = list(set(my_list))

print(dedup_list)


# ciklusok és elágazások

# indentáció

# elágazások

# C típusú nyelvekben: pl.
# if (logikai vizsgálat) {

#     SDSDgdgSDDgDG;
#     DgDG
# }
# else {

# }


# python if else

# if logikai vizsgálat:
#     utasítások
#     utasításha3_224



