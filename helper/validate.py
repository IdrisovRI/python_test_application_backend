class PackageDataValidator(object):

    @staticmethod
    async def validate(package: str):
        result = False
        if "Symbol" in package and "Bid" in package and "Ask" in package:
            result = True

        return result
