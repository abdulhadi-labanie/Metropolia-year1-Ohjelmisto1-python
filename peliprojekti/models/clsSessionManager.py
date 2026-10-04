class clsSessionManager:
    _active_manager = None

    @classmethod
    def set_active_manager(cls, manager_obj):
        cls._active_manager = manager_obj

    @classmethod
    def get_active_manager(cls):
        return cls._active_manager
