#4
class OfficeEquipmentWarehouse:
 
    storage:dict = {}
    def __init__(self):
        # self.storage = {
        #     "printer" :{},
        #     "scaner"  :{},
        #     "xerox"   :{}
        # }
        pass
    def add_equipment(self, equipment, count):
        # if isinstance(equipment, Printer):
        #     storage["printer"][equipment.name.lower()] = count
        equipment_type = equipment.__class__.__name__
        try:
            self.storage[equipment_type][equipment.name] += count
        except KeyError:
            if equipment_type not in self.storage:
                self.storage[equipment_type] = {}
                self.storage[equipment_type][equipment.name] = count
            elif equipment.name not in self.storage[equipment_type]:
                self.storage[equipment_type][equipment.name] = count
            # ну-ка давай ещё раз
 
    def __str__(self):
        output = ''
        for k, equipment in self.storage.items():
            output += f'{k}:\n'
            print(equipment)
            for e, count in equipment.items():
                output += f'\t{e} {count}\n'
                
       return output         
