test_assets_data = [
    dict(
        ticker="BTC",
        name="Bitcoin",
        unified_cryptoasset_id=1,
        can_withdraw=True,
        can_deposit=True,
        min_withdraw=0.0018,
        max_withdraw=1000,
        maker_fee=0.10,
        taker_fee=0.10
    ),
    dict(
        ticker="USDT",
        name="Tether",
        unified_cryptoasset_id=825,
        can_withdraw=True,
        can_deposit=True,
        min_withdraw=5.0,
        max_withdraw=100000,
        maker_fee=0.10,
        taker_fee=0.10
    )
]

test_coins_data = [
    {
        "name": "BTC",
        "description": "Bitcoin - BTC",
        "backing_coin": "BTC",
        "symbol": "RUDEX.BTC",
        "deposit_allowed": True,
        "withdrawal_allowed": True,
        "memo_support": False,
        "precision": 8,
        "issuer": "rudex-bitcoin",
        "issuer_id": "1.2.852589",
        "wallet_type": "bitcoin",
        "min_amount": 180000,
        "withdraw_fee": 50000,
        "deposit_fee": 0,
        "confirmations": 3
    },
    {
        "name": "STEEM",
        "description": "Steem - STEEM",
        "backing_coin": "STEEM",
        "symbol": "RUDEX.STEEM",
        "deposit_allowed": True,
        "withdrawal_allowed": True,
        "memo_support": True,
        "memo_version": 2,
        "precision": 3,
        "issuer": "rudex-steem",
        "issuer_id": "1.2.382392",
        "gateway_wallet": "rudex",
        "wallet_type": "steem",
        "min_amount": 50000,
        "withdraw_fee": 10000,
        "deposit_fee": 0,
        "confirmations": 0
    },
]
