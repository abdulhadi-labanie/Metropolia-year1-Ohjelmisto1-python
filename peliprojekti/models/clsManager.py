from models.clsCareer import clsCareer

class clsManager:
    def __init__(self, user_name: str, age: int, career: list):
        self.user_name = user_name
        self.age = age
        self.career = career

    @classmethod
    def from_dict(cls, data: dict):
        careers_list = []
        
        for career_data in data.get("career", []):
            new_Career = clsCareer.from_dict(career_data)
            careers_list.append(new_Career)
            
        new_manager_object = cls(user_name=data.get("user_name"),age=data.get("age"),career=careers_list)
        
        return new_manager_object

    
    def get_active_company(self) -> clsCareer:
        for company in self.career:
            if company.is_active:
                return company
        return None
