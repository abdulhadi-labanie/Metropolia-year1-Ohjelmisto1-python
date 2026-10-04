class clsPlane:
    def __init__(self, specs: dict, stats: dict):
        # (specs)
        self.aircraft_ID = specs.get("aircraft_ID", "")
        self.manufacturer = specs.get("manufacturer", "")
        self.model = specs.get("model", "")
        self.required_crew = specs.get("required_crew", 0)
        self.passengers_capacity = specs.get("passengers_capacity", 0)
        self.ticket_price = specs.get("ticket_price", 0)
        self.optimal_range_km = specs.get("optimal_range_km", 0)
            # (financials)
        financials = specs.get("financials", {})
        self.price = financials.get("price", 0)
        self.annual_maintenance_cost = financials.get("annual_maintenance_cost", 0)
        self.daily_operating_cost = financials.get("daily_operating_cost", 0)
        self.daily_net_profit = financials.get("daily_net_profit", 0)
            # (operations_24h)
        self.flights_per_24h = specs.get("operations_24h", {}).get("flights_per_24h", 0)
            # (environmental_impact)
        env_impact = specs.get("environmental_impact", {})
        self.co2_emissions_per_km = env_impact.get("co2_emissions_per_km", 0.0)
        self.co2_rating = env_impact.get("co2_rating", 0.0)
        # (Stats)
        self.total_flights = stats.get("total_flights", 0)
        self.failed_landings = stats.get("failed_landings", 0)
        self.total_passengers_capacity = stats.get("total_passengers_capacity", 0)
        self.net_profit = stats.get("net_profit", 0)
        self.total_co2_emissions_tonnes = stats.get("total_co2_emissions_tonnes", 0.0)
        self.supported_airports = stats.get("supported_airports", [])
        self.airline_selected = stats.get("airline_selected", "")
        self.total_plane_co2_rating = stats.get("total_plane_co2_rating", 0.0)
        self.total_profit_rating = stats.get("total_profit_rating", 0.0)

        self.specs = specs
        self.stats = stats
        
    @classmethod
    def from_dict(cls, data: dict):
        return cls(specs=data.get("specs", {}), stats=data.get("stats", {}))

    def to_dict(self) -> dict:
            return {
                "specs": {
                    "aircraft_ID": self.aircraft_ID,
                    "manufacturer": getattr(self, "manufacturer", "Unknown"),
                    "model": self.model,
                    "required_crew": self.required_crew,
                    "passengers_capacity": self.passengers_capacity,
                    "ticket_price": self.ticket_price,
                    "optimal_range_km": self.optimal_range_km,
                    "financials": {"price": getattr(self, "price", 0),"annual_maintenance_cost": self.annual_maintenance_cost,"daily_operating_cost": self.daily_operating_cost,"daily_net_profit": getattr(self, "daily_net_profit", 0)},
                    "operations_24h": {"flights_per_24h": getattr(self, "flights_per_24h", 0)},
                    "environmental_impact": {"co2_emissions_per_km": self.co2_emissions_per_km,"co2_rating": getattr(self, "base_co2_rating", self.co2_rating)}
                },
                "stats": {"total_flights": getattr(self, "total_flights", 0),"failed_landings": getattr(self, "failed_landings", 0),"total_passengers_capacity": getattr(self, "total_passengers_capacity", 0),
                    "net_profit": getattr(self, "net_profit", 0),"total_co2_emissions_tonnes": getattr(self, "total_co2_emissions_tonnes", 0.0),"supported_airports": getattr(self, "supported_airports", []),
                    "airline_selected": getattr(self, "airline_selected", ""),"total_plane_co2_rating": getattr(self, "total_plane_co2_rating", 0),"total_profit_rating": getattr(self, "total_profit_rating", 0)}
            }
