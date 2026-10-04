class clsPlane:
    def __init__(self, specs: dict, stats: dict, supported_airports: list):
        self.specs = specs
        self.stats = stats
        self.supported_airports = supported_airports
        
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            specs=data.get("specs", {}),
            stats=data.get("stats", {}),
            supported_airports=data.get("supported_airports", [])
        )
