from htmlTemplates.tier_1 import *
from htmlTemplates.tier_2 import *

LINEA_CHAIN_ID = 59144
BASE_CHAIN_ID = 8453
ZKEVM_CHAIN_ID = 1101
BLAST_CHAIN_ID = 81457
ZKSYNC_CHAIN_ID = 324
MODE_CHAIN_ID = 34443
ZORA_CHAIN_ID = 7777777

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
            "width" : 332,
            "height" : 595
        },
        "TIER2" : {
            "template" : HTML_TEMPLATE_BASE_2,
            "width" : 332,
            "height" : 595
        }
    },
    ZKEVM_CHAIN_ID : {
        "TIER1" : {
            "template" : HTML_TEMPLATE_ZKEVM_1,
        }
    },
    BLAST_CHAIN_ID : {
        "TIER1" : {
            "template" : HTML_TEMPLATE_BLAST_1,
            "width" : 331,
            "height" : 593
        },
        "TIER2" : {
            "template" : HTML_TEMPLATE_BLAST_2,
            "width" : 331,
            "height" : 593
        }
    },
    ZKSYNC_CHAIN_ID : {
        "TIER1" : {
            "template" : HTML_TEMPLATE_ZKSYNC_1,
            "width" : 331,
            "height" : 593
        },
        "TIER2" : {
            "template" : HTML_TEMPLATE_ZKSYNC_2,
            "width" : 331,
            "height" : 593
        }
    },
    MODE_CHAIN_ID : {
        "TIER1" : {
            "template" : HTML_TEMPLATE_MODE_1,
            "width" : 331,
            "height" : 593
        },
        "TIER2" : {
            "template" : HTML_TEMPLATE_MODE_2,
            "width" : 331,
            "height" : 593
        }
    },
    ZORA_CHAIN_ID : {
        "TIER1" : {
            "template" : HTML_TEMPLATE_ZORA_1,
            "width" : 331,
            "height" : 593
        },
        "TIER2" : {
            "template" : HTML_TEMPLATE_ZORA_2,
            "width" : 331,
            "height" : 593
        }
    }
}


