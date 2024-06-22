TG_TOKEN = 'your_tg_token'
TG_ID = 0 

DATA = {
    'ethereum'      : {'rpc': ['https://mainnet.gateway.tenderly.co', 'https://singapore.rpc.blxrbdn.com', 'https://eth-mainnet.public.blastapi.io', 'https://rpc.payload.de', 'https://api.securerpc.com/v1'], 'scan': 'https://etherscan.io/tx', 'token': 'ETH', 'chain_id': 1},

    'optimism'      : {'rpc': ['https://optimism.llamarpc.com', 'https://optimism.rpc.subquery.network/public', 'https://op-pokt.nodies.app', 'https://rpc.ankr.com/optimism'], 'scan': 'https://optimistic.etherscan.io/tx', 'token': 'ETH', 'chain_id': 10},

    'bsc'           : {'rpc': ['https://binance.llamarpc.com', 'https://bsc.blockpi.network/v1/rpc/public', 'https://bsc-dataseed.bnbchain.org', 'https://bscrpc.com'], 'scan': 'https://bscscan.com/tx', 'token': 'BNB', 'chain_id': 56},

    'opBNB'          : {'rpc': ['https://opbnb-mainnet.nodereal.io/v1/e9a36765eb8a40b9bd12e680a1fd2bc5', 'https://opbnb-mainnet.nodereal.io/v1/64a9df0874fb4a93b9d0a3849de012d3', 'https://opbnb-mainnet-rpc.bnbchain.org', 'https://opbnb.drpc.org', 'https://opbnb-rpc.publicnode.com'], 'scan': 'https://opbnbscan.com/tx', 'token': 'BNB', 'chain_id': 204},

    'polygon'       : {'rpc': ['https://rpc-mainnet.matic.quiknode.pro', 'https://polygon-pokt.nodies.app'], 'scan': 'https://polygonscan.com/tx', 'token': 'MATIC', 'chain_id': 137},

    'polygon_zkevm' : {'rpc': ['https://zkevm-rpc.com', 'https://polygon-zkevm.drpc.org', 'https://polygon-zkevm-mainnet.public.blastapi.io'], 'scan': 'https://zkevm.polygonscan.com/tx', 'token': 'ETH', 'chain_id': 1101},

    'arbitrum'      : {'rpc': ['https://public.stackup.sh/api/v1/node/arbitrum-one', 'https://arbitrum.llamarpc.com', 'https://arb-pokt.nodies.app'], 'scan': 'https://arbiscan.io/tx', 'token': 'ETH', 'chain_id': 42161},

    'avalanche'     : {'rpc': ['https://1rpc.io/avax/c', 'https://api.avax.network/ext/bc/C/rpc', 'https://avalanche-c-chain-rpc.publicnode.com'], 'scan': 'https://snowtrace.io/tx', 'token': 'AVAX', 'chain_id': 43114},

    'fantom'        : {'rpc': ['https://rpc.ankr.com/fantom', 'https://fantom-mainnet.public.blastapi.io', 'https://fantom-pokt.nodies.app'], 'scan': 'https://ftmscan.com/tx', 'token': 'FTM', 'chain_id': 250},

    'nova'          : {'rpc': ['https://nova.arbitrum.io/rpc', 'https://arbitrum-nova.publicnode.com', 'https://arbitrum-nova.drpc.org', 'https://arbitrum-nova.public.blastapi.io'], 'scan': 'https://nova.arbiscan.io/tx', 'token': 'ETH', 'chain_id': 42170},

    'zksync'        : {'rpc': ['https://mainnet.era.zksync.io', 'https://zksync-era.blockpi.network/v1/rpc/public', 'https://zksync2-mainnet.zksync.io', 'https://zksync.rpc.thirdweb.com'], 'scan': 'https://explorer.zksync.io/tx', 'token': 'ETH', 'chain_id': 324},
    
    'celo'          : {'rpc': ['https://forno.celo.org', 'https://forno.celo.org', 'https://rpc.ankr.com/celo'], 'scan': 'https://celoscan.io/tx', 'token': 'CELO', 'chain_id': 42220},

    'gnosis'        : {'rpc': ['https://rpc.ankr.com/gnosis', 'https://gnosis.blockpi.network/v1/rpc/public', 'https://gnosis.drpc.org', 'https://1rpc.io/gnosis'], 'scan': 'https://gnosisscan.io/tx', 'token': 'xDAI', 'chain_id': 100},

    'core'          : {'rpc': ['https://rpc.coredao.org', 'https://rpc-core.icecreamswap.com', 'https://rpc.ankr.com/core'], 'scan': 'https://scan.coredao.org/tx', 'token': 'CORE', 'chain_id': 1116},

    'harmony'       : {'rpc': ['https://api.harmony.one', 'https://api.s0.t.hmny.io', 'https://hmyone-pokt.nodies.app'], 'scan': 'https://explorer.harmony.one/tx', 'token': 'ONE', 'chain_id': 1666600000},

    'moonbeam'      : {'rpc': ['https://rpc.ankr.com/moonbeam', 'https://moonbeam.unitedbloc.com', 'https://moonbeam-rpc.publicnode.com', 'https://moonbeam.api.onfinality.io/public'], 'scan': 'https://moonscan.io/tx', 'token': 'GLMR', 'chain_id': 1284},

    'moonriver'     : {'rpc': ['https://moonriver.public.blastapi.io', 'https://moonriver-rpc.dwellir.com', 'https://moonriver.unitedbloc.com', 'https://moonriver-rpc.publicnode.com'], 'scan': 'https://moonriver.moonscan.io/tx', 'token': 'MOVR', 'chain_id': 1285},

    'linea'         : {'rpc': ['https://rpc.linea.build', 'https://linea.decubate.com', 'https://1rpc.io/linea'], 'scan': 'https://lineascan.build/tx', 'token': 'ETH', 'chain_id': 59144},

    'base'          : {'rpc': ['https://mainnet.base.org', 'https://base.llamarpc.com', 'https://base.blockpi.network/v1/rpc/public', 'https://base.gateway.tenderly.co'], 'scan': 'https://basescan.org/tx', 'token': 'ETH', 'chain_id': 8453},

    'metis'          : {'rpc': ['https://andromeda.metis.io/?owner=1088', 'https://metis.drpc.org', 'https://metis-pokt.nodies.app', 'https://metis-mainnet.public.blastapi.io'], 'scan': 'https://andromeda-explorer.metis.io/tx', 'token': 'METIS', 'chain_id': 1088},
}
