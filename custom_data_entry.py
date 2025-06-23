from data_entry import DataEntry

class CustomDataEntry(DataEntry):
    def get_description(self):
        description = super().get_description()
        return description or "No description provided"
