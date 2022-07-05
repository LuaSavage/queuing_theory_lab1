class ParamView:
    @staticmethod
    def get(params):
        params_copy = params.copy()
        params_copy["y"] = len(params_copy.get("y", []))
        params_copy["y"] = "y["+str(params_copy["y"])+"]"
        return str(params_copy)
    