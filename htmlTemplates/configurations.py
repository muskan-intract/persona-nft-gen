from htmlTemplates.tier_1 import *
from htmlTemplates.tier_2 import *

LINEA_CHAIN_ID = 59144
BASE_CHAIN_ID = 8453
ZKEVM_CHAIN_ID = 1101

configuraitons = {
    LINEA_CHAIN_ID : {
        "TIER1" : {
            "template" : HTML_TEMPLATE_LINEA_1,
            "width" : 330,
            "height" : 520
        },
        "TIER2" : {
            "template" : HTML_TEMPLATE_LINEA_2,
            "width" : 330,
            "height" : 524
        }
    },
    BASE_CHAIN_ID : {
        "TIER1" : {
            "template" : HTML_TEMPLATE_BASE_1,
            "width" : 333,
            "height" : 599
        },
        "TIER2" : {
            "template" : HTML_TEMPLATE_BASE_2,
            "width" : 333,
            "height" : 599
        }
    },
    ZKEVM_CHAIN_ID : {
        "TIER1" : {
            "template" : HTML_TEMPLATE_ZKEVM_1,
        }
    },
}


