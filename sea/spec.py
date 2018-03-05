"""Spec for cleaned version of example csv."""
from dretch.spec import(
    Identifier,
    Ordinal,
    Categorical,
    Spec,
    DateTime,
    StatisticalArea,
    Ranked)

X = Spec(
    # "longitude", Ordinal(),
    # "latitude", Ordinal(),
    "bathymetry", Ordinal(),
    "nitrate", Ordinal(),
    "oxygen", Ordinal(),
    "phosphate", Ordinal(),
    "productivity", Ordinal(),
    "salinity", Ordinal(),
    "silicate", Ordinal(),
    "temperature", Ordinal(),
)

Y = Spec(
    "lithology", Categorical([
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
    ])
)
