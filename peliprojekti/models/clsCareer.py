from models.clsYear import clsYear

class clsCareer:
    def __init__(self, company_name, country, hub_airport, company_budget, is_active, fleet_count, years):
        self.company_name = company_name
        self.country = country
        self.hub_airport = hub_airport
        self.company_budget = company_budget
        self.is_active = is_active
        self.fleet_count = fleet_count
        self.years = years

    @classmethod
    def from_dict(cls, data: dict):
        years_dict = {}
        for year_label, year_data in data.get("years", {}).items():
            years_dict[year_label] = clsYear.from_dict(year_label, year_data)

        return cls(company_name=data.get("company_name"), country=data.get("country"), hub_airport=data.get("hub_airport"),
            company_budget=data.get("company_budget"), is_active=data.get("is_active"),
            fleet_count=data.get("fleet_count"), years=years_dict)

    def to_dict(self) -> dict:
            years_dict = {}
            for year_key, year_obj in self.years.items():
                years_dict[year_key] = year_obj.to_dict()

            return {"company_name": self.company_name,"country": self.country,"hub_airport": self.hub_airport,"company_budget": self.company_budget,
                    "is_active": self.is_active,"fleet_count": self.fleet_count,"years": years_dict}
