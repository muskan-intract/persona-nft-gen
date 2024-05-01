from htmlTemplates.tier_1 import *
from htmlTemplates.tier_2 import *

LINEA_CHAIN_ID = 59144
BASE_CHAIN_ID = 8453
ZKEVM_CHAIN_ID = 1101

configuraitons = {
    LINEA_CHAIN_ID : {
        "TIER1" : HTML_TEMPLATE_LINEA_1,
        "TIER2" : HTML_TEMPLATE_LINEA_2,
    },
    BASE_CHAIN_ID : {
        "TIER1" : HTML_TEMPLATE_BASE_1,
        "TIER2" : HTML_TEMPLATE_BASE_2,
    },
    ZKEVM_CHAIN_ID : {
        "TIER1" : HTML_TEMPLATE_ZKEVM_1
    },
}