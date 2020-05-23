from marshmallow import Schema, fields, ValidationError


class BoolLowerCase(fields.Field):
    """
    Field that serializes bool value to lower case string
    """
    def _serialize(self, value, attr, obj, **kwargs):
        return str(value).lower()


class AssetDataSchema(Schema):
    name = fields.Str(required=True)
    unified_cryptoasset_id = fields.Str()
    can_deposit = BoolLowerCase()
    can_withdraw = BoolLowerCase()
    min_withdraw = fields.Str()
    max_withdraw = fields.Str()
    maker_fee = fields.Str()
    taker_fee = fields.Str()
