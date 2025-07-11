class MenuResponse:
    @staticmethod
    def success(data):
        return {"status": 1000, "data": data}

    @staticmethod
    def failed(data):
        return {"status": 1001, "data": data}

    @staticmethod
    def other(data):
        return {"status": 1002, "data": data}
