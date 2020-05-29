from marshmallow import Schema, fields, ValidationError


class BoolLowerCase(fields.Field):
    """
    Field that serializes bool value to lower case string
    True -> "true", False -> "false"
    """
    def _serialize(self, value, attr, obj, **kwargs):
        return str(value).lower()


class ConfirmationSchema(fields.Field):
    """
    If confirmations == 0, this mean that transactions are considered confirmed when "irreversible" blockchains
    time has come.
    If confirmations > 0, this mean that gateway need to counting "value" of next blocks after goal transaction block
    """
    def _serialize(self, value, attr, obj, **kwargs):
        if value == 0:
            return {"type": "irreversible"}
        else:
            return {"type": "block", "value": value}


class AssetDataSchema(Schema):
    class Meta:
        ordered = True

    name = fields.Str(required=True)
    unified_cryptoasset_id = fields.Str()
    can_deposit = BoolLowerCase()
    can_withdraw = BoolLowerCase()
    min_withdraw = fields.Str()
    max_withdraw = fields.Str()
    maker_fee = fields.Str()
    taker_fee = fields.Str()


class CoinDataSchema(Schema):
    class Meta:
        ordered = True

    name = fields.Str(required=True)
    description = fields.Str(required=True)
    backing_coin = fields.Str()
    symbol = fields.Str()

    deposit_allowed = fields.Bool()
    withdrawal_allowed = fields.Bool()

    memo_support = fields.Bool()
    memo_version = fields.Int(load_only=True)

    precision = fields.Int()

    issuer = fields.Str()
    issuer_id = fields.Str()

    gateway_wallet = fields.Str(load_only=True)
    wallet_type = fields.Str()

    min_amount = fields.Int()
    withdraw_fee = fields.Int()
    deposit_fee = fields.Int()

    # gate_fee do not store in database, and calculated as withdraw_fee / 10 ** precision
    gate_fee = fields.Str()

    confirmations = ConfirmationSchema()
