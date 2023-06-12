from models.Supplies import Supplies as SuppliesModel


class SuppliesService():
    def __init__(self,db):
        self.db = db

    
    def get_supplies(self):
        result = self.db.query(SuppliesModel).all()
        return result
    


    def create_supplies(self,supplies:SuppliesModel):
        new_supplies = SuppliesModel(
            sup_id = supplies.sup_id,
            pro_id = supplies.pro_id,
            purchase_price = supplies.purchase_price
        )
        self.db.add(new_supplies)
        self.db.commit()
        self.db.refresh
        return


    def get_supplies_for_id(self,id:int):
        result = self.db.query(SuppliesModel).filter(SuppliesModel.id == id).first()
        return result
    

    def update_supplies(self,data:SuppliesModel):
        supplies = self.db.query(SuppliesModel).filter(SuppliesModel.id == data.id).first()
        supplies.sup_id = data.sup_id
        supplies.pro_id = data.pro_id
        supplies.purchase_price = data.purchase_price
        self.db.commit()
        return
    

    def delete_supplies(self,id:int):
        self.db.query(SuppliesModel).filter(SuppliesModel.id == id).delete()
        self.db.commit()
        return