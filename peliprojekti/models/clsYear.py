from models.clsPlane import clsPlane

class clsYear:
    def __init__(self, year_label: str, planes: list, total_company_co2_rating):
        self.year_label = year_label
        self.planes = planes
        self.total_company_co2_rating = total_company_co2_rating

    @classmethod
    def from_dict(cls, year_label: str, data: dict):
        planes_list = []
        for plane_data in data.get("planes", []):
            new_plane = clsPlane.from_dict(plane_data)
            planes_list.append(new_plane)
        return cls(year_label=year_label, planes=planes_list, total_company_co2_rating=data.get("total_company_co2_rating", 0))
    
    def get_my_fleet(self) -> list:
        return self.planes

    def to_dict(self) -> dict:
        planes_list = []
        for plane in self.planes:
            planes_list.append(plane.to_dict())
        return {"planes": planes_list}
